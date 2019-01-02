#!!!bs4 must be in the SAME FOLDER
from bs4 import BeautifulSoup

fname = '**fliename.xml**'
bs = BeautifulSoup(open(fname))
print(bs.prettify())
