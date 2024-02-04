# Import the sqlite3 library to work with SQLite databases
import sqlite3

try:
    # Connect to the SQLite database (or create it if it doesn't exist)
    db = sqlite3.connect('python_programming_db')
    cursor = db.cursor()  

    # Create a table named 'python_programming' with columns 'id', 'name', and 'grade'
    cursor.execute('''
        CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT,
                        grade INTEGER)
    ''')
    db.commit()

    # Reassign the cursor for further operations
    cursor = db.cursor()
    
    # Define a list consist of students' id, name and grade
    students_grades =[(55, 'Carl Davis', 61), (66, 'Dennis Fredrickson', 88), (77, 'Jane Richards', 78),
                    (12, 'Peyton Sawyer', 45), (2, 'Lucas Brooke', 99)]
    
    # Insert multiple records (students' id, name and grade) into the table
    cursor.executemany('''INSERT INTO python_programming(id, name, grade)
                    VALUES(?,?,?)''', (students_grades))
    print('all users in the list inserted')
    db.commit()

    # Select and print records (id and name) where grade is between 60 and 80
    cursor.execute('''SELECT id, name FROM python_programming WHERE grade BETWEEN 60 and 80''')
    student = cursor.fetchall()
    print(student)

    # Update a student's grade
    grade = 65
    name1 = 'Carl Davis'
    cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ? ''', (grade, name1))
    print('Student data updated!')

    # Delete a student's record
    name2 = 'Dennis Fredrickson'
    cursor.execute('''DELETE FROM python_programming WHERE name = ? ''', (name2,))
    print('Student records deleted.')

    # Update the grade for students with 'id' less than 55
    grade1 = 100
    cursor.execute('''UPDATE python_programming SET grade = ? WHERE id < 55 ''', (grade1,))
    print('Student data updated!')

    db.commit()
except Exception as e:
    # If an exception occurs, rollback any changes to the database
    db.rollback()
    raise e
finally:
    # Close the database connection
    db.close()
    print('Connection to database closed')


