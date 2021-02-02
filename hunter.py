# Import and split bitcoin addresses into files of 1m addresses each, labelled 1.txt, 2.txt...to 31.txt
# > https://www.bitkeys.work/faq.php and splitter.py ==> 1.txt and bitcoin1.txt (up to 31.txt and bitcoin31.txt)

# This works for me in python 3.9.1, but with few dependencies it should be fine in any 3.x

### to run this > python hunter.py

# THIS PROGRAM:
# Take word list and calculate all permutations (this asks you for the permutation length, so requires user input)
# > Permuter.py + MyWordList.txt ==> seedlist.txt

# Use those permutations to calculate Private Keys, and Addresses
# > SeedHasher.py + seedlist.txt ==> addresses.txt + addr_priv.txt

# Check Addresses against database & produce an output of valid keys
# KeyChecker.py + addresses.txt vs 1.txt ==> FREE_MONEY_unique_results.txt

# Loop the whole thing 31x (somehow)

import multiprocessing, time
mpCores=multiprocessing.cpu_count()
print("This PC has", mpCores,"cores. Currently only utilising 1, upgrades to follow")

tic = time.perf_counter()                                           # ** Start the timer                                    

exec(open("LargeFileSplitter.py").read())    # convert the btc addresses csv file (of 32million accounts with balances) into a text file (smaller files if desired, my 64GB of ram avoids this)
exec(open("Permuter.py").read())    # take your word list and convert it into every possible combination, this can take ages
exec(open("SeedHasher.py").read())  # turn your word combos into private keys, then public addresses
exec(open("KeyChecker.py").read())  # check those addresses generated against our btc database, save them to a new tex tfile if there's a collision

toc = time.perf_counter()                                           # ** Stop the timer
print("TOTAL RUN TIME: ", f"{toc - tic:0.2f} seconds")   # the 0.4f means 4 decimal places


  