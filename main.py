# ---------------------------------------------------------------
# 📘 SQLAlchemy Beginner Example — Full CRUD + Filtering Tutorial
# ---------------------------------------------------------------

# Import core components
from sqlalchemy import create_engine, Column, Integer, String, CHAR, and_, or_, update
from sqlalchemy.orm import declarative_base, sessionmaker

# ---------------------------------------------------------------
# 1️⃣ Create Database Engine
# ---------------------------------------------------------------
# sqlite:///students.db → creates or connects to a local SQLite file
# echo=True → shows SQL commands being executed (for learning/debugging)
engine = create_engine("sqlite:///students.db", echo=True)

# ---------------------------------------------------------------
# 2️⃣ Create Base Class for ORM Models
# ---------------------------------------------------------------
Base = declarative_base()

# ---------------------------------------------------------------
# 3️⃣ Define the Student Model (Table)
# ---------------------------------------------------------------
class Student(Base):
    __tablename__ = "students"  # Table name

    id = Column(Integer, primary_key=True)  # Primary Key (unique ID)
    name = Column(String)                   # Student Name
    age = Column(Integer)                   # Age
    gender = Column(CHAR)                   # 'M' or 'F'

    # Constructor (for easier object creation)
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    # Representation (for clean print output)
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, gender='{self.gender}')>"

# ---------------------------------------------------------------
# 4️⃣ Create the Table in the Database
# ---------------------------------------------------------------
Base.metadata.create_all(engine)

# ---------------------------------------------------------------
# 5️⃣ Create a Session
# ---------------------------------------------------------------
Session = sessionmaker(bind=engine)
session = Session()

# ---------------------------------------------------------------
# 6️⃣ Add Records (Only run once — comment out after first run)
# ---------------------------------------------------------------
# s1 = Student(1, "Jay Mondal", 22, "M")
# s2 = Student(2, "Aditi Chakraborty", 21, "F")
# s3 = Student(3, "Joyabrata Mondal", 21, "M")
# s4 = Student(4, "Chandan Das", 22, "M")
# s5 = Student(5, "Dipanjan Mondal", 22, "M")
# session.add_all([s1, s2, s3, s4, s5])
# session.commit()

# ---------------------------------------------------------------
# 7️⃣ Update Single Record
# ---------------------------------------------------------------
student = session.query(Student).filter_by(name="Jay Mondal").first()
student.age = 23  # Change the age
session.commit()
print("\n✅ Updated Jay Mondal's age to 23")

# ---------------------------------------------------------------
# 8️⃣ Update Multiple Records (bulk update)
# ---------------------------------------------------------------
# Example: Increase every student’s age by 1
session.query(Student).update({Student.age: Student.age + 1})
session.commit()
print("\n✅ Increased age of all students by 1")

# ---------------------------------------------------------------
# 9️⃣ Delete Record
# ---------------------------------------------------------------
student = session.query(Student).filter_by(name="Dipanjan Mondal").first()
if student:
    session.delete(student)
    session.commit()
    print("\n✅ Deleted record for Dipanjan Mondal")

# ---------------------------------------------------------------
# 🔟 Filter / Search Examples
# ---------------------------------------------------------------
# Students older than 22
older_students = session.query(Student).filter(Student.age > 22).all()

print("\n🎯 Students older than 22:")
for s in older_students:
    print(s.name, s.age)

# Students whose name starts with 'J'
students_with_J = session.query(Student).filter(Student.name.like('J%')).all()

print("\n🎯 Students whose name starts with 'J':")
for s in students_with_J:
    print(s.name, s.age)

# Male students or age less than 22
filtered = session.query(Student).filter(
    or_(Student.gender == 'M', Student.age < 22)
).all()

print("\n🎯 Male students or age less than 22:")
for s in filtered:
    print(s.name, s.age, s.gender)

# ---------------------------------------------------------------
# 1️⃣1️⃣ Sort and Limit Results
# ---------------------------------------------------------------
sorted_students = session.query(Student).order_by(Student.age.desc()).limit(3).all()

print("\n🎯 Top 3 oldest students:")
for s in sorted_students:
    print(s.name, s.age)

# ---------------------------------------------------------------
# 1️⃣2️⃣ Display All Final Records
# ---------------------------------------------------------------
print("\n📋 Final Student Table:")
students = session.query(Student).all()
for s in students:
    print(s.id, s.name, s.age, s.gender)


# What You Learned Here

# create_engine() → connects Python to a database

# Base = declarative_base() → base class for all ORM models

# Column() → defines table fields and data types

# session.add_all() → adds multiple records at once

# session.commit() → saves all changes permanently

# filter() / filter_by() → searches for specific records

# update() → modifies existing records

# delete() → removes records from the table

# order_by() → sorts query results

# limit() → restricts how many records are returned
