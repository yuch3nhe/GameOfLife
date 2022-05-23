import urllib
#open(c:/Desktop/rules.txt, mode)
#open(Desktop/rules.txt, mode)

'''
#  read from a website
import requests

link = "https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life"
f = requests.get(link)
print(f.text)
'''

#  read from a .txt file
f = open('venv/Scripts/rules.txt', 'r')
f.close()
with open('venv/Scripts/rules.txt') as f:
    contents = f.read()
    print(contents)


#link = '<a href="https://www.educationperfect.com/app/#/login">Link</a>'
#QTextBrowser.append(link)
#QTextBrowser.show()

#label.setText('<a href="http://stackoverflow.com/">Link</a>')
#label.setOpenExternalLinks(True)
