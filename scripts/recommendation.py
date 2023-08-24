"""
Script for posts recommendation in Elasticsearch.

This script utilizes Elasticsearch to recommend posts to a user based on various factors.
It applies a scoring mechanism to rank posts and provide personalized recommendations to the user.

Requirements:
- Elasticsearch connection details must be properly configured in the 'scripts.config' module.
- The Elasticsearch library must be installed (`pip install elasticsearch`).

Usage:
1. Ensure that the Elasticsearch connection details are correctly set in 'scripts.config.ES_HOST'.
2. Modify the 'USER_ID' variable to specify the user for whom posts should be recommended.
3. Run the script. The recommended posts will be printed to the console.
"""

from elasticsearch import Elasticsearch

from scripts.config import ES_HOST

USER_ID = 8


def recommend_posts_to_user(user_id: int) -> None:
    """Recommend posts to a user using Elasticsearch scoring.

    Args:
        user_id (int): ID of the user for whom posts should be recommended.

    Returns:
        None
    """
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
                        "weight": 10,
                    },
                    # more likely recommend posts that are trending in the moment
                    {
                        "filter": {
                            "term": {
                                "booster_trending": 1,
                            }
                        },
                        "weight": 10,
                    },
                    # less likely recommend posts that were already seen by the user
                    {
                        "filter": {
                            "term": {
                                "penalty_consumed_by_users": user_id,
                            }
                        },
                        "weight": 0.01,
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
