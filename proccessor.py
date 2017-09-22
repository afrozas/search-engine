from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
import textract, re

class TextExtractor:
	"""
	"""
	txt = textract.process("BITS.pdf") # returns byte text
	txt = txt.decode() # converts bytes to string
					   # printing here leads to non-printable characters also being displayed
	txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '',txt)	# removes escape characters using regex
	txt = txt.encode('ascii','ignore') # removes unicode characters like \u0097 and type(txt) is bytes
	txt = txt.decode('unicode_escape') # conversion to desired string 
	print(' '.join(txt.split()))

class Tokenizer:
	"""
	"""
	def tokenize(file_content):
		"""
		"""
		tokens = word_tokenize(file_content)
		return tokens

class Stemmer:
	"""
	"""
	def stem(tokens):
		"""
		"""
		ps = PorterStemmer()
		return ps.stem(tokens)
