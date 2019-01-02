import sqlite3
import re

conn = sqlite3.connect('emaildb_hw.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue

    #FIND From: ddd@ddd.com
    pieces = line.split()


    email = pieces[1]

    #FIND \S+ after @  -> LIST to STR
    organize = str(re.findall('\S+@(\S+)', email))

    #MUST INPUT TEXT as contract: org TEXT
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (organize,))
    row = cur.fetchone()

    #count value save 1 or ++count
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (organize,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (organize,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
# READ org count in ORDER
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'


for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
