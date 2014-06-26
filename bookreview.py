from bs4 import BeautifulSoup
import urllib2
import html5lib
query=raw_input("Enter The Book title You Want to search for??")
print("searching in goodreads")
baseurl="https://www.goodreads.com/search?query="
query=query.strip()
d=query.split()
st=""
for e in d:
    st+=e+"+"
url=baseurl+st[:-1]
print url
title=[]
author=[]
links=[]
bs = BeautifulSoup(urllib2.urlopen(url).read(), "html.parser")
for msg in bs.select(".bookTitle"):
    title.append(msg.text)
for msg in bs.select(".bookTitle"):
    links.append(msg['href'])
for msg in bs.select(".authorName"):
    author.append(msg.text)
books=zip(title,author)
i=0
for e in books:
     i=i+1
     print i,e[0].strip(),e[1].strip()
choice=int(raw_input("enter your choice"))
link= links[choice-1]
reviewlink="https://www.goodreads.com"+link
bs=BeautifulSoup(urllib2.urlopen(reviewlink).read(),"html.parser")
i=0
reviewgr=[]
for msg in bs.select(".readable"):
   i=i+1
   if i%2==0:
      reviewgr.append(msg.text)

fliplink="http://www.flipkart.com/search?q="+st[:-1]
bs = BeautifulSoup(urllib2.urlopen(fliplink).read(), "html.parser")
for link in bs.select('.lu-title'):
     print link['href']
     break   


   
   
