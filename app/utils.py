from app.settings import VECTOR_DB_THRESHOLD


def filter_db_results(db_results: dict) -> str:
    num_result = len(db_results["ids"][0])
    matched_results = []
    for index in range(num_result):
        document = db_results["documents"][0][index]
        distance = db_results["distances"][0][index]
        if distance >= VECTOR_DB_THRESHOLD:
            matched_results.append(document)

    return " ".join(matched_results)
