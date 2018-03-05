import re
import requests
def getHTMLText(url):
	try:
		kv = {'user-agent' : 'Mozilla/5.0'}
		a = requests.get(url, headers = kv)
		a.raise_for_status()
		a.encodng = a.apparent_encoding
		return a.text
	except:
		return ''

def parsePage(ilt, html):
	try:
		price = re.findall(r'"price":"[\d]*"', html)
		#plt = re.findall(r'"view_price":"[\d\.]*"',html)
		print("ss")
		name = re.findall(r'"title":".*?"', html)
		print(len(price))
		for i in range(len(price)):
			p = eval(price[i].split(':')[1])
			n = eval(name[i].split(':')[1])
			ilt.append([p,n])
			#print("{}  {}".format(p, n))
	except:
		print("")
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
	url = 'https://s.taobao.com/search?q='
	q = '平板'
	url = url + q
	list1 = []
	depth = 3
	for i in range(depth):
		try:
			Url = url + '&s=' + str(i*48)
			html = getHTMLText(Url)
			#print(html[0:3000])
			parsePage(list1, html)
		except:
			pass
	printGoodsList(list1)
main()
