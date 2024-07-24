# YesWorkflow

## Usage
Tested on macos (arm)

1. Build the docker image
```
docker build -t yesworkflow .
```

2. Use the provided render.sh script to render a python script (with annotations) to a grpahviz .dot file and .png
```
./render.sh ./scripts/example.py
```
