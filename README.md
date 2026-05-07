# Klassenchat MVP

Ein minimaler webbasierter Klassenchat als Flask-Prototyp.

## Architektur

- Browser UI
- Flask App
- In-Memory Message Store
- Ein Endpoint: `GET /` und `POST /`

## Lokal starten

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Dann im Browser öffnen: http://127.0.0.1:5000

## Deployment auf Render

- GitHub Repository mit diesen Dateien erstellen
- Render Web Service verbinden
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

## Limitation

Nachrichten werden nur im Arbeitsspeicher gespeichert und gehen bei Restart/Redeploy verloren.
