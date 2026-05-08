________________________________
1.
Ziel der Übungen

Ziel der Herstellung dieses RPG-Spiels ist es, Sie an Python heranzuführen. Dabei werden Bezüge zu bereits bekanntem (Java, C) hergestellt, sowie neue Konzepte und Datenstrukturen vermittelt.

Hinweise

Es wird empfohlen, Source Codes nicht per copy’n’paste in Ihre Programme zu übernehmen, sondern ihn abzutippen. Immer wenn sich Ihr Gehirn für eine Leistungserbringung anstrengen muss erscheint ihm das Aufgenommene speichernswerter – So trainieren Sie Ihr Gehirn mit Python-Syntax.
Ebenso ist es empfehlenswert die "Hintergrund"-Abschnitte sorgfältig durchzuarbeiten. Sie führen weitere Konzepte/Ideen ein und zeigen die Unterschiede zu anderen Programmiersprachen.
Sollte es vorkommen, dass Sie bei den Übungen auf Inhalte stoßen, die Ihnen gänzlich unbekannt sind bzw. bei denen Sie möglicherweise noch einmal Grundlagenwissen benötigen, sichten Sie die externen Verlinkungen in den Kapiteln "Basics & More". Hier finden Sie auch Hinweise zu weiterführenden Themen (für Fortgeschrittene).
Den vollständigen Source Code zu einer Übung finden Sie im entsprechenden "Source Code"-Bereich (falls freigeschaltet).
Letzter Tipp (ehrlich!): In der Bibliothek der Außerstelle finden Sie zahlreiche Grundlagen- und Ergänzungsliteratur zum Thema (und man kann dort z. B. in Freistunden ganz in Ruhe arbeiten).
Ausblick

Sehen Sie sich an was wir herstellen wollen: https://trinket.io/embed/python/d06adeb527?outputOnly=true&start=result

Viel Spaß dabei!

Quelle

Die Idee und große Teile des Source Codes entstammen dem Projekt "RPG" - einem Tutorial der Raspberry Pi Foundation zum Erlernen der Programmiersprache Python. Adresse: https://projects.raspberrypi.org/en/projects/rpg
_________________________________
2.
RPG-GAME
Ü1 - Erste Schritte
Ziel der Übung

Herstellung eines ersten, lauffähigen Programms
Ausgabe statischer Informationen
Ein leeres Python-Programm

Gehen Sie wie folgt vor, um ein neues (erstes) Python-Programm anzulegen:

Wechseln Sie in Ihr „Home“-Laufwerk.

Legen Sie die Ordner „python“ und darunter „rpggame“ an.

Erstellen Sie im Ordner eine neue Textdatei mit dem Namen „rgpgame.py“.

Erste Anweisungen ergänzen

Öffnen Sie die Datei in einem Text-Editor Ihrer Wahl (z. B. „Windows Editor“).

Übernehmen Sie den nachstehenden Programmcode in die geöffnete, noch leere Datei und speichern Sie die Änderung.

print('''
Welcome to your own RPG Game
============================

Get to the Garden with a key and a potion.
Avoid the monsters!

Commands:
  go [direction]
  get [item]
''')
Das Programm ausführen

Starten Sie Ihr Programm indem Sie eine Kommandozeile öffnen, in den Pfad navigieren und den nachstehenden Befehl ausführen:
python rpggame.py
_____________________________________
3.
RPG-GAME
↪ Hintergrund - Ausgabe
Ausgaben mit print() und Dynamische Typisierung

In Python werden Benutzerausgaben vergleichbar wie in C und Java gestaltet. Mit der Anweisung

print("Welcome to your own RPG Game!")
wird die als Parameter übergebene Zeichenkette ausgegeben. Im Bespiel wurden statt doppelter Anführungszeichen (") drei aufeinander folgende einfache Anführungszeichen (') verwendet. Diese Anwendung erlaubt es, dass die zwischen den Anführungszeichen eingesetzten Zeichen exakt wie angegeben (z. B. inklusive der Zeilenumbrüche) in der Konsole ausgegeben werden.

Ebenso ist es möglich, Inhalte von Variablen auszugeben, die zuvor deklariert wurden. Hier ergeben sich aber möglicherweise ungewohnte Abweichungen gegenüber den bisher erlernten Programmiersprachen.

numberOfMonsters = 7
print(numberOfMonsters)
Python unterstützt die sogenannten dynamische Typisierung. Währen in C und Java bei jeder Variablendeklaration der Typ mit anzugeben war (z. B. "int numberOfMonsters;") ist das in Python nicht nötig. Python wählt den zur Zuweisung passenden Datentyp. Im Beispiel wird die Variable "numberOfMonsters" zur Ganzzahl-Variable (int), indem ihr der ganzzahlige Wert "7" zugewiesen wird. Eine Ausgabe mittels "print()" ebenso möglich. Wenn eine Funktion unterschiedliche Datentypen unterstützt, sagen wir, dass die Funktion überschrieben wurde (z. B. "print(str)", "print(int)", "print(float)", ...).

Im nächsten Beispiel soll die Ausgabe der ganzzahligen Monsteranzahl um eine vorangestellte Zeichenkette ergänzt werden.

print("Anzahl Monster: ", numberOfMonsters);
Die Funktion "print()" unterstützt auch verschiedene Anzahlen von Parameter. während in den oberen Beispielen immer nur ein Parameter übergeben wurde ("Welcome to my RPG Game!" oder die Variable "numberOfMonsters") werden hier zwei Parameter übergeben (1. "Anzahl Monster: ", 2. numberOfMonsters). Wenn Funktionen mit gleichem Bezeichner, aber verschiedenen Parameteranzahlen existieren, sprechen wir vom Überladen der Funktion.

Der letzte Schritt geht noch einmal zur dynamischen Typisierung zurück. Zum besseren Verständis werden die oben besprochenen Beispiel noch einmal eingefügt und um die letzten beiden Zeilen ergänzt.

print("Welcome to my RPG Game!")
numberOfMonsters = 7
print(numberOfMonsters)
print("Anzahl Monster: ", numberOfMonsters);
numberOfMonsters = "Seven"
print(type(numberOfMonsters))
In der vorletzten Zeile wird der bereits deklarierten Integer-Variable "numberOfMonsters" der Wert "Seven" zugewiesen - eine Zeichenkette. Die letzte Anweisung nutzt die Funktion "type()" um den Datentyp des Parameters (hier die Variable "numberOfMonsters") auszugeben. Die nachstehende Ausgabe zeigt das Ergebnis.

<class 'str'>
Der Typ der Variable wurde also durch die neue Zuweisung von "Seven" (einer Zeichenkette) von "int" zu "str" geändert - dynamische Typisierung eben :-)
_______________________________________________________________
4.
RPG-GAME
↪ Basics & More
Basics: Datentypen

In dieser externen Ressource werden die elementaren (und weiterführende) Datentypen inklusive Beispielen erläutert.

https://www.w3schools.com/python/python_datatypes.asp

Hinweis: Die auf der Internetseite erläuterten Datentypen Liste (list) und Dictionary (dict) werden in Ü02 behandelt.
___________________________________________________________________
5.
RPG-GAME
Ü2 - Grundstruktur
Ziele der Übung

Herstellung einer Funktion zur Ausgabe von Spiel-Anweisungen (Was kann der Spieler tun).
Einführung einer Variable zur Speicherung der vollständigen Spielewelt.
Einführung einer Variable zur Speicherung des aktuellen Raums, indem sich der Spieler gerade befinden.
Herstellung einer Funktion zur Anzeige des aktuellen Spiel-Zustandes (Anzeige des aktuellen Raums, Gegenstände im Raum, Anzeige Inventar)
Einführung "showInstructions()"

Der "print()"-Aufruf aus der vorherigen Übung soll in eine Funktion namens "showInstructions()" verschoben werden.

def showInstructions():
  #print a main menu and the commands
  print('''
Welcome to your own RPG Game
============================

Get to the Garden with a key and a potion.
Avoid the monsters!

Commands:
  go [direction]
  get [item]
''')
Einführung "showStatus()"

Um den aktuellen Status unseres Charakters und unserer Spielwelt bzw. Umgebung ausgeben zu können, soll die Funktion "showStatus()" eingeführt werden:

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")
Die Funktion gibt aus, in welchem Raum sich der Spieler befindet ("print('You are in the ' + currentRoom)"), was er in seinem Inventar mitführt ("print('Inventory : ' + str(inventory))") und ob sich Gegenstände ("items") im aktuellen Raum befinden - falls ja, werden diese angezeigt.

Einführung des "Inventories" (Liste)

Damit unser Spiele-Charakter Dinge bei sich tragen kann, führen wir die Variable "inventory" vom Typ "Liste" (list) ein:

#an inventory, which is initially empty
inventory = []
Einführung der Spielewelt: "rooms" und "currentRoom"

Der Aufbau der Spielewelt soll in der Variablen "rooms" vom Typ "Dictionary" (kurz "dict") abgebildet werden.

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : { 
                  'south' : 'Kitchen'
                },

            'Kitchen' : {
                  'north' : 'Hall'
                }

         }
