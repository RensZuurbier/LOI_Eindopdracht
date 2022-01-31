geheime_woord = 'banaan'
lengte = float(len(geheime_woord))
gegokte_woord = ' '
print(lengte)
while lengte != 0:
    gegokte_woord.append('_')
print(gegokte_woord)

print('we zijn nu hier')
for i in range(len(geheime_woord)):

print(gegokte_woord)


def maak_streepjes_woord():
    streepjes_woord = []
    for i in range(len(geheim_woord)):
        streepjes_woord.append("_")
    print('Tot nu toe geraden woord:', streepjes_woord)
    return streepjes_woord
