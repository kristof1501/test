print("alma")
# fh = open("sms.txt")
# lines = fh.readlines()
# max = 0
# id = 0
# for i in range(1,len(lines[1:])+1):
#     if i % 2 == 0:
#         current = len(lines[i])
#         print(i, lines[i], current,max)
#         if current > max:
#             max = current
#             id = i
#
# a = lines[id-1].strip()
# print("max:\n{0}\n{1}".format(a,lines[id].strip()))
#
# sms_number = 0
# director = set()
# hour = int(lines[1].split()[0])
# for i in range(1,len(lines[1:])+1):
#     if i % 2 != 0:
#         print(lines[i].split()[0:2])
#         print(hour)
#         if lines[i].split()[0] == str(hour):
#             sms_number += 1
#             print(sms_number)
#             if sms_number > 1:
#                 director.add(hour)
#             # if lines[i+1].split()[0] != str(hour):
#             #     hour += 1
#             #     sms_number = 0
#         else:
#             hour = int(lines[i].split()[0])
#             sms_number = 1
#
# print(director)


# x = "abcdefghij"
# if len(x) > 10:
#     print(x[0:10],end="...")
# else:
#     print(x)

# import re
#
# x = "salma sreba s  , \ndssadaals kkks al."
# a = 0
# b = len(x)
#
# print(re.subn("al","00",x))
# print(re.escape("""\\\\\\\\"""))
# print(re.search("s",x))
#
#
# while True:
#     m = re.compile("s+")
#     y = m.search(x,a)
#
#     if y == None:
#         break
#     print(y)
#     print(y.group())
#
#     a = y.end()
# print(y)
# print("alma")
# input()

# sec = 31536001
# évek,maradék = divmod(sec,(60*60*24*365))
# honapok,maradék = divmod(maradék,(60*60*24*30))
# napok,maradék = divmod(maradék,(60*60*24))
# orak,maradék = divmod(maradék,(60*60))
# percek,maradék = divmod(maradék,60)
# print(évek,honapok,napok,orak,percek,maradék)


# n = 2000
#
# if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
#     print("igen")
# else:
#     print("nem")

# print(divmod(8,4))
# x,y = divmod(8,3)
# print(x,y)
# def solution(mp):
#     year = mp //(60*60*24*365)
#     time = mp % (60*60*24*365)
#     month = time // (60*60*24*30)
#     time = time % (60*60*24*30)
#     day = time // (60*60*24)
#     time = time % (60*60*24)
#     hour = time // (60*60)
#     time = time % (60*60)
#     minute = time // (60)
#     sec = time % (60)
#     print(year, month,day,hour,minute,sec)
#
#
# solution(36665522)
#
#
# import datetime
#
# x = ((str(datetime.timedelta(seconds=36665522)).split())[0])
# print(x)






# import os,sys
# # wind = open("wind.txt","w+")
# # sys.stdout = wind
# os.system("ipconfig > wind.txt")
# wind = open("wind.txt","r+")
# for i in wind:
#     pass
# wind.write("aldsdasdma")

# fh = open("teszt.txt","r")
# x = fh.readlines()
# fh.close()
# fh = open("teszt.txt","w")
# for i,j in enumerate(x):
#     print(i,j)
#     if i == 0:
#         continue
#     fh.write(j)
#
# fh.close()
#
# import os
# os.rmdir("alma")
#
#
#
#

# import string
# fh = open("teszt.txt","r")
# lines = fh.readlines()
# csere = str.maketrans({"1":"egy"})
# for line in lines:
#     line = line.strip()
#     if line == "": continue
#     line = line.translate(csere)
#     print(line)
#
#
#
#
#

# from tkinter import *
# class Windows(Frame):
#     def __init__(self,master = None):
#         Frame.__init__(self,master)
#         self.master = master
#         self.init_windows()
#         self.buttons_back = [["0" for i in range(18)] for i in range(18)]
#
#     def kiir(self,i,j):
#         print(i,j)
#
#     def x(self,i,j):
#         self.buttons[i][j].config(bg="red",text="ea")
#
#     def init_windows(self):
#         self.buttons = []
#         self.master.title("aknakereső")
#         self.pack(fill=BOTH,expand=1)
#
#
#         for i in range(18):
#             self.buttons.append([])
#             for j in range(18):
#                 self.buttons[i].append(Button(self,text=str(i),command=lambda row=i,column=j: self.x(row,column)))
#                 self.buttons[i][j].grid(row=i,column=j,sticky=E)
#         for i in range(18):
#             for j in range(18):
#                 self.buttons[i][j].config(height=2,width=4)
#
#         for i in range(18):
#             for j in range(18):
#                 self.buttons[i][j].place(x = 600/18*i,y=600/18*j)
#







        # button = Button(self)
        # button.config(height=1,width=2)
        # button.place(x = 20,y =20)
#
# root = Tk()
# app = Windows(root)
# root.geometry("600x600")
# root.mainloop()
#
# import smtplib,email.mime.text
#
# en = "szazholdaspagony@micimacko.com"
# en2 = ""
# mail_server = "mail.t-online.hu"
#
# uzenet= email.mime.text.MIMEText("teszt")
#
# uzenet["From"] = en
# uzenet["To"] = en2
#
# uzenet["Subject"] = "lépesméz"
# server = smtplib.SMTP(mail_server)
# valasz = server.sendmail(en,en2,uzenet.as_string())
# if valasz != {}:
#     print("kuédesi hiba")
# else:
#     print("lekudve")
#
# server.quit()
# def x(n):
#     for i in range(n):
#         yield i
#
# a = x(10)
# for i in a:
#     print(i)
# print("---")
# for i in a:
#     print(i)
# print(False and True)
# print(ord("€"))
# import time
# t0 = time.process_time()
# m = 10
# def x():
#     global m
#     print(m)
#
# x()
# for i in range(100000):
#     m+=i
# t1 = time.process_time()
# print(t1-t0)
# class alma:
#
#     def __init__(self):
#         self.piros_alma = 10
#         self.zold_alma = 20
#
#     def __str__(self):
#         return ("{0},{1}".format(self.piros_alma,self.zold_alma))
#
# class korte(alma):
#
#     def __init__(self):
#         self.barna_korte = 30
#         # super().__init__()
#
# x = isinstance(1,float)
# print(x)
# def search(lista,value):
#     lista.sort()
#     left = 0
#     right = len(lista)
#     while left < right:
#         middle = (left + right) // 2
#         if lista[middle] < value:
#             left = middle + 1
#
#         else:
#             right = middle
#
#
#     while (left < len(lista)) and (lista[left] == value):
#         del lista[left]
#
#     return lista
# x = [1,2,4,4]
# print(search(x,4))
#
# print(iter([1,2],3))
#
#

# class SortedList:
#
#     def __init__(self,sequence = None,key = None):
#         self.sequence = sequence
        # self._key = key
        # assert hasattr(self._key,"__call__")
        # if sequence in None:
        #     self._list = []
        # elif (isinstance(sequence,SortedList) and sequence.key == self._key):
        #     self._list = sequence._list[:]
        # else:
        #     self._list = sorted(list(sequence),key=self._key)
#
#     def _alma(self):
#         print("alma")
#
#     def joska(self):
#         self._alma()
#
# x = SortedList([1,27,2])
# x.joska()
#
# y = lambda y: y[0]
# x = [(1,10),(20,2),(3,15)]
# x.sort(key=y)
# print(x)

# class x:
#     def __init__(self,a):
#         self._a = a
#
#     def __str__(self):
#         return ("{0}".format(self._a))
#
#     @property
#     def a(self):
#         return self._a
#
#     def set_a(self,value):
#         self._a = value
#
# y = x(10)
# # y.set_a(1000)
# y._a = 100
# print(y.a)
# x = 1.102802
# h = hash(x)
# print(h)
# print(round(x,3))
# class X:
#     def __init__(self):
#         self.x = 1.0
#
#     # def __repr__(self):
#     #     return ("{0}".format(self.x))
#
#     def __str__(self):
#         return ("{0}".format(self.x))
#
#     def __float__(self):
#         return float(self.x)
#
#
# m = X()
# print(m)
# print(type(m))
# print(type(m))
#
# print(repr(float()))

# import os
# n = "D:\\Kiki"
# for x in os.walk("D:\\Kiki"):
#     if x[2] != []:
#         for i in x[2]:
#             print(os.path.join(x[0],i))
#

# class grid:
#     def __init__(self,row,column):
#         self.list = [["0" for i in range(column)] for j in range(row)]
#
#     def __str__(self):
#         result = ""
#         for i in self.list:
#             for j in i:
#                 result += j + " "
#             result+="\n"
#         return result
#
# x = grid(10,10)
# print(x)


# import timeit,time,urllib,webbrowser,sched,threading
#
#
# while True:
#     x = webbrowser.open("""https:\\google.hu""")
#     time.sleep(5.0)

