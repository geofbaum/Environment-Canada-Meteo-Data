from xml.dom import minidom
import itertools
import numpy as np
import csv

xmldoc = minidom.parse('2017-05-11-0000-CWIT-AUTO-swob.xml')
itemlist = xmldoc.getElementsByTagName("identification-elements")[0].getElementsByTagName("element")
itemlista = xmldoc.getElementsByTagName("elements")[0].getElementsByTagName("element")
itemlist1 = xmldoc.getElementsByTagName("qualifier")
#print(len(itemlist))  #Prints out the amount of values (i.e. length) in the list
#print(itemlist[0].attributes['value'].value) # Just prints through the list that fall under the value category.

outfile = open('data.txt','w')
with open('data.csv', 'w', newline='') as result:
    wr = csv.writer(result)

    for element in itemlist:
        print(element.attributes['name'].value , element.attributes['uom'].value , element.attributes['value'].value, file=outfile)
        wr.writerow([element.attributes['name'].value]+[element.attributes['uom'].value]+[element.attributes['value'].value])
    for element, qualifier in itertools.zip_longest(itemlista, itemlist1):
        if qualifier is not None:
            print(element.attributes['name'].value , element.attributes['uom'].value , element.attributes['value'].value , qualifier.attributes['name'].value , qualifier.attributes['uom'].value , qualifier.attributes['value'].value, file=outfile)
            wr.writerow([element.attributes['name'].value]+[element.attributes['uom'].value]+[element.attributes['value'].value]+[qualifier.attributes['name'].value]+[qualifier.attributes['uom'].value]+[qualifier.attributes['value'].value])
        else:
            print(element.attributes['name'].value , element.attributes['uom'].value , element.attributes['value'].value, file=outfile)
            wr.writerow([element.attributes['name'].value]+[element.attributes['uom'].value]+[element.attributes['value'].value]) 
        
outfile.close()
result.close()
