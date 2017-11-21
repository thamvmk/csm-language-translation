#!/usr/bin/python3

# import the MySQLdb and sys modules
import datetime
import MySQLdb
import sys
import re
from translate import trans

connection = MySQLdb.connect (host = "dev.kewmann.com", user = "vincent_tham", passwd = "P@$$w0rd", db = "csm")
cursor = connection.cursor ()

query = ("SELECT url, content, lastupdated FROM csm.online_news WHERE LastUpdated BETWEEN %s AND %s")

lastupdate_start = datetime.date(2016, 12, 9)
lastupdate_end = datetime.date(2016, 12, 10)

cursor.execute(query, (lastupdate_start, lastupdate_end))

for ( url, content, lastupdated) in cursor:
    translated_text_en    = ""
    translated_text_zh_cn = ""
    a = ""
    print ("URL        : %s" % url)
    print ("content    : %s" % content)
    print ("lastupdated: %s\n" % lastupdated)
    #content = content.replace("\"","")
    #content = content.replace("\'","")
    if ('\"' in content):
        print ("Yes, content has \"\n")
        a = re.sub('[^A-Za-z0-9\.\"\?\s\w]+', ' ', content)
        print ("a = %s" % a)
        input("Press Enter to continue...")
    elif ('\'' in content):
        print ("Yes, content has \'\n")
        a = re.sub('[^A-Za-z0-9\.\"\?\s\w]+', ' ', content)
        #a = re.sub(r'[\'|"|“|\|\[|]}“]',r'',content)
        #a = a.replace('`', '')
        print ("a = %s" % a)
        input("Press Enter to continue...")
    else:
        a = content
    #print ("content    : %s" % a)
    translated_text_en    = trans(a, "en") 
    print ("content_en : %s" % translated_text_en)
    translated_text_zh_cn = trans(a, "zh-cn") 
    print ("content_ch : %s" % translated_text_zh_cn)
    input("Press Enter to continue...")
cursor.close()
connection.close()
