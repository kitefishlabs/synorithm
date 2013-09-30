from wordnik import *
from phoney import *
# from googleTTS import *
# import pyaudio
import re
import sys
import urllib, urllib2
import time, random

apiUrl = 'http://api.wordnik.com/v4'
apiKey = '35fe51a6b87809e09500c047c3402b14396168459d65abed3'
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordApi.WordApi(client)

#example = wordApi.getTopExample('irony')
#example.text
'''
def synspeech(phrase):
    mp3url = "http://translate.google.com/translate_tts?tl=%s&q=%s&total=%s&idx=%s" % (args.language, urllib.quote(val), len(combined_text), idx)
    headers = {"Host":"translate.google.com",
    "Referer":"http://www.gstatic.com/translate/sound_player2.swf",
   	 "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.163 Safari/535.19"}
    req = urllib2.Request(mp3url, '', headers)
    sys.stdout.write('.')
    sys.stdout.flush()
    if len(val) > 0:
        try:
            response = urllib2.urlopen(req)
            args.output.write(response.read())
            time.sleep(.5)
        except urllib2.HTTPError as e:
            print ('%s' % e)
'''
def synonym(phrase): # supposed to replace a string of words w/ their synonyms
	wordList = re.sub("[^\w]", " ",  phrase).split()
	newWords = []
	for word in wordList:
		translate = wordApi.getRelatedWords(word, relationshipTypes = 'synonym')
		#print translate[0].text
		if translate:
			#print dir(translate[0])
			#print translate[0].words[0]
			#newWords.append(translate[0].words[0])
			print(translate[0].words[0] + ' ')
		else:
			#newWords.append(word)
			print(word + ' ')

	newSentence = ' '.join(newWords) + '.'
	print(newSentence)

def hypernym(phrase): # supposed to replace a string of words w/ their hynonyms
	wordList = re.sub("[^\w]", " ",  phrase).split()
	newWords = []
	for word in wordList:
		translate = wordApi.getRelatedWords(word, relationshipTypes = 'hypernym')
		#print translate[0].text
		if translate:
			#print dir(translate[0])
			#print translate[0].words[0]
			#newWords.append(translate[0].words[0])
			print(translate[0].words[0] + ' ')
		else:
			#newWords.append(word)
			print(word + ' ')
		transaudio = synspeech(translate)
	newSentence = ' '.join(newWords) + '.'
	print(newSentence)

def phononym(phrase): # supposed to replace a string of words w/ their hynonyms
	wordList = re.sub("[^\w]", " ",  phrase).split()
	newWords = []
	for word in wordList:
		translate = related_words(word)
		#print translate[0].text
		if translate:
			#print dir(translate[0])
			#print translate[0].words[0]
			try:
				newWords += [translate[random.randint(0,4)]]
			except IndexError:
				newWords += [translate[0]]
			print(translate[0] + ' ')
		else:
			#newWords.append(word)
			print(word + ' ')

	newSentence = ' '.join(newWords) + '.'
	print(newSentence)
	return newWords

# READ IN TEXT FILE
# textString = ""
# with open ("../texts/test1.txt", "r") as myfile:
#     textString = myfile.read()

#synonym('The kitchen is lovely.')
#synonym(textFile)
#hypernym(textFile)
#print phononym(textFile)

#main()
