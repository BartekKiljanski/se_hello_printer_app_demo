# Notatki laboratoryjne

To sa moje krotkie notatki z wykonania cwiczenia. Nie sa potrzebne do uruchomienia aplikacji, ale zostawiam je w repozytorium, zeby bylo widac przebieg pracy.

## Wykonane kroki

1. Sklonowanie aplikacji `se_hello_printer_app_demo`.
2. Uruchomienie aplikacji lokalnie na porcie `5000`.
3. Sprawdzenie endpointow:
   - `/`
   - `/outputs`
4. Zmiana imienia w aplikacji z `Beata` na `Bartlomiej`.
5. Poprawienie testu po zmianie imienia.
6. Dodanie biblioteki `prometheus-client`.
7. Dodanie endpointu `/metrics`.
8. Dodanie metryk:
   - `printer_app_http_requests_total`
   - `printer_app_http_request_duration_seconds`
9. Dodanie testu dla endpointu `/metrics`.
10. Przygotowanie konfiguracji Prometheusa.
11. Uruchomienie Prometheusa i Grafany przez Docker Compose.
12. Sprawdzenie w Prometheusie, czy target aplikacji ma status `UP`.
13. Dodanie Prometheusa jako datasource w Grafanie.
14. Utworzenie dashboardu dla aplikacji.

## Przydatne komendy

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt -r test_requirements.txt
python -m pytest -q
python main.py
```

```powershell
docker compose -f monitoring/docker-compose.yml up -d
docker ps
```

## Sprawdzone adresy

```text
http://127.0.0.1:5000
http://127.0.0.1:5000/outputs
http://127.0.0.1:5000/metrics
http://localhost:9090
http://localhost:3000
```

## Problem / obserwacja

Aplikacja Flask byla uruchomiona lokalnie na Windowsie, a Prometheus dzialal w kontenerze Docker. Z tego powodu w `prometheus.yml` nie mozna bylo uzyc `localhost:5000`, bo dla kontenera oznaczaloby to jego wlasne srodowisko. Uzyty zostal adres `host.docker.internal:5000`.
