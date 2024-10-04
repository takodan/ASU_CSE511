# Module 7: Apache Spark
## M7U1L1 RDD and Apache Spark
1. Resilient Distributed Database (RDD)
    1. Read-only
    2. Partitioned collection records
    3. Can only be created through
        1. data in stable storage
        2. other RDDs
    4. Components
        1. a set of partitions
        2. a set of dependencies on parent RDDs
        3. a function for computing the dataset based on its parents (對父數據進行操作的函式)
        4. metadata about its partitioning scheme and data placement
    5. RDD is a memory base system: high-speed but error-prone
        1. Fault tolerance is important: through lineage retrieval 
            - (經由紀錄對原始數據的操作，讓錯誤發生時可以重新生成RDD)
        2. Lazy Evaluation: a RDD will not be created until a output job
2. RDD operations
    1. Transformations: to build RDDs through deterministic operation s on other RDDs
        1. map, filter, join
        2. they are lazy operation
    2. action to return or export value
        1. count, collect, save, reduce-like
        2. triggers execution
    3. Steps
        1. build operator Directed Acyclic Graph (DAG)(有向無環圖)
        2. split graph into stages of tasks
        3. launch tasks via cluster manager
        4. execute task
3. Spark vs Hadoop
    1. Spark has a DAG execution engine; Hadoop only supports Map and Reduce
    2. Spark supports im-memory cluster (RDD); Hadoop's intermediate data has to be on disk
    3. Spark has rich data processing APIs; Hadoop only uses Map and Reduce
    4. Spark runs on myriad storage engines; Hadoop runs in HDFS


## M7U1L2 Apache Spark ecosystem
1. Apache Spark
    1. Spark SQL API
    2. Spark Streaming: real-time processing
    3. MLib: for machine learning
    4. GraphX
2. Spark Streaming
    1. chop up the stream into batch of seconds data
    2. Spark treats each batch of data as RDDs and processes them
    3. results are returned in batches

3. Example: Twitter Stream
    ```scala
    // Scala

    // get a stream data from twitterStream API
    // store in memory as a sequence of RDD (Dstream)
    val tweets = ssc.twitterStream(<Twitter username>, <Twitter password>)

    // flatMap status to a new Dstream
    val hashTags = tweets.flatMap (status => getTags(status))

    // save hashTags to disk (HDFS)
    hashTags.saveAsHadoop3

    // count the hashtag over last 10 mins
    // window is 10 mins long, move window every 1 secs
    cal tagCounts = hashTag.window(Minutes(10), Seconds(1)).countByValue()
    // similar to the preceding line, but with improved performance
    cal tagCounts = hashTag.countByValueAndWindow(Minutes(10), Seconds(1))
    ```
    1. for fault tolerance
        1. RDD remember the sequence of operations that created if from the original input
        2. since we get data from Twitter API, for fault tolerance, we need to
            1. replicate Tweets RDDs in memory of multiple worker nodes
            2. or output Tweets RDDs to external entity (like HDFS)
    2. Dstream: sequence of RDDs
    3. `window`, `countByValueAndWindow`:stateful operations
    4. `foreach`: do things with each batch of results

## M7U2 Spatial Data 空間數據
1. between spatial compared to general data
    1. Very tied to the physical space
    2. Multi-dimensional (three dimension, time...)
    3. Complex geometrical shapes
    5. New query API needs
2. Spacial Data Example: NYC Taxi Trips in SQL
    1. data is stored in tables
    2. Range Query: search for trips within a specified range
        1. Define a latitude and longitude boundary (經緯度範圍)
        2. Filter the data row by row
    3. k-nearest neighbors (KNN) Query:
        1. Specify coordinates
        2. Calculate the distance from each data point to a given coordinate
        3. Sort by distance
        4. Find the k nearest
    4. Direct SQL queries are less efficient
    5. Extend SQL to Support Spatial Data: use PostGIS for Example
    ```sql
    SELECT Restaurant.name
    FROM city, restaurant
    -- ST_Contains: Spatial Transmission Contains; geom: geometry
    WHERE ST_Contains(city.geom, restaurant.geom)
    AND city.name = 'Tempe'
    ```

3. Spacial Data Example: NYC Taxi Trips in NoSQL
    1. Most NoSQL databases support spatial data processing
    2. use mongoDB for Example
    ```cpp
    Var neighborhood = db.neighborhoods.findOne({
    geometry:{$geoIntersects: {$geometry: {type:
    “Point”, coordinates: [-73.93414657,
    40.82302903]}}}})

    Db.restaurants.find({location: {$geoWithin:{
    $geometry: neighborhood.geometry}}}).count()
    ```

4. Spatial data in Spark: Geospark
    1. Geospark is now an Apache top-level project, rebranded as Apache Sedona.
    2. main Components
        1. new APIs to perform spatial data queries
        2. Spatial Query Processing Layer
            1. Range: using multiple points.
            2. Range join:　merge multiple ranges into a single, larger range.
            3. Distance
            4. Distance join: the distance between a point and a line defined by another distance.
            5. KNN
        3. Spatial RDD Layer
            1. It partitions data according to spatial relationships
            2. Spatial index
            3. Geometrical Operation Library
    3. SQL-like Query Example
    ```sql
    SELECT superhero.name
    FROM city, superhero
    WHERE ST_Contains(city.geom, superhero.geom)
    AND city.name = 'Gotham'
    ```
    