# def is_balanced(text):
#     forward = {"(":")","{":"}","[":"]","<":">"}
#     backward = {")":"(","}":"{","]":"[",">":"<"}
#     forward_count = {"(": 0, "{": 0, "[": 0, "<": 0}
#     backward_count = {")": 0, "}": 0, "]": 0, ">": 0}
#
#     for i in range(len(text)):
#
#         if text[i] in forward:
#             forward_count[text[i]] += 1
#             y = text.find(forward[text[i]])
#             x = text.find(text[i])
#             if len(text[x+1:y]) == 0:
#                 pass
#             # if text[x+1]== text[y]:
#             #     pass
#             # print(x,y)
#             if y == -1: return 0
#             m = is_balanced(text[x+1:y])
#             if m == 0:
#                 return 0
#         elif text[i] in backward:
#             if backward_count[text[i]] >= forward_count[backward[text[i]]]:
#                 return 0
#             else:
#                 backward_count[text[i]] += 1
#         else:
#             pass
#
#     for i,j in forward_count.items():
#         if j == backward_count[forward[i]]:
#             pass
#         else:
#             return 0
#
#     return 1
# print(is_balanced("<()>(dsdegy)(ketto)"))

# import string
# def simplify(text,delete = ""):
#     text = text.strip(string.whitespace)
#     result = ""
#     for i in range(len(text)):
#         if text[i] in delete:
#             continue
#         elif text[i] in string.whitespace:
#             if text[i+1] in string.whitespace:
#                 continue
#             else:
#                 result += " "
#         else:
#             result += text[i]
#
#     print(result.strip(string.whitespace))
#
# simplify(" egy   almafa\n\tds ","a")
#
#

# x = "  egy         alma  fa  dss   "
# # y = x.strip()
# y = x.split()
# x = ""
# for i in y:
#     x += i
#     x += " "
#
# print(x)


# import webbrowser,time,pstats
# from karaktertorles import *
#
# alma.egy("")
# while True:
#     t0 = str(time.time())
#     if ("0.1") in  t0:
#      webbrowser.open("https://google.hu")
#

# def szokoev(x):
#     return (1 if (x % 4 == 0 and (x % 400 == 0 or x % 100 != 0)) else 0)
#
# print(szokoev(100))

# PYTHONOPTIMIZE = 0
# for i in (10,1,3,0,10,1,3,0):
#     print(i)
#     assert i, "hiba"
#
# PYTHONOPTIMIZE = 0
# x = [(2,120,"Mg"),(5,22,"Ss")]
# m = 1
# y = lambda y: y[0] if m == 1 else (y[1] if m == 2 else y[2])
# x.sort(key=y)
# print(x)
# import sys
# x = 10 if sys.platform.startswith("win") else 20
# print(x)
#
# def x(m):
#     if m == 1:return ""
#     return "s"
# x = lambda x: "" if x == 1 else "s"
# print("alma{0}".format(x(0)))
# def append_if_even(x, lst=[]):
#     """alma"""
#     if x % 2 == 0:
#         lst.append(x)
#     return lst
#
# print(append_if_even(10))
# print(append_if_even(100))
#

# def kivetel(x):
#     class Kivetel(Exception): pass
#     if x == 10:
#         # sajat_hiba = ValueError("hiba")
#         raise Kivetel
#     else:
#         return x
#
# kivetel(10)

# for i in range(10):
#     print(i)
#     for j in range(10):
#         if j <= 5:
#             print("dd",j)
#         else:
#             break
#     else:
#         print("alma")
#

# x = 5
# import sys
# print("alma") if x == 3 else print("körte")
# print(sys.platform)

# import collections
# class Statistics:
#     def __init__(self,file):
#         self.file = file
#         self.mode2 = []
#         self.mean = 0.0
#         self.median = 0.0
#         self.numbers_occurence = collections.defaultdict(int)
#         self.numbers = []
#
#     def __str__(self):
#         pass
#     def open_and_count(self):
#         for line in open(self.file):
#             line = line.strip()
#             for number in line.split(","):
#                 self.numbers.append(float(number))
#                 self.numbers_occurence[number] += 1
#
#     def mean1(self):
#         count = float(0)
#         for i in self.numbers:
#             count += i
#         self.mean = count/len(self.numbers)
#
#     def median1(self):
#         x = sorted(self.numbers)
#         if len(self.numbers) % 2 == 0:
#             one = x[len(self.numbers) // 2 -1]
#             two = x[len(self.numbers) // 2]
#             self.median = (one + two)/ 2
#         else:
#             self.median = x[(len(self.numbers) // 2)]
#
#     def mode1(self):
#         x = []
#         for i,j in self.numbers_occurence.items():
#             x.append((j,i))
#
#         x.sort(reverse=True)
#         i = 0
#         while True:
#             self.mode2.append(x[i][1])
#             if x[i+1][0] == x[i][0]:
#                 i = 1
#                 continue
#             else:
#                 break
#
#     def main(self):
#         self.open_and_count()
#         self.mean1()
#         self.median1()
#         self.mode1()
#         print(len(self.numbers))
#         print(self.median)
#         print(self.mode2)
#         print(self.mean)
#
#         print("{0}....{1}...{2}...{3}".format((len(self.numbers)),self.median,self.mode2,self.mean))
#
#
# x = Statistics("teszt.txt")
# x.main()

# def swap(t):
#     return (t[1],t[0])
#
# x = [(1,"vamlma"),(2,"katica")]
# x.sort(key=swap)
# print(x)

# import collections
#
# x = collections.defaultdict(int)
# for i in ("egy ketto harom negy egy egy ketto harom harom negy".split()):
#     print(i)
#     x[i]+=1
#
# print(x)

# m = list("a" for i in range(10) if i %2)
# print(m)
# alma = 3
# x = {"egyy":1}
# print(x)
# x.setdefault("egy",alma)
# print(x)


# import urllib.request,pickle
#
# url = urllib.request.urlopen("""http://www.pythonchallenge.com/pc/def/banner.p""").read()
# data = pickle.loads(url)
# for row in data:
#     for j in row:
#         print(j[0]*j[1],end="")
#     print()
# v = "12345"
#
# for i in range(400):
#     x = """http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=""" + v
#     page = urllib.request.urlopen(x).read()
#     line = str(page).split()
#     v = line[-1].strip()
#     print(x)

# import re
# m = "AAdssABCdaABC"
# y = re.findall("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]",x)
# print(y)

# szavak = {}
# for i in range(len(x)):
#     if x[i] in string.ascii_lowercase:
#         try:
#             if (x[i-4] in string.ascii_lowercase) and (x[i+4] in string.ascii_lowercase) and (x[i-3] in string.ascii_uppercase) and (x[i-2] in string.ascii_uppercase) and (x[i-1] in string.ascii_uppercase) and (x[i+1] in string.ascii_uppercase) and (x[i+2] in string.ascii_uppercase) and (x[i+3] in string.ascii_uppercase):
#                 print(x[i-4],x[i-3],x[i-2],x[i-1],x[i],x[i+1],x[i+2],x[i+3],x[i+4])
#         except:pass
# szavak2 = []
# for i,j in szavak.items():
#     szavak2.append((j,i))

# szavak2.sort()
# print(szavak2)

# megoldas = x.translate(csere)
# print(megoldas)



#
#
# print("{0:4}".format(" "))
# import colorama
# colorama.init()
# print("alma")
# print("\033[1;31m"+"{0:1}".format(" "),"{0:3}".format("s"),end="")
#
# input()




# import string
# text = open("teszt.txt")
# lines = text.readlines()
# strip = string.punctuation
# csere0 = {}
# for i in string.whitespace:
#     csere0[i] = " "
#
# csere = str.maketrans(csere0)
# result = ""
# for sor in lines:
#     sor = sor.translate(csere)
#     for karakter in sor:
#         if karakter not in strip:
#             result += karakter
#         else:
#             continue
# result = result.lower()
# szavak = result.split()
# solution = {}
# for i in szavak:
#     solution[i] = solution.get(i,0) +1
#
# print(solution)
#
# x = open("teszt.txt")
# lines = x.readlines()
#
# result = ""
# for i in lines:
#     i = i.lower()
#     for j in i:
#         if j in string.punctuation:
#             continue
#         else:
#             if j in string.whitespace:
#                 j = " "
#             result += j
#
# szavak = {}
# for i in result.split():
#     szavak[i] = szavak
#
# print(result)

# result = ""
# for i in lines:
#     for j in i:
#         j = j.translate(strip)
#
#     print(i)



# s = (1,2,3,4)
# v = ("egy","ketto","harom","negy")
# d = {}
# d = d.fromkeys(s,v)
# m = d.popitem()
# print(type(m))

# for i in range(10):
#     for j in "abcdefgijkl":
#         if j == "e":
#             continue
#         else:
#             print(i,j)
#
#
# result = []
# for i in "MF":
#     for j in "SMLX":
#         for m in "BGW":
#             if i == "F" and j == "X":
#                 continue
#             else:
#                 result.append(i + j + m)
#
# print(result)
#
#
# x = [y for y in range(10) if y %2 ==0]
# print(x)


# def szokoev(n):
#     if n % 400 == 0:
#         return 1
#     elif n % 100 == 0
#         return 0
#     elif n % 4 == 0:
#         return 1
#     else:
#         return 0
#
# def szokoev(n):
#     if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0
#         return 1
#     else:
#         return 0
# x = [1,2,3,4,5,6,7,8,9,10]
# # x[1::2] = [0]*(len(x[1::2]))
# joska = []
# pista = []
# kiki = []
# all = [joska,pista,kiki]
# i = 0
# for j in x:
#     kivalasztott = i % 3
#     all[kivalasztott].append(i)
#     i += 1
#
# print(joska)
# print(pista)
# u = "dsdsds"
# u = u.upper()
# print(u)

