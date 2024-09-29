# Module 5: NoSQL Database System
## M5U1 NoSQL and CAP Theorem
1. SQL good at store number and string -> more
2. NoSQL features
    1. not fully support relational features (e.g., join, group by, order by)
    2. no declarative query language
    3. Relaxed ACID (fewer guarantees)
3. common NoSQL Categories
    1. Key-value: use key for indexing, e.g., DynamoDB
    2. document-base: e.g., MongoDB (Json)
    3. column-base: e.g., BigTable
    3. graph-base: e.g., Neo4j
4. Pros and Cons
    1. Key-value
        1. Pros
            1. fast
            2. scalable
            3. simple model
            4. able to distribute horizontally
        2. Cons: many data objects can't be easily modeled as key value pairs
    2. Schema-Less (other common NoSQL)
        1. Pros
            1. good performance and scalability
            2. many are distributed
            3. model is richer than key/value pairs
        2. Cons: typically no ACID transactions or relational features

5. Scaling in RDBMS
    1. Scaling up (vertical scaling)
    2. Scaling out (horizontal scaling)
        1. Master/Slave: low write, high read
        2. Sharding
            1. good for both reads and writes
            2. distributed query processing is challenging
6. CAP Theorem
    1. Consistency: eventual consistency
    2. Availability: better read and writes availability
    3. Partition-tolerance: still operate even with partial failure
    4. corresponding to ACID


## M5U2L1 Graph Databases
1. Example: Social Network
    1. nodes
        1. Persons
        2. Friends
        3. Photos
    2. queries
        1. Find Alice’s friends
        2. How Alice & Ed are connected
        3. Find Alice’s photos with friends
2. Graph Queries
    1. using regular expression (e.g., Neo4j)
    2. reachability
        1. Example: Find Alice’s photos
        2. `Photo-Tags-'Alice'`
        3. Search for path with node:type=Photo, edge:type=Tags, node:id='Alice'
    3. Attribute
        1. `Photo{date.year='2012'}-Tags-'Alice'`
        2. `(Photo|video)-Tags-'Alice'`
    4. Arbitrary length
        1. `'Alice'(-Manages-Person)*`
        2. start from node:id='Alice', find every nodes connect with edge:id=Manages, node:type=Person
3. Query execution
    1. distributed Breadth First Search
    2. Select -> Traverse -> Join
    3. Example: `'Alice'-Tags-Photo`
        1. find node:id='Alice' on every partition
        2. find edge:type=Tags
        3. if a edge connect to another partition, Communicate this to other departments
        4. find node:type=Photo
    3. Optimization
        1. Left to right
        2. Right to left
        3. Split then join
        4. ...
    4. The time complexity could be quite high (O(n^3))

## M5U2L2 Key Value Stores and Column
1. Key-Value DBMS requirements
    1. Availability
    2. Scalability (horizontal)
    3. Fault Tolerance
    4. Manageability
    5. Example: DynamoDB
        1. Simple operations to data with unique ID (keys)
        2. No operation span multiple record 沒有跨多紀錄運算
        3. Data stored as binary objects
        4. Eventual consistency
        5. Efficient: low response time for Service Level Agreements
        6. Semantic conflict resolution pushed to application
2. Key-Value DBMS Design Decision
    1. Scalability: add nodes on-demand with minimal impact
    2. Load Balancing
    3. Replication
        1. replicate on write: reduce read complexity
        2. replicate on read: reduce write complexity
            1. DynamoDB opts to decrease write complexity
3. Dynamo's interface
    1. put (key, context, object)
        1. context: vector clocks and history (needed for merging)
    2. got (key)
4. DynamoDB Partitioning Replication
    1. Consistent hashing, to put it simply
        1. Nodes are arranged in a rin
        2. When there is a need to replicate, copy the data to the next node
5. column-base DBMS example: BigTable
    1. Similar to RDBMS, but without relationships between tables.
    2. A single column can hold different data types.
6. BigTable structure
    1. Google File System (GFS)
        1. similar to Master/Slave DBMS
    2. MapReduce
    3. Chubby Lock service: lock for a particular cell
        1. stores more information on a lock
    4. Scheduler (Google Work Queue)
7. BigTable queries
    1. `<Row, Column, Timestamp>`: for key lookup, insert, and delete
    2. Column: a Column family can have multiple Column qualifiers.
    3. No table-wide integrity constraints
    4. No multi-row transactions
8. BigTable data storage
    1. SSTable
        1. Immutable, sorted file of key-value pairs
        2. Contains chunks of data plus an index
    2. Tablet
        1. have multiple SSTable
        2. SSTables can be shared between Tablet
        3. Contains some range of rows of the table
    3. Table:
        1. have multiple Tablets
        2. Tablets do not overlap, SSTables can overlap
    4. servers manage tablets, each tablet lives at only one server
    5. Master node responsible for load balancing and fault tolerance
    6. GFS responsible for replicates data


## M5U2L3 Document Stores
1. Created in response to the explosive growth of the internet
2. The data to be saved is varied
3. Document: html -> xml -> JSON
4. MongoDB stores data in BSON
    1. a binary representation of JSO
    2. optimized for performance and index
    3. compression
5. Example: MongoDB
    1. Creating indexes: `db.locations.ensureIndex({tags:1})`
    2. Regular expression: `db.locations.find({name:/^head_string/})`
    3. For more features, please search on your own...
```
location = {
    name:"Name",
        address:"Address",
        city:"City",
        zip:"10001",
    
    tags: ["tag_a", "tag_b"]
}
```
6. Unsharded Deployment
    1. Configure as a replica set for automated failover
    2. Async replication between nodes
    3. Add more secondaries to scale reads (Master/Slave)
7. Sharded Deployment
    1. Mongo Config Server handles distribution and balancing
8. DocumentDB Advantage
    1. Documents are independent unit
        1. better performance
        2. easier to distribute data
    2. Application logic is easier to write
        1.  object model can directly turn into a document
    3. Unstructured data can be stored easily
        1. To update data, simply add a new key-value