Eine "grafische Interpretation" des Wertes der Variable "rooms" könnte so aussehen:

Die Spielewelt enthält zum aktuellen Zeitpunkt nur zwei Räume

Es soll abgebildet werden, dass man ausgehend vom Raum "Hall" den Raum "Kitchen" erreichen kann, indem man in Richtung "south" geht. Umgekehrt kann man ausgehend von "Kitchen" nach "north" gehen um den Raum "Hall" zu erreichen. Allerdings steht das so (noch) nicht im Quelltext - aktuell ist das Wechseln der Räume nicht möglich und es bleibt bei der bloßen Abbildung von Raum-Verknüpfungen im Dictionary.

Während "rooms" die Spielewelt repräsentiert, also alle Räume, die der Spieler potentiell betreten kann, benötigen wir noch eine Variable, die zeigt (speichert) in welchem Raum sich der Spieler aktuell befindet - currentRoom.

#start the player in the Hall
currentRoom = 'Hall'
Das "Hauptprogramm"

Nachdem zwei Funktionen "showInstructions()" und "showStatus()", sowie die Liste "inventory", das Dictionary "rooms" und (die Zeichenkette) "currentRoom" eingeführt wurden, wird es zeit für das eigentliche Hauptprogramm. Damit das Programm nach der Abarbeitung der vielen Ideen oben auch etwas zeigt, ergänzen Sie bitte die beiden Funktionsaufrufe am Ende Ihres Quelltextes.

showInstructions()
showStatus()
______________________________________
6.
RPG-GAME
↪ Hintergrund - Funktionen & Einrückungen
Ziele der Übung

Wiederholgung des Umgangs mit Funktionen (Verwendung, Bestandteile/Aufbau)
Herstellung von Funktionen in Python mittels "def"
Verstehen der Klammerung von Anweisungen durch Einrückungen
Wiederholung von Fallunterscheidungen zur Programmablaufsteuerung
Funktionen

Funktionen (manchmal auch Unterprogramme genannt) werden auch in Python eingesetzt um Anweisungen zu gruppieren, mit dem Ziel, der

übersichtlicheren Programmstrukturierung,
der Unterstützung des DRY-Prinzips (DRY = "don't repeat yourself", i. S. v. Source Code-Duplikaten) und der damit verbundenen
vereinfachten Wartung von Funktionalitäten (weil es den Code genau 1x gibt).
Vermutlich ist Ihnen aufgefallen, dass es in Python nicht die Klammerung zur Abgrenzung des Funktionskörpers gibt. Statt dessen wird in Python die Einrückung benutzt, um zu beschreiben, welche Zeilen des Programms zum Funktionkörper gehören und welche nicht mehr. Ein Beispiel.

In Java würde eine Funktion zum Addieren zweier Zahlen wir folgt implementiert werden können:

public double addiere(int zahl1, int zahl2){
    return zahl1 + zahl2;
}
Die geschweiften Klammern beschreiben also, was zur Implementierung (Funktionskörper) gehört - alles was zwischen "{" und "}" steht.

Die gleiche Funktion würde in Python wie folgt beschrieben werden:

def addiere(zahl1, zahl2):
    return zahl1 + zahl2
Durch die Einrückung per Tab (Tabulator-Taste) wird beschrieben, dass die Zeile mit dem "return ..." zum Funktionskörper gehört.

Zusamenfassend können wir also festhalten, dass Funktionen in Python

durch das Schlüsselwort "def" eingeleitet werden (jetzt ist bekannt, dass eine neue Funktion hergestellt werden soll),
danach der Bezeichner der Funktion folgt (im Beispiel "addiere"), dann
in runden Klammern die Menge der Übergabeparameter folgt (hier "zahl1" und "zahl2" (i. d. R. ohne Datentypangabe)) und
zuletzt ein Doppelpunkt folgt. Weiterhin müssen
alle Anweisungen, die zu der Operation gehören (Funktionskörper) anschließend gegenüber der "def"-Anweisung genau einen Tab eingerückt sein.
Wie sieht es mit diesem Beispiel aus:

def addiere(zahl1, zahl2):
    return zahl1 + zahl2
print(addiere(2, 5))
Da die letzte Zeile ("print ...") nicht eingerückt ist, gehört sie nicht mehr zum Funktionkörper. Sie steht (optisch wie logisch) mit der Funktionsdeklaration (Zeile mit "def ...") auf einer Höhe.

Müssen die Einrückungen immer genau einen Tab groß sein? Ja und Nein. Sehen wir uns folgendes Beispiel an:

def dividiere(divident, divisor):
    if divisor == 0:
        # Division durch Null ist nicht definiert
        print(divident, " / ", divisor, " = ", "Nicht lösbar!")
    else:
        print(divident, " / ", divisor, " = ", str(divident/divisor))
