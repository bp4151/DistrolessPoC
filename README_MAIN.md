# Python, Distroless Docker Container PoC

## Why

Distribution to multiple platforms is easier using a Docker container

--- but --- 

We need to protect the code and secrets inside the container

This can apply to python and dotnet core, as both Python and dotnetcore have the same issue.  

| Python     | DotNet Core      |  
|------------|------------------|  
| *.py files | *.cs files       |  
| .env file  | appsettings.json |  

Distroless images exist for both.  

Even though we are told to use environmental variables for secrets in Docker containers, users
can expose them from the interactive bash command line.

## How

### Step 1:
- We containerize our typical python app

### Step 2:  
- We containerize our typical python app as our build image  
- Using a multistage build, we add the artifacts from the build image to the distroless app image

### Step 3:
- We containerize our typical python app as our build image  
- We use pyinstaller to create a single file executable  
- Using a multistage build, we add the artifacts from the build image to the distroless app image

## Resources
[Google Distroless](https://github.com/GoogleContainerTools/distroless)  
[Dockerizing with Distroless](https://medium.com/@luke_perry_dev/dockerizing-with-distroless-f3b84ae10f3a)