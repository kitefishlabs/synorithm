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
