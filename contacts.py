#Ryan Haddadi
#October 21 2021
import json
class Contacts:
	def __init__( self, filename):
		self.v = filename
		self.t = {}
		try:
			with open(self.v) as z:
				self.t = json.load(z)
		except FileNotFoundError:
			print ("File not found")
		#	return self.t
	def add_contact(self, *, id, first_name, last_name):
		if id in self.t:
			return str("error")
		else:
			self.t[id] = [first_name, last_name]
			self.t = dict(sorted(self.t.items(), key = lambda x:x[1][1].lower(), reverse = False))
			self.t = dict(sorted(self.t.items(), key = lambda x:x[1][0].lower(), reverse = False))
			with open(self.v, 'w') as p:
				json.dump(self.t,p)
				return self.t[id]
	def modify_contact( self,*, id, first_name, last_name):
		if (id not in self.t):
			return str("error")
		else:
			self.t[id] = [first_name, last_name]
			self.t = dict(sorted(self.t.items(), key = lambda x:x[1][1].lower(), reverse = False))
			self.t = dict(sorted(self.t.items(), key = lambda x:x[1][0].lower(), reverse = False))
			with open(self.v, 'w') as p:
				json.dump(self.t,p)
				return self.t[id]
	def delete_contact( self,*, id):
		if (id not in self.t):
			return str("error")
		else:
			self.t.pop(id)
			with open(self.v, 'w') as p:
				json.dump(self.t,p)
			return self.t
	def different_filename(self, filename):
		self.v = filename
