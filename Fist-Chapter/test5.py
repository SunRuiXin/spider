import requests
import os
def getHTMLText(url):
	
	try:
		r = requests.get(url+'202.204.80.112')
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(r.text)
	except:
		return 'erro'

if __name__ == '__main__':
	url = 'http://www.ip138.com/ips138.asp?ip='
	print(getHTMLText(url))
