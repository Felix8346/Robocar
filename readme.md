# Line Following Robocar

## Hardware

Das Robocar basiert auf folgenden Komponenten:

- Raspberry Pi 3
- PCA9685 PWM-Modul
- 3 × Liniensensoren
- 4 × DC-Motoren

## Voraussetzungen

**Wichtig:** Die Software wurde für Linux entwickelt und muss auf einem Linux-System (z. B. Raspberry Pi OS) ausgeführt werden.

---

## I²C aktivieren

Für die Kommunikation mit dem PCA9685-Modul muss die I²C-Schnittstelle einmalig aktiviert werden.

### Raspberry Pi konfigurieren

```bash
sudo raspi-config
```

Anschließend:

```text
Interface Options → I2C → Yes
```

Den Raspberry Pi neu starten:

```bash
sudo reboot
```

### I²C-Tools installieren

```bash
sudo apt update
sudo apt install -y i2c-tools
```

### Funktion prüfen

```bash
sudo i2cdetect -y 1
```

Das angeschlossene PCA9685-Modul sollte nun in der Geräteliste erscheinen.

---

## Hardwaresteuerung mit Python

Für die Ansteuerung der GPIO-Pins wird die Bibliothek **lgpio** verwendet.

### Systemvoraussetzungen installieren

```bash
sudo apt install swig python3-dev python3-setuptools
```

### lgpio herunterladen und installieren

```bash
wget http://abyz.me.uk/lg/lg.zip
unzip lg.zip
cd lg
make
sudo make install
```

### Daemon starten

```bash
rgpiod &
```

---

## Virtuelle Python-Umgebung

Zur Verwaltung der Python-Abhängigkeiten wird eine virtuelle Umgebung verwendet.

### Umgebung erstellen

```bash
python3 -m venv .robocar
```

### Umgebung aktivieren

```bash
source .robocar/bin/activate
```

Eine erfolgreiche Aktivierung wird durch den Präfix `(.robocar)` in der Konsole angezeigt.

### Benötigte Bibliotheken installieren

```bash
pip3 install gpiozero lgpio
```

---

## Projektstruktur

Empfohlene Verzeichnisstruktur:

```text
robocar/
├── src/
│   └── main.py
├── .robocar/
└── README.md
```

---

## Entwicklung mit VS Code oder Zed

Für die Entwicklung empfiehlt sich eine SSH-Verbindung zum Raspberry Pi.

### Verbindung per SSH

1. Die Erweiterung **Remote - SSH** installieren.
2. Über **Connect to Host...** verbinden.
3. Mit folgendem Host verbinden:

```text
BENUTZERNAME@HOSTNAME.local
```

4. Das Projektverzeichnis öffnen:

```text
/home/pi/robocar
```

### Hinweis

Während der Entwicklung wurde festgestellt, dass Visual Studio Code auf dem Raspberry Pi teilweise einen hohen Arbeitsspeicherverbrauch verursacht. Daher wird alternativ der Editor **Zed** empfohlen, da dieser ressourcenschonender arbeitet.

---

## Arbeiten mit GitHub

### Repository klonen

Falls das Repository noch nicht auf dem Raspberry Pi vorhanden ist:

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

### Änderungen herunterladen

Vor jedem Programmstart sollte sichergestellt werden, dass die aktuelle Version verwendet wird:

```bash
git pull origin
```

### Eigene Änderungen hochladen

Dateien vormerken:

```bash
git add <DATEINAME>
```

Änderungen speichern:

```bash
git commit -m "Beschreibung der Änderung"
```

Änderungen hochladen:

```bash
git push origin
```

---

## Programm starten

Vor der Ausführung muss die virtuelle Umgebung aktiviert werden:

```bash
source .robocar/bin/activate
```

Anschließend das Hauptprogramm starten:

```bash
python3 src/main.py
```

Der Roboter kann nun die angeschlossene Hardware ansteuern und die Linienverfolgung ausführen.

---
