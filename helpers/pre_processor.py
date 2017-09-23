from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import ngrams
import string, os, math
import textract, re

class Preprocessor:
	"""
	"""
	
	def __init__(self):
		self.keywords = list()
		self.TFVectors = []
		self.fileNames = []
		self.IDFVector = {}
		self.stemmer = PorterStemmer()
		self.stopwords = [str(word) for word in stopwords.words("english")]
		self.appearances = {}
		self.TF_IDF_Vector = {}

	def extract_text(self, file):
		"""
		extract text from a file 
		file can be of different formats : .pptx, .pdf, .docx
		"""
		try:
			txt = textract.process("/home/enigmaeth/DC++/3-1/Information Retrieval/"+str(file)) # returns byte text
		except:
			txt = b""
		txt = txt.decode() # converts bytes to string
						   # printing here leads to non-printable characters also being displayed
		txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '',txt)	# removes escape characters using regex
		txt = txt.encode('ascii','ignore') # removes unicode characters like \u0097 and type(txt) is bytes
		txt = txt.decode('unicode_escape') # conversion to desired string 
		return txt.lower()


	def tokenize(self, file_content):
		"""
		Tokenize the content of the word 
		"""
		tokens = word_tokenize(file_content)
		tokens = [i for i in tokens if i not in string.punctuation]
		tokens = [word for word in tokens if len(word) > 1]
		return tokens


	def stem(self, tokens):
		"""
		"""
		stemmed = []
		stemmer = PorterStemmer()
		for item in tokens:
			stemmed.append(stemmer.stem(item))
		return stemmed


	def generate_ngrams(self, tokens):
		"""
		"""
		unigram = [' '.join(gram) for gram in ngrams(tokens,1)] 
		bigram = [' '.join(gram) for gram in ngrams(tokens, 2)]
		trigram = [' '.join(gram) for gram in ngrams(tokens, 3)]
		return [unigram, bigram, trigram]


	def dumpKeywords(self, keywords, path):
		"""
		Method to dump all the keywords in a file named 'keywords.txt'.
		In this, tokens are separed by '_' so that they can recovered later easily.
		"""
		targetFile = open(path,"w")
		targetFile.write('_'.join(self.keywords))


	def get_tf_idf(self, file, fileNum):
		"""
		"""
		txt = self.extract_text(file)
		tokens = self.tokenize(txt)
		ngrams = self.generate_ngrams(tokens)
		ngrams[0] = self.stem(ngrams[0])
		file_keywords = ngrams[0] + ngrams[1] + ngrams[2]
		file_keywords = [word for word in file_keywords if word not in self.stopwords]
		vector = {}
		for token in file_keywords:
			token = str(token)
			if token not in vector:
				vector[token] = 1
			else:
				vector[token] += 1
		self.keywords += file_keywords
		self.TFVectors.append(vector)
		self.fileNames.append(file)
		file_keywords = list(set(file_keywords))
		for keyword in file_keywords:
			if keyword in self.IDFVector:
				self.IDFVector[keyword] += 1
			else:
				self.IDFVector[keyword] = 1
			if keyword in self.appearances:
				self.appearances[keyword].append(fileNum)
			else:
				self.appearances[keyword] = [fileNum]

	def vectorize(self, numFiles):
		"""
		"""
		all_keywords = list(set(self.keywords))
		for keyword in all_keywords:
			vector = {}
			for fileNum in self.appearances[keyword]:
				tf_idf = self.TFVectors[fileNum][str(keyword)]*(1.0+math.log10(numFiles/self.IDFVector[keyword]))
				vector[fileNum] = tf_idf
			self.TF_IDF_Vector[keyword] = vector
		# print(self.TF_IDF_Vector)	

	# def remove_stop_words(self, word_tokens):
	# 	"""
	# 	"""
	# 	stop_words_to_remove = set(stopwords.words('english'))
	# 	stop_words_to_skip = set(('and', 'or', 'not'))
	# 	stop_words = set(stop_words_to_remove - stop_words_to_skip)

	# 	filtered_sentence = []
	# 	for w in word_tokens:
	# 		if w not in stop_words:
	# 			filtered_sentence.append(w)
	# 	return filtered_sentence
