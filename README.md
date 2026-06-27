# se_hello_printer_app_demo

Autor zmian: Bartlomiej Kiljanski

Projekt przygotowany do cwiczenia z monitorowania aplikacji z GitHuba za pomoca Prometheusa i Grafany.

Oryginalna aplikacja Flask zostala rozszerzona o endpoint `/metrics`, ktory wystawia metryki w formacie Prometheusa. Dodatkowo w katalogu `monitoring/` znajduje sie konfiguracja Prometheusa i Grafany uruchamiana przez Docker Compose.

## Co zostalo dodane

- zmiana imienia w aplikacji na `Bartlomiej`,
- endpoint `/metrics`,
- metryka `printer_app_http_requests_total`,
- metryka `printer_app_http_request_duration_seconds`,
- test sprawdzajacy endpoint metryk,
- konfiguracja Prometheusa,
- konfiguracja Docker Compose dla Prometheus + Grafana.

## Uruchomienie aplikacji

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt -r test_requirements.txt
python main.py
```

Aplikacja dziala lokalnie pod adresem:

```text
http://127.0.0.1:5000
```

Metryki sa dostepne pod adresem:

```text
http://127.0.0.1:5000/metrics
```

## Testy

```powershell
python -m pytest -q
```

## Prometheus i Grafana

W drugim terminalu:

```powershell
docker compose -f monitoring/docker-compose.yml up -d
```

Adresy:

- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

Prometheus scrapuje aplikacje przez:

```text
host.docker.internal:5000
```

Przykladowe zapytania PromQL:

```promql
up{job="github-app-monitoring"}
printer_app_http_requests_total
sum by (endpoint) (printer_app_http_requests_total)
rate(printer_app_http_request_duration_seconds_count[1m])
```

## Dokumentacja

Sprawozdanie z wykonania zadania jest przygotowywane osobno w pliku Word/PDF ze zrzutami ekranu.
