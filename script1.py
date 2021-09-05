#!/usr/bin/python3

print ("\nRunning Script...\n")

import os

files = os.listdir()    #get list of files

unedited_word = 'server_1'  #what to change
edited_word = 'server_2'    #change for what 

n = 0
for f in files:

    if f == __file__[2:]:  #don't edit itself
        continue

    try:                   #go forvard if there are directories
        fin = open(f, "rt")

        data = fin.read()

        n+=data.count(unedited_word)   #counting how many words need to change
        data = data.replace(unedited_word, edited_word)

        fin.close()

        fin = open(f, "wt")

        fin.write(data)

        fin.close()
    finally:
        continue

print (f'''Checked {len(files)-1} items\nFixed {n} times''')
print ("\nDone\n")


