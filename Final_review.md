## Practice questions
1. three levels of abstraction
    0. M1U2L2
    1. views: what user see
    2. conceptual/logical schema: it defines the logical structure that is used for the data. developer design
    3. single physical schema: it describes the files and indexes used. DBMS controls

2. advantage of using a DBMS
    0. M1U2L1
    1. Data Independence
    2. Efficient Data Access
    3. Data Integrity and Security
    4. Data Administration
    5. Concurrent Access 併發訪問
    6. Crash Recovery
    7. Reduced App Development Time

3. designing a database phases
    0. M1U3L1
    1. Requirement Analysis
    2. Conceptual Database Design 概念數據庫設計 (Build ER diagram)
    3. Logical Database Design (Convert ER diagram to relational database schema)

4. An entity is described using a set of attributes
    0. M1U3L1

5. primary key: a unique attribute for each entity
    0. M1U3L1

6. Ternary Relationship: a relationship that connects three entities
    0. M1U3L2?
    1. Multiple Relationship
    2. Binary Relationship (e.g., 員工實體"屬於"部門實體)
    3. Unary Relationship (e.g.,員工實體"管理"員工實體)
    4. Ternary Relationship (e.g.,顧客 產品 訂單)

7. Basic SQL querie: SELECT columns FROM table WHERE condition
    0. M2U2L1

8. intersection 交集, union 聯集
    0. M2U1L2

9. DISTINCT command is used to eliminate duplicate rows from query results
    0. M2U2L1

10. Theta Join
    0. M2U1L2
    1. join with condition

11. hardware in decreasing order of speed: CPU Registers > L2 > L3 > Hard disk
    0. M3U1L1

12. The buffer manager loads pages from external storage devices to the main memory buffer pool
    0. M3U1L1

13. Heap Files storage
    0. M3U1L2
    1. Random order store
    2. Suitable when access is a file scan retrieving all records
    3. Efficient for frequent insertions
    4. Inefficient for queries that need to search for specific records, as the entire file must be traversed.

14. Sorted Files
    0. M3U1L2
    1. Best if records must be retrieved in some order
    2. or only a range of records is needed
    3. Efficient for queries and range searches
    4. Inefficient for insertions and deletions, as the data must remain in order

15. Indexes
    0. M3U1L2
    1. Data structures to organize records via B+ trees or hashing
    2. Tree structures are ideal for range queries
    3. Hashing is best suited for equality-based searches (e.g., finding a specific record by its unique key)

16. ER diagram
    0. M1U3L1

17. SQL query
    0. M1U3L3, M2U2L1

18. Cartesian product
    0. M2U1L2
19. relational algebra
    0. M2U1L2

20. clustered index, unclustered index
    0. M3U2L2
21. B+ tree index
    0. M3U2L1
21. hash-based index
    0. M3U2L1

22. ACID
    0. M3U3L1
    1. Atomicity guarantees that all operations within a transaction are either
    2. Consistency ensures that the database remains in a consistent state before and after a transaction
    3. Isolation ensures that the operations of a transaction are not affected by other concurrent transactions.
    4. Durability ensures that once a transaction is committed, its changes are permanently saved and will not be lost.

23. schedule conflict serializable
    0. M3U4L2

24. Deadlock
    0. M3U4L1
    1. multiple transactions waiting for locks to be released by each other

25. Logging for recovering
    0. M3U4L2
    1. contains: Transaction Identifier, operation type, old value, new value, data item
    2. recovering phases: analysis -> redo(rewrite with the new value) or undo(rewrite with the old value)