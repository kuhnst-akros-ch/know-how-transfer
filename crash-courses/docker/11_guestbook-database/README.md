# 📦 Guestbook app (with PostgreSQL)

- The **frontend (nginx)** serves a static HTML form on [http://localhost:8081](http://localhost:8081)
- The **backend (Python Flask)** handles form submissions and stores guest names in a PostgreSQL database
- **nginx routes**:
  - `GET /` → serves `index.html`
  - `POST /add` → forwarded tothe backend at `http://app:5000/add`
  - `GET /list` → forwarded tothe backend at `http://app:5000/list`
- The **PostgreSQL DB is stored in a Docker volume**, which survives container restarts

## ▶️ Usage

Run the app:

```bash
podman compose up -d
```

Then open http://localhost:8081 in your browser.

## ▶️ Usage with ENV variables

In the default `docker-compose.yml`, the DB user/password are hard coded.

To set env vars from outside, you can use a `.env` file.

Run:

```bash
podman compose down
podman compose --file docker-compose.env-variables.yml up -d --build
```

This will rebuild the image from `docker-compose.env-variables.yml` (which uses env variables) and start the containers with the external config.
