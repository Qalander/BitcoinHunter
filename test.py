
# All this crap just to move a file to a different location:
""" import time
import shutil

fileToArchive = time.strftime("Date_%Y_%m_%d_@_Time_%Hh_%Mm_%Ss")
print (fileToArchive)
PrivKeyArchive = "Private_Key_Archive_"
fileToArchive2 = PrivKeyArchive+fileToArchive+".txt"

print (fileToArchive2)

time.sleep(2)

with open('seedlist.txt','r') as firstfile, open(fileToArchive2,'a+') as secondfile: 
    # read content from first file 
    for line in firstfile:         
             # write content to second file 
             secondfile.write(line) 

#secondfile.close()

# now move the file to archive
newPath = shutil.move(fileToArchive2, 'archives')
 """
