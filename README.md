Mapa trzęsień ziemi
Jest to projekt, który pobiera dane o trzęsieniach ziemi z publicznego API USGS (amerykańska służba geologiczna), zapisuje je w bazie danych PostgreSQL działającej w kontenerze Docker i wyświetla na interaktywnej mapie świata.
Każde trzęsienie to kółko na mapie — im większe i bardziej czerwone, tym silniejszy wstrząs. Po kliknięciu pokazują się szczegóły: miejsce, magnituda, głębokość i czas.

Baza danych: PostgreSQL 16 (w kontenerze Docker)
Backend: Python + Flask
Frontend: HTML + Leaflet (mapa) + OpenStreetMap (kafelki)
Źródło danych: publiczne API USGS (bez klucza)

Wymagania

Docker Desktop
Python 3

Uruchomienie

Sklonuj repozytorium i wejdź do folderu:

bash   git clone https://github.com/twoja-nazwa/earthquake-db.git
   cd earthquake-db

Uruchom bazę danych w kontenerze (Docker Desktop musi być włączony):

bash   docker compose up -d

Zainstaluj zależności Pythona:

bash   py -m pip install -r requirements.txt
(na macOS/Linux użyj python3 zamiast py)

Pobierz dane z API do bazy:

bash   py fetch.py

Uruchom serwer:

bash   py app.py

Otwórz w przeglądarce: http://localhost:5000

Aby dociągnąć świeże dane, uruchom py fetch.py ponownie (w osobnym oknie terminala) i odśwież stronę.
Struktura projektu
earthquake-db/
├── docker-compose.yml   # konfiguracja kontenera z bazą PostgreSQL
├── init.sql             # schemat tabeli (tworzony przy starcie bazy)
├── fetch.py             # pobiera dane z API USGS i zapisuje do bazy
├── app.py               # backend Flask — podaje dane i serwuje stronę
├── index.html           # mapa z trzęsieniami (Leaflet)
├── requirements.txt     # zależności Pythona
└── .gitignore
Źródło danych
Dane pochodzą z publicznego feedu USGS Earthquake Hazards Program — trzęsienia o magnitudzie 2.5+ z ostatnich 24 godzin. API jest darmowe i nie wymaga klucza.
Pomysły na rozwój

Suwak do filtrowania trzęsień po magnitudzie
Przycisk „odśwież dane" bezpośrednio na stronie
Automatyczne pobieranie danych co kilka minut (np. cron albo drugi kontener)
Statystyki: najsilniejsze trzęsienie, średnia głębokość
