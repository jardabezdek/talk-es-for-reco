"""Script for posts recommendation in the ElasticSearch."""

from elasticsearch import Elasticsearch

from scripts.config import ES_HOST

USER_ID = 8


def recommend_posts_to_user(user_id: int) -> None:
    """Search `users` index for the `search_input`."""
    es = Elasticsearch(ES_HOST)

    search_result = es.search(
        index="posts",
        query={
            "function_score": {
                "functions": [
                    # more likely recommend to user that are following the post author
                    {
                        "filter": {
                            "term": {
                                "booster_followers": user_id,
                            }
                        },
                        "weight": 1_000,
                    },
                    # more likely recommend posts that are trending in the moment
                    {
                        "filter": {
                            "term": {
                                "booster_trending": 1,
                            }
                        },
                        "weight": 100,
                    },
                    # less likely recommend posts that were already seen by the user
                    {
                        "filter": {
                            "term": {
                                "penalty_consumed_by_users": user_id,
                            }
                        },
                        "weight": 0.001,
                    },
                    # try to NOT recommend posts created by the user
                    {
                        "filter": {
                            "term": {
                                "user_id": user_id,
                            }
                        },
                        "weight": 0.00001,
                    },
                ],
                "boost_mode": "multiply",
                "score_mode": "multiply",
            }
        },
    )

    # print the retrieved documents
    for hit in search_result["hits"]["hits"]:
        print("Document ID:", hit["_id"])
        print("Document Score:", hit["_score"])
        print("Document Source:", hit["_source"])
        print("=" * 50)


if __name__ == "__main__":
    recommend_posts_to_user(user_id=USER_ID)
