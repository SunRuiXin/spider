import requests
#http://www.baidu.com/s?wd=搜索词
#http://www.so.com/s?q=搜索词
def getHTMLText(url, keyword):
	try:
		kv = {'user-agent' : 'Mozilla/5.0'}
		ks = {'wd': keyword}
		r = requests.get(url, params = ks, headers = kv, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(r.request.url)
		return len(r.text)
	except:
		return 'erro'

if __name__ == '__main__':
	url = 'http://www.baidu.com/s'
	keyword = 'Python'
	print(getHTMLText(url, keyword))
