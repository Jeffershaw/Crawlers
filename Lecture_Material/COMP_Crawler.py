# -*- coding:utf-8 -*-
#env: python2.7
#not sure for the correctness, at least I can run.
import urllib2
import os
import re
import urllib
import multiprocessing


def cbk(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print
    '%.2f%%' % per


def download(url, name):
    urllib.urlretrieve(url, name)


def scan(url, file_name):
    os.mkdir(base_dir + "\\" + file_name)
    os.chdir(base_dir + "\\" + file_name)

    result = urllib2.urlopen(url).read()

    pattern = re.compile(r"<tr>(.*?)</tr>", re.DOTALL)
    f_list = pattern.findall(result)

    current_folder_list = []
    for list_item in f_list:
        pattern_1 = re.compile(r"(\d\d\d\d-\d\d-\d\d \d\d:\d\d)", re.DOTALL)
        if pattern_1.search(list_item):
            pattern_2 = re.compile(r"<a href=\"(.+?)\">", re.DOTALL)
            current_folder_list.extend(pattern_2.findall(list_item))

    next_folder_list = []
    pdf_list = []

    for item in current_folder_list:
        pattern_3 = re.compile(r"pdf|ppt", re.DOTALL)
        pattern_4 = re.compile(r"/$", re.DOTALL)
        if pattern_3.search(item):
            pdf_list.append(item)
        elif pattern_4.search(item):
            next_folder_list.append(item)

    for item in pdf_list:
        # urllib.urlretrieve(url+r"/"+item,item,cbk)
        p = multiprocessing.Process(target=download, args=(url + r"/" + item, item))
        # download(url+r"/"+item,item)
        p.start()
    # p.join()

    print
    file_name

    for folder in next_folder_list:
        print
        url + folder, file_name + folder
        scan(url + folder, file_name + folder)


res_dic = {"comp323": "https://cgi.csc.liv.ac.uk/~spirakis/COMP323-Fall2017/",
           "comp329": "https://cgi.csc.liv.ac.uk/~rmw/329_info.php",
           "comp319": "https://cgi.csc.liv.ac.uk/~coopes/comp319/",
           }

base_dir = "C:\\Users\\Jeff\\desktop"
'''
os.makedirs(base_dir+"lecture")
#os.chdir("lecture")

for item in res_dic:
    result = urllib2.urlopen(res_dic[item]).read()
    #pattern = r"<tr>(.*)?<a href=\"(.+)?\">(.*)?(\d\d\d\d-\d\d-\d\d \d\d:\d\d)(.*)?</tr>"

    pattern= re.compile(r"<tr>(.*?)</tr>",re.DOTALL)
    f_list = pattern.findall(result)

    current_folder_list = []
    for list_item in f_list:
        pattern_1 = re.compile(r"(\d\d\d\d-\d\d-\d\d \d\d:\d\d)",re.DOTALL)
        if pattern_1.search(list_item):
            pattern_2 = re.compile(r"<a href=\"(.+?)\">",re.DOTALL)
            current_folder_list.extend(pattern_2.findall(list_item))
           '''
if __name__ == "__main__":
    scan(res_dic["comp319"], "comp319/")