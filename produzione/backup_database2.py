#!/usr/bin/python3
import pymysql
import subprocess
# Define database connection details
host = "31.11.39.80"
database = "Sql1612418_4"
user = "Sql1612418"
password = "8TCS$SXucy#$jN%SixrX$WHyzp9GbMHet7!XKixhoy7LY6g9%sJePwN4ANgiQJzG"

backup_file = "/home/gb-home/backup.sql"


# Establish connection with the MySQL database
connection = pymysql.connect(host=host, user=user, password=password, database=database)

# Execute the mysqldump command
command = f"mysqldump −h {host} −u {user} −p {password} {database} > {backup_file}"
subprocess.run(command, shell=True)

# Close the database connection
connection.close()
