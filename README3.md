# Dockerfile3

Python build with pyinstaller and Google Distroless Python 

```
docker build --rm -f ./Dockerfile3 -t distroless_poc . 
docker run --rm -it distroless_poc
docker run --rm -it --entrypoint=sh distroless_poc
```

1) Container bash is accessible, but OS commands like ls, cat, cd are not
2) We can't expose the Secrets\__init__.py content because the only thing moved into the app image is the main executable built by pyinstaller
3) We can't decompile the main executable because apt and pip are not installed.

```
import os
os.listdir()
os.listdir('Secrets')
open('Secrets\__init__.py','r').read()
```




