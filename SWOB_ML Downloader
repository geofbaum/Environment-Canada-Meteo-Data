import urllib.parse
import urllib.request
import urllib3
import os
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print ("[*] Please download and install Beautiful Soup first!")
    sys.exit(0)

url = 'http://dd.weather.gc.ca/observations/swob-ml/DATE/STATIONID/'  # Put in the Date and Station ID of the data you want
                                                                      # Date Format: YYYYMMDD ID Example: CYYZ is Toronto Pearson Intl  
download_path = "Enter your valid file path"                          # Enter the folder where you want to download the files
http = urllib3.PoolManager()

#try:
i = 0
    
request = http.request('GET', url)
#html = urllib3.urlopen(request)
soup = BeautifulSoup(request.data, "lxml")
    
for tag in soup.findAll('a', href=True): #find <a> tags with href in it so you know where the urls are
   
    tag['href'] = urllib.parse.urljoin(url, tag['href'])

    # this is where we are getting the extension (splitext) from the last name of the full url
    #the splitext splits it into the filename and the extension so the [1] is for the extension
    if os.path.splitext(os.path.basename(tag['href']))[1] == '.xml':         # Search for our xml files
        current = urllib.request.urlopen(tag['href'])
        print("\n[*] Downloading: %s" %(os.path.basename(tag['href'])))

        f = open(download_path + os.path.basename(tag['href']), "wb")
        f.write(current.read())
        f.close()
        i+=1

print ("\n[*] Downloaded %d files" %(i+1))
