import os
from helpers.file_manager import FileManager
from helpers.format_converter import FormatConverter
from helpers.query import Query


def pre_process_and_query():
	"""
	Indexes the corpus using tf-idf vectorization
	Query pre-processed and documents returned on the basis of similarity
	"""


	# Query object is created which instances Prepocessor class
	q = Query()

	# Convert any ppt file to text extractable form
	print("starting conversion")
	FormatConverter.ppt_to_pdf()

	# Get the list of all files to be indexed
	print("Getting files to be indexed")
	fm = FileManager()
	files, fileNum = fm.get_files_to_be_indexed(), 0
	print(files)

	# TF-IDF of each file and vectorization in file list to be indexed
	for file in files:
		print(fileNum, file)
		q.preprocessor.get_tf_idf(file, fileNum)
		fileNum += 1 
	q.preprocessor.vectorize(len(files))

	fileNum = 0
	for file in files:
		print(fileNum, ": ", file)
		fileNum += 1

	# Loop to support query any number of times
	while True:

		# query pre-processing
		q.query_preprocess()

		# escape string to quit the main program
		if q.input == "quit()":
			break

		# displaying resutls
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
		print()


if __name__ == '__main__':
	pre_process_and_query()