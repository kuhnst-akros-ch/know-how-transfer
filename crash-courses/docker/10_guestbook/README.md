# 📦 Guestbook App (in-memory)

- The **frontend (nginx)** serves a static HTML form at http://localhost:8080
- The **backend (Python Flask)** handles form submissions and stores guest names in memory
- **nginx routes**:
  - `GET /` → serves `index.html`
  - `POST /add` → forwarded to the backend at `http://app:5000/add`
  - `GET /list` → forwarded to the backend at `http://app:5000/list`
- The **frontend talks to the backend** via Docker's internal network using the service name `app` (no exposed port required)

## ▶️ Usage

Run the app:

```bash
docker compose up -d
```
(`-d`/`--detach` to run in background)

Then open your browser at:

👉 http://localhost:8080

To view submitted entries in the backend logs:

```bash
docker compose logs -f
```
