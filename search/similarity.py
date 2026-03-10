from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(query_vector, tfidf_matrix):

    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)

    return similarity_scores