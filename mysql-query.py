#!/usr/bin/python3

# import the MySQLdb and sys modules
import datetime
import MySQLdb
import sys

connection = MySQLdb.connect (host = "dev.kewmann.com", user = "vincent_tham", passwd = "P@$$w0rd", db = "csm")

cursor = connection.cursor ()


query = ("SELECT url, content, lastupdated FROM csm.online_news WHERE LastUpdated BETWEEN %s AND %s")

lastupdate_start = datetime.date(2016, 12, 6)
lastupdate_end = datetime.date(2016, 12, 7)

cursor.execute(query, (lastupdate_start, lastupdate_end))

for ( url, content, lastupdated) in cursor:
  print("{}, {} was updated on {:%d %b %Y}".format(
     url, content, lastupdated))

cursor.close()
connection.close()
