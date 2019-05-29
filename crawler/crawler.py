import urllib
import urllib.request
import re


page = urllib.request.urlopen('https://tieba.baidu.com/p/1753935195')
htmlBytes = page.read()
encoding = "utf-8"
htmlCode = htmlBytes.decode(encoding)
print('download html from internet successfull')

pageFile = open('baidu.txt', 'w')
pageFile.write(htmlCode)
pageFile.close()
print('write to local file successfull')


reg = r'src="(.+?\.jpg)"'
reg_img = re.compile(reg)
imglist = reg_img.findall(htmlCode)

for img in imglist:
    print(img)

for i in range(len(imglist)):
    urllib.request.urlretrieve(imglist[i], str(i) + ".jpg")

