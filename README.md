# CMPSC-431W-project
This repository is a CLI based implementation of a SQL database using PostgreSQL 16.
The data tables come from https://www.kaggle.com/datasets/open-source-sports/baseball-databank
The tables used in the actual implementation are included in the folder labeled "Tables". This is becuase I did not include every single cloumn from the Kaggle dataset and I also split a few of the tables into multiple tables so that they would follow Boyce-Codd Normal Form (BCNF).
I have also included the Entity-Relationship Diagram from which the tales were based on.

## The following functionalities are implemented in the database management system:
1. Insert Data: Allow adding new records to tables.
2. Delete Data: Enable removing specific records from tables.
3. Update Data: Support modifying existing records in tables.
4. Search Data: Allow finding records based on specified criteria.
5. Aggregate Functions: Perform calculations like sum, average, count, min, and max on data.
6. Sorting: Enable arranging query results based on specified columns.
7. Joins: Combine data from multiple tables using relationships.
8. Grouping: Group query results based on specified columns.
9. Subqueries: Support nested operations within queries.
10. Transactions: Ensure consistency and reliability of database operations.
11. Error Handling: Catch and handle exceptions gracefully during database operations
12. Exit: Exits the CLI entirely

## In order to use the CLI program properly the following steps must be followed:
1. First you muct select one of the above functionalities you would like to complete by typing in the number corresponding to that functionality.
2. Follow the on-screen instructions provided and when you have finished typing you response, press the enter key.
3. You may not exit a functionality once you have selected it, so make sure you choose the correct one.
4. While not in the middle of a functionality, you may exit the program entirely.
5. If you are inputting string values for an attribute make sure to put quotation marks around the values (single or double is fine).
6. If you incorrectly input values an error will be given after you have inputted all the information requested. The error will let you know which portion of your input was not compatible with the functionality you were attempting to implement.
7. When you have successfully implement a selected functionality either the results of that query or a success message will be given. After which you may select another functionality or exit the program.
8. '>>' indicates that the input requested is going to be used in a query.
9. '>>>>' indicates you may now select one of the functionalities given in the welcome message.
    
## Detailed descriptions of each Functionality:
1. INSERT
   - Allow adding new records to tables.
2. 
