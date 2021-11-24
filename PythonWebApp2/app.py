
from flask import Flask
from flask import render_template
import pyodbc

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Creating connection Object which will contain SQL Server connection
connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=KAIRMT90596;Database=claimsDB;Trusted_Connection=yes;')

cursor = connection.cursor()

#headings = ("Name", "Role", "Salary")
#data = (
    #("Rolf", "Software Engineer", "$70,000.00"), 
    #("Amy", "Software Engineer", "$70,000.00")
#)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

headings = list()
data = list()

claimsHeadings = list()
claimsData = list()

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", headings=headings, data=data);

@app.route('/greensheet', methods=['GET'])
def greensheet():
    cursor.execute("SELECT * From Persons");
    #for row in cursor.columns(table='Persons'):
    #    headings.append(row.column_name)
    #    print(row.column_name)

    cursor.execute("SELECT PersonID, LastName, FirstName, Address, City, age from Persons");
    #for row in cursor.fetchall():
    #    data.append(row)
    #    print(row)
    return render_template("greensheet.html", headings=headings, data=data)

@app.route('/claims', methods=['GET'])
def claims():
    cursor.execute("SELECT * From claimstestDB");
    for row in cursor.columns(table='claimstestDB'):
        headings.append(row.column_name)

    cursor.execute("select Id, Workflow_Transaction_Name, Goal, Max, RunID_6977, RunID_6972, RunID_6949, RunId_6942, RunID_6942, RunID_6924, RunID_6920 from claimstestdb;");
    for row in cursor.fetchall():
        data.append(row)
    return render_template("claims.html", headings=headings, data=data)
    




print(data)

if __name__ == '__main__':
    # Run the app server on localhost:4444
    app.run('localhost', 4444)