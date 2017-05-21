# Environment-Canada-Meteo-Data
Some files to download the Hourly Meteorological Data that is stored on the Environment Canada (EC) server for free for 30 days. 
It offers the ability to have access to data that is not regularly needed by the general public but could be for Meteorologists 
or anyone who needs to more specific weather data then is available through the the regular EC Historical Data portal. The script 
that is written to read in the data files is specific to the XML format used for the SWOB-ML files. A User Guide in PDF format is 
available in both English and French from the following link as well as other pertinent information:
http://dd.weather.gc.ca/observations/doc/

Please also remember that by downloading and using the data provided by EC you are entering into an agreement with EC regarding the 
use of that data. PLease see file LICENCE_GENERAL.txt for a copy of the current data licence file that is stored on the EC server
at this link: http://dd.weather.gc.ca/doc/

The two main files in this repository are for two seperate purposes but could easily be combined if need be. The one set of code is for
downloading the data files from the EC server, while the other code is for translating the XML format and writing it to a text file.

My likely next step is to configure it to write to a csv file and have all of the data write across one single row so that the data would
be in a format similar to the files that you can download from EC as far as the standard meteorological data or that you can pay to 
recieve if it is this higher level meteorological data.

For information regarding what the different header names represent please see the file Header_Information.txt that is available in this
repo.

Current format (minus the '-' marks) of the data is as such for the meteorological data:
Header name - Unit of Measurement - Value - QA Summary (if available) - QA Unit of Measure (it is unitless) - QA Value
