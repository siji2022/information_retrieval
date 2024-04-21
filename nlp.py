from datasets import load_dataset
# dataset = load_dataset("wikimedia/wikipedia”, “20231101.en")
import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords
stop=set(stopwords.words('english'))