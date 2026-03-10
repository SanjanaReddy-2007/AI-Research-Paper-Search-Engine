from database.db import get_all_papers
from search.vectorizer import PaperVectorizer
from search.similarity import compute_similarity

class SearchEngine:

    def __init__(self):
        self.vectorizer = PaperVectorizer()
        self.vectorizer.build_index()

    def search(self, query, top_k=5):

        vectorizer = self.vectorizer.get_vectorizer()
        tfidf_matrix = self.vectorizer.get_matrix()
        papers = self.vectorizer.get_papers()

        query_vector = vectorizer.transform([query])

        similarity = compute_similarity(query_vector, tfidf_matrix)

        ranked_indices = similarity.argsort()[0][::-1]

        results = []

        for i in ranked_indices[:top_k]:
            results.append(papers[i])

        return results