diviere(10, 2)
diviere(10, 3)
diviere(10, 0)
Wir deklarieren eine Funktion namens "dividiere", die zwei Parameter (Divident und Divisor) übergeben bekommt. Die Division durch Null ist nicht erlaubt. Die Zeile "if divsisor == 0:" testet auf die Gleichheit mit Null und ändert in diesem Fall die Berechnung ab. Der Normalfall ist im "else"-Zweig enthalten. Wie Sie sehen können, funktioniert auch hier die (weitere) Einrückung als eine Art Klammer: Sowohl der Kommentar ("# ...", als auch der erste "print"-Aufruf gehören zum Than-Zweig, der zweite "print"-Befehl gehört zum "else"-Zweig. Die "dividiere(10, 2) ..."-Aufrufe gehören nicht mehr zur Funktion, weil sie nicht eingerückt sind.

Die Ausgabe sieht übrigens wie erwartet aus (die 5 ganz am Ende der zweiten Zeile ist übrigens ein Problem der Numerik):

10  /  2  =  5.0
10  /  3  =  3.3333333333333335
10  /  0  =  Nicht lösbar!
_________________________________________________________________
7.
RPG-GAME
↪ Hintergrund - Liste
Ziele der Übung

Deklaration und Definition von Listen
Kennen ausgewählter Funktionen, die auf Listen angewandt werden können
Arbeiten mit geschachtelten Listen
Unterscheidung von Listen und Tupeln
Listen herstellen

Listen werden in Python verwendet, um Informationen datentypübergreifend, mengenwertig und sortiert abzulegen.

Schauen wir uns an Beispielen an, was diese Adjektive bedeuten:

inventory = []
print(inventory)
Das Beispiel legt eine neue Liste an, die auf den Namen "inventory" hört. Dass "inventory" eine Liste ist, erkennt man an den eckigen Klammern "[" und "]". Die "print ..."-Anweisung gibt den Inhalt von "inventory" wieder aus. Das Ergebnis ist:

[]
Das ist die sogenannte leere Liste - eine Liste, in der sich (aktuell) nichts befindet.

Damit es nicht so langweilig bleibt, kann man die Liste von Anfang an mit Werten befüllen.

inventory = ["Compass", "Water Pistol", "Chopsticks", 84, 3.2]
print(inventory)
Jeder (mittels Komma vom "Nachbarn" getrennte) Eintrag ist ein sogenanntes Element. Die Ausgabe ist die Folgende:

['Compass', 'Water Pistol', 'Chopsticks', 84, 3.2]
Dabei sind folgende Eigenschaften von Listen bzw. der enthaltenen Elemente merkenswert. Listen sind ...

... datentypübergreifend, was man daran erkennen kann, dass sowohl Elemente von Typ Zeichenketten als auch unterschiedliche Zahlenarten in einer Liste gespeichert werden können
... mengenwertig, sie können beliebig viele Elemente (auch keine) speichern
... soriert. Die Elemente haben eine festgelegte Reihenfolge, denn Sie wurden extakt in der Reihenfolge aussgeben, wie Sie eingegeben wurden.
Auf Listenelemente zugreifen

Man kann auf Listenelemente mithilfe von Indizes zugreifen. Der Index (Einzahl von Indizes) ist das n-te Element einer Liste, wobei die Zählung bei Null startet. Der Index wird dabei in eckigen Klammern an die Liste gehängt
inventory = ["Compass", "Water Pistol", "Chopsticks", 84, 3.2]
print(inventory[0])
print(inventory[2])
print(inventory[-1])
Die Ausgabe sieht (fast) wie erwartet aus:

Compass
Chopsticks
3.2
An 1. Stelle (Index 0) der Liste "inventory" steht der Kompass, an 3. Stelle (Index 2) die Essstäbchen und an letzter Stelle die Fließkommazahl 3,2. Man kann mit dem Index "[-1]" also das letzte Element der Liste erreichen.

Ebenso ist es möglich, mithilfe des Index gezielte Veränderungen an den Werten von Listenelementen vorzunehmen:

inventory = ["Compass", "Water Pistol", "Chopsticks"]
print(inventory)
inventory[0] = "Paper airplane"
print(inventory)
Die dazugehörige Ausgabe:

['Compass', 'Water Pistol', 'Chopsticks']
['Paper airplane', 'Water Pistol', 'Chopsticks']
Quizfrage! Was haben diese Anweisungen ...

inventory = []
print(inventory[-1])
... und diese Anweisungen ...

inventory = ["Compass", "Water Pistol", "Chopsticks", 84, 3.2]
print(inventory[123])
... gemeinsam!?!

Korrekt! Sie erzeugen die gleiche Fehlermeldung!

IndexError: list index out of range
Die Anweisung "print(inventory[-1])" versucht auf das letzte Element einer leeren Liste zuzugreifen - das gibt es nicht. Ebenso versucht die Anweisung "print(inventory[123])" auf das 124. Element (Index 123) der Liste zuzugreifen. Wenn wir die Fehlermeldung frei übersetzten, sagt sie uns, dass wir versuchen auf einen Index zuzugreifen, der auserhalb der Indizes der Liste liegt.

Pro-Tipp: Die genaue Fehlermeldung sagt sogar aus, wo genau unser Programm den Fehler erzeugt:

Traceback (most recent call last):
  File "C:\Users\...\031-Listen.py", line 15, in <module>
    print(inventory[-1])
IndexError: list index out of range
Kurzform: in Zeile 15 hat die Anweisung "print(inventory[-1])" einen Indexfehler erzeugt.  -> Keine Angst vor kompliziert (erscheinenden) Fehlermeldungen!

Funktionen für Listen

Python bringt eine Menge von Funktionen mit, die speziell für die Arbeit mit Listen entwickelt wurden. In diesem Abschnitt wollen wir einen Blick auf ausgewählte Funktionen und deren Anwendung werfen.

Schauen wir uns dazu einige Beispiele an.

inventory = []
cities = ["Leipzig", "Halle", "Berlin", "Dresden", "Chemnitz"]
print(len(inventory))
print(len(cities))
Die Funktion "len( )" benötigt als Übergabeparameter eine Liste und gibt die Anzahl der Elemente dieser Liste zurück. Im Beispielaufruf "print(len(inventory))" wird also zunächst die Länge der leeren Liste "inventory" bestimmt. Diese hat den Wert Null (0). Anschließend wird dieser Wert als einziger Parameter der "print"-Funktion übergeben und diese druckt die Null auf den Bildschirm.

Beim zweiten Aufruf für die Liste "cities" wird eine 5 ausgegeben.

Hinweis: Zu beachten ist hierbei, dass es sich um die Anzahl von Elementen in der Liste handelt (also 5) und nicht um den Wert des größten Index (also 4).

Jetzt wollen wir unser Inventar ein bisschen erweitern, indem wir lauter Elemente hinzufügen:

inventory = []
inventory.append("rubber duck")
inventory.append("chocolate")
inventory.append("racoon")
print(inventory)
Wie zu erwarten gibt der "print..."-Befehl "['rubber duck', 'chocolate', 'racoon']" aus.

Jeder "append( )"-Aufruf hängt an die vorhande Liste das übergebene Element an. Was aber, wenn wir an einer bestimmten Stelle ein Element einfügen wollen? Dabei hilft uns "insert( )". Wir ergänzen das letzte Programm um die folgenden Zeilen:

inventory.insert(2, "glue")
print(inventory)
Die Ausgabe sieht wie folgt aus. Zur Vereinfachung des Verständnisses wurde in der ersten Zeile noch einmal die Ausgabe von oben eingefügt ("vorher").

['rubber duck', 'chocolate', 'racoon']
['rubber duck', 'chocolate', 'glue', 'racoon']
An der 3. Stelle (Index 2) ist der Kleber einsortiert worden. Der Waschbär ist eine Stelle nach hinten gerückt. Wenn wir uns den "insert..."-Aufruf noch einmal im Detail anschauen, stellen wir fest, dass er zwei Übergabeparameter benötigt:

den Index (nicht die Stelle) der Liste, an der das neue Element eingefügt werden soll (im Beispiel 2) und
den Wert des einzufügenden Elementes (im Beispiel "glue").
Probieren Sie unbedingt mal aus, an welcher Stelle / welchem Index die Gurke eingefügt wird, wenn Sie den nächsten Befehl anwenden. Möglicherweise sieht die Liste hinterher anders aus, als Sie es erwarten würden. ☺

inventory.insert(-1, "cucumber")
Die letzte Funktion, mit der wir im Zusammenhang von Listen arbeiten wollen, ist "pop( )". Sehen Sie sich dieses Beispiel an und versuchen Sie die Arbeitsweise festzustellen.

toDoList = ["Bad putzen", "einkaufen", "zocken", "programmieren üben!!"]
print("Noch zu tun: ", toDoList)
nextTask = toDoList.pop()
print("Als nächstes: ", nextTask)
print("Noch zu tun: ", toDoList)
Die Ausgabe sieht dabei wie folgt aus:

Noch zu tun:  ['Bad putzen', 'einkaufen', 'zocken', 'programmieren üben!!']
Als nächstes:  programmieren üben!!
Noch zu tun:  ['Bad putzen', 'einkaufen', 'zocken']
Wie sie der Ausgabe entnehmen können, nimmt "pop( )" das letzte Element der Liste und gibt es zurück. Im Beispiel wird es der Variablen "nextTask" als Wert zugewiesen. Man sieht auch, dass das Element der Liste dauerhaft entfernt wurde, denn "programmieren üben!!" fehlt jetzt in der letzten Ausgabe (und damit in der "toDoList").

Halten wir den Zwischenstand fest:

len(): "Länge" bzw. Anzahl Elemente einer Liste bestimmen
append(): Element an eine vorhanden Liste anhängen
insert(): Element in einer vorhande Liste einfügen
pop(): das letzte Element (Index "-1" oder "len(liste)-1") der Liste entfernen und zurückgeben
Listen von Listen (von Listen (von ...

Wenn eine Liste aus einzelnen Elementen bestehen kann, kann dann so ein einzelnes Element auch eine (zweite) Liste sein? Die Antwort ist ja. Jedes Element kann wiederum eine separate Liste sein. Beginnen wir mit einem Beispiel:

toDoList = [["Bad putzen", "einkaufen", "Brokkoli essen"], ["zocken", "Streaming", "Pizza essen"]]
Zum besseren Verständnis kann man die Anweisung auch so darstellen:

Listen als Elemente von Listen

Soll ein bestimmtes Element adressiert werden, z. B. "Brokkoli essen", muss man zunächst verstehen, dass "toDoList" aus nur zwei Elementen besteht, nicht aus sechs, wie man vermuten könnte. Da das erste Element eine vollständige Liste ist (wie immer an den den eckigen Klammern zu erkennen), ist es notwendig, zunächst diese auszuwählen. Mit "toDoList[0]" erhält man das 1. Element der toDoList, also die "grüne" Liste als ein Element zurück. Da "toDoList[0]" wie bereits festgestellt eine Liste ist, kann man natürlich das Element "Brokkoli essen" auswählen, indem man den den Index "2" bzw. "-1" auswählt.

Fasst man diese Überlegungen zusammen, muss man von toDoList im Index 0 (grüne Liste) den Index 2 ("Brokkoli essen") auswählen, also "toDoList[0][2]" oder (da "Brokolli essen" das letzte Element der "grünen Liste" ist) "toDoList[0][-1]"

Im Quellcode sieht das genauso aus:

toDoList = [["Bad putzen", "einkaufen", "Brokkoli essen"], ["zocken", "Streaming", "Pizza essen"]]
print(toDoList)
print(toDoList[0])
print(toDoList[0][-1])
Die Ausgabe entspricht ebenfalls den Überlegungen:

[['Bad putzen', 'einkaufen', 'Brokkoli essen'], ['zocken', 'Streaming', 'Pizza']]
['Bad putzen', 'einkaufen', 'Brokkoli essen']
Brokkoli essen
Listen und Tupel

Der letzte Abschnitt soll eine (gar nicht so) neue Datenstruktur einführen, die Tupel (engl. "tuple"). Tupel sind in Python Listen, deren Inhalt (also die Elemente) - einmal definiert - im Laufe des Programms nicht mehr geändert werden können.

Damit man Listen und Tupel sicher unterscheiden kann, sieht die Python-Syntax vor, dass Tupel in runden Klammern dargestellt werden.

Hier zunächst ein Beispiel mit einer Liste (_nicht_ Tupel).

cityList = ["Leipzig", "Halle", "Dresden"]
print(cityList)
print(cityList[-1])
cityList.append("Berlin")
print(cityList)
Die Ausgabe zeigt keine Überraschungen:

['Leipzig', 'Halle', 'Dresden']
Dresden
['Leipzig', 'Halle', 'Dresden', 'Berlin']
Jetzt das gleiche Beispiel mit einem Tupel anstelle der Liste. Der einzige Unterschied sind die runden anstelle der eckigen Klammern.

cityTupel = ("Leipzig", "Halle", "Dresden")
print(cityTupel)
print(cityTupel[-1])
cityTupel.append("Berlin")
print(cityTupel)
Die Ausgabe zeigt jetzt Unterschiede:

('Leipzig', 'Halle', 'Dresden')
Dresden
Traceback (most recent call last):
  File "C:\Users\...\035-Listen-Tupel.py", line 12, in <module>
    cityTupel.append("Berlin")
AttributeError: 'tuple' object has no attribute 'append'
Die ersten beiden "print..."-Anweisungen erzeugen noch das Erwartungsbild. Beachten Sie, dass auch in der Ausgabe runde anstelle der eckigen Klammen verwendet werden. So kann man Tupel zielsicher von Listen unterscheiden.

Der "append( )"-Aufruf erzeugt jedoch die Fehlermeldung "AttributeError: 'tuple' object has no attribute 'append'", die aussagt, dass Tupel-Objekte über kein "append" verfügen. Und das müssen sie auch nicht, denn ein Anhängen von Elemente an ein Tupel würde dieses verändern. Und Tupel sollen nicht veränderbar sein (vgl. oben).
__________________________________________________________
8.
RPG-GAME
↪ Hintergrund - Dictionary
Ziele der Übung

Deklaration und Definition von Dictionaries
Hinzufügen und Entfernen von Einträgen in Dictionaries
Anwenden ausgewählter Funktionen auf Dictionaries
Verstehen der Arbeitsweise von bzw. mit Schlüsseln
Entfernen von Wien aus der Liste der relevanten Hauptstädte
Dictionary = Wörterbuch = häää?

Zugegeben, man kann in der Datenstruktur Dictionary auch hervorragend Wörterbücher abbilden, aber das ist bei weitem nicht die einzige Verwendung. Aber fangen wir erst einmal locker an.

Ein Dictionary in Python (auch in anderen Programmiersprachen als assoziatives Array bezeichnet), dient der Speicherung von Werten, die über einen Schlüssel abgerufen werden können. Klingt kompliziert? Beispiel!

members = { 1 : "Peter", 2 : "Pia", 3 : "Saria", 4 : "Maik" }
Element-Bezeichnungen im Datentyp Dictionary

Lassen Sie uns die einzelnen Bestandteile der Abbildung durchgehen:

Möchte man einen Wert in einem Programm mehrfach / längere Zeit nutzen, benötigt man eine Variable mit entsprechendem Variablenbezeichner oder -namen, hier "members".
Das es sich bei dem Ausdruck rechts vom "="-Zeichen um ein Dictionary handelt, erkennt man (und auch der Python-Interpreter) an den gescheiften Klammern. Ähnlich wie bei Listen, ist das "kleinst-mögliche" Dictionary das leere Dictionary: "members = { }".
Bei nicht-leeren Dictionaries folgt befindet sich innerhalb der geschweiften Klammern mindestens ein Schlüssel-Wert-Paar. Mehrere Schlüssel-Wert-Paare werden durch Komma getrennt. Im Beispiel oben gibt es vier Schlüssel-Wert-Paare: "1 und Peter", dann "2 und Pia", ...
Wenn wir uns das erste Schlüssel-Wert-Paar im Beispiel betrachten, können wir festhalten, dass
"1" der Schlüssel ist (weil er links vom Doppelpunkt steht) und
"Peter" der Wert zum Schlüssel ist (weil er rechts vom Doppelpunkt steht).
Hinweis: Der Schlüssel hat eigentlich keine Anführungszeichen, weil es sich um eine Ganzzahl handelt.
Dictionaries sind Datenstrukturen, die das Ablegen und Abrufen von Werten anhand der Schlüssel ermöglichen. Bestimmte Werte kann man nur über den Schlüssel abrufen. Man sagt daher auch, dass "der Schlüssel auf den Wert abbildet" (wie bei Funktionen in der Mathematik, x -> x²).

Lassen Sie uns noch ein paar Beispiele ansehen und mit Ihnen arbeiten ...

members = { 1 : "Peter", 2 : "Pia", 3 : "Saria", 4 : "Maik" }
print(members[2]);
Welches ist eigentlich unser 2. Mitglied? Ah, Pia! Genauer gesagt müsste die Frage lauten: "Welcher Wert ist eigentlich zum Schlüssel 2 gespeichert"? Bitte beachten Sie hier den Unterschied zu den Listen: Die Adressierung "members[2]" greift nicht an die zweite Stelle des Dictionary zu (ist also kein Index), sondern lädt den Wert zum Schlüssel 2. Hier der "Beweis":

members = { 2 : "Pia", 4 : "Maik", 3 : "Saria", 1 : "Peter" }
print(members[2]);
Auch hier ist die Ausgabe wieder "Pia", und dass obwohl Pia als erster Eintrag steht.

Lassen Sie uns festhalten: Dictionaries kennen keine Ordnung (Sortierung).

Noch ein Beispiel, bei dem deutlich wird, dass "members[2]" kein Index sein kann:

birthdays = {"Peter" : "12.12.2000", "Franziska" : "04.05.2012", "Frauke" : "09.10.1985"}
print("Peter hat am", birthdays["Peter"], "Geburtstag!")
Hier die Ausgabe:

Peter hat am 12.12.2000 Geburtstag!
Da der Schlüssel hier eine Zeichenkette ist, muss auch die Adressierung per Zeichenkette erfolgen: birthdays["Peter"]

Zum Abschluss dieses Abschnittes noch eine spannende Sache: Die Werte können natürlich auch von beliebigen Datentypen sein, so auch Listen!!!

verlieheneDinge= {"Peter" : ["Schwimmbeutel", "Gummibaum", "10 Ost-Mark"], "Claus" : ["Bierzeltgarnitur", "Eintagsfliege", "Wanderstab"]}
print("An Claus verliehen:", verlieheneDinge["Claus"])
Die Ausgabe zeigt alles an, was an Claus verliehen wurde. Es ist eine Liste von Dingen (erkennbar an den eckigen Klammern):

An Claus verliehen: ['Bierzeltgarnitur', 'Eintagsfliege', 'Wanderstab']
Dictionaries zur Laufzeit Werte hinzufügen und entfernen

Lassen Sie uns zur Laufzeit (also während der Programmausführung ein paar Schlüssel-Wert-Paare zu einem Dictionary hinzufügen.

capitals = {}
capitals["Deutschland"] = "Bärliehn"
capitals["Frankreich"] = "Paris"
print(capitals)
capitals["Deutschland"] = "Berlin"
print("Die Hauptstadt von Deutschland ist", capitals["Deutschland"])
Die Ausgabe sieht wie folgt aus:

{'Deutschland': 'Bärliehn', 'Frankreich': 'Paris'}
Die Hauptstadt von Deutschland ist Berlin
Einträge zu Dictionaries werden also einfach durch die Angabe eines Schlüssels und eines Wertes hinzugefügt: "capitals["Frankreich"] = "Paris"". Ist der Schlüssel bereits vorhanden (wie bei "Deutschland"), wird der Wert einfach aktualisiert.

Oh, wie unangenehm: Wien fehlt in der Liste der wichtigen Hauptstädte. Schnell ... bevor das noch jemand merkt:

capitals["Österreich"] = "Wien"
Puhh! Das war knapp!

Angenommen, es gibt Listeneinträge die kein Mensch, jemals wieder, also wirklich niiiiiieeeeeeeee wieder jemand braucht, dann kann man diese Schlüssel-Wert-Paare anhand des Schlüssels entfernen:

capitals = {"Deutschland" : "Berlin", "Frankreich" : "Paris", "Polen" : "Warschau", "Österreich" : "Wien"}
del capitals["Österreich"]
Das "del"-Schlüsselwort kann in Python unter anderem verwendet werden, um dies durchzuführen. Allgemeiner formuliert lautet die Anweisung "del <dictionary>[<key>]", also z. B. "del capitals["Österreich"]"

Der Schlüsseldienst für Dictionaries

Was passiert, wenn man einen Schlüssel adressieren möchte, der im Dictionary nicht existiert?

capitals = {"Deutschland" : "Berlin", "Frankreich" : "Paris", "Polen" : "Warschau"}
print("Die Hauptstadt von Österreich ist", capitals["Österreich"])
Na klar, es kommt eine Fehlermeldung:

Traceback (most recent call last):
  File "C:\Users\...\041-Dictionary.py", line 11, in <module>
    hauptstadtOesterreich = capitals["Österreich"]
KeyError: 'Österreich'
"KeyError: 'Österreich'" ist ziemlich eindeutig. Der Schlüssel existiert nicht. Für uns Programmierer und Programmiererinnen existieren ein paar Operatoren, mit deren Hilfe wir so ein Problem vermeiden können. Die wichtigste ist "in" zur Prüfung, ob ein Schüssel in einem Wörterbuch vorhanden ist.

capitals = {"Deutschland" : "Berlin", "Frankreich" : "Paris", "Polen" : "Warschau"}
if ("Österreich" in capitals):
    print("Die Hauptstadt von Österreich ist", capitals["Österreich"])
else:
    print("Es existiert kein Eintrag für Österreich im Wörterbuch der relevanten Hauptstädte. Sorry, Rainer.")
Die Zeile ""Österreich" in capitals" oder allgemeiner gesprochen "<Schlüssel> in <dictionary>" gibt einen Wahrheitswert zurück. Da in unserem Beispiel Österreich nicht in "capitals" enthalten ist, ergibt die Prüfung "false" und es wird der "else"-Zweig der Fallunterscheidung ausgeführt. Mit dieser Variante kann man die oben beschriebene Fehlermeldung vermeiden. Aber noch schönes wäre es doch, wenn man über alle Einträge des Dictionaries iterieren könnte.

Auslesen aller Schlüssel in einem Dictionary.

capitals = {"Deutschland" : "Berlin", "Frankreich" : "Paris", "Polen" : "Warschau"}
for country in capitals:
    print(country)
Die zweite Zeile bedeutet, dass einmal alle Einträge des Dictionary in einer Schleife durchlaufen werden und für jeden Schleifendurchlauf (Iteration)

der Wert des aktuellen Schlüssel in der Variable "country" gespeichert wird und
der Schleifenkörper ausgeführt wird.
Für das Beispiel-Dictionary sieht das Ganze also so aus:

Durchlauf: country hat den Wert "Deutschland"
Durchlauf: country hat den Wert "Frankreich"
Durchlauf: country hat den Wert "Polen"
Wenn man mithilfe des "in"-Operators alle Schlüssel eines unbekannten Wörterbuchs auslesen kann, kann man anschließend auch auf die Werte (mithilfe der dann bekannten Schlüssel) zugreifen:

capitals = {"Deutschland" : "Berlin", "Frankreich" : "Paris", "Polen" : "Warschau"}
for country in capitals:
    print("Die Hauptstadt von", country, "ist", capitals[country])
Die unüberraschende Ausgabe:

Die Hauptstadt von Deutschland ist Berlin
Die Hauptstadt von Frankreich ist Paris
Die Hauptstadt von Polen ist Warschau
Übrigens ist die Anweisung "country in capitals.keys( )" semantisch äquivalent ("macht das Gleiche") zum verwendeten "country in capitals". Warum ist das erwähnenswert? Raten Sie mal, was "capital in capitals.values( )" macht?

capitals = {"Deutschland" : "Berlin", "Frankreich" : "Paris", "Polen" : "Warschau"}
for capital in capitals.values():
    print("Wichtige Hauptstadt:", capital)
Genau!

Wichtige Hauptstadt: Berlin
Wichtige Hauptstadt: Paris
Wichtige Hauptstadt: Warschau
Hmm, wieder kein Wien dabei ... Schade eigentlich.

capitals["Österreich"] = "Wien"
Prüfung, ob alles geklappt hat:

print(len(capitals))
Ahh, jetzt sind es vier Einträge. Die len( )-Funktion (eingeführt bei den Listen) klappt also auch bei Dictionaries.

Letzter Abschnitt: Dictionaries mit Dictionaries als Werte

Bei den Listen haben wir kennengelernt, dass ein Listenelement eine komplette (zweite) Liste sein kann. Genau das geht bei Dictionaries auch. Der Wert zu einem Schlüssel eines Dictionary ist wiederum ein (neues, zweites) Dictionary. Im bisherigen Source Code der Übung 2 haben Sie bereits das "room"-Dictionary angelegt. Hier sehen Sie eine "aufgepimpte" Version davon.

Visuelle Darstellung des "room"-Dictionary

Wie im allerersten Beispiel in diesem Abschnitt ist das Wörterbuch insgesamt durch blaue, geschweifte Klammern markiert, jeder Schlüssel ist rot eingefärbt und jeder Wert in grüner Farbe. Das Trennzeichen zwischen Schlüssel und Wert ist der Doppelpunkt - hier in Orange eingefärbt.

Besonders interessant ist die Tatsache, dass die Werte im Beispiel wiedum vom Typ Dictionary sind. Was also aus Sicht des "room"-Dictionary ein Wert ist, kann wiederum separat betrachtet werden:

Visuelle Darstellung des Wertes vom "room"-Dictionary mit dem Schülle "Hall"

Der aus Sicht von "rooms" durch den Schlüssel "Hall" repräsentierte Wert ist ein vollständiges eigenes Dictionary. Dieses unterteilt sich wiederum in einzelne Schlüssel-Wert-Paare, z. B. gehört der Wert "Kitchen" zum Schlüssel "south" oder der Wert "key" ist über den Schlüssel "item" erreichbar.

Lassen wir uns im Beispiel man den Wert zum Schlüssel "Hall" ausgeben:

rooms = {
            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },        
            'Kitchen' : { 'north' : 'Hall',
                  'item'  : 'monster'
                },
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion'
                },             
            'Garden' : { 'north' : 'Dining Room' }
         }

print(rooms["Hall"])
btw: Ob man ein Dictionary in einer Zeile (aus Platzgründen) oder wie oben mit lauter "Enter" an den richtigen Stellen schreibt (aus Gründen der besseren Lesbarkeit) ist dem Interpreter egal.

Die Ausgabe:

{'south': 'Kitchen', 'east': 'Dining Room', 'item': 'key'}
Um nun an einen Wert innerhalb des "inneren" Wörterbuches zu gelangen, müssen ähnlich wie bei "Listen von Listen" zwei Schlüssel genutzt werden. Der 1. Schlüssel lädt den Wert (das "innere" Dictionary, letzte Ausgabe), während der 2. Schlüssel für das Laden des Wertes innerhalb des "inneren" Wörterbuches zuständig ist.

print(rooms["Hall"]["item"])
Die Ausgabe ist "key".

Hier noch ein Dreizeiler der die ineinander geschachtelten Wörterbücher durchläuft und alles ausgibt:

for room in rooms:
    for key in rooms[room]:
        print("Im Raum", room, "kommt man in Richtung", key, "in den Raum", rooms[room][key])
Die Ausgabe:

Im Raum Hall kommt man in Richtung south in den Raum Kitchen
Im Raum Hall kommt man in Richtung east in den Raum Dining Room
Im Raum Hall kommt man in Richtung item in den Raum key
Im Raum Kitchen kommt man in Richtung north in den Raum Hall
Im Raum Kitchen kommt man in Richtung item in den Raum monster
Im Raum Dining Room kommt man in Richtung west in den Raum Hall
Im Raum Dining Room kommt man in Richtung south in den Raum Garden
Im Raum Dining Room kommt man in Richtung item in den Raum potion
Im Raum Garden kommt man in Richtung north in den Raum Dining Room
Wie man erkennen kann, beinhalten die "inneren" Dictionaries auch die Dinge, die im jeweiligen Raum zu finden sind (Schlüssel "item"). Daher sollten wir Sätze wie z. B. "Im Raum Kitchen kommt man in Richtung item in den Raum monster" filtern. Machen Sie das mal bitte - ich bin hier fertig.
_________________________________________________________________________
9.
Ü3 - Bewegung!!
Ziele der Übung:

Herstellung einer kopfgesteuerten Schleife, die sicherstellt, dass das Spiel nur unter bestimmten Bedingungen abbricht.
Implementierung der Bewegung innerhalb der Welt
Sicherstellung der Aktualisierung der Anzeige, zur Orientierung des Spielers
Einführung einer (Endlos)-Schleife

Damit der Spielablauf solange wiederholt wird, bis das Ziel erreicht (oder der Nutzer aufgibt) implementieren wir zunächst eine Endlosschleife. Da die Anweisungen zur Spielbedienung nur einmal beim Spielstart angezeigt werden sollen, der aktuelle Status des Spieles (Raum, Inventar-Inhalt) jedoch bei jedem Spielzug zu aktualisieren sind, wird "showInstructions( )" außerhalb der Schleife, "showStatus( )" jedoch im Schleifenkörper angesiedelt. Ändern Sie Ihr Programm aus Ü2 im unteren Bereich ab, dass es wie folgt aussieht (achten Sie auf die korrekte Einrückung von "showStatus( )" wie im Abschnitt "Hintergrund - Funktionen beschrieben"):

...
showInstructions()
while True:
    showStatus()
...
Sie müssen das Programm aktuell noch nicht starten (es gibt nur unendlich oft den aktuellen Status aus). Sollten Sie jedoch bereits getan haben, können Sie die Ausführung unter Winders mithilfe der Tastenkombination "STRG" + "C" beenden.

Bewegung im Spiel I

Um die Möglichkeit der Beweung des Spielers in der Spielwelt zu gewährleisten, bitten wir ihn einfach, einmal pro Schleifendurchlauf seinen Zug (engl. "move") über die Tastatur einzugeben:

    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split()
    if move[0] == "exit":
        break
Da "pro Zug" bedeutet, dass es einmal pro Schleifeniteration ausgeführt wird, achten Sie auch hier wieder auf die korrekte Einrückung, damit die Befehle zum Schleifenkörper gehören. Testen Sie jetzt die Erweiterungen. Sie sollten bereits durch die Eingabe von "exit" die Schleife (und damit das Programm) beenden können.

Die erste Zeile deklariert und initialisiert die Variable "move" (mit dem Startwert '', also der leeren Zeichenkette). Diese Variable soll den Zug des Spielers pro Spielrunde speichern. Damit das Programm sicherstellt, dass der Benutzer nicht nur Enter drückt, wird in der zeiten Zeile geprüft, ob "move" "leer" und in Zeile 3 die Eingabe vom Nutzer erzwungen. Das wird so lange wiederholt, bis der Nutzer tatsächlich etwas eingibt, dass ungleich der leeren Zeichenkette ist. In Zeile 4 wird die Benutzereingabe mithilfe der lower( )-Funktion in Kleinbuchstaben umgewandelt und anschließend mithilfe der split-Funktion anhand von Leerzeichen aufgeteilt. Als Folge ändert sich der Datentyp von move von einer einfachen Zeichenkette zu einer Liste. Zeile 5 prüft, ob der Nutzer das Wort "exit" eingeben hat. Ist dies der Fall, wird durch Zeile 6 die Endlosschleife (und damit das Programm) beendet.

Bewegung im Spiel II

Soweit also zur Eingabe (dem Einlesen von der Tastatur) und der Prüfung auf "exit", also den Wunsch des Spieles, das Spiel zu beenden, ohne das Ziel erreicht zu haben. Kümmern wir uns jetzt um die eigentliche Fortbewegung. Ergänzen Sie den nachstehenden Pogrammcode nach der Zeile mit dem "break". Achten Sie auf Einrückungen!

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')
Dieser Fünfzeiler ist die eigentliche Navigation des Spiels.

Die Zeile 1 prüft, ob der Benutzer "go" (lt. Bedienunganleitung "showInstruction( )" der Befehl zum Bewegen zwischen Räumen) eingegeben wurde.
Die Zeile 2 prüft, ob zusätzlich zum "go" die Richtung, in die sich der Spieler bewegen möchte, im Raum, in dem er sich gerade befindet ("currentRoom") überhaupt existiert. Man könnte auch fragen, ob es überhaupt eine Tür gibt, die in eingegebene Richtung führt.
Die Zeile 3 folgt im Erfolgsfall der Prüfung aus Zeile 2 und aktualisiert den Raum, da der Nutzer diesen erfolgreich gewechselt hat.
Die Zeilen 4 und 5 geben eine passende Meldung aus, aus der hervorgeht, dass der Spieler in die gewünschte Richtung nicht laufen kann, weil es keine Tür in diese Richtung gibt.
Soweit zum fachlichen Teil, die technischen Besonderheiten werden wieder in den "Hintergrund"-Bereichen erläutert.
___________________________________________________________
10.
Ü3 - Bewegung!!
↪ Hintergrund - Schleifen
Ziele:

In diesem Abschnitt soll dargestellt werden, wie Schleifen (Wiederholungen) in Python umgesetzt werden.

Schleifen dienen generell der Wiederholung von bestimmten Programmabschnitten, solange eine zuvor definierte Bedingung erfüllt ist. Das was wiederholt werden soll, nennt man den Schleifenkörper.

Wir wollen in diesem Abschnitt die in allen gängigen Programmiersprachen vorhandenen Schleifen betrachten:

Anwendung von kopfgesteuerten Schleifen
Anwendung von Zählschleifen
Anwendung von fußgesteuerten Schleifen
Kopfgesteuerte Schleifen anwenden

Eine Schleife nennt man kopfgesteuert, wenn vor dem Betreten des Schleifenkörpers überprüft wird, ob eine Bedingung erfüllt ist.

Kopfgesteuerte Schleife als PAP

Im Beispiel Ü3 wurde eine Kopfgesteuerte verwendet:

while True:
    print("Endlosschleife ... Abbruch mit Strg+C")
Diese "while"-Schleife wiederholt den Inhalt des Schleifenkörpers so lange, wie die Bedingung hinter dem "while" wahr ist. Genau genommen steht dort "while True == True", also "entspricht der Wert von True  dem von True"? Ja, dass kann man schon mal sagen. "True" ist gleich "True". Meistens ist es sinnvoll, hier eine Variable vom Datentyp "Boolean" einzutragen. Im Beispiel wurde jedoch bereits der Boolesche Wert "True" eingetragen (keine Boolesche Variable, sondern der Boolesche Wert "True"). Da der Wert "True" die Eigenschaft hat, immer wahr zu sein, ist das Beispiel "while True" eine Endlosschleife, die niemals aufhört (außer man bricht das gesamte Programm manuell mittels "Strg + C" oder die Schleife mithilfe des Befehls "break" im Schleifenkörper ab.

Btw: Hat man im Schleifenkörper die Notwendigkeit, die Schleife sofort in die nächste Iteration (bzw. deren vorangestellte Prüfung) zu bringen, kann man mithilfe von "continue" genau das erreichen: Der Schleifenkörper wird dann nicht bis zum Ende durchlaufen, sondern für diesen Durchlauf sofort beendet.

Wann ist die Anwendung einer Endlosschleife sinnvoll? Z. B. beim Einsatz von Microcontrollern wie dem Arduino. Sobald so ein Gerät eine Betriebsspannung bekommt, wiederholt es endlos die einprogrammierten Anweisungen, bis die Spannung wieder gekappt wird.

Ein anderes Beispiel für eine kopfgesteuerte Schleife:

anzahl = 3
while True:
    print("anzahl:", anzahl)
    anzahl-=1
    if(anzahl <= 0):
        break
print("Schleife verlassen ...")
Die Ausgabe lautet:

anzahl: 3
anzahl: 2
anzahl: 1
Schleife verlassen ...
Hier wird eine Varable "anzahl" auf den Wert 3 gesetzt. Dann startet eine Endlosschleife. In jeder Iteration (Schleifenkörperdurchlauf) wird "anzahl" dekrementiert (verringert). Weiterhin finden in der Auswahl "if ..." eine Überprüfung statt, ob "anzahl" bereits den Wert 0 oder kleiner erreicht hat. Ist dies der Fall, wird mithilfe von "break" die Endlosschleife abgebrochen.

Lassen Sie uns mal mit booleschen Variablen arbeiten:

exit = False
while not exit:
    print("Schleifenkörper noch einmal durchlaufen ...")
    if(input("Schleife abbrechen (j/n):") == "j"):
        exit = True
print("Schleife verlassen")
Die Interaktion und Ausgabe:

Schleifenkörper noch einmal durchlaufen ...
Schleife abbrechen (j/n):n
Schleifenkörper noch einmal durchlaufen ...
Schleife abbrechen (j/n):j
Schleife verlassen
Das Programm arbeit wieder mit "while", jedoch lautet die Bedingung, damit der Schleifenkörper betreten wird, in diesem Fall "not exit". Da "exit" den Wert "False" hat (Zeile 1), entspricht "not exit" dem Ausdruck "not False". Und da "not False" dem Umkehrwert von False entspricht, und damit dem Wert "True", steht dort eigentlich "while True == True". Die Schleife wird betreten.

Die Zeile "if(..." darf man wie folgt lesen: Wenn das mittels "input" von der Tastatur eingelese dem Wert "j" (für "ja") entspricht, dann ist die Bedingung erfült und die Auswahl wird betreten. Dort wird der Wert von "exit" auf "True" gesetzt. Für Details kommt noch der Abschnitt mit den Hintergrundinfos zur Eingabe mit "input".

Kommen wir zur Prüfung des Schleifenkopfes nach dem Ändern von "exit" auf den Wert "True". Die Bedingung lautet zwar noch immer "not exit", allerdings ist der Wert jetzt "True". Aus "not True" folgt "False". Die Bedingung in Langform lautet also "while False == True". Da das nicht zutrifft, ist die Bedingung nicht erfüllt und der Schleifenkörper wird nicht noch einmal betreten.

Zählschleifen anwenden

Zählschleifen sind eine Sonderform der kopfgesteuerten Schleifen, denn auch bei ihnen wird überprüft, ob eine Bedingung noch erfüllt ist. Ist das nicht der Fall, wird der Schleifenkörper nicht betreten.

Zählschleifen im PAP

Was in der Darstellung wir eine reine Überprüfung einer booleschen Bedingung aussieht, ist in der Praxis in den meisten Programmiersprachen (und auch in Python) etwas umfangreicher und flexibler. Schauen wir uns ein Beispiel an:

for i in range(0,2):
    print("Schleifendurchlauf:", i)
Das sieht für C und Java-Enthusiasten und -innen zunächst ein bisschen ungewoht aus, aber es ist semantisch äquivalent (macht das gleiche) mit

for (int i = 0; i < 2; i++){ ...}
Zwar verhält sich die Python-Variante wie die C und Java-Programme - alle durchlaufen den Schleifenkörper 2 Mal, jedoch ist dies in Python nicht so explizit zu sehen - Die 2 als Obergrenze ist nicht mehr enthalten. "i" nimmt demnach die Werte 0 und 1 an. Das kann man in C und Java durch den Ausdruck "... i < 2; ..." deutlicher ablesen (finde ich zumindest).

Nätürlich kann man auch in Python die Schrittweite erhöhen. Dazu existiert eine überschriebene, dreistellige Funktion (dreistellige Funktion = Funktion mit drei Übergabeparametern):

for i in range(0, 8, 3):
    print("i hat jetzt den Wert:", i)
Ausgabe:

i hat jetzt den Wert: 0
i hat jetzt den Wert: 3
i hat jetzt den Wert: 6
Zuletzt noch ein generischer Gedanke: Die "for"-Schleife wurde auch schon einmal im Abschnitt mit den Hintergrundinfos zu Dictionaries verwenden. Vielleicht erinnern Sie sich.

capitals = {"Deutschland" : "Berlin", "Frankreich" : "Paris", "Polen" : "Warschau"}
for country in capitals:
    print(country)
Ebenso ist es möglich, mithilfe von "for" über eine Liste zu iterieren:

items = ["foo", "bar", "foobar", "foofoobar"]
for item in items:
    print(item)

Warum geht das alles? Genau genommen ist "for" keine Zählschleife, sondern eine Schleife, die über eine sogenannte Sequenz iteriert. Und was ist nun schon wieder eine Sequenz? Alles in Python, was eine Folge von Informationen darstellt. Und trifft ein paar Bekannte von uns zu:

Zahlenbereiche: "range(1,10)"
Listen "[1, 3, 22, 333]"
Schlüssel (keys) eines Dictionaries ["Deutschland", "Frankreich", "Polen"] (Achtung: Diese Darstellung ist nur die Liste der Schlüssel und kein Dictionary!)
Alle diese Beispiele sind Sequenzes. Deshalb ist "for" auf alle diese Datentypen anwendbar. Total praktisch, oder?

Fussgesteuerte Schleifen anwenden

Wenn der Schleifenkörper einmal ausgeführt wurde, und erst danach die Bedingung geprüft wird, spricht man von fussgesteuerten Schleifen.

Fussgesteuerte Schleife im PAP

Sie haben schon genug von Schleifen? Dann habe ich eine gute Nachricht für Sie. In Python gibt es keine explizite Syntax zur Darstellung von fussgesteuerten Schleifen!

Sie haben noch nicht genug von Schleifen? Dann habe ich eine gute Nachricht für Sie. Zwar gibt es in Python keine explizite Syntax zur Darstellung von fussgesteuerten Schleifen, aber das soll uns nicht weiter stören. Schauen Sie sich diesen "work-around" an:

exit = False
while not exit:
    print("Schleifenkörper noch einmal durchlaufen ...")
    if(input("Schleife abbrechen (j/n):") == "j"):
        exit = True
print("Schleife verlassen")
Kommt Ihnen bekannt vor? Dann haben Sie ein gutes Kurzzeitgedächtnis. Wenn man das Beispiel ganz nüchtern betrachtet, findet die Prüfung natürlich im Schleifenkopf statt ("while not exit"). Aber die fachliche Steuerung der im Kopf ausgewerteten Variable "exit" findet im "ja"-Zweig der Auswahl "if(..." statt. Und diese ist die letzte Anweisung im Schleifenkörper.

Also doch fussgesteuert? Technisch (programmatisch) nicht, fachlich vielleicht schon.
____________________________________________________
11.
Ü3 - Bewegung!!
↪ Hintergrund - Eingabe
Ziele der Übung

Benutzereingaben entgegen nehmen
Typumwandlungen von Benutzereingaben durchführen
Reagieren auf Laufzeitfehler mithilfe von "try-except-else"-Blöcken
Die Eingaben von Benutzern sind in fast allen Programmen essentiell, weil damit der Programmfluss, also was zu tun ist, gesteuert wird. In diesem Abschnitt wird erklärt, wie man Benutzereingaben im Programm anfordern kann, wie man die Eingaben in verschiedene Datentypen umwandelt, um damit arbeiten zu können und wie man Laufzeitfehler (die i. d. R. einen Programmabsturz nach sich ziehen) vermeiden kann.

Benutzereingaben entgegen nehmen

Das laufende Programm anzuhalten, um den Benutzer um eine Eingabe zu bitten, ist mithlife der Funktion "input( )" schnell umgesetzt:

benutzereingabe = input()
print("Deine Eingabe war", benutzereingabe)
Dabei wird, was auch immer der Benutzer eingegeben und mit einem Druck auf die "Enter"-Taste abgeschlossen hat, in der Variablen "benutzereingabe" gespeichert.

Um dem Benutzer einen Tipp zu geben, was er eigentlich eingeben soll, ist eine vorangestellte Ausgabe sicherlich hilfreich. Dabei kann man natürlich einen "print( )"-Aufruf vor dem Input machen:

print("Gib eine Zeichenkette ein:")
benutzereingabe = input()
print("Deine Eingabe war", benutzereingabe)
Die Ausgabe sieht wie folgt aus:

Gib eine Zeichenkette ein:
Test-Zeichenkette
Deine Eingabe war Test-Zeichenkette
Das ist schon mal viiieeel besser, weil der Benutzer jetzt immerhin weiss, was von ihm erwartet wird. Aber es geht noch besser:

benutzereingabe = input("Gib eine Zeichenkette ein: ")
print("Deine Eingabe war", benutzereingabe)
Jetzt wird jedem Benutzer sofort klar, dass die Ausgabe zur Eingabe gehört:

Gib eine Zeichenkette ein: Testzeichenkette
Deine Eingabe war Testzeichenkette
Fassen wir bis hierher zusammen: Die Funktion "input( )" dient der Eingabe von Informationen über die Tastatur. Dabei wird das Programm angehalten und erst nach Drücken der "Enter"-Taste fortgesetzt. Es ist möglich der Funktion einen Übergabeparameter in Form einer Zeichenkette mitzugeben, die dann auf die Eingabeaufforderungen (Kommandozeile) gedruckt wird. So kann das Verständnis des Benutzers erhöht werden.

Eingabe unterschiedlicher Datentypen

Lassen Sie uns jetzt ein bisschen rechnen. Der Benutzer soll eine ganze Zahl eingeben, wir berechnen das Quadrat davon und geben das Ergebnis aus:

benutzereingabe = input("Gib eine ganze Zahl ein: ")
print("Die Quadratzahl von", benutzereingabe, "ist", benutzereingabe*benutzereingabe)
Was würden Sie erwarten, wenn der Benutzer eine 4 eingibt? 16? Lassen Sie es uns prüfen:

Gib eine natürliche Zahl ein: 4
Traceback (most recent call last):
  File "C:\Users\...\051-input.py", line 4, in <module>
    print("Die Quadratzahl von", benutzereingabe, "ist", benutzereingabe*benutzereingabe)
TypeError: can't multiply sequence by non-int of type 'str'
Hier ist ein Problem dass Python nicht selbstständig löst: Eine Typumwandlung. Alle per "input( )" eingelesenen Eingaben sind vom Typ Zeichenketten ("str", für String). Und einen String kann man (nicht ohne weiteres) quadrieren. Wir müssen die Zeichenkette "4" also in eine Zahl 4 umwandeln:

benutzereingabe = int(input("Gib eine ganze Zahl ein: "))
Neu ist, dass um den Input-Aufruf noch ein "int( )"-Aufruf eingefügt wurde. Gestatten Sie mir, diese Zeile noch einmal genau auseinanderzunehmen, obwohl es sich hier um einen "ganz normalen Funktionsaufruf" handelt. Folgende Überlegungen sollten Ihnen so oder so ähnlich durch den Kopf gehen, wenn Sie diese Zeile betrachten. Dabei "denke ich zunächst von aussen nach innen":

Was auch immer die rechte Seite vom "=" ergibt, es wird der Variablen "benutzereingabe" als Wert zugewiesen.
Die Funktion "int( )" versucht, was auch immer ihr als Parameter übergeben wird, in einen Integer umzuwandeln. Und was soll eigentlich umgewandelt werden? Aha, der Parameter ist ein "input( )"-Funktionsaufruf.
Lies mithilfe von "input( )" einen Wert von der Tastatur ein.
Jetzt könnte man das ganze auch "innen nach aussen" denken:

Etwas wird von der Tastutur eingelesen. Da "input( )" immer alles als Zeichenkette zurückgibt, ist es vom Datentyp "str" (String).
Diese String-Eingabe wird mithife der "int( )"-Funktion in einen Integer-Wert übertragen.
Die Variable "benutztereingabe" wird also zum Datentyp "int" und erhält den eingelesenen und umgewandelten Wert zugewiesen.
Jetzt rechnet unser Programm auch richtig :-)

Gib eine ganze Zahl ein: 4
Die Quadratzahl von 4 ist 16
Aber was ist mit dem hier:

Gib eine ganze Zahl ein: sieben
Na klar. Fehlermeldung:

Traceback (most recent call last):
  File "C:\Users\...\051-input.py", line 6, in <module>
    benutzereingabe = int(input("Gib eine ganze Zahl ein: "))
ValueError: invalid literal for int() with base 10: 'sieben'
Die Meldung drückt im Wesentlichen aus, dass die Zeichenkette "sieben" nicht in eine Zahl (also einen Integer-Datentyp) umgewandelt werden kann. Das ist zwar schade, aber irgendwie auch nachvollziehbar. Was können wir tun, um übereifrige bzw. untalentierte Nutzer zu unterstützen, also unser Programm gegen Fehleingaben abzusichern? Eine Überlegung heisst "type( )":

print("Typ von 7 ist", type(7))
print("Typ von 7.7 ist", type(7.7))
print("Typ von sieben ist", type("sieben"))
Und hier die Ausgabe:

Typ von 7 ist <class 'int'>
Typ von 7.7 ist <class 'float'>
Typ von sieben ist <class 'str'>
Mal von dem "class" und den spitzen Klammern abgesehen (wobei Klassen, ... da war doch was ... OOP) kommt das heraus, was man erwarten würde: Eine 7 ist vom Typ Interger, eine 7.7 ist eine Fließkommazahl und "sieben" ist eine Zeichenkette.

Bleibt bloß noch ein Problem:

benutzereingabe = input("Gib eine ganze Zahl ein: ")
print(type(benutzereingabe))
Ausgabe:

Gib eine ganze Zahl ein: 7
<class 'str'>
"input( )" gibt immer eine Zeichenkette zurück ... blöd, aber ja, dass stand schon mal weiter oben. Wir müssen also das Umwandeln von "str" nach "int" probieren. Und nur wenn es klappt, arbeiten wir weiter. Andernfalls müssen wir den Benutzer ausschimpfen ...

while True:
    try:
        benutzereingabe = int(input("Gib eine ganze Zahl ein: "))
    except ValueError:
        print("Bitte nur ganze Zahlen eingeben!")
    else:
        break
print("Das Quadrat von", benutzereingabe, "ist", benutzereingabe*benutzereingabe)
Hier die Erklärung:

Zeile 1: eine Endlosschleife
Zeile 2: Der "try"-Block (Einrückung beachten). Alles was sich im try-Block befindet, wird normal ausgeführt (hier also nur die Eingabe und die Typumwandlung in Zeile 3).
Zeile 4 der "except"-Block: Dessen inhalt wird ausgeführt, falls im "try"-Block ein (bestimmter) Fehler auftritt. Im Beispiel wird der Inhalt des "except"-Blocks nur ausgeführt, wenn ein sogenannter "ValueError", also ein Wertefehler, auftritt. Eine nicht fehlerfrei durchführbare Typumwandlung ist ein "ValueError". In Zeile 5 wird dem Benutzer noch einmal die Anforderung "ganze Zahl eingeben" angezeigt. Denn offentlichtlich hat er das nicht getan, sonst gäbe es keinen "ValueError".
Zeile 6: Sollte kein "ValueError" auftreten, wird dieser "else" (ansonsten)-Block ausgeführt. Da das Betreteten des Blockes im Beispiel bedeutet, dass die Typumwandlung erfolgreich durchgeführt werden konnte, wird hier die Endlosschleife beendet.
letzte Zeile: Ist die Schleife beendet, ist der Wert von "benutzereingabe" vom Typ "int" und die Quadrierung der Zahl kann durchgeführt werden.
Hier ein paar Eingaben und das Verhalten des Programmes:

Gib eine ganze Zahl ein: sieben
Bitte nur ganze Zahlen eingeben!
Gib eine ganze Zahl ein: 7.7
Bitte nur ganze Zahlen eingeben!
Gib eine ganze Zahl ein: 7
Das Quadrat von 7 ist 49
Jetzt haben wir es! Wir können von der Benutzereingabe Informationen einlesen, diese in unterschiedliche Typen umwandeln und mithilfe von "try-except-else"-Konstrukten Programmfehler gezielt abfangen und behandeln.

Sie machen das super! Halten Sie durch!
_____________________________________________________________________
12.
Ü4 - Sammeln & Exit
Ziele

Die Ziele dieser Übung sind

die Spielwelt zu erweitern und mit Gegenständen (und Monstern) auszustatten,
die Gegenstände aus den Räumen in das Inventar des Spielers aufnehmen zu können und
- endlich!!! - der Spieler das Spiel gewinnen kann.
Let's expand!

Die Funktionalität zum Aufnehmen von Gegenständen, die sich in Räumen befinden, ist der des Bewegens durch die Spielwelt sehr ähnlich. Lassen Sie uns zunächst die Spielwelt inkl. dem Inventar ins Spiel programmieren, damit es mehr Räume und vor allem Dinge zum aufheben gibt.

Ersetzen Sie das "rooms"-Dictionary durch diesen Code:

rooms = {
            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },        
            'Kitchen' : { 'north' : 'Hall',
                  'item'  : 'monster'
                },
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion'
                },
            'Garden' : { 'north' : 'Dining Room' }
         }
