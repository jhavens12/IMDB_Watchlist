import json
import pprint
import sys
import os
import subprocess
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

timestamp = datetime.now()

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('IMDB_Watchlist').sheet1
time = datetime.now()
title = input("Title? ")
print()
comment = input("Whats your comment? ")
print()
print("1 - Really Looks Good")
print("2 - Could Be Interesting")
print("3 - Someone Told Me About It")
print("4 - Future Sequel Type")
print("5 - Found Online Somewhere")
print()

rating = input("Rating? ")
print()

url = sys.argv[1]
print(url)
split_url = url.split('/')

movie_id = split_url[4].split('tt')[1]

report_line = [timestamp,title,"imdb:"+split_url[4],rating,comment,url]
sheet_data = sheet.get_all_values()
row = str(len(sheet_data)+1)
range_build = 'A' + row + ':F' + row
cell_list = sheet.range(range_build)

# Update values
for cell,data in zip(cell_list,report_line):
    cell.value = data

print("Updating Sheet...")

# Send update in batch mode
sheet.update_cells(cell_list)
print("DONE!")
