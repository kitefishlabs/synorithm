from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '35fe51a6b87809e09500c047c3402b14396168459d65abed3'
client = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(client)
example = wordApi.getTopExample('irony')
example.text


wordApi = WordApi.WordApi(client)
definitions = wordApi.getDefinitions('badger',
                                     partOfSpeech='verb',
                                     sourceDictionaries='wiktionary',
                                     limit=1)
definitions[0].text


import re
wordApi = WordApi.WordApi(client)
def synonym(phrase): # supposed to replace a string of words w/ their synonyms
	wordList = re.sub("[^\w]", " ",  phrase).split()
	for word in wordList:
		translate = wordApi.getRelatedWords(word, relationshipTypes = 'synonym')
	#print translate[0].text
	print translate[0]

synonym('The kitchen is lovely.')



find_synonym_for_this = wordApi.getRelatedWords('house',
									relationshipTypes = 'synonym',
									limitPerRelationshipType = 1)
print find_synonym_for_this[0].text