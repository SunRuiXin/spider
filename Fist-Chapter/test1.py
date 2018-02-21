import requests
def getHTMLText(url):
	try:
		
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text[:1000]
	except:
		return 'erro'

if __name__ == '__main__':
	url = 'https://item.jd.com/5911960.html'
	print(getHTMLText(url))
