#!/usr/bin/python3

# To schedule the script to run every 6 hours, you need to:
# edit crontab configuration file by using command: crontab - e 
# and next add:  0 */6 * *  *  <PATH_TO_THE_SCRIPT>


import random
from datetime import datetime


curent_time = datetime.now().strftime("%H:%M")

s1 = ''
all_char = '1234567890-=_+!@#$%^&*()\|/[]{}`~qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

for i in range (10):
    s1 = ''.join((random.choice(all_char) for i in range(1000)))
    curent_file = open(f'''test_{curent_time}_{i+1}.txt''', "w+")
    curent_file.write(s1)
    curent_file.close()
