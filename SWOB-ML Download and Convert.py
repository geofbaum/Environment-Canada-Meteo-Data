import urllib.parse
import urllib.request
import urllib3
import os
import sys
from xml.dom import minidom
import itertools
import numpy as np
import csv
import datetime
from pathlib import Path


def download_meteo(date, station, path):
    # Script to download xml files from Environment Canada web server for a specific date and station into a local folder.
    date = date
    station = station
    download_path = path

    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print ("[*] Please download and install Beautiful Soup first!")
        sys.exit(0)

    url = 'http://dd.weather.gc.ca/observations/swob-ml/'+date+'/'+station+'/'
    http = urllib3.PoolManager()

    #try:
    i = 0
    
    request = http.request('GET', url)
    soup = BeautifulSoup(request.data, "lxml")
    
    for tag in soup.findAll('a', href=True): #find <a> tags with href in it so you know it si for urls
        #so that if it doesn't contain the full url it can ? the url itself to it for the download
        tag['href'] = urllib.parse.urljoin(url, tag['href'])

        # this is where we are getting the extension (splitext) from the last name of the full url
        #the splitext splits it into the filename and the extension so the [1] is for the extension
        if os.path.splitext(os.path.basename(tag['href']))[1] == '.xml':
            current = urllib.request.urlopen(tag['href'])
            f_path = download_path + os.path.basename(tag['href'])
            # Check to see if file from server already exists on local drive
            if not os.path.exists(f_path):
                print("\n[*] Downloading: %s" %(os.path.basename(tag['href'])))
                f = open(download_path + os.path.basename(tag['href']), "wb")
                f.write(current.read())
                f.close()
                i+=1
            else:
                #print("\n[*] Already Downloaded: %s" %(os.path.basename(tag['href'])))
                continue

    print (("\n[*] Downloaded %d files" %(i)),station, date)
    
def convert_toTxt(directory):
    #
    # Script to convert all of the xml files in folder into text files.
	# Creates a text file for every xml file that is present in the folder.
	# Not necessary to do this if you just want the daily csv.
    #

    directory = directory
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".xml"):
                xmldoc = minidom.parse(os.path.join(directory + file))
                itemlist = xmldoc.getElementsByTagName("identification-elements")[0].getElementsByTagName("element")
                itemlista = xmldoc.getElementsByTagName("elements")[0].getElementsByTagName("element")
                itemlist1 = xmldoc.getElementsByTagName("qualifier")                       
                name = os.path.splitext(os.path.basename(file))[0]            
                filename = os.path.join(directory + name + ".txt")
                outfile = open(filename,'w')
                for element in itemlist:
                    #add if statement here to only write the name and uom values if the file has the 0000 hour in it or is the first file in the list
                    print(element.attributes['name'].value , element.attributes['uom'].value , element.attributes['value'].value, file=outfile)
                for element, qualifier in itertools.zip_longest(itemlista, itemlist1):
                    if qualifier is not None:
                        print(element.attributes['name'].value , element.attributes['uom'].value , element.attributes['value'].value , qualifier.attributes['name'].value , qualifier.attributes['uom'].value , qualifier.attributes['value'].value, file=outfile)
                    else:
                        print(element.attributes['name'].value , element.attributes['uom'].value , element.attributes['value'].value, file=outfile)
                outfile.close()

def convert_toCSV(directory, date):
    #
    # Script to convert and merge all of the xml files in folder into a single csv file
    #
    directory = directory
    date = date
    for root,dirs,files in os.walk(directory):
        for file in files:
            if file.endswith(".xml"):
                xmldoc = minidom.parse(os.path.join(directory + file))
                itemlist = xmldoc.getElementsByTagName("identification-elements")[0].getElementsByTagName("element")
                itemlista = xmldoc.getElementsByTagName("elements")[0].getElementsByTagName("element")
                itemlist1 = xmldoc.getElementsByTagName("qualifier")                       
                name = "CWIT_"+date            
                filename = os.path.join(directory + name + ".csv")
                with open(filename, 'a', newline='') as result:
                    wr = csv.writer(result)
                    list_name = []
                    list_uom = []
                    list_value = []         
                    for element in itemlist:
                        list_value.append(element.attributes['value'].value)
                        #add if statement here to only write the name and uom values if the file has the 0000 hour in it or is the first file in the list
                        #print(element.attributes['name'].value , element.attributes['uom'].value , element.attributes['value'].value, file=outfile)
                        #wr.writerow([element.attributes['name'].value]+[element.attributes['uom'].value]+[element.attributes['value'].value])
                    for element, qualifier in itertools.zip_longest(itemlista, itemlist1):
                        if qualifier is not None:
                            list_value.append(element.attributes['value'].value)
                            list_value.append(qualifier.attributes['value'].value)
                        else:
                            list_value.append(element.attributes['value'].value)

                    wr.writerow(list_value)
                
                    result.close()

def create_fldrs(month, stations, main_dir):
    month = month
    stations = stations
    main_dir = main_dir
    for station in stations:
        for date in date_list:
            path_dir = main_dir+station+"\\"                            # path to folder for each station
            path_month = main_dir+station+month                         # path to folder for each month within each stations folder
            path = main_dir+station+month+date.strftime('%Y%m%d')+"\\"  # path to folder for each date in the date list within each month folder and station folder
            my_file = Path(path)
            if my_file.exists():
                # file exists
                print("Directory already exists", path)
                continue
            else:
                print("File or Directory Doesn't Exist, we should then create it...")
                # Check to see if Station Directory Exists, if it does not create it
                if not os.path.exists(path_dir):
                    os.mkdir(path_dir)
                    # Check to see if Month directory exists, if it doesn't create it
                    if not os.path.exists(path_month):
                        os.mkdir(path_month)
                    else:
                        continue
                
                # After checking to see if the station and month directories are there
                # It should then be safe to create the directory related to the date  
                os.mkdir(path)
                print("Directory ", path, " Created ")

#
# Main Short Component of script
#
#

#sets the variable "today" as the datetime object.
today = datetime.datetime.today()
date_list = [today - datetime.timedelta(days=x) for x in range(1, 8)] # This will create a list of dates from yesterday to seven days ex. if today was Jan 8th,
                                                                      # the list would be of Jan 7th to Jan 1st. I chose a list of 7 days because I normally
                                                                      # download data once a week so obviously this could be changed to go back a longer or shorter
                                                                      # amount of time to check for and download the files.
i = 0
month = "\\Mars 2019\\"
stations = ['CWIT',       # Ste-Clotilde, QC
            'CYUL',       # Montreal/Trudeau International
            'CWTQ',       # MONTREAL/PIERRE ELLIOTT TRUDEAU INTL -- Has Hourly and 1-min data
            'CWTA',       # McTavish -- Has Hourly and 1-min data
            'CWVQ',       # Ste-Anne-De-Bellevue 1 -- Has Hourly and 1-min data
            'CWIZ']       # L'Acadie -- Has Hourly and 1-min data


main_dir = "C:\\Users\\geoffrey\\Downloads\\Donnes Meteo\\"

create_fldrs(month, stations, main_dir)

for station in stations:
    for date in date_list:
        directory = main_dir+station+month+date.strftime('%Y%m%d')+"\\"
        #print(directory)
        download_meteo(date.strftime('%Y%m%d'),station,directory)
        convert_toTxt(directory)
        convert_toCSV(directory,date.strftime('%Y%m%d'))
