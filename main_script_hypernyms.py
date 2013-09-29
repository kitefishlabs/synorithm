from wordnik_test import *
from googleTTS_single import *
import multiprocessing

NUM_POOLS = 4


def worker(pair):
	"""thread worker function"""
	i = pair[0]
	word = pair[1]

	print 'Worder: ', i, " | ", word

	# filter stop words
	outname = str(i) + '_' + word + '.wav'
	outfile = '/Users/dennisgreenberg/synorithm/audio_out/' + outname
	doGoogleTTS(word, outfile)

	return

textString = ""
with open ("../texts/test1.txt", "r") as myfile:
	textString = myfile.read()

resultList = phononym(textString)



# if __name__ == '__main__':

pool = multiprocessing.Pool(NUM_POOLS)
pool.map(worker, zip(range(10), resultList[:10]))

