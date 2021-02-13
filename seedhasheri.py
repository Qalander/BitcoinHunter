from bitcoin import privtopub, pubtoaddr, sha256   
import time
import shutil    

number_of_lines = len(open('seedlisti.txt').readlines())


i = 1
j = 1
print ("Moving to Hashing Phase of the operation")
print('Total hashes so far...',j,'...calculating')

with open("seedlisti.txt", "r") as ourfile, open("addressesi.txt", "a+") as adds, open("addr_privi.txt", "a+") as addpriv: # Open our txt file to read from, file to write to, and 3rd file is only used if we hit a match and need to reference the priv key
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


# Lets save the private addresses/keys so we never need to calc them again, into a folder called "/archives"
fileToArchive = time.strftime("Date_%Y_%m_%d_@_Time_%Hh_%Mm_%Ss")
print (fileToArchive)
addr_priv_Archive = "addr_priv_Archive_"
fileToArchive2 = addr_priv_Archive+fileToArchive+".txt"

print (fileToArchive2)

time.sleep(2)

with open('addr_priv.txt','r') as firstfile, open(fileToArchive2,'a+') as secondfile: 
    # read content from first file 
    for line in firstfile:         
             # write content to second file 
             secondfile.write(line) 

# now move the file to archive
newPath = shutil.move(fileToArchive2, 'archives')