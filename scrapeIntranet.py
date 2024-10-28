import requests #library to request access to a specific URL
from bs4 import BeautifulSoup #library that will allow me to scrape requested data

#asking which webpage to ask the request to
page = input('Enter \'main\' for main page or \'all files\' for all files page: ')

#making a request
if(page == 'all files'):
    request = requests.get('https://intranet.iiit.ac.in/offices/default/display_all_files')
else:
    request = requests.get('https://intranet.iiit.ac.in/offices')

#printing request response to see if request was successful
print(request)

#formatting the page as an html code would be parsed
parsedPage = BeautifulSoup(request.content, 'html.parser')

#function for fetching links
def extractLink():
    #opening a file to write to
    file = open('urls.txt', 'w')

    #taking input for the type of link wanted
    typeInput = input()
    
    #getting all the link Elements
    linkElements = parsedPage.find_all('a', href = True)
    
    #looping through each link
    for link in linkElements:
        #checking if it is a desired link, then writing to file
        try:
            link['href'].index(typeInput)
            file.write(link['href']+'\n')
        #if undesired(index throws an exception), just continuing
        except:
            continue

    #close the file to prevent any corruption
    file.close()

#The function to extract all the requested links    
extractLink()