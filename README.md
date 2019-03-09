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
downloading the data files from the EC server, while the other code is for translating the XML format and writing it to a text file and now
CSV like the one you would get from Environment Canada. The data is now in a format similar to their files though it does not necessarily
go through the same verification process that could occur in addition to their basic quality assurance (QA) that is performed on the data 
you can get through this process. If you need the possibility of higher QA is necessary you can still pay for their data though it is not 
necessarily true that the data you recieve has gone through any better QA. Also for obvious reasons, you the user must verify 
the data and do any additional QA that you see fit or is neccessary. This is raw data and should not be used for any legal proceedings and 
is not admissible in court. If you require something along those lines you'll have to pay Environment Canada for it.

For information regarding what the different header names represent please see the file Header_Information.txt that is available in this
repo.

Current format (minus the '-' marks) of the data is as such for the meteorological data:
Header name - Unit of Measurement - Value - QA Summary (if available) - QA Unit of Measure (it is unitless) - QA Value


<h4>Due to a planned update coming for the operational data I will be working to update this repostiory to make sure any new information is
  accounted for and that these scripts still work. As of March 8, 2019, the downloading and parsing of the data in the new format should still 
  be accurate, however the location of the data in the output files may change, the header/column names being passed may be changed, data may 
  no longer be in the new format, or additional data is likely to be present. I will do my best to go through and make note of these changes 
  for anyone who might be using these for their own use. Cheers!</h4>
