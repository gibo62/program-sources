#!/usr/bin/python3

import pyodbc

# Connection parameters
server = 'mysql.nsvalme.cloud'
database = 'Sql1612418_4'
username = 'Sql1612418'
password = '8TCS$SXucy#$jN%SixrX$WHyzp9GbMHet7!XKixhoy7LY6g9%sJePwN4ANgiQJzG'

# Create a connection object
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# Create a cursor object
cursor = conn.cursor()
import os

# Backup directory
backup_dir = '/home/gb-home/'

# Backup file name
backup_file = database+'_backup_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.bak'

# Backup command
backup_command = 'BACKUP DATABASE mydatabase TO DISK='+backup_dir+ backup_file +''
print (backup_command)
# Execute the backup command
cursor.execute(backup_command)
