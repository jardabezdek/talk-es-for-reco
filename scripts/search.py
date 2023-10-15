"""
This script utilizes the Elasticsearch library to search the 'users' index based on the provided 
search input. 

Requirements:
- Elasticsearch connection details must be properly configured in the 'scripts.config' module.
- The Elasticsearch library must be installed (`pip install elasticsearch`).

Usage:
1. Ensure that the Elasticsearch connection details are correctly set in 'scripts.config.ES_HOST'.
2. Modify the 'SEARCH_INPUT' variable to specify the search term.
3. Run the script. The search results will be printed to the console.
"""

from elasticsearch import Elasticsearch

from scripts.config import ES_HOST

SEARCH_INPUT = "german"


def search_users_index(search_input: str) -> None:
    """Search the 'users' index for the provided search input and print matching documents.

    This function utilizes Elasticsearch to perform a search in the 'users' index based on the given
    search input. It performs a multi-field match search with optional fuzzy matching to find
    documents that match the provided input within the 'name', 'city', and 'country' fields. The
    retrieved documents are then printed, displaying their respective document IDs and source data.

    Args:
        search_input (str): String to search for within the 'name', 'city', and 'country' fields.

    Returns:
        None

    Note:
    - This function requires the Elasticsearch connection to be properly set with the 'ES_HOST'.
    - Fuzzy search allows finding results even with slight misspellings in the search input.
    """
    es = Elasticsearch(ES_HOST)

    search_result = es.search(
        index="users",
        query={
            "multi_match": {
                # string that will be searched for
                "query": search_input,
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
