#!/bin/bash

docker run -it --rm -p 10000:8888 -v /Users/kni/Downloads:/home/jovyan/downloads -v /Users/kni/Machines:/home/jovyan/machines -v /Users/kni/Machines/NEU2023/local-machine:/home/jovyan/work jupyter/tensorflow-notebook