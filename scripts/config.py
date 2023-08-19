"Configuration file."

ES_HOST = "http://elasticsearch:9200"

INDEX_NAME_TO_CONFIG = {
    "users": {
        "settings": {"number_of_shards": 1, "number_of_replicas": 0},
        "mappings": {
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "text"},
                "created_at": {"type": "integer"},
                "city": {"type": "text"},
                "country": {"type": "text"},
            }
        },
    },
    "posts": {
        "settings": {"number_of_shards": 1, "number_of_replicas": 0},
        "mappings": {
            "properties": {
                "id": {"type": "integer"},
                "user_id": {"type": "integer"},
                "description": {"type": "text"},
                "booster_followers": {"type": "integer", "store": "yes"},
                "booster_trending": {"type": "integer"},
                "penalty_consumed_by_users": {"type": "integer", "store": "yes"},
            }
        },
    },
}