# tomb = [["0" for i in range(4)] for j in range(4)]
# print(tomb)
# for i in tomb:
#     print(i)
#
# tomb2 = []
# for i in range(4):
#     tomb2.append([])
#     for j in range(4):
#         tomb2[i].append("0")
#
# print(tomb2)
# x = [9,8,1,4,2,3,4]
# y = [5,6,7]
# print(x.pop())
# x = sorted(x)
# print(x)
# import string
# x = "Egy almafa. Meg egy másik nokeldi, amugy a nokeldi finom, nagyon finom"
# x = x.lower()
# csere0 = {}
# for i in string.whitespace:
#     csere0[i] = " "
#
# for i in string.punctuation:
#     csere0[i] = ""
#
# csere = str.maketrans(csere0)
# x = x.translate(csere)
# szavak = {}
# y = x.split()
# for i in y:
#     szavak[i] = szavak.get(i,0) + 1
#
# print(szavak)
# import re
#
# x = "1a11 t"
#
# prog = re.compile("[0-9]")
# result = prog.match(x)
# print(result)
#
# y = re.fullmatch("[0-9][0-5]?\.+[0-9][0-5]?\.[a,f]?","15.12.")
# if y != None:
#     h = y.string.split(".")
#     print(h)
# print(int(0b11000110))

# allow_zero = False
# while True:
#     szam = int(input())
#     if szam < 0 and not allow_zero:
#         print("nincs engedelyekzve a nulla")
#     else:
#         x = szam
#         break
# def solution(a,b,c):
#     import math,cmath
#
#     if a == 0:
#         return "hamis"
#     diszkriminans = b**2 - 4 * a * c
#     print(diszkriminans)
#     if diszkriminans == 0:
#         return ((-b)/(2*a))
#     elif diszkriminans < 0:
#         x1 = ((-b)+(cmath.sqrt(b**2 - 4*a*c)))/(2*a)
#         x2 = ((-b)-(cmath.sqrt(b**2 - 4*a*c)))/(2*a)
#         return x1,x2
#     else:
#         x1 = ((-b)+(math.sqrt(b**2 - 4*a*c)))/(2*a)
#         x2 = ((-b)-(math.sqrt(b**2 - 4*a*c)))/(2*a)
#         return x1,x2

# print(solution(0,0,-7.25))
# import sys
#
# print(sys.maxunicode)
# for i in range(sys.maxunicode):
#     print(chr(i))


# x = 10018
# y = chr(x)
# m = ord(y)
# print(y)
# print(m)
# print(hex(m))

# print("{0:1.2}".format("abcdefghijklmnop"))
# import string
#
# for i in string.whitespace:
#     print(i.encode("ascii"))
# x = [1,2,3,4,5,6,7,8,9]
# print(x[1:3])
# result = {}
# m = "egy egy , e ketto"
# m = m.lower()
# csere = str.maketrans({",":""," ":""})
# m = m.translate(csere)
# print(m)
#
# for i in m:
#
#     result[i] = result.get(i,0) + 1
#
#     print(result)
#
# print("{{{0}}},}}".format("qgy"))
# n = " egy   mdsm\n ww"
# for i in string.whitespace:
#     n = n.replace(i,"")
#
# print(n)
# import string
# y = "asd"
# x = str.maketrans({"\t":"1"})
# print(y.translate(x))
# print(y.upper())
# print(y.islower())
# print(y)
# def szokoev(n):
#     if n % 4 == 0:
#         if n % 100 == 0:
#             if n % 400 == 0:
#                 return 1
#             return 0
#         return 1
#     else:
#         return 0
#
# print(szokoev(2000))
# print(dir())
# print(True and True)
# import sys,math
#
# print(sys.float_info.epsilon)
# print(math.ceil(3.8))
# print(sum((1,2,3)))
#
# s = 14.25.hex()
# print(s)
#
# print(math.hypot(2,6))
# for _ in range(10):
#     print(23/1.049)
# print(23/1.05)
# print(23/1.05)
# print(23/1.05)
# x = 23/1.05
# print(x)
# print("""ez egy olyan almafa
# ami nagyon szép\
# de na \
# .""")
# print("al \\a ma")
# print("\N{euro sign}")
# print("\u20AC")
# print(ord("€"))
# print(chr(1914))
# print("\u1f85")
# y = ""
# x = ["egy","ketto","harom"]
# for i in x:
#     y += i + " "
#
# print(y)
#
#
# n = " ".join(x)
# print(n)
# print(n.startswith("eh"))
# import random
#
# x = random.random()
# print(x)


# x = []
# for i in range(5):
#     x.append([])
#     for j in range(5):
#         x[i].append(j)
#
# for i in x:
#     print(i)
# y = [["0" for i in range(5)] for i in range(5)]
# print(y)
# for i in range(5):
#     for j in range(5):
#         # print(i,j)
#         y[4-j][i] = x[i][j]
#
# print(y)
# for i in y:
#     print(i)
#
# # def solution(n):
#     for i in range(len(n)):
#         if n[i] != i+1:
#             return i+1
#
#
# x = [1,2,3,4,6]
#
# print(solution(x))
#

# for i in range(10):
#     for j in range(10):
#         if  j <=i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()




# def solution(x):
#     count = 0
#     for i in x:
#         if (x.count(i)) % 2 > 0:
#             count += 1
#             del x[x.index(i)]
#
#     return count
#
# x = [9, 3, 9, 3, 9, 7]
# print(solution(x))
# import collections
# almafajtak = collections.namedtuple("almafajtak","piros zold kek sarga")
# x = almafajtak(1,2,3,9)
# print(x.sarga)

#
# def solution(n,k):
#
#     for _ in range(k):
#         last = n[-1]
#         for i in range(len(n)-2,-1,-1):
#             print(n[i])
#             n[i+1] = n[i]
#
#         del n[0]
#         n.insert(0, last)
#         print(n)
#
#         print(last)
#
#
# solution([1,3,6,2,8,9],2)
# x = [["0" for i in range(3)] for i in range(7)]
# print(x)
#
# y = ["egy","ketto"]
# y.append("harom")
# print(y)
#
# def solution(n):
#     binary = bin(n)
#     binary = list(binary)
#     for _ in range(2): del binary[0]
#     binary.append("vege")
#     count = 0
#     result = []
#     print(binary)
#     for i in range(len(binary)):
#         if binary[i] == "1":
#             for j in range(i+1,len(binary)):
#                 if binary[j] == "0": count += 1
#                 elif binary[j] == "1":
#                     result.append(count)
#                     count = 0
#                     continue
#                 elif binary[j] == "vege":
#                     count = 0
#                     break
#     if len(result) == 0:
#         return 0
#     else:
#         return max(result)
#
#
# print(solution(259))

# for i in range(4):
#     for j in range(7):
#         if j >=i and j <=6-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# for i in range(4):
#     for j in range(10):
#         if j >= 3-i and j <= 9-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# def solutin(n):
#     result = []
#     max1 = 0
#     current = 0
#     for i in range(len(n)):
#         current = 0
#         for j in range(i+1,len(n)):
#             print(n[j],end=" ")
#             current = n[j] - n[i]
#             # if current > max1:
#             #     max1 = current
#             max1 = max(max1,current)
#             # print(n[i]+n[j],end=" ")
#             # for m in range(i,j+1):
#             #     print(n[i] + n[j],end=" ")
#         print()
#     return max1
#
# for i in range(8,0,-1):
#     print("dsds")
#
# n = [1,5,2,3,7,6,4,10]
# print(solutin(n))
# print(3/2)

#
# # def solution(N):
#
# def solution(N):
#     import random
#     result = []
#     if N % 2 != 0:
#         result.append(0)
#     while True:
#         for i in range(1,100):
#             result.append(i)
#             result.append(-i)
#             result = set(result)
#             result = list(result)
#             if len(result) == N:
#                 return result
#
# print(solution(99))
# def solution(D,S):
#     dict1 = {"one":1, "two":2, "three":3, "four":4, "five":5}
#     # x = dict1
#     return (D * dict1[S])
#
# def solution(N):
#     biggest = 10**9
#     if N > biggest-1:
#         return -1
#     elif N % 10 == 0:
#         return (N + 10)
#     elif N % 10 !=0:
#         for i in range(10):
#             N = N + 1
#             if N % 10 == 0:
#                 return N
#
# print(solution(1000000000))
# D = 4
# S = "five"
# print(solution(D,S))

# def solution(A):
#     A.sort()
#     print(A)
#     A = list(set(A))
#     print(A)
#     result = []
#     for i in range(len(A)):
#         if A[i] > 0:
#             result.append(A[i])
#     if len(result) == 0:
#         return 1
#     if result[0] > 1:
#         return 1
#     for i in range(1,len(result)):
#         if result[i-1]+1 == result[i]:
#             continue
#         elif result[i-1]+1 != result[i]:
#             return (result[i-1]+1)
#
#     return (result[len(result)-1]+1)
#
# print(solution([-2,-3,-6,1,3,4]))
# def binaris_kereses(xs,ertek):
#     also_hatar = 0
#     felso_hatar = len(xs)
#     while True:
#         if also_hatar == felso_hatar:
#             return -1
#
#         kozep_index = (also_hatar + felso_hatar) // 2
#         kozep_elem = xs[kozep_index]
#
#         if kozep_elem == ertek:
#             return kozep_index
#         if kozep_elem < ertek:
#             also_hatar = kozep_index +1
#         else:
#             felso_hatar = kozep_index
#
# x = [1,2,3,4,5,6,7,8,9,10,11]
# print(binaris_kereses(x,5))

