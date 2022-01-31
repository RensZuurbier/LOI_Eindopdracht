#bevat_geen_nummer = False

#def bevat_nummer(woord):
#    global bevat_geen_nummer
#    for i in woord:
#        if i.isdigit():
#            bevat_geen_nummer = True
#            print(bevat_geen_nummer)

#woord = "banaan12"
#bevat_nummer(woord)

isnr = None

print(isnr)

def containsNumber(value):
    print(value)
    global isnr
    for i in value:
        if i.isdigit():
            isnr = True
        else:
            isnr = False

value = "banaan"
containsNumber(value)
print(isnr)
