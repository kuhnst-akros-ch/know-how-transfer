# ⚙️ Use ENV Vars and Volumes

This example builds on the basic `hello-world` image and splits into two independent topics.

---

## 🧪 Part 1: Use ENV Vars

Let’s make our container greet a name based on a configurable environment variable.

### Dockerfile

Create a folder `hello-env` and add this `Dockerfile`:

```dockerfile
FROM alpine
ENV NAME=World
CMD echo "Hello, $NAME"
```

---

### Option A: Pass env var in `podman run`

```bash
cd hello-env
podman build -t yourname/hello-env .
podman run -e NAME=Docker yourname/hello-env
```

Expected output:

```
Hello, Docker
```

---

### Option B: Use `.env` file

Create a file named `.env` in the same folder:

```
NAME=FromFile
```

Run the container using `--env-file`:

```bash
podman run --env-file .env yourname/hello-env
```

Expected output:

```
Hello, FromFile
```

---

## 📦 Part 2: Use Volumes to Save Output

Now let’s use `tee` to also write the output to a file.

### Dockerfile

Create a folder `hello-volume` and add this `Dockerfile`:

```dockerfile
FROM alpine
ENV NAME=World
CMD echo "Hello, $NAME" | tee -a /output/greeting.txt
```

---

### Option A: Mount a host folder

```bash
mkdir ./output
podman build -t yourname/hello-volume .
MSYS_NO_PATHCONV=1 podman run -e NAME=Host -v "./output:/output" yourname/hello-volume
```

Check `./output/greeting.txt` on your host.

> 📌 MSYS_NO_PATHCONV=1 disables Git Bash’s automatic path conversion (e.g., /c/ → C:\).

---

### Option B: Use a Docker-managed volume

```bash
podman volume create hello-vol
podman run -e NAME=Volume -v hello-vol:/output yourname/hello-volume
```

You **cannot** directly access Docker volumes from the host file system.
To inspect contents, run a debug container:

```bash
podman run -it -v hello-vol:/output alpine sh
# inside container
ls /output
cat /output/greeting.txt
```

Delete the volume when finished:

```bash
podman volume rm hello-vol
```

---

You’ve now seen how to:
- configure containers via env vars (inline and via file)
- persist output using volumes (host and Docker-managed)
