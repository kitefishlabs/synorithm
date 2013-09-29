import sys, pyaudio
import argparse
import re
import urllib, urllib2
import time

# # READ IN TEXT FILE
# textFile = ""
# with open ("../texts/test1.txt", "r") as myfile:
#     textFile = myfile.read()

    
def doGoogleTTS(wordstring, outfile):


    outfile = open(outfile, 'w+')
    #download chunks and write them to the output file
    
    mp3url = "http://translate.google.com/translate_tts?tl=%s&q=%s&total=%s" % ('en', urllib.quote(wordstring), len(wordstring)) # &idx=%s
    headers = {"Host":"translate.google.com",
      "Referer":"http://www.gstatic.com/translate/sound_player2.swf",
      "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.163 Safari/535.19"}
    req = urllib2.Request(mp3url, '', headers)
    sys.stdout.write('.')
    sys.stdout.flush()
    if len(wordstring) > 0:
        try:
            response = urllib2.urlopen(req)
            outfile.write(response.read())
            time.sleep(.5)
        except urllib2.HTTPError as e:
            print ('%s' % e)

    outfile.close()
    print('Saved MP3 to %s' % outfile)
