# Module 4: Distributed and Parallel Database System
## M4U1L1 Distribution relational database
1. Benefits: sharing information and services
    1. availability
    2. scalability
    3. reliability/fault tolerance
    4. transparency: make use of the distributed database the same as a centralized database
    5. performance
2. Distributed DBMS environment
    1. logically interrelated databases
    2. communicate through network
    3. have a management/main node and many distributed node

# M4U2L1 Fragmentation
1. Correctness of Fragmentation
    1. Completeness: fragmentation will not result in any loss of data.
    2. Reconstruction: guaranteed to be a operation to reconstruct the original data from the fragmented pieces
    3. Disjointness: Each data fragment will contain unique data (before replication).
2. Horizontal Fragmentation: Fragmentation based on range of keys (rows)
3. Derived Horizontal Fragmentation: Fragmentation
    1. To fragment multiple related tables. Based on one table's key
    2. example
        1. there is a link between salary table S and employee table E
        2. fragment S by salary greater or less then 20
        2. also fragment E by salary greater or less then 20
4. Vertical Fragmentation:
    1. Fragmentation based on columns
    2. attribute affinities: Related attributes should be grouped into the same fragment
        1. the relationship is determined by the query
        2. example
            1. Numbers of queries related to A1 and A2 are 50
            2. Numbers of queries related to A1 and A3 are 2
            3. Numbers of queries related to A2 and A3 are 3
            4. attribute affinity Matrix
                |  |A1|A2|A3|
                |--|--|--|--|
                |A1|  |  |  |
                |A2|50|  |  |
                |A3| 2| 3|  |
            5. A1 and A2 should be grouped into the same fragment
5. Large database fragmentation often involves multiple methods

## M4U2L2 Replication
1. Pros
    1. increased availability 
    2. faster query evaluation
2. Cons
    1. update are challenging
3. if read more then update, replication is advantageous
4. Optimization
    1. Cost: more replication usually cost more
        1. hardware cost
        2. communication cost
        3. update cost
        4. maintenance cost
    2. Performance
    3. Response time: queries' geographic location
    4. Throughput
    5. Constraints

## M4U3L1 Query Processing
1. high-level user query (like SQL) -> query processor -> Low-level commands for DBMS
2. query processor also need to optimize the query
3. if it is a distributed DBMS, there are more considerations for optimization (like communication costs.)
4. Query Optimization Process
    1. Input query: SQL
    2. Search space generation: find the database where the data is located
    3. Generate equivalent query execution plan(QEP)
    4. Filtering search strategies: perform a preliminary simulation based on a cost model
    5. If the costs of the strategies are similar, it revisit previous steps to gather more information and perform more detailed calculations. Detailed calculations can also be quite costly.
    6. Best QEP
5. Possible costs
    1. memory space
    2. I/O cost
    3. computing cost
    4. communication cost
    5. number of queries
    6. analysis cost


## M4U3L2 Distributed Query Processing
1. Local sites can also optimize for queries
2. Query Processing - Decomposition
    1. Normalization
        1. detect invalid expression
        2. convert valid expression to low-level commands (e.g., relational algebra) 
    2. Eliminate redundancy
        1. (A < 10) ∧ (A < 5) -> A < 5
        2.  sub-expressions: merge some redundant commands
3. Query Processing - Algebraic rewriting
    1. push conditions down before union : (e.g., reduce the size of the Cartesian product by applying partial conditions upfront)
    2. localization: replace relations by corresponding fragments
    3. The underlying idea is applying filters to the data to reduce the dataset size before further processing.


## M4U3L3 Total Cost of a Query Execution Plan
1. Total cost/time = CPU cost + I/O cost + communication cost
    1. CUP cost = unit instruction cost * number of instructions
    2. I/O cost = unit cost * number
    3. communication cost = message initiation cost + transmission cost
2. cost calculation
    1. A more accurate  calculation is more costly.
    2. Calculate primary cost factor first
    3. Simplifying assumption: (e.g., the data is normally distributed or uniformly distributed.)
    4. In most cases, time is of the essence


## M4U4 Parallel DBMS
1. Parallel database types:
    1. Pipeline Parallelism: many machines each doing one step in a multi-step process
    2. Partition Parallelism: many machines doing the same thing to different pieces of dat
2. benefit
    1. Speed-Up: ideally, increasing one unit of resource can increase one unit of throughput.
    2. Scale-Up: Ideally, a linear increase in both data and resources would yield a constant processing time.
3. Parallel DBMS architecture
    1. Shared Memory: many computer share single memory. Easy to program, difficult to build and scale up (vertical scaling only).
    2. Shared Disk: many computer with its own memory share many disk
    3. Shared Nothing: many computer with its own memory and disk. Difficult to program, Easy to build and horizontal scaling.
4. Parallel DBMS types:
    1. intra-operator parallelism: all machines computing a given operation
    2. inter-operator parallelism: each operator may run concurrently on a different machines (pipelining)
    3. inter-query parallelism: different queries run on different machines
5.  Data Partitioning
    1. Range
    2. Hash
    3. Round Robin: Each new piece of data is stored in a different machines
6. Partial Scans/Select
    1. Scan in parallel, and merge.
    2. Selection may only require a range or a hash partition
    3. Indexes can be built at each partition
7. Parallel Sorting
    1. Scan in parallel, then distribute data among computers by range-partition.
    2. "local sorting" on each computers
    3. skew: Depending on the selected attribute, some computers may receive significantly more data than others
    4. sample the data at start to determine partition points to avoid skew
8. Parallel Join
    1. Nested loop: Each outer tuple must be compared with each inner tuple that might join.
    2. Sort-Merge: Sorting gives range-partitioning then merging locally


## Knowledge Check Quiz
1. Which of the following operations is not part of query decomposition?
    -  Local optimization
2. What is the correct order of tasks in a typical distributed query processing?
    - Decomposition, Localization, Optimization 
3. In which type of database parallelism do all machines work together to compute a given operation at the same time?
    - Intra-operator parallelism
4. In which step of the query optimization process should the cost model be considered?
    - When developing a search strategy
5. What does query decomposition mean?
    - Mapping of SQL commands to algebraic operations such as Select, Project, and Join.
6. What does data localization mean?
    - Applying data distribution information to algebraic operations such as Select, Project, and Join.