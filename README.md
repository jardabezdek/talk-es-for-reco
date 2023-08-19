# :rocket: talk-pycon-my-2023

Demo code for the following talk: "Shaping Elasticsearch for Recommendation System"

## :pencil: Authors

- [Jaroslav Bezdek](https://www.github.com/jardabezdek)

## :construction_worker_man: Setup

### :wrench: Local development

In order to create a working environment, the [docker](https://www.docker.com/)
is used. To start it, please, follow the next steps.

1. Launch the docker daemon.
1. Get to the repository root folder: `cd ~/projects/talk-pycon-my-2023/`
1. Run the docker containers: `docker compose up`
1. In another terminal instance, check that both containers - `talk-pycon-my-2023-python-1`,
and `talk-pycon-my-2023-elasticsearch-1` - are running: `docker ps`
1. In another terminal instance, get into the container with python environment:
`docker exec -it talk-pycon-my-2023-python-1 /bin/bash`
1. Inside the container, run python scripts: `python <path/to/script.py>`

## :floppy_disk: Data

- Datasets for the demo purposes are stored in the [`./data` folder](./data/).

## :link: Links

- [PyCon MY 2023](https://2023.pycon.my/home)
