from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import ngrams
import string, os, math
import textract, re

class Preprocessor:
	"""
	Preprocessor class provides method required for indexing the corpus
	TF-IDF model used for retrieval
	"""
	
	def __init__(self):
		"""
		initialize several variables to use them throughout the program and for object instances
		"""
		self.keywords = list()
		self.TFVectors = []
		self.fileNames = []
		self.IDFVector = {}
		self.stemmer = PorterStemmer()
		self.stopwords = [str(word) for word in stopwords.words("english")]
		self.appearances = {}
		self.TF_IDF_Vector = {}
		self.docLength = {}

	def extract_text(self, file):
		"""
		extract text from a file
		file can be of different formats : .pptx, .pdf, .docx
		:param file: expects file path as param to be processed by textract
					 textract extracts text from various file formats
		:return: text extracted from file in lower case
		"""
		try:
			txt = textract.process(str(file)) # returns byte text
			txt = txt.decode('utf-8') # converts bytes to string
						   # printing here leads to non-printable characters also being displayed
			txt = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '',txt)	# removes escape characters using regex
			txt = txt.encode('ascii','ignore') # removes unicode characters like \u0097 and type(txt) is bytes
			txt = txt.split()
			newTxt = []
			for text in txt:
				try:
					newTxt.append(text.decode('unicode_escape')) # conversion to desired string 
				except:
					pass
			txt = ' '.join(newTxt)	
		except:
			txt = ""
		return txt


	def tokenize(self, file_content, file=None):
		"""
		Tokenize the content of the word
		:param file_content: the text content of a file
		:return: list of tokens obtained by using nltk.word_tokenize()
		"""
		# print(file)
		tokens = word_tokenize(file_content)
		tokens = [i for i in tokens if i not in string.punctuation]
		tokens = [word for word in tokens if len(word) > 1]
		return tokens


	def stem(self, tokens):
		"""
		Stemming of the tokens
		:param tokens: list of tokens to be stemmed down
		:return: list of stemmed tokens
		"""
		stemmed = []
		stemmer = PorterStemmer()
		for item in tokens:
			stemmed.append(stemmer.stem(item))
		return stemmed


	def generate_ngrams(self, tokens):
		"""
		Generate uni, bi and tri-grams from the stemmed down tokens of file text
		:param tokens: list of stemmed down tokens
		:return: list containing three separate lists - one each for unigram, bigram and trigram
		"""
		unigram = [' '.join(gram) for gram in ngrams(tokens,1)] 
		bigram = [' '.join(gram) for gram in ngrams(tokens, 2)]
		trigram = [' '.join(gram) for gram in ngrams(tokens, 3)]
		return [unigram, bigram, trigram]


	def dumpKeywords(self, keywords, path):
		"""
		Method to dump all the keywords in a file represented by path
		In this, tokens are separed by '_' so that they can recovered later easily.
		:param keywords: List of keywords to be dumped to external storage for cleaning up space on RAM
		:param path: path where the dump file is intended to be created
		:return: None
		"""
		targetFile = open(path,"w")
		targetFile.write('_'.join(self.keywords))


	def get_tf_idf(self, file, fileNum):
		"""
		Method to get tf-idf for each keyword
		:Saves term frequency of all words in each file as list of dicts 'TFVectors'
		:Saves occurrences of keywords in files in dict 'appearances'
		:Saves inverse document frequency of each keyword in form of dict 'IDFVector'
		:param file: file path from where keywords are to extracted
		:param fileNum: total number of files in the corpus

		"""
		try:
			txt = self.extract_text(file)
			tokens = self.tokenize(txt, file)
			ngrams = self.generate_ngrams(tokens)
			ngrams[0] = self.stem(ngrams[0])
			file_keywords = ngrams[0] + ngrams[1] + ngrams[2]
			file_keywords = [word for word in file_keywords if word not in self.stopwords]
			self.docLength[fileNum] = len(file_keywords)
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
		except:
			print("Could not process... ", file)

	def vectorize(self, numFiles):
		"""
		Vectorization of each file
		The keywords are indexed in the following format:
			{ key_word1 : { <doc1> : <tf-idf value based on model> , <doc2> : ... } , key_word2 : { ... } ... }
		:Saves the values for each keyword in entire corpus in the above format in dict of dicts TF_IDF_Vector
		:param numFiles: total number of files in corpus
		:return:
		"""
		all_keywords = list(set(self.keywords))
		for keyword in all_keywords:
			vector = {}
			for fileNum in self.appearances[keyword]:
				try:
					tf_idf = self.TFVectors[fileNum][str(keyword)]*(1.0+math.log10(numFiles/self.IDFVector[keyword]))
					vector[fileNum] = tf_idf
				except:
					pass
			self.TF_IDF_Vector[keyword] = vector
