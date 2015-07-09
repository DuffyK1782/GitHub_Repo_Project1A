from lxml.html import parse
from urllib import urlopen
parsed = parse(urlopen('http://finance.yahoo.com/q/hp?s=PFE&a=06&b=7&c=2015&d=06&e=7&f=2015&g=d'))
doc = parsed.getroot()

links = doc.findall('.//a')

print "links length = ", len(links)

urls = [lnk.get('href') for lnk in doc.findall('.//a')]

tables = doc.findall('.//table')
len(tables)
table14 = tables[13]
table14.text_content()

import re

strTable14 = str(table14.text_content())
table14Search = re.findall('\S+OpenHigh\S+\s\S+', strTable14)
print table14Search

strTable14 = str(table14Search)

headerDate = re.search('Date',strTable14)
if headerDate:
    print headerDate.group(0)
	
headerOpen = re.search('Open',strTable14)
if headerOpen:
    print headerOpen.group(0)

headerHigh = re.search('High',strTable14)
if headerHigh:
    print headerHigh.group(0)
	
headerLow = re.search('Low',strTable14)
if headerLow:
    print headerLow.group(0)
	
headerClose = re.search('Close',strTable14)
if headerClose:
    print headerClose.group(0)
	
headerVolume = re.search('Volume',strTable14)
if headerVolume:
    print headerVolume.group(0)
	
	
headerAdjClose = re.search('Adj\sClose',strTable14)
if headerAdjClose:
    print headerAdjClose.group(0)