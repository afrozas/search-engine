import os
from helpers.query import Query

def get_files(path=None):
	"""
	returns list of files to be included in the index
	set `path` variable to the desired path
	:return:
	"""
	root = '/home/enigmaeth/31'
	files_list = []
	accepted_formats = ['pdf', 'pptx', 'docx', 'doc']
	#accepted_formats = ['docx', 'doc']
	for path, subdirs, files in os.walk(root):
	    for name in files:
	    	#print(os.path.join(path, name))
	    	if(name.split('.')[-1] in accepted_formats and os.stat(os.path.join(path, name)).st_size < 5000000):
	    		files_list.append(os.path.join(path, name))
	return files_list[0:-1]

def pre_process():
	"""
	Indexes the corpus using tf-idf vectorization
	Query pre-processed and documents returned on the basis of similarity
	"""
	q = Query()
	files, fileNum = get_files(), 0
	for file in files:
		print(fileNum, file)
		q.preprocessor.get_tf_idf(file, fileNum)
		fileNum += 1
	q.preprocessor.vectorize(len(files))
	fileNum = 0
	for file in files:
		print(fileNum, ": ", file)
		fileNum += 1
	while True:
		q.query_preprocess()
		if q.input == "XXX":
			break
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