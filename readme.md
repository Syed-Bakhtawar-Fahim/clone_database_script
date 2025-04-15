# 🐬 Clone MySQL Database with Tables, Views, and Routines

This Python script allows you to **clone a MySQL database** including its **tables**, **views**, and **routines** (stored procedures and functions) from one database to another on the same MySQL server.

---

## 📌 Features

- ✅ Clone all **tables** along with their data
- ✅ Clone all **views**
- ✅ Clone all **stored procedures** and **functions**
- ✅ Handles foreign key constraints and definer issues
- ✅ Automatically creates the target database

---

## 📦 Prerequisites

- Python 3.6 or above
- Access to a MySQL server
- MySQL user with permission to read and create databases, tables, views, and routines

---

## 🛠 Installation

Install the required Python package using pip:

```bash
pip install mysql-connector-python
```

## 📂 File Structure
```bash 
    clone_mysql_database.py  # Main Python script
```
## 🚀 How to Use
1. Open the script file clone_mysql_database.py.
2. Scroll to the bottom and replace the placeholders in the function call:

```bash
clone_mysql_database_with_objects(
    host='YOUR_HOST',
    port=3306,
    user='YOUR_USER_NAME',
    password='YOUR_DB_PASSWORD',
    old_db='DB_NAME_TO_BE_CLONED',
    new_db='NEW_DB_NAME'
)
```

---

## 🔍 What It Does

This script will:

- ✅ Connect to the MySQL server
- 🔄 Drop the new database if it exists
- 🆕 Create a new empty database
- 📋 Clone all **base tables** (structure + data)
- 👁️ Clone all **views**, replacing schema references
- ⚙️ Clone all **stored routines** (procedures and functions)
- 🔐 Disable and re-enable **foreign key checks** to ensure smooth copying

## 👨‍💻 Author

Developed by **Syed Bakhtawar Fahim**  
🛠 Passionate about database automation and backend development  
📬 Feel free to connect or contribute!

---

## 📃 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this script.

---

