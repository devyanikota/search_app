import os
import sys
import requests
import json
import time
import pdb
import collections


def json_log():
    pathname = os.path.dirname(sys.argv[0])
    fullpath = os.path.abspath(pathname)
    listof_files = []
    location_list = []
    big_list = collections.defaultdict(list)
    start_time = time.time()
    i = 0
    fout = open("test.json", 'w')
    for dirname, dirnames, filenames in os.walk('.'):
        for subdirname in dirnames:
            os.path.join(dirname, subdirname)
        for filename in filenames:
            location = os.path.join(dirname, filename)
            location_list.append(location)
            file_name = filename
            s = tuple(file_name)
            r = []
            for size in range(1, len(s)+1):
                for index in range(len(s)+1-size):
                    x = file_name[index:index+size]
                    big_list[x].append(i)
            i = i + 1
    k = 1
    while k != 0:
        g = raw_input("enter the name of the file ")
        if g == "stop":
            break
        if g in big_list:
            n = big_list[g]
            l = 0
            for v in n:
                l = location_list[v]
                l = l[1:]
                print fullpath + l

if __name__ == "__main__":
    json_log()