# for i in range(10):
#     for j in range(10):
#         if i == 0 or i == 9 or j == 0 or j == 9:
#             print("*", end=" ")
#         elif i == j :
#             print("*", end=" ")
#         elif 9-i == j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# print()
# for i in range(4):
#     for j in range(7):
#         if j >= i and j <= 6-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# def solution(n):
#     count = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             count +=1
#
#     print(count)
#
# solution(26)
#
# x = [1,2,3,10,1,5]
# for i in range(len(x)):
#     for j in range(i,len(x)):
#         for n in range(i,j+1):
#             print(n)



# x = [1,2,3,4,4,4,2]
# y = {}
# for i in x:
#     y[i] = y.get(i,0)+1
#
# print(y)

# x = {1,4,3,2}
# n = x.pop()
# x.add(5)
# print(n)
# print(x)
# x = set(x)
# print(x)
# def solution(a):
#     a = set(a)
#     print(len(a))
#
#
# import random
#
# n = random.randrange(0,100)
# a = []
# for i in range(n):
#     a.append(random.randrange(-200,200))
#
# print(a)
# solution(a)
# import random,string
# def solution(A,B,K):
#     count = 0
#     for i in range(A,B+1):
#         if i % K == 0:
#             count +=1
#             print(i)
#     print(count)
#
# while True:
#     A = random.randrange(0,100)
#     break
#
# solution(0,0,13)
#
# x = "asdcads"
# x = x.upper()
# print(x)
# import random
# def solution(x):
#     result = []
#     for i in range(1,len(x)+1):
#         result.append(i)
#     print(result)
#
#     try:
#         for i in result:
#             find = x.index(i)
#     except:
#         print("ez nem permutation")
#         return 0
#
#     print("ez jo")
#     return 1
# x = [1,2,3,4,5,6,7,8,10]
# solution(x)

# import random
# road_position = random.randrange(1,10)
# frog_position = random.randrange(1,road_position )
#
# frog_jump = random.randrange(1,10)
# print(frog_position,road_position,frog_jump)
# i = 0
# while True:
#     i += 1
#     frog_position += frog_jump
#     if frog_position >= road_position:
#         print(i," ugrás kellett neki")
#         break
#     else:
#         continue
# x = [9,9,3,9,3,9,7,9,1,2,2,2,3,8]
# y = set()
# for i in range(len(x)):
#     count = x.count(x[i])
#     if count % 2 == 1 :
#         y.add(x[i])
#
# print(y)


# x = [1,2,3,4,5]
# last = x[-1]
# for _ in range(len(x)-1):
#     current = x[0]
#     del x[0]
#     x.append(current)
#
# print(x)
# sorok = 4
# oszlopok = 7
# for i in range(sorok):
#     for n in range(i):
#         print(" ", end=" ")
#     for m in range(oszlopok-i*2):
#         print("*",end=" ")
#     for o in range(i):
#         print(" ", end=" ")
#     print()
#
# for i in range(5):
#     for n in range(i):
#         print("*", end=" ")
#     print()
#
#
#
# def solution(n):
#     n = str(bin(n))
#     # max = 0
#     # current = 0
#     def count(x):
#         current = 0
#         max = 0
#         for i in range(len(x)):
#             if x[i] == "0":
#                 current +=1
#             if x[i] == "1":
#                 max = current
#                 current = 0
#                 m = count(x[2+i:])
#                 uu = max(max,m)
#         return uu
#     u = count(n[2:])
#
#     return u
#
# print(bin(2345))
#
# print(solution(529))
# import math
# S = ((-5),3)
# P = (4,(-2))
# print(P[0] - S[0]
#
# # print((P[0] - S[0]) + ([P[1] - S[1]]))
# D = math.sqrt((P[0] - S[0])**2 + (P[1] - S[1])**2)
#
# print(D)


# kodlemez = []
# for i in open("kodlemez.txt"):
#     i = i.rstrip()
#     kodlemez.append(list(i))
#
# print(kodlemez)
# with open("kodlemez.txt") as ff:

    # for i in range(len(x)):
    #     x [i] = x[i].rstrip()
    #     y = list(x[i])
    #     print(y)
    #     kodlemez.append(y)
#
# m = "egy ketto harom"
# n = m.split()
# print(n)
# separator = ":"
# numlist = ["1","2","3"]
# print(separator.join(numlist))
# numlist2 = "1,2,3"
# cseretabla = str.maketrans({"1":"egy","2":"ketto","3":"harom"})
# numlist2 = numlist2.translate(cseretabla)
# print(numlist2)

# print(y)

# m = "egy almafa"
# n = list(m)
# print(n)
# x = open("D:\\Kiki\\egy.txt")
# szoveg = x.readlines()
#
# for i in szoveg:
#     i.encode()
#     print(i)

# megnyit = open("teszt.txt","r")
# eredmey = open("eredmeny.txt","w")
# szoveg = megnyit.readlines()
#
# for i in szoveg:
#     i = i.rstrip()
#     if "a" in i:
#         eredmey.write(i + "\n")
# x = [["0" for i in range(2)] for i in range(3)]
# for i in x:
#     print(i)
# print(x)



# import sqlite3
#
# # Hozz létre egy adatbázist!
# kapcsolat = sqlite3.connect("D:\\Hallgatok.db")
#
# # Hozz létre egy új táblát három mez˝ovel!
# kurzor = kapcsolat.cursor()
# kurzor.execute("""CREATE TABLE HallgatoTargyak(hallgatoNev text, ev integer, targy text)""")
# print("A HallgatoTargyak adatbázistábla létrehozva.")
# # Hozz létre néhány tesztadatot és tárold a táblában!
# teszt_adat = [
#     ("Petra", 2018, ["Informatika", "Fizika"]),
#     ("Milán", 2018, ["Matematika", "Informatika", "Statisztika"]),
#     ("Anita", 2017, ["Informatika", "Könyvelés", "Közgazdaságtan", "Menedzsment"]),
#     ("János", 2017, ["Adatbázis-kezelés", "Könyvelés", "Közgazdaságtan", "Jog"]),
#     ("Ferenc", 2018, ["Szociológia", "Közgazdaságtan", "Jog", "Statisztika", "Zene"])]
#
# for (hallgato, ev, targyak) in teszt_adat:
#     for targy in targyak:
#         tmp = (hallgato, ev, targy)
#         kurzor.execute("INSERT INTO HallgatoTargyak VALUES (?,?,?)", tmp)
#
# kapcsolat.commit()
#
# kurzor.execute("SELECT COUNT(*) FROM HallgatoTargyak")
# eredmeny = kurzor.fetchall()
# rekor_szam = eredmeny[0][0]
# kurzor.close()

# import http.server
# import socketserver
#
# port = 8080
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("",port),Handler) as httpd:
#     print("server at port",port)
#     httpd.ser
# import smtplib,email.mime.text
#@gmail.com"
# en2 = "@gmail.com"
# mail_server = "smtp.upcmail.hu"
#
# uzenet= email.mime.text.MIMEText("hali")
#
# uzenet["From"] = en
# uzenet["To"] = en2
#
# uzenet["Subject"] = "dsds"
# server = smtplib.SMTP(mail_server)
# valasz = server.sendmail(en,en2,uzenet.as_string())
# if valasz != {}:
#     print("kuédesi hiba")
# else:
#     print("lekudve")
#
# server.quit()



#
# for i in range(2):
#     n = 10 + i
#     print(n)
#
# print(2)
# print(5)
# print(3)

# import re
# x = "(3 + 777) * 9"
# y = re.split("([^0-9])",x)
# print(y)
# sum = []
# for i in y:
#     if i == "" or i == " ": continue
#     sum.append(i)
# sum.append("vege")
#
# print(sum)
# class Fa:
#     def __init__(self, adatresz, bal=None, jobb=None):
#         self.adatresz = adatresz
#         self.bal = bal
#         self.jobb = jobb
#
#     def __str__(self):
#         return str(self.adatresz)
#
#
# bal = Fa(2)
# jobb = Fa(3)
#
# faa = Fa(1,bal,jobb)
# i = 0
#
# bal = Fa(2,4)
# print(faa)


# x = osszeg(faa)
# print(x)
#
# def osszeg2(fa):
#     if fa is None: return 0
#     sum = fa.adatresz
#     sum += osszeg2(fa.bal)
#     sum += osszeg2(fa.jobb)
#     return sum
#
# y = osszeg2(faa)
# print(y)
#
# class Sor:
#     def __init__(self):
#         self.priorizalt_sor = {}
#
#     def __str__(self):
#         return str(self.priorizalt_sor)
#
#     def uj_ember_a_sorban(self,neve,prioritasa):
#         self.priorizalt_sor[neve] = prioritasa
#
#     def ki_a_kovetkezo(self):
#         n = list(self.priorizalt_sor.values())
#         n.sort()
#         kovetkezo = n.pop()
#         for x,y in self.priorizalt_sor.items():
#             if y == kovetkezo:
#                 del self.priorizalt_sor[x]
#                 return x
#
#     def ures_e(self):
#         if self.priorizalt_sor == {}:
#             return True
#
# class Golfozok:
#     def __init__(self,neve,pont):
#         self.neve = neve
#         self.pont = pont
#
#     def __str__(self):
#         return ("{0} {1}".format(self.neve,self.pont))
#
# tiger = Golfozok("Tiger Woods", 61)
# phil = Golfozok("Phil Mickelson",72)
# hal = Golfozok("Hal Sutton",69)
#
# sorrend = Sor()
# sorrend.uj_ember_a_sorban(tiger.neve,tiger.pont)
# sorrend.uj_ember_a_sorban(phil.neve,phil.pont)
# sorrend.uj_ember_a_sorban(hal.neve,hal.pont)
#
# print(sorrend)


