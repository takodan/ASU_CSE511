# Module 6: MapReduce
## M6U1 in MapReduce
1. Hadoop: open source version of MapReduce

2. Data Management
    1. split data
    2. store: workers (nodes) execute map
    3. read: workers (nodes) execute reduce
    4. output file

3. Hadoop distributed file system (HDFS)
    1. similar to google file system
    2. Single namespace for entire cluster, this NameNode/MetadataNode store Key-metadata
    3. Files split into 64MB, 128MB or 1GB blocks
    4. Replicates blocks (key-data) store on 3 or more data nodes for fault-tolerance
    5. Centralized name node point to many data nodes
    6. Optimized for large files, sequential reads
    7. Files are append only (no update on data nodes) for maximize output


4. MapReduce Framework (main node)
    1. Pushes nodes execute map and reduce function
    2. Manages work distribution and fault-tolerance
    3. key-value records
    4. Execution steps
        1. split data to data nodes for map
        1. map function(key1, value1) -> list(key2,value2)
            1. Example: key = word, value = number of times
            2. `(key1, "Apple is sweet")`
            3. -> `[(Apple, 1), (is, 1), (sweet, 1)]`
        2. sort then assign to data nodes for reduce
        3. reduce function(key2,list(value2)) -> list(key, Value3)
            1. Example:
            2. `[(is, 1), (is, 1), (sweet, 1), (sweet, 1)]`
            3. -> `[(is, 2), (sweet, 2)]`
        4. Reduce only happens after all the maps are finished.

5. MapReduce Execution Details
    1. Mappers (data nodes for map) preferentially placed on same node or same rack as their input block
    2. Mappers save outputs to local disk before serving to reducers
    3. If a task crashes
        1. Retry on another node
        2. OK for a map because it had no dependencies
        3. OK for reduce because map outputs are on the disk
    4. If a node crashes
        1. Re-launch its current tasks on other nodes
        2. Re-launch any maps the node previously ran because outputs on the disk are lost

6. Operators in MapReduce
    1. Select row (WHERE): You can filter the data by setting specific conditions during the mapping process
    2. Projection (SELECT): By setting the columns we want to discard as keys before the mapping, they'll be excluded from the output
    3. Sorting: By setting the columns we want to sorted as keys in the mapping, the map reduce will sort the data based on that key, 
    4. Group: Use the reduce function during the reduce step
        1. Example: Group picture
            1. after map, there are `[(Blue, 1), (Green, 1), (Green, 1), (Green, 1)]`
            2. reduce `[(Blue, 1), (Green, (1, 2, 3))]`
            3. The value here is not a frequency but an identifier


7.  Apache Hadoop ecosystem
    1. Hive: SQL-like API on top of Hadoop
    2. Pig: using Pig Latin language to create complex data flow programs on top of Hadoop
    3. Hbase: Google BigTable
    4. Zookeeper: distributed configuration service