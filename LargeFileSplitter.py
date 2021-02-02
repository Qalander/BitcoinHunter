# Source of Blockchain Addresses/Balances: https://www.bitkeys.work/faq.php updated weekly, https://bitkeys.work/btc_balance_sorted.csv
# code improved from: https://stackoverflow.com/questions/36445193/splitting-one-csv-into-multiple-files-in-python/36446203#36446203?newreg=4961e491003b4230b892f07cda6ce3db
# In terminal> python LargeFileSplitter.py <GO>
# Only the first file generated (1.txt) contains the headers
# This should take about 45 seconds on a standard PC, all the CSV is turned into txt files of 1,000,000 each, or however user defines.
# output files called 1.txt (without private key) and bitcoin1.txt (contains the private key)
import time

# Check file exists first, and if so, open it

try:
    with open('btc_balance_sorted.csv') as f:
        print(" Bitcoin Database File Located ")
except IOError:
    print("\n \t ERROR ! Cannot find file <btc_balance_sorted.csv>, this needs to be downloaded first from https://bitkeys.work/btc_balance_sorted.csv \n")
    time.sleep (4)

csvfile = open('btc_balance_sorted.csv', 'r') # You will need to save the CSV locally and rename this if different
AddressData = csvfile.readlines()   #This reads the data out of the file and saves it as variable AddressData

# check to see if 1.txt exists, if not create it
filelocated = 0

def does_file_already_exist():
    try:
        f = open("1.txt")
        print (" text version of database file located ")
        filelocated = 1
        return filelocated
    except IOError:
        print("generating simplified txt file of database")
        filename = 1 #for simplicity our first file is called 1.txt
        SplitSize = 32000000       # How many lines the new file should have - 1,000,000 makes an 87MB file (under github limit), 32million covers every known account as of Feb 1st
        for i in range(len(AddressData)):
            if i % SplitSize == 0:                                        
                open(str(filename) + '.txt', 'w+').writelines(AddressData[i:i+SplitSize])
                filename += 1
        csvfile.close()         # Always be closing!
    finally:
        print("generated.")

filelocated = does_file_already_exist()


### Strip the balance, last block address and RIPEMD160 (column 2,3,4 ) data leaving just the raw addresses of column 1
if filelocated == 0:
    f = open("1.txt", "r")          # so this is a txt file exact copy of the csv file, but it has 4 columns and is very large
    g = open("bitcoin1.txt", "w")   # Name of the clean file with just the address columns only.

    for line in f:
        if line.strip():
            g.write("\t".join(line.split(",")[:1]) + "\n")

    f.close()
    g.close()

# END SPLITTER #