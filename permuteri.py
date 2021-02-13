# Take MyWordList and crack on with it

import itertools as it
import time
import math
import shutil

## ## ## STEP 1: Get Inputs, includes a 3 second timeout, and using default name if enter is pressed without typing ## ## ## -----------------------------------------------
inputFileName = "MyWordList.txt"

print (" \n ", "   opening ", inputFileName, "\n")

lineNos=0           # count how many lines there are to process
with open(inputFileName, 'r') as f:
    for line in f:
        lineNos += 1
print("> Total number of items to scramble is ----> ", (lineNos), "\n", "\n")     # add 1 if you start from zero

permuteLengthMin = lineNos
permuteLengthMax = lineNos


# sticking to default "seedlisti.txt"       i for infinite
oName = "seedlisti.txt"

# open the list from file specified and ignore the \n at the end
with open(inputFileName) as f:          # open the list from file specified and ignore the \n at the end
    wordlist = f.read().splitlines()
# Note, if the text file has 2 words on one line it will treat it as one, eg "hello world" is 1 item, but with a delimiter (,) as on 1 line "hello", "world" is 2 items.
f.close()   ## Save RAM, close the file! 

## ## ## STEP 2: PERMUTE the wordlist ## ## ## -----------------------------------------------
print ("Calculating....\n")
loopz = 0
while int(permuteLengthMin+loopz)<= int(permuteLengthMax):
    tic = time.perf_counter()                                           # ** Start the timer                                    
    with open(oName, 'w') as outfile:
        for sent in it.permutations(wordlist, int(permuteLengthMin+loopz)):
            outfile.write(f"{' '.join(sent)}\n")                # Save to text file as a list of words
    toc = time.perf_counter()                                           # ** Stop the timer
    print("Calculation of permutation of length:",int(permuteLengthMin+loopz), f", in {toc - tic:0.4f} seconds")   # the 0.4f means 4 decimal places
    loopz = int(loopz + 1)   
    

print ("\t RESULTS in " + oName + "\n")


## NOW ARCHIVE THE SEEDLISTi.TXT FILE FOREVER
fileToArchive = time.strftime("Date_%Y_%m_%d_@_Time_%Hh_%Mm_%Ss")
print (fileToArchive)
SeedlistArchive = "Seedlist_Archive_"
fileToArchive2 = SeedlistArchive+fileToArchive+".txt"

print (fileToArchive2)

time.sleep(1)

with open('seedlisti.txt','r') as firstfile, open(fileToArchive2,'a+') as secondfile: 
    # read content from first file 
    for line in firstfile:         
             # write content to second file 
             secondfile.write(line) 

# now move the file to archive
newPath = shutil.move(fileToArchive2, 'archives')
