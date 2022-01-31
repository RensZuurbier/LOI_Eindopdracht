geheime_woord = ['c','l','o','w','n','b','a','a','r','d',]
gegokte_woord = ['_','_','_','_','_','_','_','_','_','_']
geraden = False

def gok():
    woord_raden = input("\nwil je het woord raden? yes/no: ")
    if woord_raden == 'yes':
        woord_input = input('Geef het woord op: ')
#        print('Dus jij denkt',woord_input)
        woord_input = list(woord_input)
        if woord_input == geheime_woord:
            geraden = True

        else:
            print('Helaas, dit is niet het geheime woord')
    elif woord_raden == 'no':
        letter = input("\ngeef een letter: ")

        if letter in geheime_woord:
            print('\nGoed geraden!')
            for i in range(len(geheime_woord)):
                if geheime_woord[i] == letter:
                    gegokte_woord[i] = letter
        else:
            print('\nmispoes\n')

    print('Je hebt nu:', gegokte_woord)

while geraden == False:
    gok()
    
print('Gefeliciteerd je hebt het woord geraden!')
