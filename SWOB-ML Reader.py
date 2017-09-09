from xml.dom import minidom
import itertools
import numpy as np
import csv

xmldoc = minidom.parse('filename') # Example filename: 2017-05-11-0000-CWIT-AUTO-swob.xml
itemlist = xmldoc.getElementsByTagName("identification-elements")[0].getElementsByTagName("element")
itemlista = xmldoc.getElementsByTagName("elements")[0].getElementsByTagName("element")
itemlist1 = xmldoc.getElementsByTagName("qualifier")

outfile = open('data.txt','w')
with open('data.csv', 'w', newline='') as result:
    wr = csv.writer(result)
    list_name = []  # name of data
    list_uom = []   # unit of measure for that data
    list_value = [] # the actual value

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
    # Printing the list values to a text file if necessary. This can be commented out.
    # Then writing the lists to a csv file to bring them into line
    # with the format of the Messages 11 file from Enviornment Canada.
    # If you are downloading the files at a regular pace this could save you a couple 
    # of hundered dollars down the line as you won't have to pay Environment Canada $100+
    # for more then one year of data from their archives in the same format CSV.
    # You will however have to remove the first rows of this file if you are combining
    # multiple files into one as they are just repeated lines. The only list of value
    # is the list_value as it's the one with the data in it.
    #
    
    print(list_1, list_a, list_b, file=outfile)
    wr.writerow(list_1)
    wr.writerow(list_a)
    wr.writerow(list_b) 
    
outfile.close()
result.close()
