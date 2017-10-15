import os


class FileManager:
	"""
	This class provides functions related to file management required for the indexer
	"""

	def __init__(self):
		"""
		initialize variables: root path and accepted formats for the indexer
		"""
		self.root = '/home/enigmaeth/TestDump'
		self.accepted_formats = ['pdf']


	def get_all_files(self):
		"""
		List all files recursively in the root specified by root
		"""
		files_list = []
		for root, subdirs, files in os.walk(self.root):
		    for name in files:
		    	files_list.append(os.path.join(self.root, name))
		return files_list[0:-1]


	def get_files_to_be_indexed(self):
		"""
		returns list of files to be included in the index
		set `root` variable to the desired root
		:return: list of files to be indexed
		"""
		files_list = self.get_all_files()
		for name in files_list:
			if(name.split('.')[-1] in self.accepted_formats and os.stat(os.path.join(self.root, name)).st_size < 5000000):
				files_list.append(os.path.join(self.root, name))
		return files_list[0:-1]
