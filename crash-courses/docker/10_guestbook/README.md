# 📦 Guestbook App (in-memory)

This example introduces **Docker Compose** — a tool for defining and running multi-container Docker applications.

Instead of running `docker` commands manually for each container, we now define all services (frontend, backend) in one file and start them together with a single command.

---

## 🛠️ Setup Instructions

1. Create a new folder for this project (if you haven’t already):

   ```bash
   mkdir guestbook
   cd guestbook
   ```

2. Inside this folder, create a file named `docker-compose.yml`  
   (copy the `docker-compose.yml` file provided in this folder)

3. Then you can start the app with Docker Compose:

   ```bash
   docker compose up -d
   ```
   (`-d`/`--detach` runs it in the background)

---

## 📋 How It Works

- The **frontend (nginx)** serves a static HTML form at [http://localhost:8080](http://localhost:8080)
- The **backend (Python Flask)** handles form submissions and stores guest names in memory
- **nginx routes**:
  - `GET /` → serves `index.html`
  - `POST /add` → forwarded to the backend at `http://app:5000/add`
  - `GET /list` → forwarded to the backend at `http://app:5000/list`
- The **frontend talks to the backend** via Docker's internal network using the service name `app` (no exposed backend port needed)

---

## ▶️ Access the App

Open your browser at:

👉 [http://localhost:8080](http://localhost:8080)

To view submitted entries in the backend logs:

```bash
docker compose logs -f
```
