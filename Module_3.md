# Module 3: Data Storage and Indexing
## M3U1L1 Introduction to Data Storage
1. Memory Hierarchy: CPU Cache -> Memory -> External Storage (HDD, SSD, etc.)
2. Buffer manager stages pages(固定大小的資料) from external storage to the main memory buffer pool.
3. File and/or index layers make calls to the buffer manager.

## M3U1L2 Alternative File Organizations
1. File Organizations
    1. Heap Files
        1. random order
        2. Suitable when access is a file scan retrieving all records
    2. Sorted Files
        1. Best if records must be retrieved in some order
        2.  or only a range of records is needed
    3. Indexes
        1. Data structures to organize records via trees or hashing
2. The Database Cost Model
    1. Page access cost is usually the dominant cost
    2. An accurate cost model is too complex for analyzing

3. Heap Files
    1. Header Page (point to)-> Data page -> (another) Data page -> (another) Data page ->...
    2. Efficient:
        1. for bulk loading data. (當讀取批量/連續數據是高效的)
        2. for relatively small relations, as indexing overheads are avoided. (當資料關聯較小時是高效的(免去建立索引的開銷))
        3. when queries need to fetch a large proportion of stored records. (讀取大量資料數據是高效的(建立排序/索引的成本過高))
    3. Not Efficient:
        1. for selective queries.
        2. for sorting

4. Indexes
    1. Speeds up selections on the search key fields
    2. Any subset of the fields of a relation can be the search key for an index on the relation.
    3. B+ Tree Indexes
        1. Non-leaf pages as index, leaf pages sorted by search key
        2. (利用數狀結構建立索引，從根節點可以快速的找到位於葉節點的資料)
        3. (例如要找標記為數字7的資料，可以利用每個非葉節點二分資料縮小資料範圍(大於5指向a，小於5指向b)，來快速找到目標的資料)
    4. Hash based Index

## M3U2L2 Index Classification
1. Primary Index: the search key contains the primary key
2. Clustered Index: the order of data records is the same as the order of data entries
    1. usually the index only clustered on the most search key
3. Workload
    1. The data used for indexing is typically determined by its workload.
    2. query in the workload
        1. the relations it accesses
        2. retrieved attributes (WHERE)
        3. selection/join conditions
        4. the type of selection (precise or range)
    3. update in the workload
        1. the type of update (INSERT/DELETE/UPDATE) and the attributes that are affected
        2. indexed attributes should be subject to minimal changes
4. When Creating a New Index
    1. Consider the most important/common queries
    2. Consider the best plan using the current indexes
    3. Determine if a better plan is possible with an additional index
5. Composite Search Keys
    1. The clustering method is determined by the order of attributes in the composite search key
    2. more important attributes should be placed first
6. By selecting a good index, it is possible to read only the index and reduce the need to read the records.

## M3U3L1 Principles of Transactions Intro ACID Properties
1. transaction: the DBMS's abstract view of a user program, a sequence of reads and writes
2. database state when a transaction process
    1. begin: database in a consistent state
    2. execution: temporarily in an inconsistent state
    3. end: back to a consistent state
3. Concurrency
    1. The concurrency implementation determines the processing speed when many users submit transactions.
    2. Concurrency is achieved by the DBMS
    3. Each transaction must leave the database in a consistent state. Otherwise, it will crash.

4. Principle of Transactions (ACID)
    1. atomicity (不可分割性)
        1. all or nothing
        2. Always executing all actions in a transaction, or not executing any actions at all.
    2. consistency
        1. no violation of integrity constraints
        2. e.g., referential integrity
    3. isolation
        1. changes must be serializable
        2. If several transactions are executed concurrently, the results must be the same as if they were executed serially in order.
    4. durability
        1. committed updates persist
        2. guarantee the results of operations will never be lost


## M3U4L1 Lock Based Concurrency Control
1. Strict Two-phase Locking (Strict 2PL) Protocol
    1. Shared Lock before reading
    2. Exclusive Lock before writing
    3. released all locks when the transaction completes
    4. strict 2PL allows only serializable schedules
    5. Locking and unlocking are atomic operations (one operation at a time)
    5. transaction that holds a Shared Lock can be upgraded to hold an Exclusive Lock
2. Deadlocks
    1. Cycle of transactions waiting for locks to be released by each other
    2. Create a waits-for graph to detect Deadlock
 

## M3U4L2 Database Recovery
1. if a transaction stop during an execution, database may be in an inconsistent state
2. Types of Failures
    1. Transaction failures: unilaterally or due to deadlock
    2. System failure
    3. Media failure: secondary storage failure, hardware controller failure
    4. communication failure
3. Local Recovery Management Architecture
    1. secondary storage (e.g, HDD) is generally more stable.
    2. Transactions are handled in a volatile memory and written to secondary storage by the Database Buffer Manager only after transactions is complete.
4. In-Place Update Recovery Information
    1. Every action of a transaction also write a log record to an append-only file.
    2. object, old value, new value, and action are recorded in the log
    3. log record must saved before the database change happened
    4. recovering phases: analysis -> redo(rewrite with the new value) or undo(rewrite with the old value)


## M3U5L1 Concurrency Control
1. Scheduling Transactions
    1. Serial schedule
    2. Equivalent Schedule
    3. Serializable Schedule: all Serial schedule's Equivalent Schedule is Serializable Schedule
    4. Conflict Serializable Schedules
        1. conflict: involve the actions (belong to different transactions) to the same data 
        2. conflict equivalent: every pair of conflicting actions is ordered the same way
            1. transaction_A has actions_A and actions_B
            2. transaction_C has actions_C and actions_D
            3. if actions_ABCD has same result as actions_ACBD, it is conflict serializable
            4. ABCD and ACBD are both A before C and B before D


