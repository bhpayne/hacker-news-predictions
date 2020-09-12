help:
	@echo "make docker"

.PHONY: docker docker_build docker_run
docker: docker_build docker_run
docker_build:
	docker build -t hnews_rec .
docker_run:
	docker run -it --rm -v `pwd`:/scratch hnews_rec /bin/bash

