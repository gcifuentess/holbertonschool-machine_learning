# 0x02. Databases

## Resources :books:
Read or watch:

---
## Learning Objectives :bulb:
What you should learn from this project:

* What’s a relational database
* What’s a none relational database
* What is difference between SQL and NoSQL
* How to create tables with constraints
* How to optimize queries by adding indexes
* What is and how to implement stored procedures and functions in MySQL
* What is and how to implement views in MySQL
* What is and how to implement triggers in MySQL
* What is ACID
* What is a document storage
* What are NoSQL types
* What are benefits of a NoSQL database
* How to query information from a NoSQL database
* How to insert/update/delete information from a NoSQL database
* How to use MongoDB

---

## Links to Files :file_folder:

### [0. Create a database](./0-create_database_if_missing.sql)
* Write a script that creates the database db_0 in your MySQL server.


### [1. First table](./1-first_table.sql)
* Write a script that creates a table called first_table in the current database in your MySQL server.


### [2. List all in table](./2-list_values.sql)
* Write a script that lists all rows of the table first_table in your MySQL server.


### [3. First add](./3-insert_value.sql)
* Write a script that inserts a new row in the table first_table in your MySQL server.


### [4. Select the best](./4-best_score.sql)
* Write a script that lists all records with a score >= 10 in the table second_table in your MySQL server.


### [5. Average](./5-average.sql)
* Write a script that computes the score average of all records in the table second_table in your MySQL server.


### [6. Temperatures #0](./6-avg_temperatures.sql)
* Import in hbtn_0c_0 database this table dump: download


### [7. Temperatures #2](./7-max_state.sql)
* Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)


### [8. Genre ID by show](./8-genre_id_by_show.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download


### [9. No genre](./9-no_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download 


### [10. Number of shows by genre](./10-count_shows_by_genre.sql)
* Import the database dump from hbtn_0d_tvshows to your MySQL server: download 


### [11. Rotten tomatoes](./11-rating_shows.sql)
* Import the database hbtn_0d_tvshows_rate dump to your MySQL server: download


### [12. Best genre](./12-rating_genres.sql)
* Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download


### [13. We are all unique!](./13-uniq_users.sql)
* Write a SQL script that creates a table users following these requirements:


### [14. In and not out](./14-country_users.sql)
* Write a SQL script that creates a table users following these requirements:


### [15. Best band ever!](./15-fans.sql)
* Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans


### [16. Old school band](./16-glam_rock.sql)
* Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity


### [17. Buy buy buy](./17-store.sql)
* Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.


### [18. Email validation to sent](./18-valid_email.sql)
* Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.


### [19. Add bonus](./19-bonus.sql)
* Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.


### [20. Average score](./20-average_score.sql)
* Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.


### [21. Safe divide](./21-div.sql)
* Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.


### [22. List all databases](./22-list_databases)
* Write a script that lists all databases in MongoDB.


### [23. Create a database](./23-use_or_create_database)
* Write a script that creates or uses the database my_db:


### [24. Insert document](./24-insert)
* Write a script that inserts a document in the collection school:


### [25. All documents](./25-all)
* Write a script that lists all documents in the collection school:


### [26. All matches](./26-match)
* Write a script that lists all documents with name="Holberton school" in the collection school:


### [27. Count](./27-count)
* Write a script that displays the number of documents in the collection school:


### [28. Update](./28-update)
* Write a script that adds a new attribute to a document in the collection school:


### [29. Delete by match](./29-delete)
* Write a script that deletes all documents with name="Holberton school" in the collection school:


### [30. List all documents in Python](./30-all.py)
* Write a Python function that lists all documents in a collection:


### [31. Insert a document in Python](./31-insert_school.py)
* Write a Python function that inserts a new document in a collection based on kwargs:


### [32. Change school topics](./32-update_topics.py)
* Write a Python function that changes all topics of a school document based on the name:


### [33. Where can I learn Python?](./33-schools_by_topic.py)
* Write a Python function that returns the list of school having a specific topic:


### [34. Log stats](./34-log_stats.py)
* Write a Python script that provides some stats about Nginx logs stored in MongoDB:


### [35. Optimize simple search](./100-index_my_names.sql)
* Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.


### [36. Optimize search and score](./101-index_name_score.sql)
* Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.


### [37. No table for a meeting](./102-need_meeting.sql)
* Write a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.


### [38. Average weighted score](./103-average_weighted_score.sql)
* Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.


### [39. Regex filter](./104-find)
* Write a script that lists all documents with name starting by Holberton in the collection school:


### [40. Top students](./105-students.py)
* Write a Python function that returns all students sorted by average score:


### [41. Log stats - new version](./106-log_stats.py )
* Improve 34-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs:

---

