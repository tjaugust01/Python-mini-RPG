# Python Mini-RPG (Pygame Edition)

Ein kleines 2D-Tile-basiertes RPG / Dungeon-Crawler-Spiel in Python.

---

## Hintergrund & Entstehung

Dieses Projekt ist im Rahmen einer Abgabe in der Berufsschule entstanden. Die ursprüngliche Aufgabenstellung diente zum Einstieg in Python und sah die Entwicklung eines rein textbasierten Konsolenspiels (CLI) vor.

Als Teil der Prüfungsaufgabe sollte jeder Schüler das Spiel um eine eigene Neuerung oder Besonderheit erweitern.

**Meine Erweiterung:**
Ich habe mich dazu entschieden, das Spiel aus dem reinen Terminal herauszuholen und eine **grafische 2D-Oberfläche mit [Pygame](https://www.pygame.org/)** zu implementieren. Die Spielwelt, Räume, Spielerfigur und Gegenstände werden visuell dargestellt und über die Tastatur gesteuert. Die originale CLI-Version ist als Vergleich weiterhin enthalten.

---

## 🎮 Spielprinzip & Ziele

Der Spieler erkundet ein zufallsgeneriertes Raster (Grid) aus verschiedenen Räumen (*Hallway*, *Kitchen*, *Garden*, *Library*, *Office*, *Laboratory*). Auf dem Weg müssen Gegenstände aufgesammelt und Gefahren ausgewichen werden.

### Siegbedingungen (Win Conditions)
Das Spiel kann auf zwei Wegen gewonnen werden:
1. **Garten-Flucht:** Erreiche den Raum **Garden** mit einem **Key** (Schlüssel) und einer **Potion** (Trank) im Inventar.
2. **Labor-Erfolg:** Erreiche das **Laboratory** mit dem **BookOfLife** und dem **Beam-O-Mat** im Inventar.

### Niederlage
- Trittst du in einen Raum mit einem **Monster**, hast du sofort verloren!

---

## 🕹️ Steuerung

### Grafische Pygame-Version (`main2.py`)
| Taste | Aktion |
|---|---|
| `W` | Nach oben bewegen (Nord) |
| `A` | Nach links bewegen (West) |
| `S` | Nach unten bewegen (Süd) |
| `D` | Nach rechts bewegen (Ost) |
| `E` | Item im aktuellen Raum aufheben |

### Klassische CLI-Version (`main.py`)
| Befehl | Beispiel | Beschreibung |
|---|---|---|
| `go <richtung>` | `go north` / `go up` / `go w` | In die angegebene Richtung gehen |
| `get <item>` | `get key` / `get potion` | Gegenstand aufnehmen |

---

## 🚀 Installation & Start

### Voraussetzungen
- Python 3.10+
- [Pygame](https://www.pygame.org/)

### 1. Abhängigkeiten installieren
```bash
pip install pygame
```

### 2. Spiel ausführen

**Pygame-Version starten (empfohlen):**
```bash
python main2.py
```

**Klassische CLI-Version starten:**
```bash
python main.py
```

---

## 📁 Projektstruktur

```
Python-mini-RPG/
├── game.py          # Pygame-Hauptklasse, Rendering & Event-Schleife
├── main2.py         # Startpunkt für die grafische Pygame-Version
├── main.py          # Startpunkt für die klassische CLI-Version
├── type.py          # Datenklassen und Enums (Player, Room, Item, NPC, RoomType)
├── util.py          # Spiellogik (Räume generieren, Siegbedingungen, etc.)
├── sprites/         # Grafiken und Sprites (Räume, Spielfigur, Endscreens)
└── Requirements.md  # Ursprüngliche Aufgabenstellung aus der Berufsschule
```
