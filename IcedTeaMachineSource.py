# Import necessary libraries 
import requests
import os
from datetime import date, timedelta
import datetime
import zipfile

# Get today's date
todays_date = date.today()
month = todays_date.month

# Check if month needs to be rolled back
if todays_date.day == 1:
    if datetime.datetime.today().weekday() == 0:
        priordate = date.today() - timedelta(days=3)
        daystr = priordate.day
        month = priordate.month
    else:
        priordate = date.today() - timedelta(days=1)
        daystr = priordate.day
        month = priordate.month
# Check if it is monday to get friday's file
elif datetime.datetime.today().weekday() == 0:
    priordate = date.today() - timedelta(days=3)
    daystr = priordate.day
else:
    priordate = date.today() - timedelta(days=1)
    daystr = priordate.day

# Check if date value is single digit
if len(str(daystr)) == 1:
    daystr = '0' + str(daystr)

# Update URL
url = "https://www.theice.com/publicdocs/irm_files/iceu/{}/{}/IPE{}{}F.CSV.zip".format(todays_date.year, month, month, daystr)

daypathval = todays_date.day
if len(str(daypathval)) == 1:
    daypathval = '0' + str(daypathval)

# Set path
path = "W:\Risk Control\public\TEA\{}\{}\{}{}{}".format(todays_date.year, todays_date.month, todays_date.month, daypathval, todays_date.year)
r = requests.get(url, allow_redirects=True)

# Download .zip to dated folder
open('%s\ICE.zip' % path, 'xb+').write(r.content)

# Extract file from zip
with zipfile.ZipFile('%s\ICE.zip' % path, 'r') as file:
    print(file.printdir())
    file.extractall(path)
    print('\nFile Extracted . . . ')

# Delete zip
os.remove('%s\ICE.zip' % path)
print ('\nRemoved zip . . . ')
print ('\nComplete.\n')

# print('Your content from \n {} \nhas been saved to \n {}'.format(url, path))