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
            1. Example:
            2. `(key1, "Apple is sweet")`
            3. -> `[(Apple, 1), (is, 1), (sweet, 1)]`
        2. sort then assign to data nodes for reduce
        3. reduce function(key2,list(value2)) -> list(key, Value3)
            1. Example:
            2. `[(is, 1), (is, 1), (sweet, 1), (sweet, 1)]`
            3. -> `[(is, 2), (sweet, 2)]`
        4. Reduce only happens after all the maps are finished.
        
    
            