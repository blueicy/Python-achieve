import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('trackdb2.sqlite')
#LINKER of DB *.sqlite
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id integer not null primary key AUTOINCREMENT UNIQUE,
    name text UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter flie name:')
if (len(fname) < 1):
    fname = 'Library.xml'

#PRINT pretty XML


#FIND Key then read Value located next
def lookup(d, key):
    found = False
    for child in d:
        #RETURN string between <string>___</string>
        if found:
            return child.text
        #FIND <key> and CHECK matched text before </key>
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
#print prettyxml wiht bs4
#bs = BeautifulSoup(open(fname))
#print(bs.prettify())

all = stuff.findall('dict/dict/dict')

print('Dict count:', len(all))

for entry in all:
    if (lookup(entry, 'Track ID') is None ):
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup(entry, 'Play Count')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, genre, length, rating, count)

    #SET artist name
    cur.execute('''INSERT or IGNORE INTO Artist (name) VALUES (?)''', (artist, ))
    #SET id number autometically
    cur.execute('SELECT id from Artist WHERE name = ?', (artist, ))
    #Build artist_id as Foreign Key
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT or IGNORE INTO Genre (name) VALUES (?)''', (genre, ))
    cur.execute('SELECT id from Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    #SET album name and artist_id
    cur.execute('''INSERT or IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album, artist_id) )
    cur.execute('SELECT id from Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    #SET everyinfo on top tree
    cur.execute('''INSERT or IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)''' , (name, album_id, genre_id, length, rating, count))

    #SHOW Tables
    #cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name, FROM Track JOIN Genre JOIN Album JOIN Artist on Track.genre_id = Genre.id AND Track.album_id=Album.id AND Album.artist_id=Artist.id ORDER BY Artist.name LIMIT 3''')

    #COMMIT cur.execute on SQLite
    conn.commit()
