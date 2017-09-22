from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
#import textract, re

class Preprocessor:
	"""
	"""
	
	# def extract_text(file):
	# 	"""
	# 	"""
	# 	txt = textract.process("BITS.pdf") # returns byte text
	# 	txt = txt.decode() # converts bytes to string
	# 					   # printing here leads to non-printable characters also being displayed
	# 	txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '',txt)	# removes escape characters using regex
	# 	txt = txt.encode('ascii','ignore') # removes unicode characters like \u0097 and type(txt) is bytes
	# 	txt = txt.decode('unicode_escape') # conversion to desired string 
	# 	#print(' '.join(txt.split()))
	# 	return txt


	def tokenize(self, file_content):
		"""
		"""
		tokens = word_tokenize(file_content)
		tokens = [i for i in tokens if i not in string.punctuation]
		return tokens


	def stem(self, tokens):
		"""
		"""
		stemmed = []
		stemmer = PorterStemmer()
		for item in tokens:
			stemmed.append(stemmer.stem(item))
		return stemmed

	def remove_stop_words(self, word_tokens):
		"""
		"""
		stop_words_to_remove = set(stopwords.words('english'))
		stop_words_to_skip = set(('and', 'or', 'not'))
		stop_words = set(stop_words_to_remove - stop_words_to_skip)

		filtered_sentence = []
		for w in word_tokens:
			if w not in stop_words:
				filtered_sentence.append(w)
		return filtered_sentence