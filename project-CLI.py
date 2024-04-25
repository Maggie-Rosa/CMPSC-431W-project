import psycopg2
import cmd

tableList = "\nChoose a Table by typing its name: \n1. Team\n2. Franchise\n3. Manager\n4. TeamID\n5. TeamWins\n6. Salary\n7. Pitchers\n8. Fielders\n9. Batters\n10. Players\n11. PlayerIDs\n12. AllStarPlayers\n13. AllStarGames\n14. HallOfFamePlayers\n>> "

teamAttributes = "teamid, yearid, lgid, rank, name, park (optional), attendance (optional), teamidbr (optional), franchid"
franchiseAttributes = "franchid, franchname, active (optional)"
managerAttributes = "yearid, teamid, inseason, rank (optional), playerid, games (optional)"
teamIDAttributes = "teamidbr, yearid, teamidlahman45, teamidretro"
teamWinsAttributes = "teamid, yearid, divwin (optional), wcwin (optional), lgwin (optional), wswin (optional)"
salaryAttributes = "salary, yearid, playerid, teamid"
pitchersAttributes = "playerid, yearid, teamid, wins, losses, games, gamestarts, completedgames"
fieldersAttributes = "playerid, yearid, teamid, games, position, errors (optional), assists (optional), passedball (optional), caughtstealing (optional), putouts (optional), doubleplays (optional)"
battersAttributes = "playerid, yearid, teamid, games, at_bats (optional), runs (optional), hits (optional), doubles (optional), triples (optional), homeruns(optional), rbis (optional), stolenbases (optional), caughtstealing (optional), walks (optional), strikeouts (optional), intentionalwalks (optional), hit_by_pitch (optional), sacrificebunts (optional), sacrificeflies (optional)"
playersAttributes = "playerid, birthyear (optional), birthmonth (optional), birthday (optional), birthcountry (optional), birthstate (optional), birthcity (optional), namefirst (optional), namelast, namegiven (optional), weight (optional), height (optional), debut (optional), finalgame (optional)"
playerIDAttributes = "playerid, retroid (optional), bbrefid (optional)"
allStarPlayerAttributes = "playerid, teamid, gameid, gp (optional), stratingpos (optional), gamenum"
allStarGameAttributes = "gameid, yearid"
hallOfFamePlayerAttributes = "playerid, yearid, ballots (optional), needed (optional), votes (optional), inducted, category"

functionalities = 'Please type in the number of the option you would like to proceed with: \n \n 1. Insert Data \n 2. Delete Data \n 3. Update Data \n 4. Search Data \n 5. Aggregate Functions \n 6. Sorting \n 7. Joins \n 8. Grouping \n 9. Subqueries \n 10. Transactions \n 11. Error Handling \n 12. Exit'

# Connect to postgres DB
connection = psycopg2.connect("dbname=baseballdb user=postgres password=cmpsc431")

# Open a cursor to perform database operations
cursor = connection.cursor()


