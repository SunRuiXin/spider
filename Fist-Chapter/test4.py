import requests
import os
def getHTMLText(url, root):
	path = root + url.split('/')[-1]
	print(str(path))

	try:
		if not os.path.exists(root):
			os.mkdir(root)
		
		if not os.path.exists(path):
			r = requests.get(url)
			with open(path, 'wb') as f:
				f.write(r.content)
				f.close()
				print('success')
		else:
			print("already had")
	except:
		return 'erro'

if __name__ == '__main__':
	url = 'http://uploads.5068.com/allimg/151120/57-1511201H157-50.jpg'
	root = "/home/sebar/pic/"
	print(getHTMLText(url, root))
