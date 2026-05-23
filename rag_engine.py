import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

CORPUS_FILE = "faiss_cache/corpus.pkl"
EMBEDDINGS_FILE = "faiss_cache/embeddings.npy"
INDEX_FILE = "faiss_cache/faiss.index"

print("Loading embedding model...")
emb_model = SentenceTransformer('all-MiniLM-L6-v2')

print("Loading corpus...")
with open(CORPUS_FILE, "rb") as f:
    corpus = pickle.load(f)

print("Loading embeddings...")
corpus_embeddings = np.load(EMBEDDINGS_FILE)

print("Loading FAISS index...")
index = faiss.read_index(INDEX_FILE)

print("RAG ready!")

def retrieve_context(query, top_k=3):

    q_emb = emb_model.encode([query])

    scores, ids = index.search(
        np.array(q_emb).astype("float32"),
        top_k
    )

    results = []

    for i in ids[0]:
        if i < len(corpus):
            results.append(corpus[i])

    return " | ".join(results)