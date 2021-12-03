# Import neccesary libraries
import requests, urllib

# Establish download link and path
url = 'https://markets.newyorkfed.org/read?productCode=50&eventCodes=500&limit=25&startPosition=0&sort=postDt:-1&format=xlsx'
path = 'W:\Risk Control\public\CXL Uploads\Fed Funds\Search.xlsx'

# Opens Excel file and saves to established path
r = requests.get(url, allow_redirects=True)
urllib.request.urlretrieve(url, path)

print ('Fed Funds Updated Successfully')