# KRISTINA SOPHIE CAMILLE

import re
class Predict(object) :


	def __init__(self, doc, nlp, seuil = 0.5) :

		self.doc = doc
		self.seuil = seuil
		self.nlpdoc = nlp(self.doc)
		self.lemmas = [token.lemma_ for token in self.nlpdoc]
		self.lemmatized=" ".join(self.lemmas)

	def workspace(self) :

		mots_pos=["beautiful","likable","engaging","impressive","sensual","genuine","fresh","mysterious","authentic","interesting","fun","nice","favourite","favorite","funny","colourful","charming","charmingly","inventive","innovative","moving","entertaining","intelligent","amusing","nicely","good","solid","memorable","impressed","wow"]
		mots_pos_plus=["should see","should watch","recommend","fascinating","unforgettable","hilarious","fantastic","thrilling","recommended","amazing","excellent","excellently","delightful","marvellous","brilliant","delight","finest","joyous","genius","masterfully","great","greatest","masterpiece","awesome","sublime","wonderful","excellently","witty","irresistible","best","must-see","must see","praise"]
		mots_neg=["annoying","off putting","ugly","weird","unfortunately","waste \w+ time","ridiculous","worse","stupid","predictable","silliest","disappoint","laughable","can not stand","screw","painful","painfully","sketchy","non-existent"]
		mots_neg_plus=["awful","crappy","terrible","badly","bad","poorly","shit","pathetic","disappointing","disappointed","hate","dislike","failure","mediocre","mediocrity","worst","fail","cliche","cliché","should not watch","dull","cornball","avoid watch","irritating","overrated","boring"]
		for mot in mots_pos:
			match=re.findall(rf"\w+ \w+ \w+ {mot} ", self.lemmatized)
			for m in match:
				if "not" in m or "no " in m or "neither " in m:
					self.seuil-=0.1
					#print(m+"-1")
				else:
					self.seuil+=0.2
					#print(m+"+1")
		for mot in mots_pos_plus:
			match=re.findall(rf"\w+ \w+ \w+ {mot} ", self.lemmatized)
			for m in match:
				if "not" in m or "no " in m or "neither " in m:
					self.seuil-=0.2
					#print(m+"-2")
				else:
					self.seuil+=0.3
					#print(m+"+2")

		for mot in mots_neg:
			match=re.findall(rf"\w+ \w+ \w+ {mot} ", self.lemmatized)
			for m in match:
				if "not" in m or "no " in m or "neither " in m:
					self.seuil+=0.1
					#print(m+"-1")
				else:
					self.seuil-=0.2
					#print(m+"+1")
		for mot in mots_neg_plus:
			match=re.findall(rf"\w+ \w+ \w+ {mot} ", self.lemmatized)
			for m in match:
				if "not" in m or "no " in m or "neither " in m:
					self.seuil+=0.1
					#print(m+"-2")
				else:
					self.seuil-=0.3
					#print(m+"+2")
		bonne_note=re.compile(r'[6-9]/10')
		mauvaise_note=re.compile(r'[0-5]/10')
		if re.search(bonne_note, self.doc):
			self.seuil=1
			#print("note explicite positive dans : ")
			#print(self.doc)
		if re.search(mauvaise_note, self.doc):
			self.seuil=0.3
			#print("note explicite negative dans : ")
			#print(self.doc)


	def predict(self) :

		self.workspace()
		#print(self.seuil)

		if self.seuil < 0.5 :
			self.predicted = 'neg'
		else :
			self.predicted = 'pos'


if __name__ == '__main__':


	pred = Predict(open('../corpus/imdb/pos/33_7.txt').read())
	pred.predict()
	print (pred.predicted)
