# This program takes a word file of mnemomics and calculates a new priv key and address from each line of the .txt file
# Work in Progress ... do we even need the (uncompressed) public key, just check the address? quicker

# > python SeedHasher.py   # defaults to seedlist.txt for input

# Printing to screen is time consuming - comment out prints if serious
from bitcoin import privtopub, pubtoaddr, sha256       

number_of_lines = len(open('seedlist.txt').readlines())
timerSecs = number_of_lines/8
timerMins = number_of_lines/18750
print ("Hashing ",number_of_lines," word combinations might take about ",timerSecs," seconds, or ",timerMins," minutes")

i = 1
j = 1
print (""" > Example of calculations:
PRIVATE key: b5c07f41e1b94acd56b6aa92c73ec8f78381ee69d1fa0f365618e3298df4dcfc , *** never share your private key ***
Public key: 04163802d0ede144c00405bd59ed9ad7212779d7b85a029f7d871fac026bccd5f144a1deb706e07c88b4cb2dcf3b462e9b48c89fc16be2ac4422859d5c1a627f6d
Bitcoin address: 1ACJL9QJN5Roe9EEYF6chPRcgwephrG3U5
""")
print('Total hashes so far...',j,'...calculating')

with open("seedlist.txt", "r") as ourfile, open("addresses.txt", "a+") as adds, open("addr_priv.txt", "a+") as addpriv: # Open our txt file to read from, file to write to, and 3rd file is only used if we hit a match and need to reference the priv key
    for line in ourfile:
        YourSeed = line
        i += 1
        j += 1
        if (i == 2500):                             # I think 2,500 is 8 seconds.
            print('Total hashes so far...',j)
            i = 0
    
        priv= sha256(YourSeed)
        #print("PRIVATE key: " + priv)
        #print ("           *** never share your private key ***")

        pub = privtopub(priv)
        #print("public key: " + pub)

        address = pubtoaddr(pub)
        #print("address: " + address)
        adds.write(address + "\n")
        addpriv.write(address+","+priv + "\n") 

        #print ("_____________________________________________")

ourfile.close()  # Close our txt file