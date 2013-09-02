import json

cmntxt = open('/users/dennisgreenberg/synorithm/texts/cmn_wrds.txt', 'r')
type(cmntxt) # 
cmn_list = cmntxt.read()
type(cmn_list)
cmntxt.close()

cmn_list_as_sep_array = cmn_list.split(" ")
cmn_list_as_sep_array[:10]
cmn_list_as_sep_array = cmn_list.split("\t") # creates sub-arrays
cmn_list_as_sep_array[:10]
del cmn_list_as_sep_array[0] # remove empty string at index 0

dict_of_pairs = dict() # empty dict
length = len(cmn_list_as_sep_array) # length of array
for i in range(1, (length-1), 2): # (length-1) as counting is inclusive -> 0; range(x, y, z) - z = nmbr of steps
	dict_of_pairs[cmn_list_as_sep_array[i]] = cmn_list_as_sep_array[i+1]

dict_of_pairs = dict() # empty dict
length = len(cmn_list_as_sep_array) # length of array
for i in range(1, (length-1), 2):
	the_word = cmn_list_as_sep_array[i]
	the_word = the_word[:-1]
	dict_of_pairs[the_word] = int(float(cmn_list_as_sep_array[i+1]))


jsonfile = open('/users/dennisgreenberg/synorithm/texts/cmn_wrds.json', 'w')
json.dump(dict_of_pairs, jsonfile)
jsonfile.close()
