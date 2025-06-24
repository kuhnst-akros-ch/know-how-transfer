# Crash Course: 🐳 Docker & Docker Compose

Welcome to a fast-paced, hands-on intro to Docker.  
You won't become a DevOps guru in 40 minutes—but you'll walk away with working examples, a mental model, and the ability to experiment on your own.

---

## 0. 🛠️ Preparation

Before you begin, make sure your system is ready:

- ✅ [Follow the setup guide](00-preparation/README.md) to install Docker or Podman
- 🔑 [Create an account on Docker Hub](https://hub.docker.com) for pushing your images

## 1. 🧭 Introduction: Why Docker?

Docker helps solve the classic “it works on my machine” problem.  
It packages applications together with their dependencies into isolated units—**containers**—that run the same regardless of environment.

### Container vs. VM

- **VMs** emulate entire operating systems and need gigabytes of space and minutes to start.
- **Containers** share the host OS kernel and start in milliseconds.
- Containers are **lightweight, fast, and easy to manage**.

### Real-World Uses

- Local development (consistent dev environments)
- CI/CD pipelines (build → test → ship)
- Microservices (each service in its own container)
- Reproducible environments (research, data science, etc.)

---

## 2. 🐳 Docker Hub

- Create a free Docker Hub account on [hub.docker.com](https://hub.docker.com/)
- Create a repository
- Log in locally via CLI

---

## 3. 🧱 Core Concepts

Before diving into commands, make sure you understand these basic building blocks:

- **Image:** snapshot of filesystem and config
- **Container:** running instance of an image
- **Volume:** persistent storage
- **Port mapping:** expose services to the host
- **Environment variables:** runtime configuration

---

## 4. 🧪 Docker Standalone: Your First Steps

Each of the following is a standalone hands-on folder:

### ✅ [01 – Write Hello World Image](01_write-hello-word/README.md)

Build a simple image using Alpine that prints a message.  
Learn how to build, run, push, and pull your first image.

### ⚙️ [02 – Use ENV Vars and Volumes](02-use-env-vars-and-volumes/README.md)

Split example:
- Use `ENV` and `-e` or `.env` to inject config
- Use `tee` and volumes (host and managed) to write persistent output

### 🌐 [03 – Expose Port and Serve Page](03_use-ports/README.md)

Serve a minimal web page and access it in your browser  
Learn how to map container ports with `-p`

---

## 5. 🧬 Docker Compose

### 👥 [10 – Guestbook: In-Memory](10_guestbook/README.md)

Two services (Python backend + Nginx)  
In-memory guestbook with no database

### 💾 [11 – Guestbook: With Database](11_guestbook-database/README.md)

Adds PostgreSQL to store entries persistently  
Shows hardcoded credentials vs `.env` configuration

---

## 6. 🧠 Try It Yourself

- Change the app logic
- Add or adjust volume mounts
- Modify port mappings or env vars
- Swap to your own images

---

## 📝 Tips

- Use `docker ps -a` and `docker logs <id>` to debug
- Clean up with `docker system prune -a`
- When stuck: `docker exec -it <id> sh` is your friend

---

## ✅ Done?

If you understand images, containers, ports, volumes, env-vars—and can read or tweak a `docker-compose.yml`—you’re good.

_Next step: try using Docker in a real project, or write your own reusable image!_

---

🏠 Return to [Know-How Transfer Home](../../README.md)
