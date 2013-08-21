import json

cmntxt = open('/prg/synory/cmn_wrds.txt', 'r')
cmn_list = cmntxt.read()
cmntxt.close()

json.load(cmn_list)
