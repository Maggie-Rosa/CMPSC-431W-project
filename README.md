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
6. If you incorrectly input values an error will be given after you have inputted all the information requested. The error will let you know which portion of your input was not compatible with the functionality you were attempting to implement, but the entire program will end as iff you exited.
7. When you have successfully implement a selected functionality either the results of that query or a success message will be given. After which you may select another functionality or exit the program.
8. '>>' indicates that the input requested is going to be used in a query.
9. '>>>>' indicates you may now select one of the functionalities given in the welcome message.
    
## Detailed descriptions of each Functionality:
1. Insert Data: Allow adding new records to tables.
   - This can be accomplished by typing 1 after the '>>>>'.
   - You will then type the name of the table you would like to insert into (ex. Franchise).
   - Then you will type the name of the columns you would like to insert into. You must list all the columns besides those that have '(optional)' after the name.
   - Then you will type the values you would like to insert for the previously selected attributes. Make sure you type them in the exact same order as the attributes you selected. For example, if you wanted to insert into the table 'Franchise' and selected to insert values for 'franhid' and 'franchname', you would have to first type the value for 'franchid' followed by the value for 'franchname' (ex. 'BRA', 'Brooklyn Atlantics'). Make sure if the values you are inserting are strings that you put quotes around them as demonstrated in the example.
   - Now if you have completed those steps properly you will receive a success message 'Successful insertion'.
     
2. Delete Data: Enable removing specific records from tables.
    - This can be accomplished by typing 2 after the '>>>>'.
    - You will then type the name of the table you would like to delete on (ex. Franchise).
    - Then you will type the WHERE condition upon which you want to perform the deletion (ex. franchid = 'BRA'). Make sure if the values you are comparing in the WHERE condition are strings that you put quotes around them as demonstrated in the example.
    - Now if you have completed those steps properly you will receive a success message 'Successful deletion'.
      
3. Update Data: Support modifying existing records in tables.
   - This can be accomplished by typing 3 after the '>>>>'.
   - You will then type the name of the table you would like to update on (ex. Franchise).
   - Then you will type the column names you would like to update followed  by their values you would like to set them equal to (ex. column1 = 'value1', column2 = value2, ...). Make sure if the values you are updating are strings that you put quotes around them as demonstrated in the example.
   - Then you will type the WHERE condition upon which you want to perform the update on (ex. franchid = 'BRA'). Make sure if the values you are comparing in the WHERE condition are strings that you put quotes around them as demonstrated in the example.
   - Now if you have completed those steps properly you will receive a success message 'Successful update'.
     
4. Search Data: Allow finding records based on specified criteria.
   - This can be accomplished by typing 4 after the '>>>>'.
   - You will then type the name of the table you would like to search on (ex. Franchise).
   - Then you will type the attributes you would like to search through. If you would like to see all the columns, just type '*'.
   - Then you will type the WHERE condition upon which you want to perform the search on (ex. franchid = 'BRA'). Make sure if the values you are searching for in the WHERE condition are strings that you put quotes around them as demonstrated in the example.
   - Now if you have completed those steps properly you will see the search results.
     
5. Aggregate Functions: Perform calculations like sum, average, count, min, and max on data.
   - This can be accomplished by typing 5 after the '>>>>'.
   - You will then type the name of the table you would like to perform an aggregate function on (ex. Franchise).
   - Then you type in the aggregate function you would like to utilize (ex. MAX)
   - Then you will type the attribute you would like to complete the previously selected aggregate function on.
   - Now if you have completed those steps properly you will see the results.
     
6. Sorting: Enable arranging query results based on specified columns.
   - This can be accomplished by typing 6 after the '>>>>'.
   - You will then type the name of the table you would like to sort on (ex. Franchise).
   -  Then you will type the attributes you would you like to sort by followed a space and then either ASC or DESC, separated by commas.
   -  Now if you have completed those steps properly you will see the results.
     
7. Joins: Combine data from multiple tables using relationships.
   - This can be accomplished by typing 7 after the '>>>>'.
   - You will then type the number of tables you would like to perform joins on.
   - Then type the names of the first table you would like to complete the joins on (ex. Franchise).
   - The you will type of the type of join you would like to perform on that table and the next selected tables.
   - The above two steps will be repeated for the number of times you previously selected.
   - Now if you have completed those steps properly you will see the results.
     
8. Grouping: Group query results based on specified columns.
   - This can be accomplished by typing 8 after the '>>>>'.
   - You will then type the name of the table you would like to sort on (ex. Franchise).
   - Then you will select the attributes you would like to select.
   - Then you will type the attributes you would you like to group by.
   - Now if you have completed those steps properly you will see the results.
     
9. Subqueries: Support nested operations within queries.
   - This can be accomplished by typing 9 after the '>>>>'.
   - You will then type the number of subqueries you would like to perform.
   - Then type the name of the first table you would like to complete the subquery on (ex. Franchise).
   - The you will type of the type the attributes you would like to select
   - The above two steps will be repeated for the number of times you previously selected.
   - Now if you have completed those steps properly you will see the results.
     
10. Transactions: Ensure consistency and reliability of database operations.
    - This can be accomplished by typing 10 after the '>>>>'.
     
12. Error Handling: Catch and handle exceptions gracefully during database operations
    - This can be accomplished by typing 11 after the '>>>>'.
     
12. Exit: Exits the CLI entirely
    - This can be accomplished by typing 12 after the '>>>>'.
    - The program will then exit completely.
