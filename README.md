# :rocket: talk-es-for-reco

Demo code for the following talk: "Shaping Elasticsearch for Recommendation System"

## :pencil: Authors

- [Jaroslav Bezdek](https://www.github.com/jardabezdek)

## :construction_worker_man: Setup

### :wrench: Local development

In order to create a working environment, the [docker](https://www.docker.com/)
is used. To start it, please, follow the next steps.

1. Launch the docker daemon.
1. Get to the repository root folder: `cd ~/projects/talk-es-for-reco/`
1. Run the docker containers: `docker compose up`
1. In another terminal instance, run `docker ps`, and check that both containers are running:
    1. `container-python`
    1. `container-elasticsearch`
1. In another terminal instance, get into the container with python environment:
`docker exec -it container-python /bin/bash`
1. Inside the container, run python scripts like this: `python <path/to/script.py>`

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
1. Run the script: `python /usr/src/app/scripts/search.py` The search results will be printed
to the console.

### :two: Recommendation

The [`recommendation.py` script](./scripts/recommendation.py) utilizes the Elasticsearch
to recommend posts to a user based on various factors. It applies a scoring mechanism to rank posts
and provide personalized recommendations to the user.

Usage:

1. Modify the `USER_ID` variable to specify the user for whom posts should be recommended.
1. Run the script: `python /usr/src/app/scripts/recommendation.py` The recommended posts will
be printed to the console, sorted from the most relevant to the least relevant one.

## :link: Links

- Conferences and meetups:
  - [Data & AI/ML Lightning Talks (Prague, Czechia)](https://www.meetup.com/strv-meetups/events/290896731/)
  - [Data & AI/ML Lightning Talks (Brno, Czechia)](https://www.meetup.com/strv-meetups/events/290896746/)
  - [Data Meetup #2: Machine learning applications in the product development (Bratislava, Slovakia)](https://www.linkedin.com/events/datameetup-2-machinelearningapp7022228737978998784/about/)
  - [PyCon MY 2023 (Kuala Lumpur, Malaysia)](https://pyconmy2023.peatix.com/)
  - [Moderni stack vol. 4 (Ostrava, Czechia)](https://agrp.dev/konference/moderni-stack-vol-4/)
