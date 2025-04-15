# Import Libraries
import mysql.connector


# Function to clone a MySQL database with tables, views, and routines
# This function connects to a MySQL server, creates a new database, and clones the tables, views, and routines from an existing database to the new one.
def clone_mysql_database_with_objects(host, port, user, password, old_db, new_db):
    conn = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password
    )
    conn.autocommit = True
    cursor = conn.cursor()

    print(f"Creating new database `{new_db}`")
    cursor.execute(f"DROP DATABASE IF EXISTS `{new_db}`")
    cursor.execute(f"CREATE DATABASE `{new_db}`")

    cursor.execute(f"USE `{old_db}`")
    cursor.execute("SHOW FULL TABLES WHERE Table_type = 'BASE TABLE'")
    base_tables = cursor.fetchall()

    cursor.execute("SET foreign_key_checks = 0;")

    for (table_name, _) in base_tables:
        print(f"Cloning table: {table_name}")
        cursor.execute(f"CREATE TABLE `{new_db}`.`{table_name}` LIKE `{old_db}`.`{table_name}`")
        cursor.execute(f"INSERT INTO `{new_db}`.`{table_name}` SELECT * FROM `{old_db}`.`{table_name}`")

    cursor.execute("SET foreign_key_checks = 1;")

    cursor.execute("SHOW FULL TABLES WHERE Table_type = 'VIEW'")
    views = cursor.fetchall()
    for (view_name, _) in views:
        print(f"Cloning view: {view_name}")
        cursor.execute(f"SHOW CREATE VIEW `{old_db}`.`{view_name}`")
        view_def = cursor.fetchone()[1]
        view_def = view_def.replace(f"CREATE ALGORITHM", f"CREATE OR REPLACE ALGORITHM")
        view_def = view_def.replace(f"CREATE VIEW", f"CREATE OR REPLACE VIEW")     
        view_def = view_def.replace(f"`{old_db}`.", f"`{new_db}`.")
        cursor.execute(f"USE `{new_db}`")
        cursor.execute(view_def)

    cursor.execute(f"""
        SELECT ROUTINE_NAME, ROUTINE_TYPE
        FROM INFORMATION_SCHEMA.ROUTINES
        WHERE ROUTINE_SCHEMA = '{old_db}'
    """)
    routines = cursor.fetchall()

    for routine_name, routine_type in routines:
        print(f"Cloning {routine_type.lower()}: {routine_name}")
        cursor.execute(f"SHOW CREATE {routine_type} `{old_db}`.`{routine_name}`")
        create_stmt = cursor.fetchone()[2]
        create_stmt = create_stmt.replace(f"DEFINER=`{user}`@`%`", "")  # Optional
        create_stmt = create_stmt.replace(f"`{old_db}`.", f"`{new_db}`.")
        cursor.execute(f"USE `{new_db}`")
        try:
            cursor.execute(create_stmt)
        except mysql.connector.Error as e:
            print(f"⚠️ Could not create {routine_type.lower()} `{routine_name}`: {e.msg}")

    print(f"\n✅ Database `{new_db}` created with tables, views, and routines cloned from `{old_db}`.")
    cursor.close()
    conn.close()


# Call the function to clone the database
# Replace with your actual database connection details
clone_mysql_database_with_objects(
    host='YOUR_HOST',
    port= 3306,
    user='YOUR_USER_NAME',
    password='YOUR_DB_PASSWORD',
    old_db= "DB_NAME_TO_BE_CLONED",
    new_db= "NEW_DB_NAME"  # Name of the new database to be created
)
