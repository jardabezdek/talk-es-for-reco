"""
This script sets up Elasticsearch indices and uploads data into the corresponding indices.
It uses the Elasticsearch library to interact with the Elasticsearch instance.
Ensure that the Elasticsearch connection details and index configurations are properly set 
in the 'scripts.config' module. Also, ensure that the data to be uploaded is available 
in the 'data' module.

Requirements:
- Elasticsearch connection details must be correctly configured in the 'scripts.config' module.
- Index configurations must be defined in 'scripts.config.INDEX_NAME_TO_CONFIG'.
- Data to be uploaded must be available in the 'data.DOCS_POSTS' and 'data.DOCS_USERS' lists.
- The Elasticsearch library must be installed (`pip install elasticsearch`).

Usage:
1. Ensure that the Elasticsearch connection details and index configurations are properly set.
2. Make sure the data to be uploaded is available in 'data.DOCS_POSTS' and 'data.DOCS_USERS'.
3. Run the script. It will create indices based on the configurations and upload the data.
"""

from elasticsearch import Elasticsearch

from data import DOCS_POSTS, DOCS_USERS
from scripts.config import ES_HOST, INDEX_NAME_TO_CONFIG

es = Elasticsearch(ES_HOST)


def create_indices(name_to_config: dict) -> None:
    """Create Elasticsearch indices based on provided configurations.

    Args:
        name_to_config (dict): Dictionary containing index names as keys, and settings as values.

    Returns:
        None
    """
    for index_name, index_config in name_to_config.items():
        es.options(ignore_status=400).indices.create(
            index=index_name,
            settings=index_config.get("settings"),
            mappings=index_config.get("mappings"),
        )
        print(f"✅ Created `{index_name}` index.")


def upload_data(index_name: str, docs: list) -> None:
    """Upload data into the specified Elasticsearch index.

    Args:
        index_name (str): Name of the target index.
        docs (list): List of documents to be uploaded.

    Returns:
        None
    """
    for doc_id, doc in enumerate(docs, start=1):
        es.index(index=index_name, id=doc_id, document=doc)

    print(f"✅ Uploaded {len(docs)} documents into `{index_name}` index.")


if __name__ == "__main__":
    print("🔄 Creating indices.")
    create_indices(name_to_config=INDEX_NAME_TO_CONFIG)

    print("🔄 Uploading data.")
    for index_name, docs in (
        ("users", DOCS_USERS),
        ("posts", DOCS_POSTS),
    ):
        upload_data(index_name=index_name, docs=docs)
