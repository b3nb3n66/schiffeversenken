#himmelsrichtung

gefeuert_aus = 'A1'
gefeuert_auf = 'B3'

# nord - süd 
if gefeuert_aus[1] > gefeuert_auf[1]:
    vertikal = 'Süd-'
elif gefeuert_aus[1] == gefeuert_auf[1]:
    vertikal = ''
else: 
    vertikal = 'Nord-'

# ost - west 
if gefeuert_aus[0] > gefeuert_auf[0]:
    horizontal = 'Ost'
elif gefeuert_aus[0] == gefeuert_auf[0]:
    horizontal = 'en'
else:
    horizontal = 'West'

# Ausgabe:
print('Kompass: Ihr Gegenspieler feuert aus', vertikal, horizontal)




# Schwer einzuschätzen wie man anfängt, weil Grundgerüst noch nicht steht.
# Python ist unspezifisch bei Datentypen und damit aber sehr flexible.

# Erst Nord/ Süd
# dann ost/ west

# dann ausgabe - Schwierigkeiten bei formulierung 

