# SeoParser
A SEO parser that detects and return the necessary data for SEO-specialist.

## How to use it

First, you need to make sure that you have Python 3.7 installed. You also need libraries:
* [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
* [urllib3 1.25.2](https://pypi.org/project/urllib3/)

Once you understand that everything you need is installed on your computer, run the [parser.py](parser.py) file in the console and paste the URL of the site that you want to parse, including the Protocol (http or https), and press Enter.

In the console you will see the received data. Also, they will be added to the file parseddata.csv that will appear next to the parser file.

You can call the script again without closing the window and enter another URL, the parsing data of which will be added to the same file below.

## What will you get

For now, you can get received next data from the website:
* Title
* Description
* Keywords
* Canonical
* H1 tag
* Tags from H2 to H6. If a tag occurs several times on the selected page, all of them will be collected in one array.

### What remains to be done

Now I have several tasks for myself:
* Rebuild the entire parser file to match the DRY concept.
* Add the ability to search for parser not only on a given page, but also on the internal pages of the site.
* Make it possible to insert several URLs at once.
* To expedite the work of the parser by implementing generators and decorators.
* To develop a GUI for it.
