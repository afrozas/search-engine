import os
from helpers.pre_processor import Preprocessor
from helpers.query import Query

def get_files(path=None):
	"""
	returns list of files to be included in the index
	set `path` variable to the desired path
	:return:
	"""
	path = '/home/enigmaeth/DC++/3-1/Information Retrieval'
	files = os.listdir(path)
	return files

def pre_process():
	"""
	Indexes the corpus using tf-idf vectorization
	Query pre-processed and documents returned on the basis of similarity
	"""
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