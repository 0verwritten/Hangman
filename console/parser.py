import requests

class Dictionary(): ## class for get description of word
	def __init__(self, word):
		if word == "":
			return "Invaild word"
		self.word  = word
		data = self.__get_data()
		if data == False:
			return f"The word you've entered isn't in the dictionary."
		return data

	def _find(self,val, query, next_val=0, start=0):
		for x in range(start, len(query)-len(val)+1):
			if query[x:(x+len(val))] == val:
				if next_val > 0:
					next_val -= 1
					continue
				return x
		return False
	def _get_value(self,start, end, query, delay=0):
			start_index = self._find(start, query)
			end_index = self._find(end, query, start=start_index, next_val=delay) + len(end)
			return [query[start_index:end_index],end_index] ## second object is to make right query cut


	def __get_data(self): ## function for get request to dictionary
		request = requests.get(f'https://www.merriam-webster.com/dictionary/{self.word}')
		if f"The word you\'ve entered isn\'t in the dictionary." in request.text:
			return False
		while True:
			res, i = self._get_value('<span class="dtText"><strong class="mw_t_bc">', '</span>', request.text)
			request = request.text[i:]
			if not self.word[:3] in res:
				res = res.replace('<', "`#")
				res = res.replace('>', "`")
				res = res.split("`")
				for x in range(len(res)-1, -1, -1):
					if '#' in res[x] or res[x] == '' or res[x] == ": ":
						del res[x]
				res = ''.join(res) # end value
				return res

class RandomWord(Dictionary): ## class to get random word
	def __init__(self):
		self.rand_word, self.description = self.__get_data()
		print(self.rand_word)



	def __get_data(self):
		request = requests.get('https://randomword.com/')
		res, i = super()._get_value('<div id="shared_section">', '</div>', request.text, delay=2)
		request = request.text[i:]
		res = res.replace('<', "`#")
		res = res.replace('>', "`")
		res = res.split("`")
		for x in range(len(res)-1, -1, -1):
			if '#' in res[x] or res[x] == '' or '\n\t\t' in res[x]:
				del res[x]
		res[1] = res[1][:len(res[1])-2]
		return res# end value

