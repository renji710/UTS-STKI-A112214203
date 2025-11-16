
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

try:
    list_stopwords = stopwords.words('indonesian')
except LookupError:
    import nltk
    nltk.download('stopwords')
    list_stopwords = stopwords.words('indonesian')

factory = StemmerFactory()
stemmer = factory.create_stemmer()

#Fungsi case folding dan membersihkan teks
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https{1,2}:\/\/\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

#Fungsi tokenisasi
def tokenize(text):
    try:
        return word_tokenize(text)
    except LookupError:
        import nltk
        nltk.download('punkt')
        return word_tokenize(text)

#Fungsi membuang stopwords.
def remove_stopwords(tokens):
    return [word for word in tokens if word not in list_stopwords]

#Fungsi stemming
def stem_tokens(tokens):
    return [stemmer.stem(word) for word in tokens]

#Pipeline seluruh proses
def preprocess_pipeline(text):
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = stem_tokens(tokens)
    return tokens