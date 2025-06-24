# 🔨 Write Your Own Docker Image

This example shows how to build and run your very first Docker image.

---

## 🧱 Step 1: Create the project folder

Create a new folder `hello-world` and add a file called `Dockerfile` with this content:

```dockerfile
FROM alpine
CMD ["echo", "Hello from my image"]
```

This image uses Alpine Linux and simply prints a message when started.

---

## 🛠️ Step 2: Build the image

```bash
cd hello-world
docker build -t yourname/hello-world .
```

✅ Don’t forget the `.` at the end — it tells Docker to use the current folder.

---

## ▶️ Step 3: Run the container

```bash
docker run yourname/hello-world
```

Expected output:

```
Hello from my image
```

---

## 🚀 Step 4: Push to Docker Hub

Login first if needed:

```bash
docker login
```

Then push your image:

```bash
docker push yourname/hello-world
```

---

## 🌍 Step 5: Pull and run

Try it on another machine, or simulate a fresh pull:

```bash
# Remove the image locally
docker image rm yourname/hello-world
docker run yourname/hello-world
```

---

You've now built, published, and reused your own Docker image.
