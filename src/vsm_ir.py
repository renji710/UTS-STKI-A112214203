
import math
import numpy as np
from collections import Counter
from .preprocess import preprocess_pipeline

#Fungsi menghitung matriks TF-IDF
def calculate_tfidf_matrix(processed_docs):
    
    #Term Frequency (TF)
    term_frequency = {doc_name: Counter(tokens) for doc_name, tokens in processed_docs.items()}
    
    #Document Frequency (DF)
    all_tokens = [token for doc_tokens in processed_docs.values() for token in doc_tokens]
    vocabulary = sorted(list(set(all_tokens)))
    
    doc_frequency = {}
    for term in vocabulary:
        count = 0
        for doc_tokens in processed_docs.values():
            if term in doc_tokens:
                count += 1
        doc_frequency[term] = count
        
    #Inverse Document Frequency (IDF)
    N = len(processed_docs)
    inverse_doc_frequency = {term: math.log(N / df) for term, df in doc_frequency.items()}
    
    #Matriks TF-IDF
    tfidf_matrix = {}
    for doc_name, tf_scores in term_frequency.items():
        doc_tfidf_scores = {term: tf * inverse_doc_frequency[term] for term, tf in tf_scores.items()}
        tfidf_matrix[doc_name] = doc_tfidf_scores
        
    return tfidf_matrix, inverse_doc_frequency

#Fungsi menghitung cosine similarity
def _cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    dot_product = sum(vec1[x] * vec2[x] for x in intersection)
    norm_vec1 = np.sqrt(sum(val**2 for val in vec1.values()))
    norm_vec2 = np.sqrt(sum(val**2 for val in vec2.values()))
    
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    
    return dot_product / (norm_vec1 * norm_vec2)

#Fungsi search dengan VSM
def search(query, tfidf_matrix, inverse_doc_frequency, top_k=5):
    #Preprocess query
    query_tokens = preprocess_pipeline(query)
    
    #Hitung vektor TF-IDF
    query_tf = Counter(query_tokens)
    query_vector = {
        term: tf * inverse_doc_frequency[term] 
        for term, tf in query_tf.items() if term in inverse_doc_frequency
    }
            
    #Hitung cosine similarity
    scores = {
        doc_name: _cosine_similarity(query_vector, doc_vector)
        for doc_name, doc_vector in tfidf_matrix.items()
    }
        
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)[:top_k]