class NLP(object):
	"""docstring for NLP"""
	def __init__(self):
		super(NLP, self).__init__()
	
	def words_split(self,sentence):
		words_list = sentence.split()
		return words_list