# Module 2: Relational Model & SQL Query Language
### M2U1L1 Relational Data Model
1. Relational Data Model
    1. relation: table
    2. tuple: column, (d1,d2,...,dn)
    3. attribute: row
    4. domain: the range of each attribute
2. Relational Database
    1. a set of relations
    2. unordered
3. Cartesian product: the set of all ordered pairs
    1. e.g., A deck of cards
    2. ranks {A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2}: 13 elements
    3. suits {spade, heart, diamond, club}: 4 elements
    4. the Cartesian product of these sets is 13*4 = 52
    5. Calculate all possible tuples of a table using the Cartesian product.
4. Query Language
    1. Procedural/Imperative Language:
        1. perform a sequence of operators to compute a result
        2. e.g., relational algebra
    2. Non-Procedural/Declarative Language: 
        1. Tells what data is to be retrieved but does not tell the system how to retrieve the data
        2. e.g., relational calculus and SQL
### M2U1L2 Relational Algebra Query Language
1. union
    1. `r ∪ s = { t | t ∈ r ∨ t ∈ s }`
    2. schema must be same
    3. will remove duplicate elements
    4. example
        1. List the student information for either computer science or electrical engineering majors
        2. `cse_majors ∪ eee_majors`

2. difference
    1. `r - s = { t | t ∈ r ∧ t ∉ s}`
    2. schema must be same
    3. example
        1. List the student information for computer science majors, who are not double majors in electrical engineering.
        2. `cse_majors - eee_majors`
        3. won't show eee_majors only students

3. cartesian_product
    1. `r × s = { t | t = tr ts where tr ∈ r ∧ ts ∈ s }`
    2. schema can be different
    3. example
        1. List all possible combinations of computer science professors teaching computer science courses.
        3. `cse_profs × cse_courses`

4. selection
    1. `σ p (r)`
    2. select a subset of rows.
    3. `p` is condition
    4. example
        1. List the student information for seniors who are majoring in computer science
        2. `σ class='SR' (cse_majors)`
        3. selection will iterate through table and keep rows satisfying the conditions

5. projection
    1. `π A (r)`
    2. select a subset of columns.
    3. `A` is attribute
    4. projection and selection are commonly combined in a single operation
    5. example
        1. List the name and id of students who are computer science majors
        2. `π id, name (cse_majors)`

6. Intersection
    1. `r ∩ s ≡ r - (r - s)`
    2. schema must be same
    3. example
        1. List the student information for those students who are double majoring in computer science and electrical engineering
        2. `cse_majors ∩ eee_major`

7. θ-Join
    1. θ-Join (r × s)
    2. combination (`cartesian_product`) then selection (`θ`)
    3. example: List combinations of students and courses have the same classroom


### M2U2L1 SQL 
1. basic SQL Query
    1. target_lists: columns
    2. relation_lists: tables
    3. qualifications: conditions
    4. direct semantics of an SQL query example
        ```sql
        SELECT [DISTINCT] target_lists
        FROM relation_lists
        WHERE qualifications
        ```
        1. compute the **cross-product** of `relation_lists`
        2. discard resulting tuples if they fail `qualifications` (**projection**)
        3. delete attributes that are not in `target_lists` (**selection**)
        4. if `DISTINCT`=`UNIQUE` is specified, eliminate duplicate rows
    5. An DBMS optimizer will find more efficient strategies to compute the same answers
        1. the Cartesian product is computationally expensive
2. SQL Query examples
    1. Find sid's of sailors who've reserved a red or a green boat: Union
    ```sql
    SELECT S.sid
    FROM Sailors S, Boats B, Reserves R
    WHERE S.sid=R.sid AND R.bid=B.bid AND (B.color='red' OR B.color='green')

    -- same as
    SELECT S.sid
    FROM Sailors S, Boats B, Reserves R
    WHERE S.sid=R.sid AND R.bid=B.bid AND B.color='red'

    UNION
    SELECT S.sid
    FROM Sailors S, Boats B, Reserves R
    WHERE S.sid=R.sid AND R.bid=B.bid AND B.color='green'
    ```

    2. Find sid's of sailors who've reserved a red and a green boat: Intersect
    ```sql
    SELECT S.sid
    FROM Sailors S, Boats B, Reserves R
    WHERE S.sid=R.sid AND R.bid=B.bid AND (B.color='red' AND B.color='green')

    -- same as
    SELECT S.sid
    FROM Sailors S, Boats B, Reserves R
    WHERE S.sid=R.sid AND R.bid=B.bid AND B.color='red'

    INTERSECT
    SELECT S.sid
    FROM Sailors S, Boats B, Reserves R
    WHERE S.sid=R.sid AND R.bid=B.bid AND B.color='green'
    ```

3. Nested Queries
    1. WHERE clause can contain an SQL query. DBMS will compute what's inside the nest
    2. `IN`= `EXISTS`, `NOT IN`
    3. Using Nested Queries might be batter the doing Cartesian product
    4. example: Find names of sailors who've reserved boat #103
    ```sql
    SELECT S.sname
    From Sailors S
    Where S.sid IN (SELECT S.sname
                    From Reserves R
                    WHERE R.bid=103)
    ```



    

