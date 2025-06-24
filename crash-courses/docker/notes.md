# 🐳 Docker Crash Course – Time Plan

**Typical session length**: ~60–75 minutes  
**Audience**: Junior developers and technically skilled team members

---

## 1. Introduction (5 min)

- Welcome and motivation
- Why Docker? What problems does it solve?
- Agenda preview: from images to compose

---

## 2. Check Existing Know-How (5–10 min)

- Ask: “Used Docker before? Seen a `Dockerfile`? Worked with containers?”
- Adjust depth/speed based on responses

---

## 3. Basics – One Image, One Container (15–20 min)

- Docker CLI basics: `docker build`, `docker run`, `docker ps`, `docker logs`, `docker stop/rm`
- Live demo: a simple `hello.py` script in a `Dockerfile`
- Explain `FROM`, `COPY`, `CMD`, `EXPOSE`
- Exercise: build and run the image

---

## 4. Docker Compose & ENV/Volumes (15–20 min)

- Why Compose? (multiple containers, shared config)
- Walk through a simple `docker-compose.yml`
- Show usage of:
    - ENV vars (`--env`, `.env`)
    - Mounts: host folder and named volume
- Demo: guestbook with frontend + backend

---

## 5. Hands-On (20–25 min)

- Exercise:
    - Modify ENV value (change greeting)
    - Mount a folder to log output
    - Run the app via Compose
- Encourage breaking things: wrong ports, missing ENV

---

**Total: ~65–75 minutes**

Optional stretch goals if time allows:

- Add a second app in Compose (e.g., DB container)
- Show `docker exec` and `docker cp`
- Show `docker volume ls` and `docker inspect`
