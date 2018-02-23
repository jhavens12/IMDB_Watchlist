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

comment = input("Whats your comment? ")

url = sys.argv[1]
split_url = url.split('/')

report_line = [timestamp,url,split_url[4],comment]

sheet_data = sheet.get_all_values()

row = str(len(sheet_data)+1)

range_build = 'A' + row + ':D' + row

cell_list = sheet.range(range_build)

# Update values
for cell,data in zip(cell_list,report_line):
    cell.value = data

# Send update in batch mode
sheet.update_cells(cell_list)
