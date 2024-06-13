import sqlite3

## Zet de connectie op met de database
db =  sqlite3.connect("C:\\Users\\rensi\\Desktop\\Programming\\LOI\\Programmeren in Python\\Eindopdracht\\chinook.db")

## -------------------------------Start Functies---------------------------- ##
# Importeert het bestand en schoont op
def getFile(bestand):
    with open(bestand) as f:
        te_zoeken_tracks = [line.rstrip() for line in f]

    return te_zoeken_tracks


# Haalt alle bestaande playlists op, zet ze in een list en
# controleert of de gegeven playlist al bestaat
def checkIfPlaylistAlreadyExists (new_playlist):
    cur = db.cursor()
    cur.execute('''SELECT Name FROM playlists
                WHERE UPPER(Name) LIKE UPPER(?)''', [new_playlist])

    return bool(cur.fetchall())


## Maakt een lijst van strings uit het bestand welke niet exact een track zijn
## Maar wel een substring van een track
def getSubstrings(te_zoeken_tracks):
    substrings = []

    for te_zoeken_track  in te_zoeken_tracks:
        cur = db.cursor()
        cur.execute('''SELECT Name FROM tracks \
                    WHERE UPPER(Name) LIKE UPPER(?)
                    AND UPPER(NAME) IS NOT UPPER(?)''', ('%'+te_zoeken_track +'%', te_zoeken_track ))

        # Als de opgehaalde data niet NIKS is wordt deze toegevoegd aan de substrings
        track = cur.fetchone()
        if track is not None:
            substrings.append(te_zoeken_track )

    return substrings


## Functie controleert gegeven lijst met exacte namen tussen de tracks
def importPlaylist(te_zoeken_tracks):
    te_zoeken_tracks = list(filter(None,te_zoeken_tracks))

    ## Maakt een lijst substrings middels de functie getSubstrings()
    substrings = getSubstrings(te_zoeken_tracks)
    new_playlist_tracks = []

    # Voegt alle tracks toe aan de lijst "new_playlist_tracks" waarvan
    # de strings exact overeen kwamen met een track uit de DB
    for te_zoeken_track in te_zoeken_tracks:
        cur = db.cursor()
        cur.execute('''SELECT Name FROM tracks \
                    WHERE UPPER(?) is UPPER(Name)''', (te_zoeken_track,))
        track = cur.fetchall()
        new_playlist_tracks.append([''.join(te_zoeken_track) for te_zoeken_track in track])
    new_playlist_tracks = list(filter(None,new_playlist_tracks))
    new_playlist_tracks = [''.join(te_zoeken_track) for te_zoeken_track in new_playlist_tracks]

    ## Controleert of er nog Strings/Items zijn in de lijst vanuit het bestand welke
    ## nog niet in "new_playlist_tracks" of "substrings" staan
    ## wat dus betekent dat er niks voor is gevonden
    for te_zoeken_track in te_zoeken_tracks:
        if te_zoeken_track not in substrings and te_zoeken_track not in new_playlist_tracks:
            print("--- Geen tracks gevonden voor {} ---".format(te_zoeken_track))

    choices = getChoices(substrings, new_playlist_tracks)
    return new_playlist_tracks

## function welke alle items afgaat welke een substring zijn van een track
## Geeft de gebruiker een keuze tussen de gevonden tracks
def getChoices(substrings, new_playlist_tracks):
    for string in substrings:

        ## Query de mogelijke tracks + artiest van de DB voor iedere substring
        cur = db.cursor()
        cur.execute('''SELECT T.Name, A.Name \
                    FROM tracks as T, artists as A, albums as B \
                    WHERE T.Name LIKE ? \
                    AND T.AlbumId = B.AlbumId \
                    AND B.ArtistID = A.ArtistID
                    ''', ('%'+string+'%',))

        tracks_artiest = cur.fetchall()

        ## Geef de gebruiker een lijst met gevonden mogelijkheden
        nr = 1
        print("\nMaak een keuze uit de volgende tracks voor", '"'+string+'"' )
        for track in tracks_artiest:
            print(nr,track[0]," | ", track[1])
            nr += 1

        ## Laat de gebruiker een keuze maken, wordt gecontroleerd op correctheid
        while True:
            try:
                keuze = int(input("\nUw keuze: "))
            except ValueError:
                print(keuze,"is geen nummer!")
            else:
                if 1 <= keuze <= len(tracks_artiest):
                    break
                else:
                    print("Buiten bereik, geef een nummer tussen de 1 -", len(tracks_artiest))

        new_playlist_tracks.append(tracks_artiest[keuze -1][0])
    return new_playlist_tracks
    ## End of inner functionik

    # "Start import" voor de niet gevonden tracks en keuzes
    print("\n--- Start import van playlist ---\n")


## - Functie maakt de nieuwe playlist aan
## - Vult de playlist aan met de gemaakte playlist ("new_playlist_tracks")
def insertNewPlaylist(playlistNaam):

    ## Insert nieuwe playlist in de DB
    cur = db.cursor()
    cur.execute('''INSERT INTO playlists(Name) VALUES(?)''', [playlistNaam])
    db.commit()

    ## Insert de tracks van de gemaakte playlist in de playlist_tracks tabel
    for track in new_playlist_tracks:
        cur = db.cursor()
        cur.execute('''INSERT INTO playlist_track (PlaylistID, TrackId)
                    SELECT P.PlaylistID, T.TrackId
                    FROM tracks as T, playlists as P
                    WHERE UPPER(T.Name) IS UPPER(?)
                    AND P.Name = ? ''', [track, new_playlist])
        db.commit()

    print("\n--- Import playlist complete ---\n")

## -------------------------------Einde Functies---------------------------- ##
## ------------------------------Start Programma---------------------------- ##

## Zolang het bestand niet gevonden kan worden wordt er gevraagd naar een bestand
while True:
    try:
        te_zoeken_tracks = getFile(input("Geef de naam van het te importeren bestand: "))
        break
    except FileNotFoundError:
        print("Bestand niet gevonden\n")

## Vraagt de naam van de te maken playlist en controleert of deze bestaat
while True:
    new_playlist = (input("Geef naam van de playlist: "))
    if not checkIfPlaylistAlreadyExists(new_playlist):
        break
    else:
        print("Deze playlist bestaat al\n")

# Maakt de lijst van substrings om op te zoeken tussen de tracks
substrings = getSubstrings(te_zoeken_tracks)

# Maakt de lijst met tracks voor de nieuwe playlist
new_playlist_tracks = importPlaylist(te_zoeken_tracks)

# Schrijf de playlist + de tracks naar de DB
insertNewPlaylist(new_playlist)
