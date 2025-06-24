# 🛠️ Preparation

This section helps you get your system ready to follow along with the Docker crash course.

---

## 🚀 1. Install Docker or Podman

### 🏢 Windows (company device)

Many companies cannot use Docker Desktop due to license restrictions.

Instead, install [Podman Desktop](https://podman-desktop.io/docs/installation/windows-install) which is free and compatible.

> 📌 **Why Podman?**  
> Docker Desktop is not free for companies with >$10 million in annual revenue or >250 employees. Podman is a drop-in alternative that avoids these restrictions.

### 🪟 Windows (private PC)

Use [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/).

### 🐧 Linux / 🍏 macOS

Install Docker or Podman using your package manager or the [official documentation](https://podman.io/getting-started/installation).

> 📌 If you're using Docker, [set up an alias for compatibility with the course examples](#-3-linuxmacos-no-podman-use-docker-instead-via-alias).

---

## 🧑‍💻 2. Create a Docker Hub Account

To push your images to the cloud, you need a free account.

1. Go to [hub.docker.com](https://hub.docker.com/)
2. Sign up with email, username, and password
3. Confirm your email address

You're now ready to push images in later sections!

---

## 🔁 3. Linux/macOS: No Podman? Use Docker instead (via alias)

This course uses `podman` in all examples.  
If you're using Docker on Linux/macOS, create an alias so you can run the same `podman` commands.

### Example

```bash
(
  echo
  echo 'alias podman=docker'
) >> ~/.bashrc
source ~/.bashrc
```

> 💡 This lets you copy/paste the `podman` commands used in this course, even if your system only has Docker installed.

---