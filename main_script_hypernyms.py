from nltk_functs import *
# from wordnik import *
from googleTTS_single import *
import multiprocessing
from subprocess import call

import sc
import time, random

NUM_POOLS = 4


def worker(pair):
	"""thread worker function"""
	i = pair[0]
	word = pair[1]

	print 'Worder: ', i, " | ", word

	# filter stop words
	outname = str(i) + '_' + word + '.mp3'
	outnamewav = '/Users/kfl/dev/git/synorithm/audio_out/' + str(i) + '_' + word + '.wav'
	outfile = '/Users/kfl/dev/git/synorithm/audio_out/' + outname
	doGoogleTTS(word, outfile)
	
	call(["sox", outfile, outnamewav])
# 	time.sleep(1.5)
# 	
# 	call(["play", outfile])
# 	
# 	wordplayer = sc.Synth("synonym_clouder")
# 	wordplayer.bufnum = sc.loadSnd( outnamewav )
# 	
# 	sc.unloadSnd( wordplayer.bufnum )
	
	return

textString = ""
with open ("texts/test1.txt", "r") as myfile:
	textString = myfile.read()

resultList = phononym(textString)



# if __name__ == '__main__':

# sc.start("/Users/kfl/bin/scsynth", verbose=1)
pool = multiprocessing.Pool(NUM_POOLS)
pool.map(worker, zip(range(100), resultList[:100]))

