
from .preprocess import stemmer

#Vocabulary
def build_vocabulary(processed_docs):
    all_tokens = [token for doc_tokens in processed_docs.values() for token in doc_tokens]
    vocabulary = sorted(list(set(all_tokens)))
    return vocabulary

#Inverted Index
def build_inverted_index(vocabulary, processed_docs):
    inverted_index = {}
    for term in vocabulary:
        doc_list = []
        for doc_name, tokens in processed_docs.items():
            if term in tokens:
                doc_list.append(doc_name)
        inverted_index[term] = doc_list
    return inverted_index

#Fungsi search query boolean
def search(query, index, all_doc_names):
    all_docs_set = set(all_doc_names)
    query = query.lower().strip()
    
    #Proses query NOT
    if query.startswith('not '):
        term = query.split(' ', 1)[1]
        term = stemmer.stem(term)
        docs_with_term = set(index.get(term, []))
        return sorted(list(all_docs_set - docs_with_term))

    #Proses query AND atau OR
    elif ' and ' in query:
        parts = query.split(' and ')
        term1 = stemmer.stem(parts[0])
        term2 = stemmer.stem(parts[1])
        docs1 = set(index.get(term1, []))
        docs2 = set(index.get(term2, []))
        return sorted(list(docs1 & docs2))
        
    elif ' or ' in query:
        parts = query.split(' or ')
        term1 = stemmer.stem(parts[0])
        term2 = stemmer.stem(parts[1])
        docs1 = set(index.get(term1, []))
        docs2 = set(index.get(term2, []))
        return sorted(list(docs1 | docs2))
        
    #Proses query satu kata
    else:
        term = stemmer.stem(query)
        return sorted(index.get(term, []))