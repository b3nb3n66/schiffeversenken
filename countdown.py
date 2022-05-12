#countdown & Spielanleitung









spielanleitung = "Spielanleitung: \n\n Als erstes verteilt Ihr Eure Flotte auf Eurem Spielfeld. Zu Eurer Flotte gehören diese Schiffe: \n XXXX \n Danach ratet Ihr abwechselnd, auf welchen Koordinaten (A1 bis J10) die gegnerischen Schiffe liegen. \n Trefft Ihr, macht Ihr ein Kreuz in das entsprechende Feld und seid gleich noch mal dran – auch mehrmals hintereinander. \n Trefft Ihr nicht, wird Euch das Feld markiert – so behaltet Ihr die Übersicht, wo Ihr es schon probiert habt. Dann ist Euer Gegenüber dran.  Wer die gegnerische Flotte als erstes versenkt hat, hat gewonnen."

print(spielanleitung)

# Quelle: https://www.zdf.de/serien/das-boot/videos/das-boot-schiffe-versenken-102.html



# Es sollte vor Spielbeginn wählbar sein, ob Timer im Spiel genutz werden soll
import time 

Zugdauer = 10

while Zugdauer:
    time.sleep(1)
    Zugdauer -= 1
    print(Zugdauer, end="\r")

# Quelle: https://junilearning.com/blog/coding-projects/make-countdown-timer-python/

# Nach Ablauf der Zeit wird ein zufälliges Feld gewählt








