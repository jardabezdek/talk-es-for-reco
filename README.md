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
1. In another terminal instance, run `docker ps`, and check that both containers are running:
    1. `talk-pycon-my-2023-python-1`,
    1. `talk-pycon-my-2023-elasticsearch-1`
1. In another terminal instance, get into the container with python environment:
`docker exec -it talk-pycon-my-2023-python-1 /bin/bash`
1. Inside the container, run python scripts: `python <path/to/script.py>`

### :floppy_disk: Elasticsearch

In order to set up Elasticsearch indices and upload data into the corresponding indices,
run the following command in the container with python environment:
`python /usr/src/app/scripts/setup.py`

## :tada: Features

In the repository, two features are introduced: search and recommendation.

### :one: Search

The [`search.py` script](./scripts/search.py) utilizes the Elasticsearch library to search
the 'users' index based on the provided search input.

Usage:

1. Modify the `SEARCH_INPUT` variable to specify the search term.
2. Run the script: `python /usr/src/app/scripts/search.py` The search results will be printed
to the console.

### :two: Recommendation

The [`recommendation.py` script](./scripts/recommendation.py) utilizes the Elasticsearch
to recommend posts to a user based on various factors. It applies a scoring mechanism to rank posts
and provide personalized recommendations to the user.

Usage:

1. Modify the `USER_ID` variable to specify the user for whom posts should be recommended.
3. Run the script: `python /usr/src/app/scripts/recommendation.py` The recommended posts will
be printed to the console.

## :link: Links

- [PyCon MY 2023](https://2023.pycon.my/home)
