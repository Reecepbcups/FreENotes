##* Copyright (C) Reece W - All Rights Reserved
##* Unauthorized editing of this file, via any medium is strictly prohibited
##* Proprietary and confidential
##* Written by Reece W <Reecepbcups@gmail.com>, November 2018

import requests
from multiprocessing import Queue # something for py2exe /shrug/
import os
import time

print("=" * 25)
print(" Reecepbcups - FreEnotes")
print("=" * 25)

# Grab Enotes Link
link = input('\nEnotes Link: ')


# Add https:// if the user did not provide
if 'https://' not in link: 
    addon = 'https://'
# Adds www. if the user did not provide.
if 'www.' not in link: 
    addon = addon + 'www.'
# Adds the https:// then/or www. to the start of the link
try:
    link = addon + link 
except:
    link = link

# Grabs the source code of the HTML page. This will still grab the CSS file from enotes, so it will look the same
try:
    page = requests.get(link)


    # Removes the blurred boxes from the code we downloaded. Epic Win.
    webpage = str(page.text).replace('hh-box__answer__text redacted anon-hide obscured','') 

    # Splits the link into sections at the '/' character, and selects the end of the link. Ex. 'how-character-lady-macbeth-change-throughout-play-387127'
    # then it selects the first 20 letters, and adds the .html file extention
    fileName = link.split('/')[-1][0:20] + '.html'

    # Creates a html file in the current working dirrectory (CWD)
    cwd = os.getcwd()
    with open(fileName, 'w') as htmlFile: # creates an ht
        htmlFile.write(webpage)

    print('\nYour file can be found at: ' + str(cwd))
    print('\nReport any errors to Reeccepbcups#3370 on discord')
    time.sleep(8)
    print('Closing')
    time.sleep(2)
    
except:
    print("\nThe link you entered does not seem to be valid.")
    print("Please restart the program and retry, or contact Reecepbcups#3370 on discord.")
    time.sleep(10)



# Now THAT is a Victory Royal!
# https://media1.tenor.com/images/7a1f78c9eb1a2f4589cfc7a1285862fe/tenor.gif
