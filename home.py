import urllib

link = "https://git.heroku.com/gentle-shore-32691.git"
f = urllib.urlopen(link)
myfile = f.read()
print myfile
