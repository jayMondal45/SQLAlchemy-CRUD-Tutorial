# 📘 SQLAlchemy CRUD Tutorial

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive beginner-friendly tutorial demonstrating **SQLAlchemy ORM** with complete CRUD operations, advanced filtering, sorting, and real-world database examples using Python and SQLite.

## 🎯 What You'll Learn

- ✅ Database connection and engine creation
- ✅ ORM model definition and table creation
- ✅ **Create** - Adding single and multiple records
- ✅ **Read** - Querying and filtering data
- ✅ **Update** - Modifying single and bulk records
- ✅ **Delete** - Removing records from database
- ✅ Advanced filtering with `and_()`, `or_()`, `like()`
- ✅ Sorting and limiting query results
- ✅ Session management and transactions

## 🚀 Features

- **Beginner Friendly**: Detailed comments explaining every step
- **Full CRUD Operations**: Complete Create, Read, Update, Delete examples
- **Advanced Queries**: Complex filtering and search operations
- **Best Practices**: Proper session handling and ORM patterns
- **Real Examples**: Student database with practical use cases

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher installed
- Basic understanding of Python
- Familiarity with databases (helpful but not required)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jayMondal45/SQLAlchemy-CRUD-Tutorial.git
cd SQLAlchemy-CRUD-Tutorial
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install sqlalchemy
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

## 📦 Project Structure

```
SQLAlchemy-CRUD-Tutorial/
│
├── main.py                 # Main tutorial file with all examples
├── students.db            # SQLite database (auto-generated)
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## 💻 Usage

### Run the Tutorial

```bash
python main.py
```

### First Run (Adding Records)

On your first run, uncomment the "Add Records" section (lines 52-57):

```python
s1 = Student(1, "Jay Mondal", 22, "M")
s2 = Student(2, "Aditi Chakraborty", 21, "F")
s3 = Student(3, "Joyabrata Mondal", 21, "M")
s4 = Student(4, "Chandan Das", 22, "M")
s5 = Student(5, "Dipanjan Mondal", 22, "M")
session.add_all([s1, s2, s3, s4, s5])
session.commit()
```

After the first run, comment these lines back to avoid duplicate entries.

## 📚 Code Examples

### 1. Create Engine & Connect to Database

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///students.db", echo=True)
```

### 2. Define ORM Model

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, CHAR

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(CHAR)
```

### 3. CRUD Operations

#### Create (Insert)
```python
student = Student(1, "Jay Mondal", 22, "M")
session.add(student)
session.commit()
```

#### Read (Query)
```python
# Get all students
students = session.query(Student).all()

# Filter by name
student = session.query(Student).filter_by(name="Jay Mondal").first()
```

#### Update
```python
student = session.query(Student).filter_by(name="Jay Mondal").first()
student.age = 23
session.commit()
```

#### Delete
```python
student = session.query(Student).filter_by(name="Dipanjan Mondal").first()
session.delete(student)
session.commit()
```

## 🔍 Advanced Filtering Examples

### Filter by Age
```python
older_students = session.query(Student).filter(Student.age > 22).all()
```

### Pattern Matching (LIKE)
```python
students_with_J = session.query(Student).filter(Student.name.like('J%')).all()
```

### Complex OR Conditions
```python
from sqlalchemy import or_

filtered = session.query(Student).filter(
    or_(Student.gender == 'M', Student.age < 22)
).all()
```

### Sorting and Limiting
```python
top_students = session.query(Student).order_by(Student.age.desc()).limit(3).all()
```

## 🎓 Key Concepts Covered

| Concept | Description |
|---------|-------------|
| **Engine** | Connects Python to database |
| **Base** | Base class for ORM models |
| **Session** | Manages database transactions |
| **Column** | Defines table fields and data types |
| **filter()** | Searches with expressions |
| **filter_by()** | Searches with keyword arguments |
| **commit()** | Saves changes permanently |
| **rollback()** | Reverts uncommitted changes |

## 🐛 Troubleshooting

### Issue: "No module named 'sqlalchemy'"
**Solution**: Install SQLAlchemy using `pip install sqlalchemy`

### Issue: Database locked error
**Solution**: Close all database connections and sessions properly

### Issue: Duplicate entries
**Solution**: Comment out the "Add Records" section after first run

## 📈 Next Steps

After mastering this tutorial, explore:

- **Relationships**: One-to-Many, Many-to-Many relationships
- **Migrations**: Use Alembic for database migrations
- **Connection Pooling**: Optimize database connections
- **PostgreSQL/MySQL**: Connect to production databases
- **Async SQLAlchemy**: Asynchronous database operations

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

**Jay Mondal**
- Email: jaymondas953@gmail.com
- GitHub: [@jayMondal45](https://github.com/jayMondal45)

## 📄 License

This project is licensed under the MIT License - feel free to use it for learning and teaching purposes.

## ⭐ Show Your Support

If this tutorial helped you learn SQLAlchemy, please give it a star ⭐️!

---

Made with ❤️ by [Jay Mondal](https://github.com/jayMondal45) | Digital Superhero 🦸‍♂️