#
# x = Sor()
# x.uj_ember_a_sorban("sanyi", 12)
# x.uj_ember_a_sorban("béla", 50)
# x.uj_ember_a_sorban("kiki",100)
# while True:
#     x.ki_a_kovetkezo()
#
#     if x.ures_e():
#         break
#
# print(x)


# import re
#
# verem = []
# szoveg = "56 3 + 4 *"
# x = re.split("([^0-9])",szoveg)
# print(x)
# for i in x:
#     print(i)
#     if i == " " or i == "":
#         continue
#     if i == '+':
#         verem.append((verem.pop() + verem.pop()))
#         continue
#     if i == "*":
#         verem.append((verem.pop() * verem.pop()))
#         continue
#     verem.append(int(i))
#
# print(verem)
# import re
#
# x = re.split("([^0-9])","123+456*/")
# print(x)
#
# y = "123+456"
# print(y.split("+"))
# class Stack:
#     def __init__(self):
#         self.tetelek = []
#
#     def push(self,tetel):
#         return self.tetelek.append(tetel)
#
#     def pop(self):
#         return self.tetelek.pop()
#
#     def ures(self):
#         return (self.tetelek == [])
#
# s = Stack()
# s.push(4)
# s.push("egy")
# s.push(8)
# print(s.tetelek)

# x = {1,2,"Egy",4.2355601,"egy",(1,2),3}
# print(x)

# class Csomopont:
#     def __init__(self, adatresz = None, kovetkezo = None):
#         self.adatresz = adatresz
#         self.kovetkezo = kovetkezo
#
#     def __str__(self):
#         return str(self.adatresz)
#
#
#
#
#
# csomopont1 = Csomopont(1)
# csomopont2 = Csomopont(2)
# csomopont3 = Csomopont(3)
#
# csomopont1.kovetkezo = csomopont2
# csomopont2.kovetkezo = csomopont3
#
# def kiir_visszafele(lista):
#     if lista in None:return
#     kiir_visszafele(lista.kovetkezo)
#     print(lista, end=" ")
#
# kiir_visszafele(csomopont1)
# class Kartya:
#     def __init__(self,szin,ertek):
#         self.szinek = {"treff":1, "káró":2, "kör":3, "pikk":4}
#         self.ertekek = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "bubi":11, "dáma":12, "király":13, "ász":14}
#         self.szin = szin
#         self.ertek = ertek
#
#     def __str__(self):
#         return ("{0} {1}".format(self.szin,self.ertek))
#
#
# class Pakli:
#     def __init__(self):
#         self.pakli = []
#         for i in ("treff","káró","kör","pikk"):
#             for n in (2,3,4,5,6,7,8,9,10,"bubi","dáma","király","ász"):
#                 self.pakli.append(Kartya(i,n))
#
#     def __str__(self):
#         s = ""
#         for i in self.pakli:
#             s = s + str(i) + "\n"
#         return s
#
#     def keveres(self):
#         import random
#         return random.shuffle(self.pakli)
#
#     def adj_lapot(self):
#         x = self.pakli.pop()
#         return x
#
#     def ures(self):
#         if len(self.pakli) == 0:
#             return True
#         return False
#
#
#     def osztas(self,kezek,lapok_szama):
#         kezek_szama = len(kezek)
#         for i in range(lapok_szama):
#             if self.ures():
#                 break
#             lap = self.adj_lapot()
#             kez = kezek[i % kezek_szama]
#             kez.add_hozza(lap)
#
#
#         return kezek
#
# class Kez(Pakli):
#     def __init__(self,nev=""):
#         self.pakli = []
#         self.nev = nev
#
#     def add_hozza(self,kartya):
#         self.pakli.append(kartya)
#
#     # def __str__(self):
#     #     s = ""
#     #     for i in self.kartyak:
#     #         s = s + str(i) + "\n"
#     #     return s
#
# pakli = Pakli()
# pakli.keveres()
# x = Kez("sanyi")
# pakli.osztas([x],5)
# print(x)


# x = Pakli()
# kez1 = []
# kez2 = []
#
# for i in range(50):
#     if x.ures():
#         break
#     kez1.append(x.oszt())
#     if x.ures():
#         break
#     kez2.append(x.oszt())
#
# for i in kez1:
#     print(i)
# print("------")
# for m in kez2:
#     print(m)
# print(x)
# print(Kartya("kör", 2))
# import random
#
# x = [1,2,3,(4,5),6,7,8,9]
# random.shuffle(x)
# print(x)


# import collections
#
# x = collections.namedtuple("x","Auto Ház Zsák Béla")
# y = x(100,2,3,51)
# print(y.Béla)
#
# n = [1,2,3,4]
# auto,kecske,bela,sanyi = n


# import math
# class Ido:
#
#     def __init__(self, orak = 0, percek = 0, masodpercek = 0):
#         self.orak = orak
#         self.percek = percek
#         self.masodpercek = masodpercek
#
#     def __str__(self):
#
#         return "{0}:{1}:{2}".format(self.orak, self.percek,self.masodpercek)

#     def __sub__(self, other):
#         ido1 = self.normal_idore_alakitas()
#         ido2 = other.normal_idore_alakitas()
#         if ido1.orak - ido2.orak < 0:
#             return Ido(0,0,0)
#         else:
#             ora = ido1.orak - ido2.orak
#
#         if ido1.percek - ido2.percek < 0:
#             if ora == 0:
#                 return Ido(0,0,0)
#             else:
#                 ora -= 1
#                 perc = 60 - abs(ido1.percek - ido2.percek)
#         else:
#             perc = ido1.percek - ido2.percek
#
#         if ido1.masodpercek - ido2.masodpercek < 0:
#             if perc == 0 and ora == 0:
#                 return Ido(0,0,0)
#             elif perc == 0:
#                 mp = 60 - abs(ido1.masodpercek - ido2.masodpercek)
#                 perc = 60 - 1
#                 ora -= 1
#             else:
#                 mp = 60 - abs(ido1.masodpercek - ido2.masodpercek)
#                 perc -= 1
#         else:
#             mp = ido1.masodpercek - ido2.masodpercek
#
#         return Ido(ora,perc,mp)
#
#     def normal_idore_alakitas(self):
#         mp = self.masodpercek % 60
#         perc = ((self.masodpercek // 60) + self.percek) % 60
#         ora = (self.masodpercek // 60 + self.percek ) // 60 + self.orak
#         return Ido(ora,perc,mp)
#
# x = Ido(10,1,1)
# print(x)
# x = str(x)
# print(x)
# print(type(x))


#
#
#     def ido_osszeado(self,ido2):
#         mp = (self.masodpercek +ido2.masodpercek) % 60
#         perc = (((self.masodpercek + ido2.masodpercek) // 60) + self.percek + ido2.percek) % 60
#         ora = ((((self.masodpercek + ido2.masodpercek) // 60) + self.percek + ido2.percek) // 60) + self.orak + ido2.orak
#         return print(Ido(ora,perc,mp))
#
#     def ora_novelese(self,ora = 0):
#         return (self.orak + ora)
#
#     def x(self,ido):
#         print(self.orak + ido)
#
#     def kiir(self):
#         print(self.orak)
#
#     def kesobb_van_e(self, ido2):
#         ido1_mp = self.masodpercek + self.percek * 60 + self.orak * 3600
#         ido2_mp = ido2.masodpercek + ido2.percek * 60 + ido2.orak * 3600
#         if ido2_mp > ido1_mp:
#             return True
#         return False
# import copy
# x = [1,2,3]
# u = str(x)
# y = copy.copy(x)
# x.reverse()
# z = x.copy()
# x.append(4)
# h = "sdsdsd "
# h = h.rstrip()
# print(h)
# print(x)
# print(z)
# print(y)
# print(u)



# print(Ido(10,44,10) - Ido(10,44,1))

# x = Ido(12,88,95).__sub__(Ido(12,5,66))

# print(Ido(10,34,55).kesobb_van_e(Ido(9,0,0)))

# Ido(10,44,55).ido_osszeado(Ido(10,4,53))
# Ido(1,2,3).kiir()
# print(Ido(12,10,1))
#
# o1,p1,mp1 = input().split()
# print(o1,p1,mp1)
# o2,p2,mp2 = input().split()
# print(o2,p2,mp2)

# Ido(1,2,3).x()
# x = Ido(3,4,5).ora_novelese(10)
# print(x)
# Ido(3,4,5).x()
# Ido.ido_osszeado(Ido(10,45,39),Ido(4,44,60))

