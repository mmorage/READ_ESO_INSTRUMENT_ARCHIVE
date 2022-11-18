#!/usr/bin/env python

import re 
from mechanize import Browser
import requests

br = Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False) # Ignore robots.txt
br.set_handle_refresh(False)  # can sometimes hang without this
# Google demands a user-agent that isn't a robot
#br.addheaders = [('User-agent', 'Firefox')]
 

br.open("http://archive.eso.org/wdb/wdb/adp/phase3_main/form")
print br.title()
response = br.response()

forms = list(br.forms())
form= forms[0]   #USEFULL !!!!!
print form

br.form = list(br.forms())[0]

#WRITE THE ESO INSTRUEMT HERE:

#br["ins_id"]=["MUSE"]
br["ins_id"]=["FORS2"]
#br["ins_id"]=["HAWKI"]
#br["ins_id"]=["FEROS"]
#br["ins_id"]=["KMOS"]

#N of rows returned by the archive. If the row number is big, the script might take some time. 50 is OK.

br["max_rows_returned"]="50"


br["wdbo"]=["csv/download"]
response=br.submit()

a=response.read()

r = requests.get('http://archive.eso.org/wdb/jslib/jqueryui/1.10.2/themes/ui-lightness/jquery-ui.css')



br.open('http://archive.eso.org/wdb/wdb/adp/phase3_main/query?collection_name=MUSE&version=&object=&order_main=wavelmin%2Cfilter%2Cexp_start%2Cexptime%2Corigfile&top=100')
aa = br.response()
print aa
#file=open("MUSE_CUBES.html",'w')
#file.write(aa)
#file.close()

print a
br.back()  


print br.form
