import os
import faiss
import pickle
import requests
import numpy as np

from sentence_transformers import SentenceTransformer

# ---------------------------------------------------
# CACHE SETUP
# ---------------------------------------------------

CACHE_DIR = "faiss_cache"

os.makedirs(CACHE_DIR, exist_ok=True)

CORPUS_FILE = os.path.join(CACHE_DIR, "corpus.pkl")
EMBEDDINGS_FILE = os.path.join(CACHE_DIR, "embeddings.npy")
INDEX_FILE = os.path.join(CACHE_DIR, "faiss.index")

# ---------------------------------------------------
# HF DATASET URLs
# ---------------------------------------------------

BASE_URL = "https://huggingface.co/datasets/harshsoni7/medify-rag-cache/resolve/main"

CORPUS_URL = f"{BASE_URL}/corpus.pkl"
EMBEDDINGS_URL = f"{BASE_URL}/embeddings.npy"
INDEX_URL = f"{BASE_URL}/faiss.index"

# ---------------------------------------------------
# DOWNLOAD HELPER
# ---------------------------------------------------

def download_file(url, path):

    if not os.path.exists(path):

        print(f"Downloading {path} ...")

        response = requests.get(url)

        response.raise_for_status()

        with open(path, "wb") as f:
            f.write(response.content)

        print(f"{path} downloaded successfully!")

# ---------------------------------------------------
# DOWNLOAD CACHE FILES
# ---------------------------------------------------

download_file(CORPUS_URL, CORPUS_FILE)
download_file(EMBEDDINGS_URL, EMBEDDINGS_FILE)
download_file(INDEX_URL, INDEX_FILE)

# ---------------------------------------------------
# LOAD EMBEDDING MODEL
# ---------------------------------------------------

print("Loading embedding model...")

emb_model = SentenceTransformer(
    'all-MiniLM-L6-v2',
    device='cpu'
)

print("Embedding model loaded!")

# ---------------------------------------------------
# LOAD CACHE FILES
# ---------------------------------------------------

print("Loading corpus...")

with open(CORPUS_FILE, "rb") as f:
    corpus = pickle.load(f)

print("Loading embeddings...")

corpus_embeddings = np.load(EMBEDDINGS_FILE)

print("Loading FAISS index...")

index = faiss.read_index(INDEX_FILE)

print("RAG ready!")

# ---------------------------------------------------
# RETRIEVAL FUNCTION
# ---------------------------------------------------

def retrieve_context(query, top_k=3):

    q_emb = emb_model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")

    scores, ids = index.search(q_emb, top_k)

    results = []

    for i in ids[0]:
        if i < len(corpus):
            results.append(corpus[i])

    return " | ".join(results)