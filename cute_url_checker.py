##!/bin/python3
##script usage: cat file_with_urls | python3 url.py > output.txt
import requests #for making the http/GET requests
import fileinput #for accepting stdin input (file.txt with www.website.com) cat file.txt | python3 url.py

##http status reply code lists, all webpage responses with one of these codes will be considered to be "alive".
HTTP_S = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226] #http_succes_codes
HTTP_R = [300, 301, 302, 303, 304, 305, 306, 307, 308] #http_redirection_codes
HTTP_F = [401, 402, 403] #http_forbidden_codes

for line in fileinput.input(): #for each line in input file:
	url = (str(line).strip("\n")) #url is the line without "\n"
	try:
		r = requests.get(url, allow_redirects=True) #try requesting and
		if r.status_code in HTTP_S or HTTP_R or HTTP_F: #- try reading and checking status code
			print (url) #if ok print "alive url"
	except Exception: #any other case gets discarded
		pass #ditch error into the abyss

#⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕
#⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕
#⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱
#⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀
#⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗
#⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕
#⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵
#⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿
#⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁
#⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈
#oh! You have actually read my code!?
#hope you like it... script is kept easy for automation

#how should an input file look for this script?
	#a "webpage url file" should look like this:
		#https://github.com
		#https://www.github.com
		#http://www.github.com
		#http://github.com
		#http://githubasdasd.com
	#only http:// and https:// web urls can be checked, an url without https:// like github.com will not work.
