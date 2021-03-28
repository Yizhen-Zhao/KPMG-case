# This Dockerfile is used to set up mysql service and create a target database


From mysql:5.7

# First log in without password, set password in privileges.sql file
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes

COPY setup.sh /mysql/setup.sh
COPY schema.sql /mysql/schema.sql
COPY privileges.sql /mysql/privileges.sql

#Start mysql service, connect to database and create target database
CMD ["sh", "/mysql/setup.sh"] 
