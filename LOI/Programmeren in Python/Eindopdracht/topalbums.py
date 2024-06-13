import sqlite3

## Zet de connectie op met de database
db =  sqlite3.connect("C:\\Users\\rensi\\Desktop\\Programming\\LOI\\Programmeren in Python\\Eindopdracht\\chinook.db")
cur = db.cursor()

## Voer de query uit om de top 10 verkochte/beluisterde albums op te halen
cur.execute(''' SELECT Ar.Name, Al.Title, count(Al.AlbumId) AS occurences
            FROM artists as Ar, albums as Al, tracks as T, invoice_items as I
            WHERE Al.AlbumId = T.AlbumId
            And Al.ArtistId = Ar.ArtistId
            And T.TrackId = I.TrackId
            GROUP BY Al.AlbumId
            ORDER BY occurences DESC LIMIT 10
            ''')
top10 = cur.fetchall()

# Print de lijst met benummering
count = 1
for album in top10:
    print(count, '  {}  |  {}   |  {}'.format(album[0],album[1],album[2]))
    count += 1
