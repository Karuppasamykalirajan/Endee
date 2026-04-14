from sentence_transformers import SentenceTransformer
import numpy as np

class VectorDB:
    def __init__(self):
        self.texts = []
        self.vectors = []
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def add(self, text):
        vec = self.model.encode(text)
        self.texts.append(text)
        self.vectors.append(vec)

    def search(self, query):
        q_vec = self.model.encode(query)
        scores = [np.dot(q_vec, v) for v in self.vectors]
        best_idx = np.argmax(scores)
        return self.texts[best_idx]
