#!/usr/bin/python2.7
#
# Interface for the assignement
#


import psycopg2

def getOpenConnection(user='postgres', password='1234', dbname='postgres'):
    return psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='localhost' password='" + password + "'")


def Load_Ratings(ratingstablename, ratingsfilepath, openconnection):
    cur = openconnection.cursor()
    
    # CREATE TABLE ratingstablename
    cur.execute("""
    CREATE TABLE IF NOT EXISTS {0} (
        userid INT,
        movieid INT,
        rating FLOAT
    );
    """.format(ratingstablename))

    # open read as file
    with open(ratingsfilepath, 'r') as file:
        for line in file:
            data = line.strip().split("::")
            user_id, movie_id, rating = int(data[0]), int(data[1]), float(data[2])
            # INSERT data
            cur.execute("INSERT INTO {0} (userid, movieid, rating) VALUES (%s, %s, %s);".format(ratingstablename),
                           (user_id, movie_id, rating))

    # commit
    openconnection.commit()
    cur.close()


def Range_Partition(ratingstablename, numberofpartitions, openconnection):
    cur = openconnection.cursor()
    
    # range size
    range_size = 5 / numberofpartitions
    
    # CREATE Range Partition TABLE
    for i in range(numberofpartitions):
        partition_table = "range_part{0}".format(i)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS {0} (
            userid INT,
            movieid INT,
            rating FLOAT
        );
        """.format(partition_table))
    
        lower_bound = i * range_size
        upper_bound = (i + 1) * range_size

        if i == 0:
            # First Partition 0 <= rating <= upper_bound
            cur.execute("""
            INSERT INTO {0} 
            SELECT * FROM {1}
            WHERE rating >= 0 AND rating <= {2};
            """.format(partition_table, ratingstablename, upper_bound))
        else:
            # else lower_bound < rating <= upper_bound
            cur.execute("""
            INSERT INTO {0} 
            SELECT * FROM {1}
            WHERE rating > {2} AND rating <= {3};
            """.format(partition_table, ratingstablename, lower_bound, upper_bound))

    openconnection.commit()
    cur.close()


def RoundRobin_Partition(ratingstablename, numberofpartitions, openconnection):
    cur = openconnection.cursor()
    
    # CREATE RoundRobin Partition TABLE
    for i in range(numberofpartitions):
        partition_table = "rrobin_part{0}".format(i)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS {0} (
            userid INT,
            movieid INT,
            rating FLOAT
        );
        """.format(partition_table))
    
    # SELECT all data
    cur.execute("SELECT * FROM {0};".format(ratingstablename))
    rows = cur.fetchall()
    
    # INSERT each record into different partitions (RoundRobin)
    for idx, row in enumerate(rows):
        partition_idx = idx % numberofpartitions
        partition_table = "rrobin_part{0}".format(partition_idx)
        cur.execute("INSERT INTO {0} (userid, movieid, rating) VALUES (%s, %s, %s);".format(partition_table), row)
    
    openconnection.commit()
    cur.close()


def RoundRobin_Insert(ratingstablename, userid, itemid, rating, openconnection):
    cursor = openconnection.cursor()
    
    # get numberofpartitions by COUNT prefix "rrobin_part"
    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name LIKE 'rrobin_part%';")
    numberofpartitions = cursor.fetchone()[0]


    # get number of records in rating
    cursor.execute("SELECT COUNT(*) FROM {0};".format(ratingstablename))
    total_records = cursor.fetchone()[0]

    # where to insert
    partition_idx = total_records % numberofpartitions
    partition_table = "rrobin_part{0}".format(partition_idx)
    
    # INSERT
    cursor.execute("INSERT INTO {0} (userid, movieid, rating) VALUES (%s, %s, %s);".format(partition_table),
                   (userid, itemid, rating))

    openconnection.commit()
    cursor.close()


def Range_Insert(ratingstablename, userid, itemid, rating, openconnection):
    cursor = openconnection.cursor()

    # get numberofpartitions by COUNT prefix "range_part"
    cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name LIKE 'range_part%';")
    numberofpartitions = cursor.fetchone()[0]

    # range size
    range_size = 5.0 / numberofpartitions

    # loop through indexes to find partition
    partition_idx = -1
    for i in range(numberofpartitions):
        lower_bound = i * range_size
        upper_bound = (i + 1) * range_size
        
        # First partition 0 <= rating <= upper_bound
        if i == 0 and 0 <= rating <= upper_bound:
            partition_idx = i
            break
        # else lower_bound < rating <= upper_bound
        elif i > 0 and lower_bound < rating <= upper_bound:
            partition_idx = i
            break
    
    if partition_idx == -1:
        raise Exception("Could not find partition for rating")

    partition_table = "range_part{0}".format(partition_idx)
    
    # INSERT
    cursor.execute("INSERT INTO {0} (userid, movieid, rating) VALUES (%s, %s, %s);".format(partition_table),
                   (userid, itemid, rating))

    openconnection.commit()
    cursor.close()

def createDB(dbname='dds_assignment'):
    """
    We create a DB by connecting to the default user and database of Postgres
    The function first checks if an existing database exists for a given name, else creates it.
    :return:None
    """
    # Connect to the default database
    con = getOpenConnection(dbname='postgres')
    con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    # Check if an existing database with the same name exists
    cur.execute('SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname=\'%s\'' % (dbname,))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute('CREATE DATABASE %s' % (dbname,))  # Create the database
    else:
        print 'A database named {0} already exists'.format(dbname)

    # Clean up
    cur.close()
    con.close()

def deletepartitionsandexit(openconnection):
    cur = openconnection.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    l = []
    for row in cur:
        l.append(row[0])
    for tablename in l:
        cur.execute("drop table if exists {0} CASCADE".format(tablename))

    cur.close()

def deleteTables(ratingstablename, openconnection):
    try:
        cursor = openconnection.cursor()
        if ratingstablename.upper() == 'ALL':
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            tables = cursor.fetchall()
            for table_name in tables:
                cursor.execute('DROP TABLE %s CASCADE' % (table_name[0]))
        else:
            cursor.execute('DROP TABLE %s CASCADE' % (ratingstablename))
        openconnection.commit()
    except psycopg2.DatabaseError, e:
        if openconnection:
            openconnection.rollback()
        print 'Error %s' % e
    except IOError, e:
        if openconnection:
            openconnection.rollback()
        print 'Error %s' % e
    finally:
        if cursor:
            cursor.close()
