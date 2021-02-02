# Some examples: 8 words in 6 length permutations gives 20,160 permutations (vs just 28 combinations)
# 2048 words in a typical bitcoin wallet, used in 12 word seeds, gives about: 5,271,537,971,301,490,000,000,000,000,000,000,000,000 possible permutations!

import itertools as it
import time
import math
import shutil

## ## ## STEP 1: Get Inputs, includes a 3 second timeout, and using default name if enter is pressed without typing ## ## ## -----------------------------------------------
inputFileName = ""

def prompt_with_timeout():          # This function gives you 3 seconds to interrupt before using a default file name, seedlist
  from time import sleep

  print('\n\t You have 3 seconds to ctrl + C, and rename the input source, or by default will use MyWordList.txt to generate random private keys')
  try:
    for i in range(0, 3): # 30 minutes is 30*60 seconds, 3 is three seconds
      sleep(1)
    print("//")
    inputFileName = "MyWordList.txt"
  except KeyboardInterrupt:
    inputFileName = input("which .txt file to read word lists from? : ")
  return inputFileName

def choose_wordset(): ############################### UNFINISHED """"
    print(" \n Randomly generate a word set")
    print(" which language to use as seeds?")
    lang = input 

if inputFileName == "": prompt_with_timeout()   # if still blank then seek a name (blank if a random word set has not been chosen)
if inputFileName == "":
    print ("\t > defaulting to MyWordList.txt as no input recieved")
    inputFileName = "MyWordList.txt"


# this section just checks you've put the .txt at the end of the filename as its a common habit to forget
nameCheck = inputFileName[-4:]      # take the last 4 char of the string
if nameCheck != ".txt":             # check the 4 chars are .txt, otherwise it has not been input
    inputFileName = inputFileName + ".txt"      # add the .txt if it has been forgotten

print (" \n ", "   opening ", inputFileName, "\n")

lineNos=0
with open(inputFileName, 'r') as f:
    for line in f:
        lineNos += 1
print("> Total number of items to scramble is ----> ", lineNos, "\n", "\n")

permuteLengthMin = int(input("What is the MINimum permutation length you seek eg 12 permutations (not combinations!) :\n "))
permuteLengthMax = int(input("\nWhat is the MAX permutation length you seek eg 20 permutations: \n"))


def total_seeds(permuteLengthMin,permuteLengthMax,nf,lineNos):
    totalSeeds = 0
    for i in range (permuteLengthMin, permuteLengthMax):
        n_minus_r=lineNos-i
        nrf = math.factorial(n_minus_r)
        xseeds = (nf/nrf)
        totalSeedsLag = totalSeeds
        totalSeeds = totalSeeds + (nf/nrf) - totalSeedsLag
        print(totalSeeds)
    return totalSeeds

nf = math.factorial(lineNos)
totalSeeds = total_seeds(permuteLengthMin,permuteLengthMax,nf,lineNos)
print ("There will be a total of ", totalSeeds, "seed combinations to create, taking around ",totalSeeds/420000, " seconds")


# outputFileName = input("which .txt file to save permutations to? ")
#
""" def getOutputFileName():
    print()
    outputFileName = ""
    while len(outputFileName) < 1: 
        outputFileName = input('which .txt file to save permutations to? ')
        if outputFileName == "": outputFileName = "seedlist.txt"
    return outputFileName

oName = getOutputFileName() """



""" # this section just checks you've put the .txt at the end of the filename as its a common habit to forget// ** EDIT, as we are arching the files remove the ability to rename seedlist
nameCheck = oName[-4:]      # take the last 4 char of the string
if nameCheck != ".txt":             # check the 4 chars are .txt, otherwise it has not been input
    oName = oName + ".txt"      # add the .txt if it has been forgotten
open(oName, 'a+').close()           # create the blank file for writing later
"""

# sticking to default "seedlist.txt"
oName = "seedlist.txt"



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


## NOW ARCHIVE THE SEEDLIST.TXT FILE FOREVER
fileToArchive = time.strftime("Date_%Y_%m_%d_@_Time_%Hh_%Mm_%Ss")
print (fileToArchive)
SeedlistArchive = "Seedlist_Archive_"
fileToArchive2 = SeedlistArchive+fileToArchive+".txt"

print (fileToArchive2)

time.sleep(2)

with open('seedlist.txt','r') as firstfile, open(fileToArchive2,'a+') as secondfile: 
    # read content from first file 
    for line in firstfile:         
             # write content to second file 
             secondfile.write(line) 

# now move the file to archive
newPath = shutil.move(fileToArchive2, 'archives')


      