# import json,gzip,io
#
# x = [1,2,1,2,4,4,2,2,1,6,34,423,41,35,245,234,1,3,123124,2,2,2,324,5,6,2,4,7,634,324,324,1]
# szotar = {}
# for i in x:
#     if i not in szotar:
#         szotar[i] = ["benne van"]
#     else:
#         szotar[i].append("plusz egy")
#
# print(szotar)
#
# f = io.TextIOWrapper(gzip.open("D:\\Kiki\\szerencse\\szotar", mode="wb"))
# # f = open("D:\\Kiki\\szerencse\\szotar","w")
# json.dump(szotar,f)
# f.close()
#
# f = io.TextIOWrapper(gzip.open("D:\\Kiki\\szerencse\\szotar", mode = "r"))
# # f = open("D:\\Kiki\\szerencse\\szotar","r")
# szotar2 = json.load(f)
# f.close()
# print(szotar2)


# import os
#
#
# def fajl_kereses(utvonal,mappak_eleresiut):
#     fajlok = os.listdir(utvonal)
#     for i in fajlok:
#         teljes_fajl = os.path.join(utvonal, i)
#         if os.path.isdir(teljes_fajl):
#             fajl_kereses(teljes_fajl,mappak_eleresiut)
#         else:
#             # print(i)
#             # mappak_eleresiut[i] = teljes_fajl
#             # print(mappak_eleresiut)
#             if i in mappak_eleresiut:
#                 pass
#             else:
#                 mappak_eleresiut[i] = teljes_fajl
#
#     return mappak_eleresiut
# mappak_eleresiut = {}
# x = fajl_kereses("D:\\Kiki\\angol",mappak_eleresiut)
# # print(x)
#
# print(x["elolap.jpg"])
#
# for i, n in x.items():
#     print("{0:<50}{1}".format(i,n))



# x = {"egy":[],"ketto":2}
# print(x.get("hat","nincs ilyen"))
# y = "egy" in x
# print(y)
# print(x["egy"])

# x = "Egy almafa elment vadászni, aztán jol hazavitte, megint almafa, megint egy, na meg megint megint"
# szoveg = x.split()
# szavak_szamolasa = {}
# for i in szoveg:
#     i = i.rstrip(",")
#     i = i.lower()
#     szavak_szamolasa[i] = szavak_szamolasa.get(i,0) + 1
#
# x = list(szavak_szamolasa.items())
# x.sort()
# print("{0:<10}{1}".format("Szaval", "Számok"))
# print("----------------------")
# for i, n in x:
#     print("{0:<10}{1}".format(i,n))
#
# print(szavak_szamolasa["egy"])
#
# print(szavak_szamolasa)
# x = {1:1,2:6}
# y = x.get(2,0)
# print(y)

# import string
# x = input("Szöveg: ")
# beolvasott_szoveg = x.lower()
# karakterek_szama = {}
#
# for karakter in beolvasott_szoveg:
#     if karakter in string.whitespace:
#         continue
#     karakterek_szama[karakter] = karakterek_szama.get(karakter,0) + 1
#
# x = list(karakterek_szama.items())
# x.sort()
# print(x)
# for i,n in x:
#     print(i," ",n)
#
#
# print(karakterek_szama)


# betu_szamolo = {}
# for i in "missisipi":
#     if i not in betu_szamolo:
#         betu_szamolo[i] = 0
#     betu_szamolo[i] += 1
#
# betu_szamolo2 = {}
# for i in "mississipi":
#     betu_szamolo2[i] = betu_szamolo2.get(i,0) + 1
# x = list(betu_szamolo2.items())
# x.sort()
# print(betu_szamolo2)
# print(x)

# szotar = {"egy": 1, "ketto": 2}
# print(szotar["egy"])
# x = [1,2,3,4]
# y = x.copy()
# y.append(7)
# print(x,"\n",y)

# import collections
# x = collections.namedtuple("x","egy ketto harom negy")
# y = x(
# print(y.ketto)

# def rekurzio_melyseg(szam):
#     print(szam)
#     try:
#         rekurzio_melyseg(szam+1)
#     except:
#         print("vege")
#
# rekurzio_melyseg(0)
# hiba = ValueError("hiba van")
# x = int(input())
# if x > 10:
#     raise hiba


# """A command line version of Minesweeper"""
# import random
# import re
# import time
# from string import ascii_lowercase
#
#
# def setupgrid(gridsize, start, numberofmines):
#     emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]
#
#     mines = getmines(emptygrid, start, numberofmines)
#
#     for i, j in mines:
#         emptygrid[i][j] = 'X'
#
#     grid = getnumbers(emptygrid)
#
#     return (grid, mines)
#
#
# def showgrid(grid):
#     gridsize = len(grid)
#
#     horizontal = '   ' + (4 * gridsize * '-') + '-'
#
#     # Print top column letters
#     toplabel = '     '
#
#     for i in ascii_lowercase[:gridsize]:
#         toplabel = toplabel + i + '   '
#
#     print(toplabel + '\n' + horizontal)
#
#     # Print left row numbers
#     for idx, i in enumerate(grid):
#         row = '{0:2} |'.format(idx + 1)
#
#         for j in i:
#             row = row + ' ' + j + ' |'
#
#         print(row + '\n' + horizontal)
#
#     print('')
#
#
# def getrandomcell(grid):
#     gridsize = len(grid)
#
#     a = random.randint(0, gridsize - 1)
#     b = random.randint(0, gridsize - 1)
#
#     return (a, b)
#
#
# def getneighbors(grid, rowno, colno):
#     gridsize = len(grid)
#     neighbors = []
#
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if i == 0 and j == 0:
#                 continue
#             elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
#                 neighbors.append((rowno + i, colno + j))
#
#     return neighbors
#
#
# def getmines(grid, start, numberofmines):
#     mines = []
#     neighbors = getneighbors(grid, *start)
#
#     for i in range(numberofmines):
#         cell = getrandomcell(grid)
#         while cell == start or cell in mines or cell in neighbors:
#             cell = getrandomcell(grid)
#         mines.append(cell)
#
#     return mines
#
#
# def getnumbers(grid):
#     for rowno, row in enumerate(grid):
#         for colno, cell in enumerate(row):
#             if cell != 'X':
#                 # Gets the values of the neighbors
#                 values = [grid[r][c] for r, c in getneighbors(grid,
#                                                               rowno, colno)]
#
#                 # Counts how many are mines
#                 grid[rowno][colno] = str(values.count('X'))
#
#     return grid
#
#
# def showcells(grid, currgrid, rowno, colno):
#     # Exit function if the cell was already shown
#     if currgrid[rowno][colno] != ' ':
#         return
#
#     # Show current cell
#     currgrid[rowno][colno] = grid[rowno][colno]
#
#     # Get the neighbors if the cell is empty
#     if grid[rowno][colno] == '0':
#         for r, c in getneighbors(grid, rowno, colno):
#             # Repeat function for each neighbor that doesn't have a flag
#             if currgrid[r][c] != 'F':
#                 showcells(grid, currgrid, r, c)
#
#
# def playagain():
#     choice = input('Play again? (y/n): ')
#
#     return choice.lower() == 'y'
#
#
# def parseinput(inputstring, gridsize, helpmessage):
#     cell = ()
#     flag = False
#     message = "Invalid cell. " + helpmessage
#
#     pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[gridsize - 1])
#     validinput = re.match(pattern, inputstring)
#
#     if inputstring == 'help':
#         message = helpmessage
#
#     elif validinput:
#         rowno = int(validinput.group(2)) - 1
#         colno = ascii_lowercase.index(validinput.group(1))
#         flag = bool(validinput.group(3))
#
#         if -1 < rowno < gridsize:
#             cell = (rowno, colno)
#             message = ''
#
#     return {'cell': cell, 'flag': flag, 'message': message}
#
#
# def playgame():
#     gridsize = 9
#     numberofmines = 10
#
#     currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]
#
#     grid = []
#     flags = []
#     starttime = 0
#
#     helpmessage = ("Type the column followed by the row (eg. a5). "
#                    "To put or remove a flag, add 'f' to the cell (eg. a5f).")
#
#     showgrid(currgrid)
#     print(helpmessage + " Type 'help' to show this message again.\n")
#
#     while True:
#         minesleft = numberofmines - len(flags)
#         prompt = input('Enter the cell ({} mines left): '.format(minesleft))
#         result = parseinput(prompt, gridsize, helpmessage + '\n')
#
#         message = result['message']
#         cell = result['cell']
#
#         if cell:
#             print('\n\n')
#             rowno, colno = cell
#             currcell = currgrid[rowno][colno]
#             flag = result['flag']
#
#             if not grid:
#                 grid, mines = setupgrid(gridsize, cell, numberofmines)
#             if not starttime:
#                 starttime = time.time()
#
#             if flag:
#                 # Add a flag if the cell is empty
#                 if currcell == ' ':
#                     currgrid[rowno][colno] = 'F'
#                     flags.append(cell)
#                 # Remove the flag if there is one
#                 elif currcell == 'F':
#                     currgrid[rowno][colno] = ' '
#                     flags.remove(cell)
#                 else:
#                     message = 'Cannot put a flag there'
#
#             # If there is a flag there, show a message
#             elif cell in flags:
#                 message = 'There is a flag there'
#
#             elif grid[rowno][colno] == 'X':
#                 print('Game Over\n')
#                 showgrid(grid)
#                 if playagain():
#                     playgame()
#                 return
#
#             elif currcell == ' ':
#                 showcells(grid, currgrid, rowno, colno)
#
#             else:
#                 message = "That cell is already shown"
#
#             if set(flags) == set(mines):
#                 minutes, seconds = divmod(int(time.time() - starttime), 60)
#                 print(
#                     'You Win. '
#                     'It took you {} minutes and {} seconds.\n'.format(minutes,
#                                                                       seconds))
#                 showgrid(grid)
#                 if playagain():
#                     playgame()
#                 return
#
#         showgrid(currgrid)
#         print(message)
#
# playgame()
# x = [5,2,4,0,1,2,5,77,4,211,23]
# y = x[:]
# x.sort(reverse=True)
# print(x)
# print(y)

