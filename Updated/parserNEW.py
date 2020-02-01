import csv
import re
import urllib.request
from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        self.allData = []

def getUrl(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, features='html.parser')

    allData = {}

    #Geting a title for page

    if soup.find('title'):
        siteTitle = soup.find('title')
    else:
        siteTitle = 'This website hasn\'t a title'

    print('\n\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n' +
            'Title is:\n' +
            siteTitle.text + '\nTitlelength is: ' +
            str(len(siteTitle.text)) + '\n')
    allData['Title'] = siteTitle.text

    #Find all meta-tags
    #If we've found a meta with name equal 'description', then we can read
    #them content

    for tag in soup.find_all("meta"):
        if tag.get("name", None) == "description":
            siteDescription = tag.get("content", None)
            print('Description of this page is:\n' + siteDescription + '\n')
            allData['Description'] = siteDescription
        else:
            pass

#'This website hasn\'t a description' + '\n'

    #Looking for a keywords

    for tag in soup.find_all("meta"):
        if tag.get("name", None) == "keywords":
            siteKeywords = tag.get("content", None)
            print('Keywords of this page is:\n' + siteKeywords + '\n')
            allData['Keywords'] = siteKeywords
        else:
            pass

    #Looking for a canonical

    if soup.find('link', rel='canonical'):
        siteCanonical = str(soup.find('link', rel='canonical'))
        siteCanonical = ''.join(re.findall(r'http\w+\:\/\/\w+.\w+.\w+.\w+', siteCanonical))
    else:
        siteCanonical = 'This website hasn\'t a canonical'

    print('Canonical is:\n' + str(siteCanonical) + '\n')
    allData['Canonical'] = siteCanonical

    #Looking for a H1 tag

    if soup.find('h1'):
        siteH1Tag = soup.find('h1')
        siteH1Tag = siteH1Tag.text
    else:
        siteH1Tag = 'This website hasn\'t an H1 tag'

    print('H1 tag is:\n' + siteH1Tag + '\n')
    allData['H1 tag'] = siteH1Tag

    #Looking for a H2 tag
    # TODO: make a decorator function for H2-H6 tags

    if soup.find_all('h2'):
        siteH2Tag = []

        for h2tag in soup.find_all('h2'):
            thisTag = h2tag.text
            siteH2Tag.append(thisTag)
            siteH2TagCompl = '\n'.join(map(str, siteH2Tag))

        print('H2 tag is:\n' + siteH2TagCompl + '\n')
        allData['H2 tag'] = siteH2Tag
    else:
        print('H2 tag is:\nThis website hasn\'t an H2 tag' + '\n')
        allData['H2 tag'] = 'This website hasn\'t an H2 tag'

    #Looking for a H3 tag

    if soup.find_all('h3'):
        siteH3Tag = []

        for h3tag in soup.find_all('h3'):
            thisTag = h3tag.text
            siteH3Tag.append(thisTag)

        print('H3 tag is:\n' + '\n'.join(map(str, siteH3Tag)) + '\n')
        allData['H3 tag'] = siteH3Tag
    else:
        print('H3 tag is:\nThis website hasn\'t an H3 tag' + '\n')
        allData['H3 tag'] = 'This website hasn\'t an H3 tag'

    #Looking for a H4 tag

    if soup.find_all('h4'):
        siteH4Tag = []

        for h4tag in soup.find_all('h4'):
            thisTag = h4tag.text
            siteH4Tag.append(thisTag)

        print('H4 tag is:\n' + '\n'.join(map(str, siteH4Tag)) + '\n')
        allData['H4 tag'] = siteH4Tag
    else:
        print('H4 tag is:\nThis website hasn\'t an H4 tag' + '\n')
        allData['H4 tag'] = 'This website hasn\'t an H4 tag'

    #Looking for a H5 tag

    if soup.find_all('h5'):
        siteH5Tag = []

        for h5tag in soup.find_all('h5'):
            thisTag = h5tag.text
            siteH5Tag.append(thisTag)

        print('H5 tag is:\n' + '\n'.join(map(str, siteH5Tag)) + '\n')
        allData['H5 tag'] = siteH5Tag
    else:
        print('H5 tag is:\nThis website hasn\'t an H5 tag' + '\n')
        allData['H5 tag'] = 'This website hasn\'t an H5 tag'

    #Looking for a H6 tag

    if soup.find_all('h6'):
        siteH6Tag = []

        for h6tag in soup.find_all('h6'):
            thisTag = h6tag.text
            siteH6Tag.append(thisTag)

        print('H6 tag is:\n' + '\n'.join(map(str, siteH6Tag)) + '\n')
        allData['H6 tag'] = siteH6Tag
    else:
        print('H6 tag is:\nThis website hasn\'t an H6 tag' + '\n')
        allData['H6 tag'] = 'This website hasn\'t an H6 tag'

    return allData


#__________________________END_OF_PARSING_____________________________#

def saveToCSV(allData, path, url):
    with open(path, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Parsed URL is ', url))
        for key, value in allData.items():
            writer.writerow([key, value])
        writer.writerow('')
        csvfile.close()

#Start our parser

def parseSite():
    print('= = = Hello! Would you like some parse now? = = =')
    print('Enter the URL below:\n')
    url = str(input())
    parse(getUrl(url))
    saveToCSV(parse(getUrl(url)), 'parseddata.csv', url)
    pass

if __name__ == '__main__':
    parseSite()
