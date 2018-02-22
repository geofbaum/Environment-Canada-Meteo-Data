from xml.dom import minidom
import itertools
import numpy as np
import csv

xmldoc = minidom.parse('filename') # Example filename: 2017-05-11-0000-CWIT-AUTO-swob.xml
itemlist = xmldoc.getElementsByTagName("identification-elements")[0].getElementsByTagName("element")
itemlista = xmldoc.getElementsByTagName("elements")[0].getElementsByTagName("element")
itemlist1 = xmldoc.getElementsByTagName("qualifier")

# allow option to print to text file instead or in addition to the CSV file
# outfile = open('data.txt','w')

with open('data.csv', 'w', newline='') as result:   # You may want to change this every time you run it or make sure that you save
    wr = csv.writer(result)                         # the data.csv file as another name after you have everything set up to your
                                                    # liking.
    list_name = []      # name of data                  
    list_uom = []       # unit of measure for that data
    list_value = []     # the actual observation data

    for element in itemlist:
        list_name.append(element.attributes['name'].value)
        list_uom.append(element.attributes['uom'].value)
        list_value.append(element.attributes['value'].value)
        #print(element.attributes['name'].value , element.attributes['uom'].value , element.attributes['value'].value, file=outfile)
    for element, qualifier in itertools.zip_longest(itemlista, itemlist1):
        if qualifier is not None:
            list_name.append(element.attributes['name'].value)
            list_uom.append(element.attributes['uom'].value)
            list_value.append(element.attributes['value'].value)
            list_name.append(qualifier.attributes['name'].value)
            list_uom.append(qualifier.attributes['uom'].value)
            list_value.append(qualifier.attributes['value'].value)
        else:
            list_name.append(element.attributes['name'].value)
            list_uom.append(element.attributes['uom'].value)
            list_value.append(element.attributes['value'].value)
    
    #
    # Printing the list values to a text file if necessary. This is currently commented out.
    # Then writing the lists to a csv file to bring them into line
    # with the format of the Messages 11 file from Enviornment Canada.
    # If you are downloading the files at a regular pace this could save you a couple 
    # of hundered dollars down the line as you won't have to pay Environment Canada $100+
    # for more then one year of data from their archives in the same format CSV.
    # Obviously this is not the exact same format as those CSV files and the data that you
    # pay for may have gone through more data quality verification.
    #
    # You will however have to remove the first rows of this file if you are combining
    # multiple files into one as that is the header line. The list called list_value
    # is the one of importance as it's the one with the actual data in it. List
    #
    
    print(list_name, list_uom, list_value) #, file=outfile)
    wr.writerow(list_name)
    wr.writerow(list_uom)
    wr.writerow(list_value) 
    
#outfile.close()
result.close()
