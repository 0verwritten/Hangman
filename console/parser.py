import requests

class Dictionary(): ## class for get description of word
	def __init__(self, word):
		if word == "":
			print("Invaild word")
			return "Invaild word"
		self.word  = word
		data = self.__get_data()
		if data == False:
			return f"The word you've entered isn't in the dictionary."
		return data

	def find(self,val, query, next_val=0, start=0):
		for x in range(start, len(query)-len(val)+1):
			if query[x:(x+len(val))] == val:
				if next_val > 0:
					next_val -= 1
					continue
				return x
		print('no')
	def get_values(self,start, end, query):
			start_index = self.find(start, query)
			end_index = self.find(end, query, start=start_index) + len(end)
			print(f"text is: '{query[start_index:end_index]}'")
			return [query[start_index:end_index],end_index] ## second object is to make right query cut


	def __get_data(self): ## function for get request to dictionary
		request = requests.get(f'https://www.merriam-webster.com/dictionary/{self.word}')
		if f"The word you\'ve entered isn\'t in the dictionary." in request.text:
			return False
		while True:
			res, i = self.get_values('<span class="dtText"><strong class="mw_t_bc">', '</span>', request.text)
			request = request.text[i:]
			if not self.word[:3] in res:
				res = res.replace('<', "`#")
				res = res.replace('>', "`")
				res = res.split("`")
				for x in range(len(res)-1, -1, -1):
					if '#' in res[x] or res[x] == '' or res[x] == ": ":
						print(res[x])
						del res[x]
				res = ''.join(res) # end value
				return res

