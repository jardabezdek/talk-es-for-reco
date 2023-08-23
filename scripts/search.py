"""Script for searching the users index in the ElasticSearch."""

from elasticsearch import Elasticsearch

from scripts.config import ES_HOST

SEARCH_INPUT = "german"


def search_users_index(search_input: str) -> None:
    """Search `users` index for the `search_input`."""
    es = Elasticsearch(ES_HOST)

    search_result = es.search(
        index="users",
        query={
            "multi_match": {
                # string that will be searched for
                "query": f"{search_input}",
                # fields that will be searched in
                "fields": ["name", "city", "country"],
                # enable fuzzy search to be able to find results even when misspelling the query
                "fuzziness": "AUTO",
            }
        },
        source={"includes": ["name", "city", "country"]},
    )

    # print the retrieved documents
    for hit in search_result["hits"]["hits"]:
        print("Document ID:", hit["_id"])
        print("Document Source:", hit["_source"])
        print("=" * 50)


if __name__ == "__main__":
    search_users_index(search_input=SEARCH_INPUT)
