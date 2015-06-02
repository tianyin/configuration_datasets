#!/usr/bin/python

import csv
import os

def existcheck(csvpath, dirpath):
    """
    Check if every of the file included in the csv file
    exists in the corresponding directory
    """
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  #skip the headers
        for row in csvreader:
            abp = os.path.join(dirpath, row[0])
            if os.path.exists(abp) == False:
                print '[ERROR] file does not exist:', row[0] 

existcheck('./httpd/v-2.2.x.metadata.csv', './httpd/v-2.2.x')
existcheck('./mysql/v-5.x.metadata.csv', './mysql/v-5.x')