Es sind jetzt mehr Räume (z. B. der Garten oder das Esszimmer) hinzugekommen. Und es wurden in den manchen Räumen Dinge platziert, die über den Schlüssel "item" adressierbar sind. So befindet sich z. B. im Raum "Hall" nun auch ein "key" genannter Gegenstand.

Let's grapsch!

Nun folgt die Funktionalität, Dinge aufzunehmen, also dem Inventar hinzuzufügen. Diese Codezeilen werden innerhalb der Schleife und unterhalb der bisherigen vorhandenen Codezeilen ergänzt (Einrückungen beachten!'):

    if move[0] == 'get' :
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')
Was tut dieser Block?

Zeile 1: Prüfung auf den nächsten Befehl, den der Benutzer eingeben kann, nämlich "get"
Zeile 2: Prüfung, ob der Gegenstand, den der Benutzer aufheben möchte, überhaupt im aktuellen Raum ist, falls ja
Hinzufügen des Gegenstandes zum Inventar (Zeile 3)
entsprechender Hinweis in der Benutzeroberfläche (Zeile 4) und
Entfernen des Gegenstandes aus dem Raum (Zeile 5)
falls die Prüfung in Zeile 2 nicht erfolgreich war ("else"-Zweig, Zeile 6) erscheint eine Meldung auf der Benutzeroberfläche (Zeile 7).
Let's finish!

Der Spieler soll das Spiel auf zwei Arten beenden können: triumphierend oder sterbend. Beginnen wir mit dem Unschönen.

Diese Codezeilen werden innerhalb der Schleife und unterhalb der bisherigen vorhandenen Codezeilen ergänzt (Einrückungen beachten!'):

  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
Wenn der Spieler einen Raum betritt in dem sich der "Gegenstand" ("item") "monster" befindet, stirbt er. Wenn diese Prüfung (Zeile 1) eintritt, also "True" ist, wird eine entsprechende Meldung ausgegeben (Zeile 2) und das Spiel beendet (Zeile 3). Schade! Naja, mehr Glück beim nächsten Mal.

Kommen wir zum triumphalen Fall (unterhalt der "Sterben"-Sektion einfügen und ja, immer noch innerhalb der Schleife und JAAA, achten Sie auf die Einrückung):

  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house... YOU WIN!')
    break
Wenn der Spieler (bisher noch) nicht vom Monster gefressen wurde, im Garten angekommen ist und im Inventar den Trank ("potion") und den Schlüssel ("key") hat, dann - und nur dann - gewinnt er das Spiel. Prüfung - Zeile 1, Siegesmeldung - Zeile 2, Verlassen der Schleife (und damit des Spiels) - Zeile 3.

Die letzte Aktion, die Sie durchführen müssen, damit das Spiel fertig ist hat nichts mit Programmieren zu tun. Viel mehr handelt es sich um das genaue Gegenteil von Programmcode schreiben - Sie müssen Programmcode löschen. Entfernen Sie diese Zeilen aus Ihrem Programm:

    if move[0] == "exit":
        break

Ihr RPG ist fertig! Ob Sie dem Monster beim Testen entkommen sind oder nicht, spielt keine Rolle. Wenn Sie sich aber bis hierher durchgearbeitet haben, haben Sie in jedem Fall gewonnen!

Herzlichen Glückwunsch!
__________________________________________________________________
13.
Ü5Z - world.grow()
Zusatzaufgabe

Erweitern Sie die Spielewelt um drei weitere Räume "library","office" und "laboratory" mit beliebegen Verknüpfungen zu anderen Räumen.
In der Bibliothek soll sich der Gegenstand "BookOfLife" befinden und im Labor der "Beam-O-Mat".
Die Siegesbedingung soll sich wie folgt ändern. Ein Spieler gewinnt das Spiel, wenn er entweder
im Garten ist und über den Schlüssel und den Trank verfügt (bisherige Siegesbedingung) oder
mit dem "Buch des Lebens" und dem "Beam-O-Mat" im Labor steht.
Erweitern Sie Ihr Programm um einen Algorithmus, der das Monster zum Programmstart einmal in einen zufälligen Raum setzt.