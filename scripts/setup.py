"""Script for ElasticSearch setup."""

from elasticsearch import Elasticsearch

from data import DOCS_POSTS, DOCS_USERS
from scripts.config import ES_HOST, INDEX_NAME_TO_CONFIG

es = Elasticsearch(ES_HOST)


def create_indices(name_to_config: dict) -> None:
    """Create ES indices."""
    for index_name, index_config in name_to_config.items():
        es.options(ignore_status=400).indices.create(
            index=index_name,
            settings=index_config.get("settings"),
            mappings=index_config.get("settings"),
        )
        print(f"✅ Created `{index_name}` index.")


def upload_data(index_name: str, docs: list) -> None:
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
