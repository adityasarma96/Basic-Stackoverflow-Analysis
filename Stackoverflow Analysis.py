import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

url = "http://stackoverflow.com/questions?sort=newest&page="
tagCount = {}
lang = ['c', 'c++', 'java', 'python', 'php', 'javascript', 'html','css','perl', 'scala','shell','swift', 'matlab',
         '.net', 'c#', 'objective-c', 'ruby', 'android','ios','linux', 'go', 'sql']
for l in lang:
    tagCount[l]=0

def pageExtract(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    # print(soup)
    resp = soup.find_all("a", {"class": "post-tag"})
    #print(resp)
    for t in resp:
        if t.string in tagCount:
            tagCount[t.string]+=1
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.01*height, '%d'%int(height),
                ha='center', va='bottom')

for i in range(1,51):
    urli = url + str(i)
    print("Extracting page ",i,"...")
    pageExtract(urli)
print("Analysis of last 50*50 questions...")
'''for t in tagCount:
    print(t,tagCount[t],sep="  :  ")'''
r = plt.bar(range(0,len(tagCount)*2,2),list(tagCount.values()),align="center",width=1)
autolabel(r)
plt.xticks(range(0,len(tagCount)*2,2),list(tagCount.keys()),rotation='vertical')
plt.ylabel("Stackoverflow analysis")
plt.show()