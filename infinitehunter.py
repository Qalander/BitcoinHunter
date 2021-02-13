# run forever until a hash is found

# Decode the large BTC database

# LOOP Begins:

    # select 12 words from standard BTC wallet
from Create12randomWords import random_12_words
random_12_words()

    # turn all 12 words into every possible permutation, but of length 12. so
    # permutations 12 length 12 = 479m. 11 of length 11 is 39million ... maybe lets leave the smaller lengths too, for completeness.

    # Hash those words into private key

