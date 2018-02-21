import requests
def getHTMLText(url):
	try:
		kv = {'user-agent' : 'Mozilla/5.0'}
		r = requests.get(url, headers = kv, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return 'erro'

if __name__ == '__main__':
	url = 'https://www.amazon.cn/gp/product/B06X9H7FCC/ref=amb_link_5/461-3033461-8027158?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-1&pf_rd_r=C8431JEXKZV4CXMGEKMN&pf_rd_r=C8431JEXKZV4CXMGEKMN&pf_rd_t=101&pf_rd_p=3c8c75b5-6d80-4f0d-ac97-39de59da54c0&pf_rd_p=3c8c75b5-6d80-4f0d-ac97-39de59da54c0&pf_rd_i=658390051'
	print(getHTMLText(url))