# import pygame,math
# pygame.init()
# felulet_meret = 1080
# fo_felulet = pygame.display.set_mode((1920, 1080))
# kis_teglalap = (300, 200, 150, 90)
# valamilyen_szin = (255, 0, 0)
# while True:
#     esemeny = pygame.event.poll()
#     if esemeny.type == pygame.QUIT:
#         break
#     fo_felulet.fill((0, 200, 255))
#     fo_felulet.fill(valamilyen_szin, kis_teglalap)
#     pygame.display.flip()
# pygame.quit()
# import os
#
# def mappa_kiiratas(utvonal):
#     fajlok = os.listdir(utvonal)
#     for i in fajlok:
#         fajl = os.path.join(utvonal, i)
#         if os.path.isdir(fajl):
#             mappa_kiiratas(fajl)
#         else:
#             print(fajl)
#
#
# mappa_eleresi_ut = "D:\\Kiki\\angol"
# mappa_kiiratas(mappa_eleresi_ut)
#


# import os
# eleresiut0 = "D:\\Kiki\\angol"
#
#
# def fajlok_kiiratasa(eleresiut):
#     mappalista = os.listdir(eleresiut)
#     for i in mappalista:
#         teljes_nev = os.path.join(eleresiut,i)
#         if os.path.isdir(teljes_nev):
#             # mappalist2 = os.listdir(teljes_nev)
#             # teljes_nev2 = os.path.join(teljes_nev,)
#             # print(mappalist2)
#             fajlok_kiiratasa(teljes_nev)
#         else:
#             print(i)
#
# fajlok_kiiratasa(eleresiut0)
# fib = [0,1]
# n = 10
# while True:
#     for i in range(1,n):
#         fib.append(fib[i] + fib[i-1])
#     break
#
# print(fib)
# # def rekurzio_melysege(szam):
# #     print("{0}, ".format(szam), end="")
# #     rekurzio_melysege(szam + 1)
# #
# # print(rekurzio_melysege(0))
#
# def rek_max(beagyazott_lista):
#     legnagyobb = 0
#     for i in beagyazott_lista:
#         if type(i) == int:
#             if i > legnagyobb:
#                 legnagyobb = i
#         else:
#             legnagyobb_listaban = rek_max(i)
#             if legnagyobb_listaban > legnagyobb:
#                 legnagyobb = legnagyobb_listaban
#     return legnagyobb
#
# def rek_sum(beagyazott_lista):
#     sum = 0
#     for i in beagyazott_lista:
#         if type(i) == int:
#             sum += i
#         else:
#             sum += rek_sum(i)
#     return sum
#
# lista = [1,2,77,[1,2,[34,5]],[4,5],5,5,[1,2,399]]
# n = rek_max(lista)
# print(n)
# class Pont:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return ("({0},{1})".format(self.x,self.y))
#
#     def pelda(self,egy = 1):
#         return egy
#     def kiiras(pt):
#         print("({0},{1})".format(pt.pelda(10),pt.pelda(11)))
#
# def sulypont(p1, p2):
#     mx = (p1.x + p2.x)
#     my = (p1.y + p2.y)
#     return Pont(mx, my)
#
# class teglalap:
#
#     def __init__(self, pozx,pozy, sz, m):
#         self.poz = Pont(pozx,pozy)
#         self.szelesseg = sz
#         self.magassag = m
#
#     def __str__(self):
#         return "({0}, {1}, {2})".format(self.poz, self.szelesseg, self.magassag)
#
#
# p = Pont().x



# class Pont:
#     """alsdasdsad"""
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#     def alma():
#         """alma"""
#         print("alma")
#
# p = Pont()
# print(p.x)
# Pont()
# # import webbrowser
# #
# # x = webbrowser.
#
# Pont.alma()

# x = open("teszt.txt", "r")
# y = x.read()
# z = y.split()
# print(z)
# print(type(z))
#
# sztring = "egy álom"
# sztring = sztring.encode(encoding="")
# print(sztring)
# x = ["nulla","egy","ketto","harom"]
# y = x.index("nulla")
# print(y)
#
# megnyit = open("teszt.txt","r")
# eredmey = open("eredmeny.txt","w")
# szoveg = megnyit.readlines()
#
# for i in szoveg:
#     i = i.rstrip()
#     if "a" in i:
#         eredmey.write(i + "\n")

# import urllib.request
#
# csatlakozo = urllib.request.urlopen("https://index.hu")
# adat = str(csatlakozo.read())
#
# print(adat)
#

# x = open("teszt.txt")
#
# while True:
#     bemenet = x.readlines()
#     print(type(bemenet))
#     print(bemenet)
# import random,time
# import karaktertorles
#
#
# x = "egy almafa"
# x = karaktertorles.karaktertorles(5,x)
# print(x)
# t0 = time.process_time()
# tesztadat = range(10000000)
# x = sum(tesztadat)
# t1 = time.process_time()
# print(x,"{0:.4f}".format(t1-t0))
#
# rand = random.Random()
# eredmeny = set({})
# print(type(eredmeny))
# while len(eredmeny) < 5:
#     x = random.randrange(1,10)
#     eredmeny.add(x)
# print(eredmeny)
# eredmeny2 = []
# for i in range(5):
#     x = random.randrange(1,10)
#     eredmeny2.append(x)
#
# print(eredmeny2)
# x = ["egy",3, 10]
# # del x[0]
# print(x)
# print(range(len(x)))
#
# a = "egy"
# b = "egy"
#
# print(a is b)
# print(x)

# turtle.setup(400, 500)
# ablak = turtle.Screen()
# ablak.bgcolor("blue")

# kiki = turtle.Turtle()
# kiki.color("red")
# kiki.pensize(1)
# kiki.speed(10)
# # kiki.write("Melinda")
#
# def ek1():
#     kiki.left(90)
#
#
# while True:
#     ablak.onkey(ek1, "q")
#     kiki.forward(1)
#     ablak.listen()
#
#

# for i in range(100):
#     kiki.left(90)
#     kiki.forward(100)
#     kiki.right(90)
#     kiki.forward(10)
#     kiki.right(90)
#     kiki.forward(100)
#     kiki.left(90)
#     kiki.forward(10)


# ablak.mainloop()


# x = [["jani", [1,2,3,4]], ("sanyi", (5,6,7)), ("Pista", (8,9))]
# for i, z in x:
#     for u in z:
#         print(u)

# import random
# y = [1,2,3,4,5,6]
#
# x = random.choice(y)
# print(x)
#

# def kovetkezo_egtaj(egtaj):
#     egtajak = ["É", "K", "D", "Ny","É"]
#     if egtaj not in egtajak:
#         return None
#     x = egtajak.index(egtaj)
#     return egtajak[x + 1]
#
# print(kovetkezo_egtaj("É"))
# print(kovetkezo_egtaj("K"))
# print(kovetkezo_egtaj("D"))
# print(kovetkezo_egtaj("Ny"))
# print(kovetkezo_egtaj(None))
# print(kovetkezo_egtaj("Éds"))
#
# napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
# x = int(input("szám: "))
# print(napok[x])
#
# y = input("nap: ")
#
# print(napok.index(y))
# import sys,
# voros = '\033[1;31m'
# #
# # print(type(voros))
# sys.stdout.write("\033[1;31m")
#
# print('\033[1;31m' + "alma")
#
# print("egy")
# x= 1
#
# import turtle
#
# ablak  = turtle.Screen()
# sanyi = turtle.Turtle()
# sanyi.forward(50)
# sanyi.left(90)
# sanyi.forward(30)
#
# ablak.mainloop()
# print(x)
# print(voros)
# import heapq
# x = [1,5,4,8,1,0,2,6,8]


# x = open("teszt.txt", "w")
# x.write("egy almafa\n")
# x.write("egy almafa")
# import sys,subprocess
# print("dsdsd")
# x = input()
# subprocess.call(["cmd.exe", "/C", "cls"])
#
# x = input()

# text = "   egy almafa\n  elment\n    vacsorára   "
# print()
# end = []
# i = None
# print(text)
# for char in text:
#     if char in ("\n"):
#         continue
#     if char in (" "):
#         if not i:
#             continue
#         else:
#             end.append(char)
#             i = 0
#     else:
#         end.append(char)
#         i = 1
#
# if end[-1] in " ":
#     end.pop(-1)
# print(end)
# for i in end:
#     print(i, end="")

# import glob, os
# #
# # os.chdir("/szerencse")
# for file in glob.glob("*"):
#     print(file)
# x = open("teszt.txt","w")
# y = "ddddfy ad d ddddd"
# z = y.lstrip("d")
# print(z)
# print("s")
# d = [1,2]
# x = d[4]
# x = ["egy","ketto","harom"]
# for i, n in enumerate(x):
#     print(i,n)
# print(type(x[0]))
# index = 0
# i = 0
# target = input("mit keresel?")
# while index < len(x):
#     if x[index] == target:
#         y = index
#     index += 1

# print(y)

