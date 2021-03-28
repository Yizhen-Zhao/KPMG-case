# This file used to start mysql service 
# and initial certain operations

set -e

# Start mysql
service mysql start
sleep 3
echo `service mysql status`


# Execute SQL in schema.sql file, create target database
mysql < /mysql/schema.sql
sleep 3
echo `service mysql status`


# Execute SQL in privileges.sql file, set username and password
mysql < /mysql/privileges.sql
echo `Done...`

tail -f /dev/null
