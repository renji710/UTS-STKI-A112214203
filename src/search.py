
import os
from .preprocess import preprocess_pipeline, stemmer
from . import boolean_ir
from . import vsm_ir

#Search Engine
class SearchEngine:
    def __init__(self, data_path='data/'):
        
        #Muat dokumen
        self.documents = self._load_documents(data_path)
        print(f"INFO: Loaded {len(self.documents)} documents.")

        #Preprocess semua dokumen
        self.processed_docs = {
            name: preprocess_pipeline(text) 
            for name, text in self.documents.items()
        }
        print("INFO: Preprocessing complete.")

        #Data untuk Boolean Model
        self.vocabulary = boolean_ir.build_vocabulary(self.processed_docs)
        self.inverted_index = boolean_ir.build_inverted_index(self.vocabulary, self.processed_docs)
        print("INFO: Boolean model data is ready.")
        
        #Data untuk VSM Model
        self.tfidf_matrix, self.inverse_doc_frequency = vsm_ir.calculate_tfidf_matrix(self.processed_docs)
        print("INFO: VSM model data is ready.")

    #Fungsi memuat txt
    def _load_documents(self, path):
        docs = {}
        base_dir = os.path.dirname(os.path.abspath(__file__))
        actual_path = os.path.join(base_dir, '..', path)
        
        for filename in os.listdir(actual_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(actual_path, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    docs[filename] = file.read()
        return docs

    #Fungsi search utama
    def search(self, query, model='vsm', k=5):
        
        if model == 'boolean':
            return boolean_ir.search(query, self.inverted_index, self.documents.keys())
        elif model == 'vsm':
            return vsm_ir.search(query, self.tfidf_matrix, self.inverse_doc_frequency, top_k=k)
        else:
            raise ValueError("Model tidak valid. Pilih 'boolean' atau 'vsm'.")