import os
from helpers.pre_processor import Preprocessor
from helpers.query import Query

def get_files():
	files = os.listdir('/home/enigmaeth/DC++/3-1/Information Retrieval')
	return files

def pre_process():
	"""
	"""
	# p = Preprocessor()
	# # txt = p.extract_text()
	# files, fileNum = get_files(), 0
	# for file in files:
	# 	p.get_tf_idf(file, fileNum)
	# 	fileNum += 1
	# p.vectorize(len(files))
	# fileNum = 0
	# for file in files:
	# 	print(fileNum, ": ", file)
	# 	fileNum += 1
	# tokens = p.tokenize(txt)
	# print(tokens)
	# tokens = p.remove_stop_words(tokens)
	# stems = p.stem(tokens)
	# print(stems)
	q = Query()
	files, fileNum = get_files(), 0
	for file in files:
		q.preprocessor.get_tf_idf(file, fileNum)
		fileNum += 1
	q.preprocessor.vectorize(len(files))
	fileNum = 0
	for file in files:
		print(fileNum, ": ", file)
		fileNum += 1
	q.query_preprocess()
	q.display_results(len(files))
	ans, rank = q.results, 1
	ans.sort()
	ans = ans[::-1]
	print()
	print("RESULTS: ")
	for element in ans:
		if element[0] > 0:
			print(rank,". ",q.preprocessor.fileNames[element[1]],"( ",element[0]," )")
			rank += 1
if __name__ == '__main__':
	pre_process()