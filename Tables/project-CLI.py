# import package
# connect database
# format strings to run queries
import psycopg2
import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()


@app.command("hi")
def sample_func():
    rprint("[red bold]Hi[/red bold] [yellow]World[yello]")

@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yello]")



if __name__ == "__main__":
    app()    

# Connect to postgres DB
connection = psycopg2.connect("dbname=baseballdb user=postgres password=cmpsc431")

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM allstargames")

# Retrieve query results
records = cursor.fetchall()

print(records)