class MyCLI(cmd.Cmd):
    prompt = '>>>> '
    intro = 'Welcome to the Baseball Database CLI Interface! \n \nPlease type in the number of the option you would like to proceed with: \n \n 1. Insert Data \n 2. Delete Data \n 3. Update Data \n 4. Search Data \n 5. Aggregate Functions \n 6. Sorting \n 7. Joins \n 8. Grouping \n 9. Subqueries \n 10. Transactions \n 11. Error Handling \n 12. Exit'

    # INSERT
    def do_1(self, line):
        """Print a greeting."""
        table = input(tableList)
        columnAttributes = teamAttributes
        if (table == "Team"):
            columnAttributes = teamAttributes
        elif (table == "Franchise"):
            columnAttributes = franchiseAttributes
        elif (table == "Manager"):
            columnAttributes = managerAttributes
        elif (table == "TeamID"):
            columnAttributes = teamIDAttributes
        elif (table == "TeamWins"):
            columnAttributes = teamWinsAttributes
        elif (table == "Salary"):
            columnAttributes = salaryAttributes
        elif (table == "Pitchers"):
            columnAttributes = pitchersAttributes
        elif (table == "Fielders"):
            columnAttributes = fieldersAttributes
        elif (table == "Batters"):
            columnAttributes = battersAttributes
        elif (table == "Players"):
            columnAttributes = playersAttributes
        elif (table == "PlayerIDs"):
            columnAttributes = playerIDAttributes
        elif (table == "AllStarPlayers"):
            columnAttributes = allStarPlayerAttributes
        elif (table == "AllStarGames"):
            columnAttributes = allStarGameAttributes
        elif (table == "HallOfFamePlayers"):
            columnAttributes = hallOfFamePlayerAttributes
 
        columns = input(f'Type the attributes you would like to insert separated by commas: {columnAttributes}\n>> ')
        values = input("Please type the values you would like to insert corresponding to the previous attributes you indicated you would like to give values for, in the same order (if the values are strings make sure to put quotation marks around them)\n>> ")

        # Execute an INSERT
        cursor.execute(f'INSERT INTO {table} ({columns}) VALUES ({values})')
    
        print("Successful insertion")
        print(functionalities)
        
    # DELETE
    def do_2(self, line):
        """Print a greeting."""
        table = input(tableList)
        whereCondition = input("Please type the WHERE condition you would like to delete on\n>> ")

        # Execute a DELETE
        cursor.execute(f'DELETE FROM {table} WHERE ({whereCondition})')
    
        print("Successful deletion")
        print(functionalities)

    # UPDATE
    def do_3(self, line): 
        """Print a greeting."""
        table = input(tableList)
        columnAttributes = teamAttributes
        if (table == "Team"):
            columnAttributes = teamAttributes
        elif (table == "Franchise"):
            columnAttributes = franchiseAttributes
        elif (table == "Manager"):
            columnAttributes = managerAttributes
        elif (table == "TeamID"):
            columnAttributes = teamIDAttributes
        elif (table == "TeamWins"):
            columnAttributes = teamWinsAttributes
        elif (table == "Salary"):
            columnAttributes = salaryAttributes
        elif (table == "Pitchers"):
            columnAttributes = pitchersAttributes
        elif (table == "Fielders"):
            columnAttributes = fieldersAttributes
        elif (table == "Batters"):
            columnAttributes = battersAttributes
        elif (table == "Players"):
            columnAttributes = playersAttributes
        elif (table == "PlayerIDs"):
            columnAttributes = playerIDAttributes
        elif (table == "AllStarPlayers"):
            columnAttributes = allStarPlayerAttributes
        elif (table == "AllStarGames"):
            columnAttributes = allStarGameAttributes
        elif (table == "HallOfFamePlayers"):
            columnAttributes = hallOfFamePlayerAttributes

        print(f'The following are columns you may update: {columnAttributes}')
        columnValues = input("Type the columnNames and the values you would like to set separated by commas, if the value is a string make sure to include the quotation marks around the value (ex. column1 = 'value1', column2 = value2, ...)\n>> ")
        whereCondition = input("Please type the WHERE condition you would like to update on or type N/A for no WHERE condition\n>> ")

        # Execute an UPDATE
        if (whereCondition == "N/A"):
            cursor.execute(f'UPDATE {table} SET {columnValues}')
        else:
            cursor.execute(f'UPDATE {table} SET {columnValues} WHERE ({whereCondition})')
    
        print("Successful update")
        print(functionalities)

    # SEARCH
    def do_4(self, line):
        """Print a greeting."""
        table = input(tableList)
        columnAttributes = teamAttributes
        if (table == "Team"):
            columnAttributes = teamAttributes
        elif (table == "Franchise"):
            columnAttributes = franchiseAttributes
        elif (table == "Manager"):
            columnAttributes = managerAttributes
        elif (table == "TeamID"):
            columnAttributes = teamIDAttributes
        elif (table == "TeamWins"):
            columnAttributes = teamWinsAttributes
        elif (table == "Salary"):
            columnAttributes = salaryAttributes
        elif (table == "Pitchers"):
            columnAttributes = pitchersAttributes
        elif (table == "Fielders"):
            columnAttributes = fieldersAttributes
        elif (table == "Batters"):
            columnAttributes = battersAttributes
        elif (table == "Players"):
            columnAttributes = playersAttributes
        elif (table == "PlayerIDs"):
            columnAttributes = playerIDAttributes
        elif (table == "AllStarPlayers"):
            columnAttributes = allStarPlayerAttributes
        elif (table == "AllStarGames"):
            columnAttributes = allStarGameAttributes
        elif (table == "HallOfFamePlayers"):
            columnAttributes = hallOfFamePlayerAttributes

        columnValues = input(f'{columnAttributes}\nPlease type the attributes you would like to select separated by commas or just *:\n>> ')
        whereCondition = input("Please type the WHERE condition you would like to select on or type N/A for no WHERE condition\n>> ")

        # Execute a SELECT
        if (whereCondition == "N/A"):
            cursor.execute(f'SELECT {columnValues} FROM {table}')
        else:
            cursor.execute(f'SELECT {columnValues} FROM {table} WHERE ({whereCondition})')

        # Retrieve query results
        records = cursor.fetchall()

        print(records) 
        print(functionalities)      

    # aggregate functions (MIN, MAX, SUM, COUNT, AVG)
    def do_5(self, line):
        """Print a greeting."""
        table = input(tableList)
        aggregate = input("Choose an aggregate function: MIN, MAX, SUM, COUNT, or AVG\n>> ")
        columnAttributes = teamAttributes
        if (table == "Team"):
            columnAttributes = teamAttributes
        elif (table == "Franchise"):
            columnAttributes = franchiseAttributes
        elif (table == "Manager"):
            columnAttributes = managerAttributes
        elif (table == "TeamID"):
            columnAttributes = teamIDAttributes
        elif (table == "TeamWins"):
            columnAttributes = teamWinsAttributes
        elif (table == "Salary"):
            columnAttributes = salaryAttributes
        elif (table == "Pitchers"):
            columnAttributes = pitchersAttributes
        elif (table == "Fielders"):
            columnAttributes = fieldersAttributes
        elif (table == "Batters"):
            columnAttributes = battersAttributes
        elif (table == "Players"):
            columnAttributes = playersAttributes
        elif (table == "PlayerIDs"):
            columnAttributes = playerIDAttributes
        elif (table == "AllStarPlayers"):
            columnAttributes = allStarPlayerAttributes
        elif (table == "AllStarGames"):
            columnAttributes = allStarGameAttributes
        elif (table == "HallOfFamePlayers"):
            columnAttributes = hallOfFamePlayerAttributes

        columnValue = input(f'{columnAttributes}\nPlease type the attribute you would like to complete the the previously selected aggregate function on:\n>> ')

        cursor.execute(f'SELECT {aggregate}({columnValue}) FROM {table}')

         # Retrieve query results
        records = cursor.fetchall()

        print(records) 
        print(functionalities)

    # sorting (ASC, DESC)
    def do_6(self, line):
        """Print a greeting."""
        table = input(tableList)
        columnAttributes = teamAttributes
        if (table == "Team"):
            columnAttributes = teamAttributes
        elif (table == "Franchise"):
            columnAttributes = franchiseAttributes
        elif (table == "Manager"):
            columnAttributes = managerAttributes
        elif (table == "TeamID"):
            columnAttributes = teamIDAttributes
        elif (table == "TeamWins"):
            columnAttributes = teamWinsAttributes
        elif (table == "Salary"):
            columnAttributes = salaryAttributes
        elif (table == "Pitchers"):
            columnAttributes = pitchersAttributes
        elif (table == "Fielders"):
            columnAttributes = fieldersAttributes
        elif (table == "Batters"):
            columnAttributes = battersAttributes
        elif (table == "Players"):
            columnAttributes = playersAttributes
        elif (table == "PlayerIDs"):
            columnAttributes = playerIDAttributes
        elif (table == "AllStarPlayers"):
            columnAttributes = allStarPlayerAttributes
        elif (table == "AllStarGames"):
            columnAttributes = allStarGameAttributes
        elif (table == "HallOfFamePlayers"):
            columnAttributes = hallOfFamePlayerAttributes

        sort = input(f'{columnAttributes}Please type the attributes you would you like to sort by followed a space and then either ASC or DESC, make sure to separate the your selections by commas\n>> ')
        
        cursor.execute(f'SELECT FROM {table} ORDER BY {sort}')

         # Retrieve query results
        records = cursor.fetchall()

        print(records)
        print(functionalities)

    # joins
    def do_7(self, line):
        """Print a greeting."""
        query = ""
        tableNum = input("Please type the number of tables you would like to perform joins on\n>> ")

        print("Please select the first table to perform join on")
        table1 = input(tableList)
        columnAttributes1 = teamAttributes
        if (table1 == "Team"):
            columnAttributes1 = teamAttributes
        elif (table1 == "Franchise"):
            columnAttributes1 = franchiseAttributes
        elif (table1 == "Manager"):
            columnAttributes1 = managerAttributes
        elif (table1 == "TeamID"):
            columnAttributes1 = teamIDAttributes
        elif (table1 == "TeamWins"):
            columnAttributes1 = teamWinsAttributes
        elif (table1 == "Salary"):
            columnAttributes1 = salaryAttributes
        elif (table1 == "Pitchers"):
            columnAttributes1 = pitchersAttributes
        elif (table1 == "Fielders"):
            columnAttributes1 = fieldersAttributes
        elif (table1 == "Batters"):
            columnAttributes1 = battersAttributes
        elif (table1 == "Players"):
            columnAttributes1 = playersAttributes
        elif (table1 == "PlayerIDs"):
            columnAttributes1 = playerIDAttributes
        elif (table1 == "AllStarPlayers"):
            columnAttributes1 = allStarPlayerAttributes
        elif (table1 == "AllStarGames"):
            columnAttributes1 = allStarGameAttributes
        elif (table1 == "HallOfFamePlayers"):
            columnAttributes1 = hallOfFamePlayerAttributes

        columnValues1 = input(f'{columnAttributes1}\nPlease type the attributes you would like to select separated by commas or just *:\n>> ')
        
        query += (f'SELECT {columnValues1} FROM {table1}')

        tableCount = int(tableNum)
        while (tableCount != 0):
            join = input("Please type the join you would like to perform with the following table: INNER JOIN, LEFT JOIN, RIGHT JOIN, or OUTER JOIN\n>> ")
            print("Make sure to select a different table for each join")
            table = input(tableList)
            columnAttributes = teamAttributes
            if (table == "Team"):
                columnAttributes = teamAttributes
            elif (table == "Franchise"):
                columnAttributes = franchiseAttributes
            elif (table == "Manager"):
                columnAttributes = managerAttributes
            elif (table == "TeamID"):
                columnAttributes = teamIDAttributes
            elif (table == "TeamWins"):
                columnAttributes = teamWinsAttributes
            elif (table == "Salary"):
                columnAttributes = salaryAttributes
            elif (table == "Pitchers"):
                columnAttributes = pitchersAttributes
            elif (table == "Fielders"):
                columnAttributes = fieldersAttributes
            elif (table == "Batters"):
                columnAttributes = battersAttributes
            elif (table == "Players"):
                columnAttributes = playersAttributes
            elif (table == "PlayerIDs"):
                columnAttributes = playerIDAttributes
            elif (table == "AllStarPlayers"):
                columnAttributes = allStarPlayerAttributes
            elif (table == "AllStarGames"):
                columnAttributes = allStarGameAttributes
            elif (table == "HallOfFamePlayers"):
                columnAttributes = hallOfFamePlayerAttributes

            columnValues = input(f'{columnAttributes}\nPlease type the attributes you would like to select separated by commas or just *:\n>> ')

            print(f'The attributes from the table selected are...\n{columnAttributes}\n')
            onCondition = input("Please type the condition on which you want to perform the join using the above attributes (from any of tables already selected) \n>> ")

            query += (f'{join} ON {onCondition}')
            
            tableCount -= 1

        # Execute a JOIN
        cursor.execute(query)

        # Retrieve query results
        records = cursor.fetchall()

        print(records)  
        print(functionalities)        

    # grouping
    def do_8(self, line):
        """Print a greeting."""
        table = input(tableList)
        columnAttributes = teamAttributes
        if (table == "Team"):
            columnAttributes = teamAttributes
        elif (table == "Franchise"):
            columnAttributes = franchiseAttributes
        elif (table == "Manager"):
            columnAttributes = managerAttributes
        elif (table == "TeamID"):
            columnAttributes = teamIDAttributes
        elif (table == "TeamWins"):
            columnAttributes = teamWinsAttributes
        elif (table == "Salary"):
            columnAttributes = salaryAttributes
        elif (table == "Pitchers"):
            columnAttributes = pitchersAttributes
        elif (table == "Fielders"):
            columnAttributes = fieldersAttributes
        elif (table == "Batters"):
            columnAttributes = battersAttributes
        elif (table == "Players"):
            columnAttributes = playersAttributes
        elif (table == "PlayerIDs"):
            columnAttributes = playerIDAttributes
        elif (table == "AllStarPlayers"):
            columnAttributes = allStarPlayerAttributes
        elif (table == "AllStarGames"):
            columnAttributes = allStarGameAttributes
        elif (table == "HallOfFamePlayers"):
            columnAttributes = hallOfFamePlayerAttributes

        columnValues = input(f'{columnAttributes}\nPlease type the attributes you would like to select separated by commas or just *:\n>> ')
        grouping = input("Please type the attributes you would like to group by seaparated by commas\n>> ")

        # Execute a SELECT with grouping
        cursor.execute(f'SELECT {columnValues} FROM {table} GROUP BY {grouping}')

        # Retrieve query results
        records = cursor.fetchall()

        print(records)
        print(functionalities)

    # subqueries  
    def do_9(self, line):
        """Print a greeting."""
        query = ""
        close = ""
        level = input("Please type the number of subqueries you would like to perform \n(ex. SELECT * FROM TableName WHERE Column IN (SELECT Column FROM AnotherTable); would be 2)")
        levelCount = int(level)
        while (levelCount != 0):
            print("Make sure to select a different table for each subquery")
            table = input(tableList)
            columnAttributes = teamAttributes
            if (table == "Team"):
                columnAttributes = teamAttributes
            elif (table == "Franchise"):
                columnAttributes = franchiseAttributes
            elif (table == "Manager"):
                columnAttributes = managerAttributes
            elif (table == "TeamID"):
                columnAttributes = teamIDAttributes
            elif (table == "TeamWins"):
                columnAttributes = teamWinsAttributes
            elif (table == "Salary"):
                columnAttributes = salaryAttributes
            elif (table == "Pitchers"):
                columnAttributes = pitchersAttributes
            elif (table == "Fielders"):
                columnAttributes = fieldersAttributes
            elif (table == "Batters"):
                columnAttributes = battersAttributes
            elif (table == "Players"):
                columnAttributes = playersAttributes
            elif (table == "PlayerIDs"):
                columnAttributes = playerIDAttributes
            elif (table == "AllStarPlayers"):
                columnAttributes = allStarPlayerAttributes
            elif (table == "AllStarGames"):
                columnAttributes = allStarGameAttributes
            elif (table == "HallOfFamePlayers"):
                columnAttributes = hallOfFamePlayerAttributes

            
            columnValues = input(f'{columnAttributes}\nPlease type the attributes you would like to select separated by commas or just *:\n>> ')
            if (levelCount == 1):
                whereCondition = input("Please type the WHERE condition you would like to select on or type N/A for no WHERE condition\n>> ")
            else:
                whereCondition = input("Please type the WHERE condition you would like to select on\n>> ")

            if (whereCondition == "N/A"):
                query += (f'SELECT {columnValues} FROM {table}')
            elif (levelCount == 1):
                query += (f'SELECT {columnValues} FROM {table} WHERE ({whereCondition})')
            else:
                query += (f'SELECT {columnValues} FROM {table} WHERE ({whereCondition}) (')
            
            close += ")"
            levelCount -= 1

        query += close

        # Execute a subquery
        cursor.execute(query)

        # Retrieve query results
        records = cursor.fetchall()

        print(records) 
        print(functionalities)      

    # transactions
    def do_10(self, line):
        """Print a greeting."""
        print("I didn't know how to implement this because we never talked about how transactions work in SQL")
        print(functionalities)

    # error handeling
    def do_11(self, line):
        """Print a greeting."""
        print("I didn't know how to implement this because we never talked about how error handeling works in SQL")
        print(functionalities)

    # Exit
    def do_12(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()
