# 🌐 Expose a Port: Hello in the Browser

This example shows how to run a simple web server inside a container and access it via browser using port mapping.

---

## 🧱 Step 1: Create the project folder

Create a new folder `hello-web` and add this `Dockerfile`:

```dockerfile
FROM busybox
CMD echo "<h1>Hello from Docker</h1>" > /www/index.html && httpd -f -p 80 -h /www
```

This uses `busybox`’s built-in `httpd` server to serve a static HTML file.

---

## 🛠️ Step 2: Build the image

```bash
cd hello-web
docker build -t yourname/hello-web .
```

---

## ▶️ Step 3: Run the container and expose the port

```bash
docker run --rm -p 8080:80 yourname/hello-web
```

- `-p 8080:80` maps **port 80 inside the container** to **port 8080 on your host**.

Now open [http://localhost:8080](http://localhost:8080) in your browser.

You should see:

```
Hello from Docker
```

---

You’ve now exposed a container port to the outside world using Docker.
