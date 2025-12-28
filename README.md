# 🌦️ WeatherMonitorService  
Ein persönliches Lernprojekt – Clean Architecture, Services, Protokolle und Docker

Dieses Projekt ist **kein fertiges Produkt**, sondern ein **Lernprojekt**, das ich nutze, um
Software-Architektur, Python-Best Practices und professionelle Projektstrukturen zu üben.
Ich bin Anfänger und arbeite mich Stück für Stück in Themen wie:

- Clean Architecture
- Dependency Injection
- Protokolle (Interfaces)
- Testbarkeit
- Service Layer
- Orchestrator Pattern
- Pydantic Settings
- Externe APIs
- Logging
- Docker

Das Projekt ist bewusst **strukturierter als nötig**, um zu lernen, wie man saubere und
wartbare Software aufbaut. Es ist nicht perfekt – aber genau das ist der Sinn.

---

## 📘 Ziel des Projekts

Der WeatherMonitorService:

1. lädt Wetterdaten von der Open-Meteo API  
2. baut eine kurze Wetter-Zusammenfassung  
3. sendet diese über Telegram  
4. nutzt dafür getrennte Schichten und klare Verantwortlichkeiten

Dieses Projekt war für mich eine Übung darin, wie professionelle Python-Systeme aufgebaut werden,
nicht nur wie man "einen API-Request macht".

---

## 📂 Projektstruktur

Ich habe versucht, das Projekt so aufzubauen, wie man es in der Software-Entwicklung häufiger sieht:

core/
config/ # Pydantic Settings
domains/ # Reine Datenklassen
protocols/ # Abstrakte Interfaces (Messenger, API)
logging_setup.py # Logging-Konfiguration

infrastructure/
weather_api_client.py # Holt Wetter vom API
messengers/
telegram_messenger.py # Telegram-Integration
console_messenger.py # Konsolen-Ausgabe

service/
weather_service.py # Logik: freezing, umbrella, summary
weather_notification_service.py # Baut und sendet Notifications
weather_monitor_service.py # Orchestrator/Coordinator des gesamten Ablaufs

main.py # Einstiegspunkt der App
Dockerfile # Für Container-Builds
requirements.txt

yaml
Code kopieren

Ich weiß, dass das für ein kleines Projekt „zu viel Struktur“ ist – genau das war aber Absicht.
Ich wollte lernen, wie eine modulare Architektur funktioniert.

---

## 🚀 Wie starten?

### 1. Repository klonen

git clone <URL>
cd WeatherMonitorService

shell
Code kopieren

### 2. Abhängigkeiten installieren

pip install -r requirements.txt

shell
Code kopieren

### 3. `.env` Datei erstellen

LOCATION_NAME=xxx
LATITUDE=xxx
LONGITUDE=xxx

TELEGRAM_CHAT_ID=<deine_chat_id>
TELEGRAM_API_TOKEN=<dein_token>

shell
Code kopieren

### 4. Starten

python main.py

yaml
Code kopieren

---

## 🐳 Docker

### Build

docker build -t weather-monitor .

shell
Code kopieren

### Run

docker run --env-file .env weather-monitor

yaml
Code kopieren

---

## 🧪 Tests

Ich habe Mock-Tests für die wichtigsten Services eingebaut, um zu lernen:

- wie man Protokolle testet  
- wie man Abhängigkeiten isoliert  
- wie Testbarkeit durch Architektur entsteht  

Beispiel:

tests/test_notification_service.py

yaml
Code kopieren

Die Tests sind einfach gehalten, weil ich noch am Anfang bin.

---

## 🚧 Was (bewusst) noch nicht perfekt ist

Da das Projekt ein Lernprojekt ist, fehlen bewusst einige Dinge:

- erweitertes Logging (File Handler, Rotation)
- vollständiges Error-Handling für API-Sonderfälle
- CLI-Argumente
- Scheduler (Cron / APScheduler)
- Caching
- Docker Compose Deployment
- Performance-Optimierungen

Ich habe mich auf Architektur, Struktur und Verständnis konzentriert.

---

## 🎯 Warum dieses Projekt existiert

Ich lerne aktuell:

- Python auf einem professionellen Niveau  
- Wie man Software strukturiert  
- Wie man wartbare Systeme schreibt  
- Wie man testet  
- Wie man Daten, Logik und Infrastruktur trennt  
- Wie man Services und Protokolle verwendet  

Dieses Projekt zeigt meinen Lernweg und meinen Fortschritt –  
nicht Perfektion.

---

## 💬 Feedback willkommen!

Da ich Anfänger bin und dieses Projekt zum Lernen nutze,
freue ich mich über jeden Hinweis:

- Verbesserungsvorschläge  
- Hinweise auf bessere Patterns  
- Kritik an Architektur oder Struktur  
- Tipps zu Tests, Logging, Docker  

---

## 🙌 Danke fürs Anschauen

Ich arbeite immer weiter an meinen Skills und Projekten.
Dieses Repository dokumentiert meinen Weg vom Anfänger
zu jemandem, der wirklich robuste Automationssysteme bauen kann.

*Zusammenfassung mit ChatGPT
