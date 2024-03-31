import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
   
    # Remove numbers and punctuation
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
   
    # Tokenize text
    tokens = word_tokenize(text)
   
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
   
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
   
    # Join tokens back into a string
    processed_text = ' '.join(tokens)
   
    return processed_text

# print(1)
# x = 'dsfh , !### twEET'
# print(preprocess_text(x) ,"%%%%%%%%%%%%%%%%%%%%%%" , x)
