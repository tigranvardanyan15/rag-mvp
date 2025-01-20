from starlette.config import Config


config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

HOST: str = config("HOST", cast=str, default="0.0.0.0")
PORT: int = config("PORT", cast=int, default=8000)
RELOAD: bool = config("RELOAD", cast=bool, default=False)
LOG_LEVEL: str = config("LOG_LEVEL", cast=str, default="error")

# Vector database configs
VECTOR_DB_NAME = config("VECTOR_DB_NAME", cast=str, default="vector_db")
VECTOR_DB_COLLECTION = config(
    "VECTOR_DB_COLLECTION", cast=str, default="master_ardshin"
)
VECTOR_DB_N_RESULTS = config("VECTOR_DB_N_RESULTS", cast=int, default=15)
VECTOR_DB_THRESHOLD = config("VECTOR_DB_THRESHOLD", cast=float, default=0.75)
VECTOR_DB_PERSIST_PATH = config(
    "VECTOR_DB_PERSIST_PATH", cast=str, default=f"db/{VECTOR_DB_NAME}"
)
VECTOR_DB_N_RESULTS = config("VECTOR_DB_N_RESULTS", cast=int, default=10)
VECTOR_DB_THRESHOLD = config("VECTOR_DB_THRESHOLD", cast=float, default=0.7)

HF_API_TOKEN = config("HF_API_TOKEN", cast=str, default="")
LLM_MODEL = config("LLM_MODEL", cast=str, default="meta-llama/Llama-2-13b")
