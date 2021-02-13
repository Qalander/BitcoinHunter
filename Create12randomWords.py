# take entire list of 2048 from BIP39_English as used by Bitcoin Wallet
def random_12_words():
    lines = []
    file = open("BIP39_English")
    for line in file :
        lines.append(line)
    file.close()

    # memory efficient way to strip \n from list variables, but as we are writing back a list we leave the \n
    #for i,s in enumerate(lines):               
    #    lines[i] = s.strip()
    #print(lines)

    # Select 12 random words from the BIP39_English List
    import random

    # Erase the previous Wordlist as w indicates a fresh page, then close it again
    open('MyWordList.txt', 'w').close()       

    # now open the file for appending
    wordfile = open('MyWordList.txt', 'a')

    x = 0
    while (x < 12):         # run from 0 to 11 (ie 12 words)
        RW = (random.choice(lines))
        print(RW)
        wordfile.write(RW)
        x +=1

random_12_words()       # call the above function.