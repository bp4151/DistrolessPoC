# Dockerfile1

Simple Python build

```
docker build --rm -f ./Dockerfile1 -t distroless_poc .
docker run --rm -it distroless_poc
docker run --rm -it --entrypoint=sh distroless_poc
```

1) Leaves Secrets/__init__.py content exposed to cat from container bash command
2) All file system executables are available


