https://github.com/ChristianOlmosUSA/BitcoinHunter
 
# Lets work together and find Satoshi's lost Bitcoin and help return it to the bitcoin ecosystem !!

step 1) download and save all bitcoin addresses into the local folder, this is a 2.6GB file so will take a while, click on the file from:
https://www.bitkeys.work/faq.php . 

step 2) pip install -r requirements.txt _______only requires bitcoin, so unlikely to need a virt env, this was built using python 3.9.1, anything 3x should work
(pip install bitcoin)

step 3) Create a WordList you wish to test, save it locally as MyWordList.txt, (or use the random generator option later on when I've built it)

step 4) > python hunter.py  _____ (OR > python3 hunter.py)


    Hunter will run the following programs:
        LargeFileSplitter (makes the database into a text file, can also split it into more manageable files)... I run with 64MB of ram, you might need to split the files into chunks...
        Permuter (Creates combinations of words for the wordlist)
        SeedHasher (Converts these word combos into Pirvate key and public address hashes)
        KeyChecker (Checks the hashes against the database to see if they exist)


all your results files will be in the gitignore, so they won't shared back to github (private keys, seedlists etc)

* This is the first complete program I've ever written, ask if you have questions! Its certainly not hugely efficient
