#!/bin/python3
#taking import or library
import os,sys
import time
import requests
import argparse
import random
#functions for letter work
os.system("clear")
"""
parser = argparse.ArgumentParser()
parser.add_argument("-fn" ,"--fname" , help = "Frist name",metavar = "<fname>")
parser.add_argument("-mn","--mname",help = "Middle or Second name:",metavar = "<mname>")
parser.add_argument("-ln","--lname",help = "Last name",metavar = "<lname>")
parser.add_argument("-d","--date",help = "Birth day",metavar = "<date>")
parser.add_argument("-m","--month" ,help = "Birth month",metavar = "<month>")
parser.add_argument("-y","--year" ,help = "Birth year",metavar = "<year>")
parser.add_argument("-cn","--cname" ,help = "Crush name",metavar = "<cname>")
parser.add_argument("-cnl","--clname",help = "crush last name",metavar = "<clname>")
parser.add_argument("-pn","--number",help = "Phone number",metavar = "<phnumber>")
parser.add_argument("-kw","--key",help = "Keywords" ,metavar = "<kw>")
args = parser.parse_args()
os.system("clear && python banner.py")
parser.print_help()
global fn,ln,tn,d,m,y,cn,cnl,pn,kw
fn = args.fname
ln = args.mname
tn = args.lname
d = args.date
m = args.month
y = args.year
cn = args.cname
cnl = args.clname
pn = args.phnumber
kw = args.kw
"""
global banner
banner = """
$$$$$$$\   $$$$$$\  $$$$$$$\  $$\   $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |$$  / 
$$ |  $$ |$$ |  $$ |$$$$$$$  |$$$$$  /  
$$ |  $$ |$$ |  $$ |$$  __$$< $$  $$<   
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$\  
$$$$$$$  | $$$$$$  |$$ |  $$ |$$ | \$$\ 
\_______/  \______/ \__|  \__|\__|  \__|
created by DarkPhinix
version 3.0
"""
def PBF():
    colors = ["\033[1;31m","\033[1;33m","\033[1;35m","\033[1;34m","\033[0;31m","\033[1;36m","\033[0m"]
    print(random.choice(colors)+banner)
    #Thare user give info of victim and program send it on a file.
    fn=input( "Enter Victim First Name:")
    ln=input( "Enter Victim Last Name:")
    tn=input( "Enter Victim 3rd Name:")
    d=input("Enter day:")
    if len(d) == 2:
        m=input( "Enter month:")
    else:
        print("You want to give 2 words Ex:01")
        d = input( "Enter day:")
        m = input( "Enter month:")
    y=input( "Ented year:")
    cn=input( "Enter Crush/GF/BF Name:")
    cnl=input( "Enter Crush/GF/BF Last Name:")
    pn=input( "Enter Number:")
    kw=input("Enter any keyword about victim:")
    fnn=fn+".txt"
    fno = "/data/data/com.termux/files/home/DORKLIN/"+fn+".txt"
    if os.path.exists(fno) != False:
        print(fn+".txt file are already exists")
        print("File are auto removed and creat again")
        os.system("rm "+fn+".txt")
        p = open(fn+".txt","a")
    else:
        p = open(fn+".txt","a")
    os.system("clear")
    print(banner)
    print("Full name:"+fn+" "+ln+" "+tn)
    print("Barth Date:"+d+"-"+m+"-"+y)
    print("Third Party name:"+cn+" "+cnl)
    if pn[0] == "0":
        print("Phone number:"+"+88"+pn)
    else:
        print("Phone number:"+pn)
    print("Keywords:"+kw)
    time.sleep(4)
    fnd = "Full name:"+fn+" "+ln+" "+tn
    lnd = "Birth Date:"+d+"-"+m+"-"+y
    lsnd = "Crush/GF/BF:"+cn+" "+cnl
    kyw = "Keyword:"+kw
    hist = open("History","a")
    hist.write(fnd +"\n")
    hist.write(lnd +"\n")
    hist.write(lsnd +"\n")
    if pn[0] == "0":
        hist.write("Victim number:"+"+88"+pn+"\n")
    else:
        hist.write("Victim number:"+pn+"\n")
    hist.write(kyw+"\n"+"------------------------------------"+"\n")
    hist.close()
    #password are making on there
    p.write(fn+"123" "\n")
    p.write(fn+"1234" "\n")
    p.write(fn+"12345" "\n")
    p.write(fn+"777" "\n")
    p.write(fn+"768" "\n")
    p.write(fn+"111" "\n")
    p.write(fn+"222" "\n")
    p.write(fn+"333" "\n")
    p.write(fn+"444" "\n")
    p.write(fn+"555" "\n")
    p.write(fn+"666" "\n")
    p.write(fn+"888" "\n")
    p.write(fn+"999" "\n")
    p.write(fn+"000" "\n")
    p.write(fn+"567" "\n")
    p.write(fn+"678" "\n")
    p.write(fn+"789" "\n")
    p.write(fn+"890" "\n")
    p.write(fn+"345" "\n")
    p.write(fn+"1111" "\n")
    p.write(fn+"2222" "\n")
    p.write(ln+"123" "\n")
    p.write(ln+"1234" "\n")
    p.write(ln+"12345" "\n")
    p.write(ln+"111""\n")
    p.write(ln+"000" "\n")
    p.write(ln+"222" "\n")
    p.write(ln+"333" "\n")
    p.write(ln+"444" "\n")
    p.write(ln+"555" "\n")
    p.write(ln+"666" "\n")
    p.write(ln+"777" "\n")
    p.write(ln+"888" "\n")
    p.write(ln+"999" "\n")
    p.write(ln+"1111" "\n")
    p.write(ln+"2222" "\n")
    p.write(ln+"3333" "\n")
    p.write(ln+"4444" "\n")
    p.write(ln+"5555" "\n")
    p.write(ln+"6666" "\n")
    p.write(ln+"7777" "\n")
    p.write(ln+"8888" "\n")
    p.write(ln+"9999" "\n")
    p.write(ln+"0000" "\n")
    p.write(tn+"123" "\n")
    p.write(tn+"1234" "\n")
    p.write(tn+"12345" "\n")
    p.write(tn+"000" "\n")
    p.write(tn+"111" "\n")
    p.write(tn+"222" "\n")
    p.write(tn+"333" "\n")
    p.write(tn+"444" "\n")
    p.write(tn+"555" "\n")
    p.write(tn+"666" "\n")
    p.write(tn+"777" "\n")
    p.write(tn+"888" "\n")
    p.write(tn+"999" "\n")
    p.write(tn+"1111" "\n")
    p.write(tn+"2222" "\n")
    p.write(tn+"3333" "\n")
    p.write(tn+"4444" "\n")
    p.write(tn+"5555" "\n")
    p.write(tn+"6666" "\n")
    p.write(tn+"7777" "\n")
    p.write(tn+"8888" "\n")
    p.write(tn+"9999" "\n")
    p.write(tn+"786" "\n")
    p.write(tn+"890" "\n")
    p.write(tn+fn+ln+"\n")
    p.write(fn+ln+tn+"\n")
    p.write(ln+fn+tn+"\n")
    p.write(ln+tn+fn+"\n")
    p.write(fn+ln+tn+"\n")
    p.write(ln+cn+cnl+"\n")
    p.write(cn+ln+cnl+"\n")
    p.write(d+m+y+"\n")
    p.write(m+d+y+"\n")
    p.write(y+d+m+"\n")
    p.write(d+y+m+"\n")
    p.write(m+y+d+"\n")
    p.write(y+m+d+"\n")
    p.write(y+d+m+"\n")
    p.write(cn+"123" "\n")
    p.write(cn+"1234" "\n")
    p.write(cn+"12345" "\n")
    p.write(cn+"786" "\n")
    p.write(cn+"999" "\n")
    p.write(cn+"111" "\n")
    p.write(cn+"222" "\n")
    p.write(cn+"333" "\n")
    p.write(cn+"444" "\n")
    p.write(cn+"555" "\n")
    p.write(cn+"666" "\n")
    p.write(cn+"777" "\n")
    p.write(cn+"888" "\n")
    p.write(cnl+"123" "\n")
    p.write(cnl+"1234" "\n")
    p.write(cnl+"12345" "\n")
    p.write(cnl+"786" "\n")
    p.write(cnl+"999" "\n")
    p.write(cnl+"111" "\n")
    p.write(cnl+"222" "\n")
    p.write(cnl+"333" "\n")
    p.write(cnl+"444" "\n")
    p.write(cnl+"555" "\n")
    p.write(cnl+"666" "\n")
    p.write(cnl+"777" "\n")
    p.write(cnl+"888" "\n")
    p.write(cnl+"999" "\n")
    p.write(pn+"\n")
    p.write(pn[:6]+"\n")
    p.write(pn[-6:]+"\n")
    p.write(pn[-7:]+"\n")
    p.write(pn[:7]+"\n")
    p.write(pn[:8]+"\n")
    p.write(pn[-8:]+"\n")
    p.write(pn[:9]+"\n")
    p.write(pn[-9:]+"\n")
    p.write(pn[:10]+"\n")
    p.write(pn[-10:]+"\n")
    p.write(kw+"\n")
    p.write(fn+kw+"\n")
    p.write(ln+kw+"\n")
    p.write(tn+kw+"\n")
    p.write(cn+kw+"\n")
    p.write(cnl+kw+"\n")
    p.close()
    hl = open(fn+".txt","r")
    passw = hl.readlines()
    for line in passw:
        print("\033[1;33mPassword are saving on "+fn+".txt :","\033[1;31m" + line)
        time.sleep(0000.1)
        os.system("clear")
    print(banner)
    fni=input("Do you want Brute Force right now:")
    if "y" == fni:
        #if y so start brute force
        os.system(" python3 DarkPBF.py")
        #or else so just save this file
    else:
        print("Passlist are created as",fn+".txt")
        print("Total "+format(len(passw))+" password are saved in "+fn+".txt")
    Lm = input("Do you want leetmode:")
    if Lm == "y":
        f = open(fn+".txt","r")
        fd = f.read()
        n = fd
        f.close()
        rep = fd.replace("a" or "A" , "4").replace("b" or "B" ,"8").replace("c" or "C" ,"(").replace("d" or "D" ,"9").replace("e" or "E" ,"3").replace("g" or "G" ,"6").replace("i" or "I" ,"!").replace("l" or "L" ,"1").replace("o" or "O" ,"0").replace("s" or "S" ,"5").replace("t" or "T" ,"7").replace("z" or "Z" ,"2")
        op = open(fn+"1337.txt","w")
        op.write(rep)
        op.close()
        oh = open(fn+"1337.txt","r")
        passwo = oh.readlines()
        for lline in passwo:
            print("\033[1;33mPassword are saving on "+fn+"1337.txt :","\033[1;31m" + lline)
            time.sleep(0000.1)
            os.system("clear")
        print(banner)
        print("Passlist created as ",fn+"1337.txt")
        print("\033[1;31mTotal "+format(len(passwo))+ " are saved in "+fn+".1337.txt")
PBF()
#file end
