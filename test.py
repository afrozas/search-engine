#from helpers.pre_processor import extract_text
from helpers.pre_processor import Preprocessor

def pre_process():
	"""
	"""
	#txt = extract_text()
	with open('ext.txt', 'r') as myfile:
		txt = myfile.read().replace('\n', '')

	p = Preprocessor()
	tokens = p.tokenize(txt)
	print tokens
	tokens = p.remove_stop_words(tokens)
	stems = p.stem(tokens)
	print stems

if __name__ == '__main__':
	pre_process()