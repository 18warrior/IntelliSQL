import sqlite3

# Connect to SQLite database (creates it if not exists)
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Create table (if not already exists)
table = '''CREATE TABLE IF NOT EXISTS Students(
    name VARCHAR(30),
    class VARCHAR(10),
    marks INT,
    company VARCHAR(30)
)'''

cursor.execute(table)

# Insert sample data
try:
    cursor.execute("INSERT INTO STUDENTS VALUES ('Ramesh', 'BCom', 89, 'Google')")
    cursor.execute("INSERT INTO STUDENTS VALUES ('Suresh', 'MCom', 78, 'TCS')")
    cursor.execute("INSERT INTO STUDENTS VALUES ('Mahesh', 'BCom', 85, 'Infosys')")
    cursor.execute("INSERT INTO STUDENTS VALUES ('Ganesh', 'MCom', 91, 'Microsoft')")
    cursor.execute("INSERT INTO STUDENTS VALUES ('Dinesh', 'BCom', 67, 'Amazon')")
except Exception as e:
    print("Error inserting:", e)

# Print data
print("Inserted records:")
df = cursor.execute("SELECT * FROM STUDENTS")
for row in df:
    print(row)

# Save and close
connection.commit()
connection.close()
