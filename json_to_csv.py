#! /usr/bin/env python3.10
import json
from datetime import datetime


def json_to_csv(file_path, csv_file):
    with open(file_path) as json_file_local:
        data = json.load(json_file_local)
        write_to_csv = open(csv_file, 'a')
        index = 0
        while index < len(data['values']):
            # Platform
            platform = data['values'][index]['properties']['platform']
            
            # Name
            name = data['values'][index]['name']
            
            # IP/CIDR
            ip = data['values'][index]['properties']['addressPrefixes']
            
            for i in ip:
                write_to_csv.write(f"Public_IPs.{platform},{name},{i},Version: {datetime.now().strftime('%B')}, Default Domain\n")
            
            index += 1
        write_to_csv.close()
            
                
if __name__ == '__main__':
    import sys
    import pathlib
    
    try:
        file_path = sys.argv[1]
        csv_file = sys.argv[2]
    
    except IndexError:
        sys.exit('Two arguments needed, JSON file and csv file name.')
    
    with pathlib.Path(file_path) as json_file_global:
        if json_file_global.is_file():
            json_to_csv(file_path,csv_file)
        else:
            sys.exit(f"Did not find {file_path}")    