## Author
* **Gabriel Cifuentes** - [gcifuentess](https://github.com/gcifuentess)


---
---

# *HBTN PROJECT:*


![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/1/9649007e163d3f014a46.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220309%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220309T225016Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4e7cf29a48425aa99b2aaaf0fc332804c2db081b720e76b6a2e5fa6a9c299c3e)


After fetching data via APIs, storing them is also really important for training a Machine Learning model.


You have multiple option: 


* Relation database
* Not Relation database
* Key-Value storage
* Document storage
* Data Lake
* etc.


In this project, you will touch the first 2: relation and not relation database.


Relation databases are mainly used for application, not for source of data for training your ML models, but it can be really useful for the data processing, labeling and injection in another data storage. In this project, you will play with basic SQL commands but also create automation and computing on your data directly in SQL - less load at your application level since the computing power is dispatched to the database.


Not relation databases, known as NoSQL, will give you flexibility on your data: document, versioning, not a fix schema, no validation to improve performance, complex lookup, etc.


Resources
---------


**Read or watch**:


* MySQL:
	+ [What is Database & SQL?](https://intranet.hbtn.io/rltoken/4iEQPoYZrI0gwzf8Oh9xrQ "What is Database & SQL?")
	+ [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/H8uUw93po3lj8SYPEDupSg "MySQL Cheat Sheet")
	+ [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/UP6ueU3eUTEj0U0xU-9pBA "MySQL 5.7 SQL Statement Syntax")
	+ [MySQL Performance: How To Leverage MySQL Database Indexing](https://intranet.hbtn.io/rltoken/6UgmWa0wvDAC11VKBTDHfQ "MySQL Performance: How To Leverage MySQL Database Indexing")
	+ [Stored Procedure](https://intranet.hbtn.io/rltoken/CWCXdKG0Rv9oeyRZPfL-4g "Stored Procedure")
	+ [Triggers](https://intranet.hbtn.io/rltoken/bPZ-uwznI-ynPg_wVkg9RA "Triggers")
	+ [Views](https://intranet.hbtn.io/rltoken/moa3QlE8qKR1x-cfQo786A "Views")
	+ [Functions and Operators](https://intranet.hbtn.io/rltoken/oy1_ueDdXR2FdI1pb_G0JQ "Functions and Operators")
	+ [Trigger Syntax and Examples](https://intranet.hbtn.io/rltoken/J9R8qLW8CAAjCSTz9R9yTw "Trigger Syntax and Examples")
	+ [CREATE TABLE Statement](https://intranet.hbtn.io/rltoken/2EsRzUQc_SYEezEKrknRlA "CREATE TABLE Statement")
	+ [CREATE PROCEDURE and CREATE FUNCTION Statements](https://intranet.hbtn.io/rltoken/QALbcWcfMrfyifFXdWFcZQ "CREATE PROCEDURE and CREATE FUNCTION Statements")
	+ [CREATE INDEX Statement](https://intranet.hbtn.io/rltoken/G5iUoR6uBpLXNAlH2bAjSw "CREATE INDEX Statement")
	+ [CREATE VIEW Statement](https://intranet.hbtn.io/rltoken/WIOV_d5KAXYBssFzN3rXng "CREATE VIEW Statement")
* NoSQL:
	+ [NoSQL Databases Explained](https://intranet.hbtn.io/rltoken/JtrFE1Dfpn12iuv0ieLkzQ "NoSQL Databases Explained")
	+ [What is NoSQL ?](https://intranet.hbtn.io/rltoken/LAfX9ZUu763LFZAwb8gcAw "What is NoSQL ?")
	+ [Building Your First Application: An Introduction to MongoDB](https://intranet.hbtn.io/rltoken/OsYxp_-MEzj7RWd3zEW48w "Building Your First Application: An Introduction to MongoDB")
	+ [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://intranet.hbtn.io/rltoken/O_AwY40S_lzoAXrPbqeQCA "MongoDB Tutorial 2 : Insert, Update, Remove, Query")
	+ [Aggregation](https://intranet.hbtn.io/rltoken/NtR645bGNduOeeQ4fCV2iw "Aggregation")
	+ [Introduction to MongoDB and Python](https://intranet.hbtn.io/rltoken/Y7VsI8r5r85G_s4Tqv7Jnw "Introduction to MongoDB and Python")
	+ [mongo Shell Methods](https://intranet.hbtn.io/rltoken/d5PF_1NZwdcKlsvD5yPHNg "mongo Shell Methods")
	+ [The mongo Shell](https://intranet.hbtn.io/rltoken/dp9YuYFiOE81me_DqY89EA "The mongo Shell")


Learning Objectives
-------------------


At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/pIRalmFSaulEKIr1Yjecsw "explain to anyone"), **without the help of Google**:


### General


* What’s a relational database
* What’s a none relational database
* What is difference between SQL and NoSQL
* How to create tables with constraints
* How to optimize queries by adding indexes
* What is and how to implement stored procedures and functions in MySQL
* What is and how to implement views in MySQL
* What is and how to implement triggers in MySQL
* What is ACID
* What is a document storage
* What are NoSQL types
* What are benefits of a NoSQL database
* How to query information from a NoSQL database
* How to insert/update/delete information from a NoSQL database
* How to use MongoDB


Requirements
------------


### General


* A `README.md` file, at the root of the folder of the project, is mandatory
* All your SQL files will be executed on Ubuntu 16.04 LTS (or 18.04) using `MySQL 5.7` (version 5.7.30)
* All your SQL queries should have a comment just before (i.e. syntax above)
* All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
* All your Mongo files will be interpreted/compiled on Ubuntu 16.04 LTS (or 18.04) using `MongoDB` (version 4.2)
* The first line of all your Mongo files should be a comment: `// my comment`
* All your Python files will be interpreted/compiled on Ubuntu 16.04 LTS (or 18.04) using `python3` (version 3.5 or 3.7) and `PyMongo` (version 3.10)
* The first line of all Python your files should be exactly `#!/usr/bin/env python3`
* Your Python code should use the `pycodestyle` style (version 2.5.*)
* All your Python modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your Python functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`
* Your Python code should not be executed when imported (by using `if __name__ == "__main__"`:)
* All your files should end with a new line
* The length of your files will be tested using `wc`


More Info
---------


### MySQL


#### Comments for your SQL file:



```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

#### Install locally



```
$  sudo apt-get install mysql-server
...
$ mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.31-0ubuntu0.16.04.1 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

```

#### Use “container-on-demand” to run MySQL


* Ask for container `Ubuntu 18.04 - Python 3.7`
* Connect via SSH
* Or via the WebTerminal
* In the container, you should start MySQL before playing with it:



```
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$

```

**In the container, credentials are `root/root`**


#### How to import a SQL dump



```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$

```

### MongoDB


#### Install MongoDB 4.2


[Official installation guide](https://intranet.hbtn.io/rltoken/LR58L0Dq-ipe1KVm6D7Xgg "Official installation guide")



```
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'

```

Potential issue if documents creation doesn’t work or this error: `Data directory /data/db not found., terminating` ([source](https://intranet.hbtn.io/rltoken/3KCcy_chtJlZl0U4qMYhUw "source") and [source](https://intranet.hbtn.io/rltoken/q-SrUv6LVACyW9l9av3agg "source"))



```
$ sudo mkdir -p /data/db

```

#### Use “container-on-demand” to run MongoDB


* Ask for container `Ubuntu 18.04 - MongoDB`
* Connect via SSH
* Or via the WebTerminal
* In the container, you should start MongoDB before playing with it:



```
$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
$

```


Tasks
-----

###  0. Create a database

Write a script that creates the database `db_0` in your MySQL server.

* If the database `db_0` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements


```
guillaume@ubuntu:~/$ cat 0-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ echo "SHOW databases;" | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
db_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 0-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 

```
###  1. First table

Write a script that creates a table called `first_table` in the current database in your MySQL server.

* `first_table` description:
	+ `id` INT
	+ `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `first_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements


```
guillaume@ubuntu:~/$ cat 1-first_table.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ echo "SHOW TABLES;" | mysql -hlocalhost -uroot -p db_0
Enter password: 
Tables_in_db_0
first_table
guillaume@ubuntu:~/$ 

```
###  2. List all in table

Write a script that lists all rows of the table `first_table` in your MySQL server.

* All fields should be printed
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat 2-list_values.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ 

```
###  3. First add

Write a script that inserts a new row in the table `first_table` in your MySQL server.

* New row:
	+ `id` = `89`
	+ `name` = `Holberton School`
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat 3-insert_value.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 2-list_values.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ cat 3-insert_value.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-insert_value.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 2-list_values.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
id  name
89  Holberton School
89  Holberton School
89  Holberton School
guillaume@ubuntu:~/$ 

```
###  4. Select the best

Write a script that lists all records with a `score >= 10` in the table `second_table` in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat setup.sql
-- Create table and insert data
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES (1, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (2, "Roy", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (4, "Bryan", 8);

guillaume@ubuntu:~/$ cat setup.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 4-best_score.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$ 

```
###  5. Average

Write a script that computes the score average of all records in the table `second_table` in your MySQL server.

* The result column name should be `average`
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat setup.sql
-- Create table and insert data
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES (1, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (2, "Roy", 5);
INSERT INTO second_table (id, name, score) VALUES (3, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (4, "Bryan", 8);

guillaume@ubuntu:~/$ cat setup.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
guillaume@ubuntu:~/$ cat 5-average.sql | mysql -hlocalhost -uroot -p db_0
Enter password: 
average
9.25
guillaume@ubuntu:~/$ 

```
###  6. Temperatures #0

Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql "download")

* GitHub repository: `holbertonschool-machine_learning`
* Directory: `pipeline/0x02-databases`
* File: `6-avg_temperatures.sql`


```
guillaume@ubuntu:~/$ cat 6-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
guillaume@ubuntu:~/$ 

```
###  7. Temperatures #2

Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql "download") (same as `Temperatures #0`)

* GitHub repository: `holbertonschool-machine_learning`
* Directory: `pipeline/0x02-databases`
* File: `7-max_state.sql`


```
guillaume@ubuntu:~/$ cat 7-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$ 

```
###  8. Genre ID by show

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download")

* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat 8-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$ 

```
###  9. No genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") 

* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat 9-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title   genre_id
Better Call Saul    NULL
Homeland    NULL
guillaume@ubuntu:~/$ 

```
###  10. Number of shows by genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql "download") 

* Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`
* First column must be called `genre`
* Second column must be called `number_of_shows`
* Don’t display a genre that doesn’t have any shows linked
* Results must be sorted in descending order by the number of shows linked
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat 10-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
genre   number_of_shows
Drama   5
Comedy  4
Mystery 2
Crime   2
Suspense    2
Thriller    2
Adventure   1
Fantasy 1
guillaume@ubuntu:~/$ 

```
###  11. Rotten tomatoes

Import the database `hbtn_0d_tvshows_rate` dump to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql "download")

* Each record should display: `tv_shows.title` - `rating sum`
* Results must be sorted in descending order by the rating
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat 11-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password: 
title   rating
Better Call Saul    163
Homeland    145
Silicon Valley  82
Game of Thrones 79
Dexter  24
House   21
Breaking Bad    16
The Last Man on Earth   10
The Big Bang Theory 0
New Girl    0
guillaume@ubuntu:~/$ 

```
###  12. Best genre

Import the database dump from `hbtn_0d_tvshows_rate` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql "download")

* Each record should display: `tv_genres.name` - `rating sum`
* Results must be sorted in descending order by their rating
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command


```
guillaume@ubuntu:~/$ cat 12-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password: 
name    rating
Drama   150
Comedy  92
Adventure   79
Fantasy 79
Mystery 45
Crime   40
Suspense    40
Thriller    40
guillaume@ubuntu:~/$ 

```
###  13. We are all unique!

Write a SQL script that creates a table `users` following these requirements:

* With these attributes:
	+ `id`, integer, never null, auto increment and primary key
	+ `email`, string (255 characters), never null and unique
	+ `name`, string (255 characters)
* If the table already exists, your script should not fail
* Your script can be executed on any database


```
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 13-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name
1   bob@dylan.com   Bob
2   sylvie@dylan.com    Sylvie
bob@dylan:~$ 

```
###  14. In and not out

Write a SQL script that creates a table `users` following these requirements:

* With these attributes:
	+ `id`, integer, never null, auto increment and primary key
	+ `email`, string (255 characters), never null and unique
	+ `name`, string (255 characters)
	+ `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
* If the table already exists, your script should not fail
* Your script can be executed on any database


```
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
bob@dylan:~$ 
bob@dylan:~$ cat 14-country_users.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
bob@dylan:~$ 
bob@dylan:~$ echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id  email   name    country
1   bob@dylan.com   Bob US
2   sylvie@dylan.com    Sylvie  CO
3   john@dylan.com  John    US
bob@dylan:~$ 

```
###  15. Best band ever!

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

* Import this table dump: [metal\_bands.sql.zip](https://holbertonintranet.s3.amazonaws.com/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220309%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220309T225016Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=78f1d29eb1edbb7fdbfeacf2fedbb2c472971b0c0fc7d59915e8a3709073666c "metal_bands.sql.zip")
* Column names must be: `origin` and `nb_fans`
* Your script can be executed on any database


```
bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 15-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA 99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
bob@dylan:~$ 

```
###  16. Old school band

Write a SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity

* Import this table dump: [metal\_bands.sql.zip](https://holbertonintranet.s3.amazonaws.com/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220309%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220309T225016Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=78f1d29eb1edbb7fdbfeacf2fedbb2c472971b0c0fc7d59915e8a3709073666c "metal_bands.sql.zip")
* Column names must be:
	+ `band_name`
	+ `lifespan` until 2020 (in years)
* You should use attributes `formed` and `split` for computing the `lifespan`
* Your script can be executed on any database


```
bob@dylan:~$ cat metal_bands.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 16-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name   lifespan
Alice Cooper    56
Mötley Crüe   34
Marilyn Manson  31
The 69 Eyes 30
Hardcore Superstar  23
Nasty Idols 0
Hanoi Rocks 0
bob@dylan:~$ 

```
###  17. Buy buy buy

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

* GitHub repository: `holbertonschool-machine_learning`
* Directory: `pipeline/0x02-databases`
* File: `17-store.sql`


```
bob@dylan:~$ cat 17-init.sql
-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");

bob@dylan:~$ 
bob@dylan:~$ cat 17-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 17-store.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 17-main.sql
Enter password: 
-- Show and add orders
SELECT * FROM items;
SELECT * FROM orders;

INSERT INTO orders (item_name, number) VALUES ('apple', 1);
INSERT INTO orders (item_name, number) VALUES ('apple', 3);
INSERT INTO orders (item_name, number) VALUES ('pear', 2);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;

bob@dylan:~$ 
bob@dylan:~$ cat 17-main.sql | mysql -uroot -p holberton 
Enter password: 
name    quantity
apple   10
pineapple   10
pear    10
--
--
name    quantity
apple   6
pineapple   10
pear    8
item_name   number
apple   1
apple   3
pear    2
bob@dylan:~$ 

```
###  18. Email validation to sent

Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

* GitHub repository: `holbertonschool-machine_learning`
* Directory: `pipeline/0x02-databases`
* File: `18-valid_email.sql`


```
bob@dylan:~$ cat 18-init.sql
-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);

bob@dylan:~$ 
bob@dylan:~$ cat 18-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 18-valid_email.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 18-main.sql
Enter password: 
-- Show users and update (or not) email
SELECT * FROM users;

UPDATE users SET valid_email = 1 WHERE email = "bob@dylan.com";
UPDATE users SET email = "sylvie+new@dylan.com" WHERE email = "sylvie@dylan.com";
UPDATE users SET name = "Jannis" WHERE email = "jeanne@dylan.com";

SELECT "--";
SELECT * FROM users;

UPDATE users SET email = "bob@dylan.com" WHERE email = "bob@dylan.com";

SELECT "--";
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 18-main.sql | mysql -uroot -p holberton 
Enter password: 
id  email   name    valid_email
1   bob@dylan.com   Bob 0
2   sylvie@dylan.com    Sylvie  1
3   jeanne@dylan.com    Jeanne  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
--
--
id  email   name    valid_email
1   bob@dylan.com   Bob 1
2   sylvie+new@dylan.com    Sylvie  0
3   jeanne@dylan.com    Jannis  1
bob@dylan:~$ 

```
###  19. Add bonus

Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

* Procedure `AddBonus` is taking 3 inputs (in this order):
	+ `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)
	+ `project_name`, a new or already exists `projects` - if no `projects.name` found in the table, you should create it
	+ `score`, the score value for the correction


```
bob@dylan:~$ cat 19-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score int default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 19-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 19-bonus.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 19-main.sql
Enter password: 
-- Show and add bonus correction
SELECT * FROM projects;
SELECT * FROM corrections;

SELECT "--";

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Python is cool", 100);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "Bonus project", 100);
CALL AddBonus((SELECT id FROM users WHERE name = "Bob"), "Bonus project", 10);

CALL AddBonus((SELECT id FROM users WHERE name = "Jeanne"), "New bonus", 90);

SELECT "--";

SELECT * FROM projects;
SELECT * FROM corrections;

bob@dylan:~$ 
bob@dylan:~$ cat 19-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name
1   C is fun
2   Python is cool
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name
1   C is fun
2   Python is cool
3   Bonus project
4   New bonus
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
2   2   100
2   3   100
1   3   10
2   4   90
bob@dylan:~$ 

```
###  20. Average score

Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student.

* Procedure `ComputeAverageScoreForUser` is taking 1 input:
	+ `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)


```
bob@dylan:~$ cat 20-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score int default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("C is fun");
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 20-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 20-average_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 20-main.sql
-- Show and compute average score
SELECT * FROM users;
SELECT * FROM corrections;

SELECT "--";
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 20-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  0
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
--
--
id  name    average_score
1   Bob 0
2   Jeanne  82
bob@dylan:~$ 

```
###  21. Safe divide

Write a SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

* You must create a function
* The function `SafeDiv` takes 2 arguments:
	+ `a`, INT
	+ `b`, INT
* And returns `a / b` or 0 if `b == 0`


```
bob@dylan:~$ cat 21-init.sql
-- Initial
DROP TABLE IF EXISTS numbers;

CREATE TABLE IF NOT EXISTS numbers (
    a int default 0,
    b int default 0
);

INSERT INTO numbers (a, b) VALUES (10, 2);
INSERT INTO numbers (a, b) VALUES (4, 5);
INSERT INTO numbers (a, b) VALUES (2, 3);
INSERT INTO numbers (a, b) VALUES (6, 3);
INSERT INTO numbers (a, b) VALUES (7, 0);
INSERT INTO numbers (a, b) VALUES (6, 8);

bob@dylan:~$ cat 21-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 21-div.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT (a / b) FROM numbers;" | mysql -uroot -p holberton
Enter password: 
(a / b)
5.0000
0.8000
0.6667
2.0000
NULL
0.7500
bob@dylan:~$ 
bob@dylan:~$ echo "SELECT SafeDiv(a, b) FROM numbers;" | mysql -uroot -p holberton
Enter password: 
SafeDiv(a, b)
5
0.800000011920929
0.6666666865348816
2
0
0.75
bob@dylan:~$ 

```
###  22. List all databases

Write a script that lists all databases in MongoDB.

* GitHub repository: `holbertonschool-machine_learning`
* Directory: `pipeline/0x02-databases`
* File: `22-list_databases`


```
guillaume@ubuntu:~/$ cat 22-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/$

```
###  23. Create a database

Write a script that creates or uses the database `my_db`:

* GitHub repository: `holbertonschool-machine_learning`
* Directory: `pipeline/0x02-databases`
* File: `23-use_or_create_database`


```
guillaume@ubuntu:~/$ cat 22-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ cat 23-use_or_create_database | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
guillaume@ubuntu:~/$

```
###  24. Insert document

Write a script that inserts a document in the collection `school`:

* The document must have one attribute `name` with value “Holberton school”
* The database name will be passed as option of `mongo` command


```
guillaume@ubuntu:~/$ cat 24-insert | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nInserted" : 1 })
bye
guillaume@ubuntu:~/$

```
###  25. All documents

Write a script that lists all documents in the collection `school`:

* The database name will be passed as option of `mongo` command


```
guillaume@ubuntu:~/$ cat 25-all | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/$

```
###  26. All matches

Write a script that lists all documents with `name="Holberton school"` in the collection `school`:

* The database name will be passed as option of `mongo` command


```
guillaume@ubuntu:~/$ cat 26-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/$

```
###  27. Count

Write a script that displays the number of documents in the collection `school`:

* The database name will be passed as option of `mongo` command


```
guillaume@ubuntu:~/$ cat 27-count | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
1
bye
guillaume@ubuntu:~/$

```
###  28. Update

Write a script that adds a new attribute to a document in the collection `school`:

* The script should update only document with `name="Holberton school"` (all of them)
* The update should add the attribute `address` with the value “972 Mission street”
* The database name will be passed as option of `mongo` command


```
guillaume@ubuntu:~/$ cat 28-update | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 26-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school", "address" : "972 Mission street" }
bye
guillaume@ubuntu:~/$ 

```
###  29. Delete by match

Write a script that deletes all documents with `name="Holberton school"` in the collection `school`:

* The database name will be passed as option of `mongo` command


```
guillaume@ubuntu:~/$ cat 29-delete | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "acknowledged" : true, "deletedCount" : 1 }
bye
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ cat 26-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
bye
guillaume@ubuntu:~/$ 

```
###  30. List all documents in Python

Write a Python function that lists all documents in a collection:

* Prototype: `def list_all(mongo_collection):`
* Return an empty list if no document in the collection
* `mongo_collection` will be the `pymongo` collection object


```
guillaume@ubuntu:~/$ cat 30-main.py
#!/usr/bin/env python3
""" 30-main """
from pymongo import MongoClient
list_all = __import__('30-all').list_all

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ ./30-main.py
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
guillaume@ubuntu:~/$ 

```
###  31. Insert a document in Python

Write a Python function that inserts a new document in a collection based on `kwargs`:

* Prototype: `def insert_school(mongo_collection, **kwargs):`
* `mongo_collection` will be the `pymongo` collection object
* Returns the new `_id`


```
guillaume@ubuntu:~/$ cat 31-main.py
#!/usr/bin/env python3
""" 31-main """
from pymongo import MongoClient
list_all = __import__('30-all').list_all
insert_school = __import__('31-insert_school').insert_school

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ ./31-main.py
New school created: 5a8f60cfd4321e1403ba7abb
[5a8f60cfd4321e1403ba7ab9] Holberton school
[5a8f60cfd4321e1403ba7aba] UCSD
[5a8f60cfd4321e1403ba7abb] UCSF 505 Parnassus Ave
guillaume@ubuntu:~/$ 

```
###  32. Change school topics

Write a Python function that changes all topics of a school document based on the name:

* Prototype: `def update_topics(mongo_collection, name, topics):`
* `mongo_collection` will be the `pymongo` collection object
* `name` (string) will be the school name to update
* `topics` (list of strings) will be the list of topics approached in the school


```
guillaume@ubuntu:~/$ cat 32-main.py
#!/usr/bin/env python3
""" 32-main """
from pymongo import MongoClient
list_all = __import__('30-all').list_all
update_topics = __import__('32-update_topics').update_topics

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ ./32-main.py
[5a8f60cfd4321e1403ba7abb] UCSF 
[5a8f60cfd4321e1403ba7aba] UCSD 
[5a8f60cfd4321e1403ba7ab9] Holberton school ['Sys admin', 'AI', 'Algorithm']
[5a8f60cfd4321e1403ba7abb] UCSF 
[5a8f60cfd4321e1403ba7aba] UCSD 
[5a8f60cfd4321e1403ba7ab9] Holberton school ['iOS']
guillaume@ubuntu:~/$ 

```
###  33. Where can I learn Python?

Write a Python function that returns the list of school having a specific topic:

* Prototype: `def schools_by_topic(mongo_collection, topic):`
* `mongo_collection` will be the `pymongo` collection object
* `topic` (string) will be topic searched


```
guillaume@ubuntu:~/$ cat 33-main.py
#!/usr/bin/env python3
""" 33-main """
from pymongo import MongoClient
list_all = __import__('30-all').list_all
insert_school = __import__('31-insert_school').insert_school
schools_by_topic = __import__('33-schools_by_topic').schools_by_topic

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    j_schools = [
        { 'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
        { 'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        { 'name': "UCLA", 'topics': ["C", "Python"]},
        { 'name': "UCSD", 'topics': ["Cassandra"]},
        { 'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ ./33-main.py
[5a90731fd4321e1e5a3f53e3] Holberton school ['Algo', 'C', 'Python', 'React']
[5a90731fd4321e1e5a3f53e5] UCLA ['C', 'Python']
guillaume@ubuntu:~/$ 

```
###  34. Log stats

Write a Python script that provides some stats about Nginx logs stored in MongoDB:

* Database: `logs`
* Collection: `nginx`
* Display (same as the example):
	+ first line: `x logs` where `x` is the number of documents in this collection
	+ second line: `Methods:`
	+ 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
	+ one line with the number of documents with:
		- `method=GET`
		- `path=/status`


```
guillaume@ubuntu:~/$ curl -o dump.zip -s "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-webstack/411/dump.zip"
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ unzip dump.zip
Archive:  dump.zip
   creating: dump/
   creating: dump/logs/
  inflating: dump/logs/nginx.metadata.json  
  inflating: dump/logs/nginx.bson    
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ mongorestore dump
2018-02-23T20:12:37.807+0000    preparing collections to restore from
2018-02-23T20:12:37.816+0000    reading metadata for logs.nginx from dump/logs/nginx.metadata.json
2018-02-23T20:12:37.825+0000    restoring logs.nginx from dump/logs/nginx.bson
2018-02-23T20:12:40.804+0000    [##......................]  logs.nginx  1.21MB/13.4MB  (9.0%)
2018-02-23T20:12:43.803+0000    [#####...................]  logs.nginx  2.88MB/13.4MB  (21.4%)
2018-02-23T20:12:46.803+0000    [#######.................]  logs.nginx  4.22MB/13.4MB  (31.4%)
2018-02-23T20:12:49.803+0000    [##########..............]  logs.nginx  5.73MB/13.4MB  (42.7%)
2018-02-23T20:12:52.803+0000    [############............]  logs.nginx  7.23MB/13.4MB  (53.8%)
2018-02-23T20:12:55.803+0000    [###############.........]  logs.nginx  8.53MB/13.4MB  (63.5%)
2018-02-23T20:12:58.803+0000    [#################.......]  logs.nginx  10.1MB/13.4MB  (74.9%)
2018-02-23T20:13:01.803+0000    [####################....]  logs.nginx  11.3MB/13.4MB  (83.9%)
2018-02-23T20:13:04.803+0000    [######################..]  logs.nginx  12.8MB/13.4MB  (94.9%)
2018-02-23T20:13:06.228+0000    [########################]  logs.nginx  13.4MB/13.4MB  (100.0%)
2018-02-23T20:13:06.230+0000    no indexes to restore
2018-02-23T20:13:06.231+0000    finished restoring logs.nginx (94778 documents)
2018-02-23T20:13:06.232+0000    done
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ ./34-log_stats.py 
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
guillaume@ubuntu:~/$ 

```
###  35. Optimize simple search

Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

* Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
* Only the first letter of `name` must be indexed


```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (2.19 sec)
mysql> 
mysql> exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 100-index_my_names.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SHOW index FROM names;
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name       | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)
mysql> 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
+-------------+
| COUNT(name) |
+-------------+
|      302936 |
+-------------+
1 row in set (0.82 sec)
mysql> 
mysql> exit
bye
bob@dylan:~$ 

```
###  36. Optimize search and score

Write a SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

* Import this table dump: [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip "names.sql.zip")
* Only the first letter of `name` AND `score` must be indexed


```
bob@dylan:~$ cat names.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| count(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (2.40 sec)
mysql> 
mysql> exit
bye
bob@dylan:~$ 
bob@dylan:~$ cat 101-index_name_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ mysql -uroot -p holberton
Enter password: 
mysql> SHOW index FROM names;
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table | Non_unique | Key_name             | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| names |          1 | idx_name_first_score |            1 | name        | A         |          25 |        1 | NULL   | YES  | BTREE      |         |               |
| names |          1 | idx_name_first_score |            2 | score       | A         |        3901 |     NULL | NULL   | YES  | BTREE      |         |               |
+-------+------------+----------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
2 rows in set (0.00 sec)
mysql> 
mysql> SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
+-------------+
| COUNT(name) |
+-------------+
|       60717 |
+-------------+
1 row in set (0.48 sec)
mysql> 
mysql> exit
bye
bob@dylan:~$ 

```
###  37. No table for a meeting

Write a SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

* The view `need_meeting` should return all students name when:
	+ They score are under (strict) to 80
	+ **AND** no `last_meeting` date **OR** more than a month


```
bob@dylan:~$ cat 102-init.sql
-- Initial
DROP TABLE IF EXISTS students;

CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(255) NOT NULL,
    score INT default 0,
    last_meeting DATE NULL 
);

INSERT INTO students (name, score) VALUES ("Bob", 80);
INSERT INTO students (name, score) VALUES ("Sylvia", 120);
INSERT INTO students (name, score) VALUES ("Jean", 60);
INSERT INTO students (name, score) VALUES ("Steeve", 50);
INSERT INTO students (name, score) VALUES ("Camilia", 80);
INSERT INTO students (name, score) VALUES ("Alexa", 130);

bob@dylan:~$ cat 102-init.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 102-need_meeting.sql | mysql -uroot -p holberton
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 102-main.sql
-- Test view
SELECT * FROM need_meeting;

SELECT "--";

UPDATE students SET score = 40 WHERE name = 'Bob';
SELECT * FROM need_meeting;

SELECT "--";

UPDATE students SET score = 80 WHERE name = 'Steeve';
SELECT * FROM need_meeting;

SELECT "--";

UPDATE students SET last_meeting = CURDATE() WHERE name = 'Jean';
SELECT * FROM need_meeting;

SELECT "--";

UPDATE students SET last_meeting = ADDDATE(CURDATE(), INTERVAL -2 MONTH) WHERE name = 'Jean';
SELECT * FROM need_meeting;

SELECT "--";

SHOW CREATE TABLE need_meeting;

SELECT "--";

SHOW CREATE TABLE students;

bob@dylan:~$ 
bob@dylan:~$ cat 102-main.sql | mysql -uroot -p holberton
Enter password: 
name
Jean
Steeve
--
--
name
Bob
Jean
Steeve
--
--
name
Bob
Jean
--
--
name
Bob
--
--
name
Bob
Jean
--
--
View    Create View character_set_client    collation_connection
XXXXXX<yes, here it will display the View SQL statement :-) >XXXXXX
--
--
Table   Create Table
students    CREATE TABLE `students` (\n  `name` varchar(255) NOT NULL,\n  `score` int(11) DEFAULT '0',\n  `last_meeting` date DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
bob@dylan:~$ 

```
###  38. Average weighted score

Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUser` that computes and store the average weighted score for a student.

* Procedure `ComputeAverageScoreForUser` is taking 1 input:
	+ `user_id`, a `users.id` value (you can assume `user_id` is linked to an existing `users`)


```
bob@dylan:~$ cat 103-init.sql
-- Initial
DROP TABLE IF EXISTS corrections;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    average_score float default 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS projects (
    id int not null AUTO_INCREMENT,
    name varchar(255) not null,
    weight int default 1,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS corrections (
    user_id int not null,
    project_id int not null,
    score float default 0,
    KEY `user_id` (`user_id`),
    KEY `project_id` (`project_id`),
    CONSTRAINT fk_user_id FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
    CONSTRAINT fk_project_id FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
);

INSERT INTO users (name) VALUES ("Bob");
SET @user_bob = LAST_INSERT_ID();

INSERT INTO users (name) VALUES ("Jeanne");
SET @user_jeanne = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES ("C is fun", 1);
SET @project_c = LAST_INSERT_ID();

INSERT INTO projects (name, weight) VALUES ("Python is cool", 2);
SET @project_py = LAST_INSERT_ID();


INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_c, 80);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 96);

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_c, 91);
INSERT INTO corrections (user_id, project_id, score) VALUES (@user_jeanne, @project_py, 73);

bob@dylan:~$ 
bob@dylan:~$ cat 103-init.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 103-average_weighted_score.sql | mysql -uroot -p holberton 
Enter password: 
bob@dylan:~$ 
bob@dylan:~$ cat 103-main.sql
-- Show and compute average weighted score
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

CALL ComputeAverageWeightedScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";
SELECT * FROM users;

bob@dylan:~$ 
bob@dylan:~$ cat 103-main.sql | mysql -uroot -p holberton 
Enter password: 
id  name    average_score
1   Bob 0
2   Jeanne  82
id  name    weight
1   C is fun    1
2   Python is cool  2
user_id project_id  score
1   1   80
1   2   96
2   1   91
2   2   73
--
--
id  name    average_score
1   Bob 0
2   Jeanne  79
bob@dylan:~$ 

```
###  39. Regex filter

Write a script that lists all documents with `name` starting by `Holberton` in the collection `school`:

* The database name will be passed as option of `mongo` command


```
guillaume@ubuntu:~/$ cat 104-find | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton school" }
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton School" }
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton-school" }
bye
guillaume@ubuntu:~/$

```
###  40. Top students

Write a Python function that returns all students sorted by average score:

* Prototype: `def top_students(mongo_collection):`
* `mongo_collection` will be the `pymongo` collection object
* The top must be ordered
* The average score must be part of each item returns with key = `averageScore`


```
guillaume@ubuntu:~/0x0D$ cat 105-main.py
#!/usr/bin/env python3
""" 105-main """
from pymongo import MongoClient
list_all = __import__('30-all').list_all
insert_school = __import__('31-insert_school').insert_school
top_students = __import__('105-students').top_students

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students

    j_students = [
        { 'name': "John", 'topics': [{ 'title': "Algo", 'score': 10.3 },{ 'title': "C", 'score': 6.2 }, { 'title': "Python", 'score': 12.1 }]},
        { 'name': "Bob", 'topics': [{ 'title': "Algo", 'score': 5.4 },{ 'title': "C", 'score': 4.9 }, { 'title': "Python", 'score': 7.9 }]},
        { 'name': "Sonia", 'topics': [{ 'title': "Algo", 'score': 14.8 },{ 'title': "C", 'score': 8.8 }, { 'title': "Python", 'score': 15.7 }]},
        { 'name': "Amy", 'topics': [{ 'title': "Algo", 'score': 9.1 },{ 'title': "C", 'score': 14.2 }, { 'title': "Python", 'score': 4.8 }]},
        { 'name': "Julia", 'topics': [{ 'title': "Algo", 'score': 10.5 },{ 'title': "C", 'score': 10.2 }, { 'title': "Python", 'score': 10.1 }]}
    ]
    for j_student in j_students:
        insert_school(students_collection, **j_student)

    students = list_all(students_collection)
    for student in students:
        print("[{}] {} - {}".format(student.get('_id'), student.get('name'), student.get('topics')))

    top_students = top_students(students_collection)
    for student in top_students:
        print("[{}] {} => {}".format(student.get('_id'), student.get('name'), student.get('averageScore')))

guillaume@ubuntu:~/0x0D$ 
guillaume@ubuntu:~/0x0D$ ./105-main.py
[5a90776bd4321e1ec94fc408] John - [{'title': 'Algo', 'score': 10.3}, {'title': 'C', 'score': 6.2}, {'title': 'Python', 'score': 12.1}]
[5a90776bd4321e1ec94fc409] Bob - [{'title': 'Algo', 'score': 5.4}, {'title': 'C', 'score': 4.9}, {'title': 'Python', 'score': 7.9}]
[5a90776bd4321e1ec94fc40a] Sonia - [{'title': 'Algo', 'score': 14.8}, {'title': 'C', 'score': 8.8}, {'title': 'Python', 'score': 15.7}]
[5a90776bd4321e1ec94fc40b] Amy - [{'title': 'Algo', 'score': 9.1}, {'title': 'C', 'score': 14.2}, {'title': 'Python', 'score': 4.8}]
[5a90776bd4321e1ec94fc40c] Julia - [{'title': 'Algo', 'score': 10.5}, {'title': 'C', 'score': 10.2}, {'title': 'Python', 'score': 10.1}]
[5a90776bd4321e1ec94fc40a] Sonia => 13.1
[5a90776bd4321e1ec94fc40c] Julia => 10.266666666666666
[5a90776bd4321e1ec94fc408] John => 9.533333333333333
[5a90776bd4321e1ec94fc40b] Amy => 9.366666666666665
[5a90776bd4321e1ec94fc409] Bob => 6.066666666666667
guillaume@ubuntu:~/0x0D$ 

```
###  41. Log stats - new version

Improve `34-log_stats.py` by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`:

* The IPs top must be sorted (like the example below)


```
guillaume@ubuntu:~/$ ./106-log_stats.py 
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
IPs:
    172.31.63.67: 15805
    172.31.2.14: 15805
    172.31.29.194: 15805
    69.162.124.230: 529
    64.124.26.109: 408
    64.62.224.29: 217
    34.207.121.61: 183
    47.88.100.4: 166
    45.249.84.250: 160
    216.244.66.228: 150
guillaume@ubuntu:~/$ 

```
---
