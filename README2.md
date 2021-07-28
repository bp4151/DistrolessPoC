# Dockerfile2

Python build with Google Distroless Python

```
docker build --rm -f ./Dockerfile2 -t distroless_poc .
docker run --rm -it distroless_poc
docker run --rm -it --entrypoint=sh distroless_poc
```

1) Container bash is accessible, but OS commands like ls, cat, cd are not
2) We can still expose the Secrets\__init__.py content by using the Python REPL from the container bash

```
import os
os.listdir()
os.listdir('Secrets')
open('Secrets/__init__.py','r').read()
```




