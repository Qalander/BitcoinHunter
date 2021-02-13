# run forever until a hash is found

# Decode the large BTC database

# LOOP Begins:

    # select 12 words from standard BTC wallet
from Create12randomWords import random_12_words
random_12_words()       # creates a 12 word MyWordList.txt file

    # turn all 12 words into every possible permutation, but of length 12. so
    # permutations 12 length 12 = 479m. 11 of length 11 is 39million ... maybe lets leave the smaller lengths too, for completeness.
from permuteri import permuteri
permuteri()          # creates a 149 million lines of seedlisti.txt

    # Hash those words into private key. 149million is a lot, so lets do it in blocks of 100,000 then save & archive those keys - should open up a multi

