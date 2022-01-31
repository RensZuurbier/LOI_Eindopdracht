## Welkomswoord
def welkomswoord():
    print('\nHoi, welkom bij jouw Galgje!')
    print('ik heb een woord in gedachten, je krijgt 10 pogingen.\n')

# Declareer het geheime woord en de variabelen
geheim_woord = ['c','l','o','w','n','b','a','a','r','d',]
geraden_woord = ['_','_','_','_','_','_','_','_','_','_']
string_geheim_woord = "clownbaard"
tot_nu_toe_geraden_woord = []
resterende_pogingen = 3
geraden = False
bevat_nummer = None

# maak het streepjes woord
def maak_streepjes_woord():
    streepjes_woord = []
    for i in range(len(geheim_woord)):
        streepjes_woord.append("_")
    print('Dit is het woord: ',streepjes_woord)
    return streepjes_woord


## GOK_LETTER FUNCTION ##
def gok_letter():
    global resterende_pogingen
    letter = input("\nGeef een letter: ")
    if letter.isalpha() and len(letter) == 1:

# Controleer of de letter in het woord zit en werk de pogingen bij
        if letter in geheim_woord:
            print('\nGoed geraden!')
            resterende_pogingen = resterende_pogingen - 1



# werk het geraden woord bij + print het tot dusver geraden woord + pogingen
            for i in range(len(geheim_woord)):
                if geheim_woord[i] == letter:
                    geraden_woord[i] = letter
            print('Dit heb je tot dusver:',geraden_woord)
            print('resterende_pogingen',resterende_pogingen)


# misgeraden, werk pogingen bij en laat zien wat er al wel geraden is
        else:
            print('\nHelaas, deze letter zit er niet in.')
            print('Dit heb je tot dusver:',geraden_woord)
            resterende_pogingen = resterende_pogingen - 1
            print('resterende_pogingen',resterende_pogingen)

    else:
        print("Verkeerde input. Geef één enkele letter op")
        gok_letter()

## GOK_WOORD FUNCTION ##
# laat de gebruiker een wordt invullen, als hij goed is stopt het spel
# als het fout is worden de pogingen bijgewerkt en kan de speler opnieuw kiezen
def gok_woord():
    global resterende_pogingen
    global geraden

    woord = input("Geef een woord: ")
    woord = list(woord)
    if woord == geheim_woord:
        geraden = True
        quit
    else:
        print('\nHelaas, dit is niet het geheime woord')
        resterende_pogingen = resterende_pogingen - 1
        print('resterende pogingen',resterende_pogingen)


## GOK FUNCTION
# Mag ofwel woord ofwel letter raden, springt door naar die functie
def gok():
    wat_raden = input("\nWil je een \letter\ of het \woord\ raden? " )
    if wat_raden == "letter":
        gok_letter()
    elif wat_raden == 'woord':
        gok_woord()
    else:
        print('\n Verkeerde input, Geef \woord\ of \letter\ op')

## BEVAT NUMMERS FUNCTION
def bevat_nummer(woord):
    global bevat_geen_nummer
    for i in woord:
        if i.isdigit():
            print('Geef een woord op zonder getallen')
            bevat_nummer = True
            gok_woord()
        else:
            bevat_nummer = False


## Start script
welkomswoord()
maak_streepjes_woord()

# Roept gok() aan zolang er nog pogingen over zijn en het woord nog niet is geraden
while resterende_pogingen > 0 and geraden == False:
    gok()
    if resterende_pogingen == 0:
        print('\nHelaas, je hebt geen pogingen meer over. Het woord was:   ',string_geheim_woord)
    elif geraden == True:
        print("\nGefeliciteerd, je hebt het woord geraden!")