# import collections
# x = [1,2,3,4,5]
# y = collections.namedtuple("y","suer name gek d g")
# z = y(x[0],"alma",x[2],x[3],x[4])
# print(z.name[2])
#
# adatok = []
#
# print("{0:^40} {1:^5} {2:^10}\n{3:-^40} {3:-^5} {3:-^10}".format("Name","ID","Username",""))
# for text in open("teszt.txt"):
#     text = text.rstrip()
#     adatok = text.split(":")
#     name = []
#     name.append(adatok[1:3])
#     print("{0},{1:.<40}".format(adatok[1],adatok[3]))
#
#     print(adatok)
#
#

# x = [1,2,3,4,5,6,7,8,9,10]
# print(x[0:8:2])
# y = list(reversed(x))
# for i in reversed(x):
#     print(i)
# forenames = []
# surenames = []
#
# for names , filename in ((forenames, "teszt.txt"),(surenames, "teszt.txt")):
#     print(names,filename)
#
#
# # szo = []
# names = []
# file = ["teszt.txt"]
# # print(file[0])
# nevek = ["ketto","harom","ha"]
# szavak = ["negy","ot"]
# for i in nevek:
#     print(i)
    # for name in open(i):
    #     print(name)

# for i, n in enumerate(range(10), start=100):
#     print(n,i)

# line = "egy alma fa avagyok"
# i = 0
# i = line.index("alma", i)
# print(i)
# fin = open("teszt.txt","w+")
# fin.write("uj sor dasd%d \r\n")
# fin.close()
# print(fin)

# x = [1,1,2,3,5,6,3,1,1,3,5,6,3,1,3]
#
# while True:
#     try:
#         x.remove(1)
#     except:
#         break
#
# print(x)
# sex = ["male ", "female "]
# size = ["S ","M ","L ","XL "]
# color = ["red","blue","black"]
# # codes =[]
# # for i in sex:
# #     for o in size:
# #         for p in color:
# #             code = i + o + p
# #             codes.append(code)
# #
# # print(codes)
#
# codes = [Sex + Size + Color for Sex in sex for Size in size for Color in color]
# print(codes)


# x = [i for i in range(1,101) if i%4 == 0]
#
# print(x)
# years = []
# for i in range(1000,2000):
#     if i%4 == 0:
#         years.append(i)
#
# print(years)


# x = ["egy","ketto","harom","negy","öt","hat","het","nyolc","kilenc","tiz"]
# y = x[::2]
# print(y)
#
# while True:
#     try:
#         del y[0]
#         print(y)
#     except:
#         pass
# for i in y:
#     x.remove(i)
#     # print(i)
#
# print(x)


# hair = ("black", "blond", "red", "brown")
# x = hair[:2]
# print(type(len(x)))
#
# for i in range(len(x)):
#     print(x[i])
#
# print(i)
# i = 0
# while i < len(x):
#     print(x[i])
#     i += 1
#
# for x, y, z in (("egy", "ketto", "sd"), ("három", "négy", "ds"), ("öt",""," ds"), ("hét","nyolc","")):
#     print(x,y,z)
#
# import collections
#
# Gyártott = collections.namedtuple("Gyárott", "autó bicikli motor")
# Motor = collections.namedtuple("Motor", "kétkerekű háromkerekű" )


# x = "egy almafa meg egy katica"
# print(x[0])
# y = x.split(" ")
# print()
#
#

# import cmath
# import math
# # allow_zero = input("Ha nem engeded a nullát nyomj egy entert, ha igen akkor nyomj meg egy gomot előtte: ")
#
#
# def geta_number(allow_zero):
#     while True:
#         try:
#             number_float = float(input("Adj meg egy számot: "))
#             if not allow_zero and number_float == 0:
#                 print("Nem engedélyezett a 0")
#                 continue
#             else:
#                 return number_float
#                 break
#         except ValueError:
#             print("Számod adj meg!")
#
# a = geta_number(False)
#
# b = geta_number(True)
#
# c = geta_number(True)
#

#
# discriminant = (b ** 2) - (4 * a * c)
# print(discriminant)
#
# x1 = None
# x2 = None
# if discriminant == 0:
#     x1 = -b / (2 * a)
# elif discriminant < 0:
#     x1 = (-b + (cmath.sqrt(discriminant))) / (2 * a)
#     x2 = (-b - (cmath.sqrt(discriminant))) / (2 * a)
# elif discriminant > 0:
#     x1 = (-b + (math.sqrt(discriminant))) / (2 * a)
#     x2 = (-b - (math.sqrt(discriminant))) / (2 * a)
#
# print(x1, x2)



# import decimal
# x = "Egy {{{0}}} vagy egy {1} "
# y = x.format("alma", "körte")
# print(y)
#
# z = " three "
# u = ["the", "tops"]
# s = z.join(u)
# print(s)
#
# p = decimal.Decimal("3.552423234232")
# print(p + 6)
# print(type(p))
#
#



# zero = ["   ***   ","  *   *  "," *     * ","*       *","*       *"," *     * ","  *   *  ","   ***   "]
# one = ["    *    ","   **    ","  * *    "," *  *    ","    *    ","    *    ","    *    "," ******* "]
# two = ["    **   ","   *  *  ","  *  *   ","    *    ","   *     ","  *      "," *       ","*********"]
# three = ["  *****  "," *     * "," **    * ","     *** ","     *** "," **    * "," *     * ","  *****  "]
# four = ["*     ","*     ","*     ","*     ","******","     *","     *","     *"]
#
# digits = [zero,one,two,three,four]
# try:
#     numbers = input("Számok:")
#     rows = 0
#     while rows < 8:
#         line = " "
#         columns = 0
#         while columns < len(numbers):
#             digit = int(numbers[columns])
#             print(digits[digit][rows],end='')
#             #line += digits[digit][rows] + " "
#             columns += 1
#         #print(line)
#         print()
#         rows += 1
# except:
#     print("vege")

# try:
#     numbers = input("Számok:")
#     rows = 0
#     while rows < 8:
#         line = " "
#         columns = 0
#         while columns < len(numbers):
#             digit = int(numbers[columns])
#             line += digits[digit][rows] + " "
#             columns += 1
#         print(line)
#         rows += 1
# except:
#     print("vege")


# for i in range(6):
#     for z in range(6):
#         print("0", end=" ")
#     print()
#
#


















# row = 0
# while row < 10:
#     column = 0
#     while column < 10:
#         print(column, end="")
#         column += 1
#     print("\n")
#     row += 1
#
#
# def x(test):
#     if test < 10:
#         return 7
#     else:
#         return 107
#
#
# egy = x(100)
#
# print(egy)
#


# threatises = ["egy","ketto","harom"]

# y =
# print(y)
# for i in threatises:
#     print(i)
# zero = ["   ***   ","  *   *  "," *     * ","*       *","*       *"," *     * ","  *   *  ","   ***   "]
# one = ["    *    ",
#        "   **    ",
#        "  * *    ",
#        " *  *    ",
#        "    *    ",
#        "    *    ",
#        "    *    ",
#        " ******* "]
# two = ["    **   ",
#        "   *  *  ",
#        "  *  *   ",
#        "    *    ",
#        "   *     ",
#        "  *      ",
#        " *       ",
#        "*********"]
#
# three = ["  *****  ",
#          " *     * ",
#          " **    * ",
#          "     *** ",
#          "     *** ",
#          " **    * ",
#          " *     * ",
#          "  *****  "]
#
# Digits = [zero, one, two, three]
# numbers = input("számok: ")
#
# try:
#     rows = 0
#     while rows < 8:
#         line = ""
#         column = 0
#         while column < len(numbers):
#             number = int(numbers[column])
#             digit = Digits[number]
#             line += digit[rows] + " "
#             column += 1
#         print(line)
#         rows += 1
# except:
#     print("vege")
#     pass



# '''print("hello", "Word")
#
# x = 14
# print(x)
#
# y=( )
# print(len(y))
#
# if x == 13:
#     print("igaz")
# elif x==14:
#     pass
# else:
#     print("vege")
#
# z = 3.5
# print(type(z))
#
# q = ["egy","ketto"]
# q += ["háeom"]
# print( q )
# total = 0
# count = 0
# while True:
#     line = input("szám: ")
#     if not line:
#         print("vége")
#         break
#     try:
#         number = int(line)
#     except:
#         print("vége")
#         break
#     total += number
#     count += 1
#
# print(total, count)
# total2 = 0
# count2 = 0
# while True:
#     try:
#         line2 = input("szam")
#         if line2:
#             number2 = int(line2)
#         else:
#             break
#     except:
#         print("vege")
#         break
#     total2 += number2
#     count2 +=1
#
# print(total2, count2)'''

#one = 0
#two = 0
#five = 0
#ten = 0


#print('1=' ,one,"\n2=",two,"\n5=", five,"\n10=", ten)

#while True:
 #   x = input("x=")
  #  if x == "1":
   #     one += 0.56
    #    two -= 0.29
     #   five -= 0.135
      #  ten -= 0.0769
#    if x == "2":
 #       one -= 0.44
  #      two += 0.71
   #     five -= 0.135
    #    ten -= 0.0769
#   if x == "5":
 #       one -= 0.44
  #      two -= 0.29
   #     five += 0.865
    #    ten -= 0.0769
 #   if x == "10":
  #      one -= 0.44
   #     two -= 0.29
    #    five -= 0.135
     #   ten += 0.9231

   # print('1=' ,one,"\n2=",two,"\n5=", five,"\n10=", ten)
