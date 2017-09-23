from helpers.pre_processor import Preprocessor
from nltk.corpus import stopwords

class Query:
	"""
	"""

	def __init__(self):
		self.input = input("Enter Query: ")
		self.preprocessor = Preprocessor()
		self.keywords = ""
		self.results = []

	def query_preprocess(self):
		"""
		"""
		tokens = self.preprocessor.tokenize(self.input)
		ngrams = self.preprocessor.generate_ngrams(tokens)
		ngrams[0] = self.preprocessor.stem(ngrams[0])
		self.keywords = ngrams[0] + ngrams[1] + ngrams[2]
		self.keywords = [word for word in self.keywords if word not in self.preprocessor.stopwords]
				
	def display_results(self, numFiles):
		"""
		"""
		self.results = []
		for fileNum in range(numFiles):
			score = 0.0
			for keyword in self.keywords:
				if keyword in self.preprocessor.TF_IDF_Vector and fileNum in self.preprocessor.TF_IDF_Vector[keyword]:
					score += self.preprocessor.TF_IDF_Vector[keyword][fileNum]
			self.results.append((score,fileNum))
		self.results.sort()