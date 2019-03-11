# Environment-Canada-Meteo-Data
Some files to download the Hourly Meteorological Data that is stored on the Environment Canada (EC) server for free for 30 days. 
It offers the ability to have access to data that is not regularly needed by the general public but could be for Meteorologists 
or anyone who needs to more specific weather data then is available through the the regular EC Historical Data portal. The script 
that is written to read in the data files is specific to the XML format used for the SWOB-ML files. A User Guide in PDF format is 
available in both English and French from the following link as well as other pertinent information:
<br>
<br>
http://dd.weather.gc.ca/observations/doc/
<br>
<br>
Please also remember that by downloading and using the data provided by EC you are entering into an agreement with EC regarding the 
use of that data. PLease see file LICENCE_GENERAL.txt for a copy of the current data licence file that is stored on the EC server
at this link: 
<br>
<br>
http://dd.weather.gc.ca/doc/
<br>
<br>
There are three main files in this repository, two of which labeled with Simple at the end of the filename are the original basic
versions of the code that I created to download, and translate/parse the XML files to text and CSV files. The third file is an updated
set of code that combines the main parts of the previous two while adding some additional features which I'll try to detail below.
In each case of creating the text or CSV file the output will be similar to the CSV file (Messages 11) that can be purchased from
Environment Canada of the archived historical data. The data is now in a format similar to their files though it does not necessarily
go through the same verification process that occurs in addition to their basic quality assurance (QA) that is performed on the data 
you can get through this process. If you need the higher level of QA, want data that is processed or analaysed further or need data that 
can be used in legal proceedings you will need to purchase the data from Environment Canada. Here is a link the current pricing for
the climate data.
<br>
<br>
http://climate.weather.gc.ca/new_price_announce_e.html
<br>
<br>
Also for obvious reasons, you the user must verify the data and do any additional QA that you see fit or is neccessary for your
purposes. This is raw data and should not be used for any legal proceedings and is not admissible in court.
<br>
<br>
Discussion of purpose of each of the main three files:
<br>
<br>
<b>SWOB-ML Downloader Simple.py</b>
- Downloads all the available XML files for one specific station for one day. Both of which are hardcoded into these examples
<br>

<b>SWOB-ML Reader Simple.py</b>
- Converts the XML files to a single CSV file
- In this example it would be a CSV file for the single day of data that was downloaded previously.

<br>
<b>SWOB-ML Download and Convert.py</b>

- User has the option to hardcode a list of the station IDs that they want to download data from.
- A list of dates is created starting from the day before the current one and going back seven days.
- Using the list of dates and list of stations, the first function checks to see if folders are present on the local drive for the data
  and if they are not, they are created.
- The next function that is called is a modified version of the code from the Downloader Simple file. Data is downloaded for each 
  station and day if it hasn't already been downloaded.
- The third and fourth functions are modified versions of the code from the Reader Simple file. With the third function, a text file 
  is created for each XML file present in the folder. This is not necessary if you just want the combined data in CSV format. The fourth
  function is the code that combines the data from the XML files into a CSV formatted file. Unlike the original Reader code, there is no
  header being written to the file for the data.
<br>

<br>
For information regarding what the different header names represent please see the file Header_Information.txt that is available in this
repo. There is also a pdf available detailing the differences between the older format and the new header format. This will give you
an idea of what was added or what was changed with the newer version of the data. Most of the changes are simply naming differences and
location in the file. However, there are also around 16 new values present in the file in addition to data flags for some of the data
that were present previously. In total with new data and data flags there are nearly 30 additional values present. Please take the time
to look at the pdf to see the changes and how they might affect your previous datasets. I will be updating the Header Information text
file with the new headers shortly and will keep a copy of the old version here for at least the forseeable future in case users of the
older data need to look up the older format. <br>
<br>
Current format (minus the '-' marks) of the data is as such for the meteorological data:<br>
Header name - Unit of Measurement - Value - QA Summary (if available) - QA Unit of Measure (it is unitless) - QA Value<br>
<br>
<br>
<h4>Due to a planned update coming for the operational data I will be working to update this repostiory to make sure any new information is
  accounted for and that these scripts still work. As of March 8, 2019, the downloading and parsing of the data in the new format should still 
  be accurate, however the location of the data in the output files may change, the header/column names being passed may be changed, data may 
  no longer be in the new format, or additional data is likely to be present. I will do my best to go through and make note of these changes 
  for anyone who might be using these for their own use. Cheers!</h4>
