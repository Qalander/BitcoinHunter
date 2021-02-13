# take entire list of 2048 from BIP39_English as used by Bitcoin Wallet, open as a list []
def random_12_words():
    lines = []
    file = open("BIP39_English",'r')
    for line in file :
        lines.append(line)
    file.close()
    # Erase the previous Wordlist as w indicates a fresh page, then close it again
    open('MyWordList.txt', 'w').close()    

    # Select 12 random words from the BIP39_English List #
    import random

    # now open the file for appending
    wordfile = open('MyWordList.txt', 'a')

    # loop and randomly select 12 words (also print them to the terminal)
    RW=""
    x = 0
    while (x < 12):         # run from 0 to 11 (ie 12 words)
        RW = (random.choice(lines)); print(RW)
        wordfile.write(RW)
        x +=1

random_12_words()       # call the above function.

    # memory efficient way to strip \n from list variables, but as we are writing back a list we leave the \n and grey out this code
    ### for i,s in enumerate(lines):               
    ###    lines[i] = s.strip()
    ### print(lines)