from bs4 import BeautifulSoup
from time import sleep
import requests

def get_title(links):

	sleep(5)
	pg = requests.get("https://"+links,headers=user_agent)


	try:
		if pg.status_code==200:
			#print(pg.text)

			title_list = list()
			soup = BeautifulSoup(pg.text,"html.parser")
			#print(soup)
			ti = soup.find('div', id='block-mainscreen-level2')
			tost = soup.find_all('a')
			for data in tost:
				print(data['href'])
			
			#for data in allLinks:
				#if data.find('a') is not None:
						#temp_list = [data.text.strip("\"\'\/\#") ,data['href']]
						#links.append(temp_list[1][2:-1])
			
			#if ti.findAll('a', class_='company-name company-name-lite-vb') is not None:
			#	print(ti.text)
			#	pass
			#print(title.text)
				#print(title.text)


	except Exception as e:
		print(e)
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://www.google.com/",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"}


search_text = "SYNTHETIC+SULFONATE+ADDITIVE".replace(" ","+")
#search_text = str(input("input search")).replace(" ","+")

print(search_text)
#curl 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=bullshit&viewtype=&tab=' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=bullshit' -H 'Cookie: ali_apache_id=33.1.201.221.165256270844.389693.3; cookie2=a6a411a4b9b9f6ff0a7dc7b5bd1a9fa9; t=d7b6f1e2bdb7d6e0a4aca47bc756a7e2; _tb_token_=fde3383b9abee; ali_apache_track=""; ali_apache_tracktmp=""; xman_us_f=x_l=0; acs_usuc_t=acs_rt=eef0218fa4c5448786d4f1e0415910c9; xman_t=7TZhlQ2QGlkSKB9pr6SY7MalmmzvQIldpGP43m0IY3c9v3X23+WPpcZZQOKSm04f5etNdKgsl+1+BxDK15UMWpHG9K73dgHW; xman_f=xy2TTolv0OssrHUs2umkU4xVLwlDnnbRDMe1jfeHD6hcFb1RwpVlLfNdXZNlz5JYyuji7j/kZxX06fL48hFA46YqFEhJrFJuollWY6ODXUVRkwGCAfAXFw==; _bl_uid=FLlqO3ge6m0dhj6qI3a8omtwmw85; cna=FgkHG74FaCwCAdl2Tl7aFX7C; JSESSIONID=2BB3F61368221E41E37D2EB85649A20B; _m_h5_tk=2fb78d3304f96cd6e65a9c26cfe0a1d2_1652564511520; _m_h5_tk_enc=4c533cf48c5ad7e13536c01563ea82a8; isg=BF5e7A72sAnG6-TtI0CV3E_erP2gHyKZvcIqVgjmy6GOK_8FcKydqZ2JI68nCBqx; tfstk=c6e5BuDCPc04PX9evusVLNnHWkD5a7vS0gg0VZMOp3yWfHEnys2vQV9CzkYxLDnf.; l=eBO2DmsgLBxh5oSCBO5BFurza779iIO48kPzaNbMiInca1RPw3wPoOChMiuWkdtfQtfXyetzy8M39dHv7e45syxoZasjui-9LxJ6-; xlly_s=1; XSRF-TOKEN=96800fcd-2550-47e2-89ed-e8d133d95931; sc_g_cfg_f=sc_b_site=RU&sc_b_locale=en_US; _samesite_flag_=true; _csrf_token=1652562903100; _ga_RVSKK1KF5N=GS1.1.1652563980.1.1.1652564380.60; _ga=GA1.1.1246943627.1652563980' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'TE: trailers'

url = ("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText="+search_text)
#more_url = ("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText="+search_text+"&page="+i)

#user_agent = {"User-Agent": "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5"}


def get_urls(url):
	page = requests.get(url, headers = user_agent)
	print(page.status_code)
	try:
		if page.status_code == 200:
			'''
			GET PAGE COUNT
			https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.37b36a6bL0a5IK&IndexArea=product_en&SearchText=SYNTHETIC_SULFONATE_ADDITIVE&page=2&f0=y
			cycle
			'''
			links = list()
			soup = BeautifulSoup(page.text,"html.parser")

			#allLinks = soup.findAll('a', class = 'company-name')
			allLinks = soup.findAll('a', class_ = 'elements-title-normal one-line')
			#print(allLinks)
			for data in allLinks:
				if data.find('span') is not None:
						temp_list = [data.text.strip("\"\'\/\#") ,data['href']]
						links.append(temp_list[1][2:-1])
			#get_title(links[1])
			#for i, j in enumerate(links):
			#	print(i,j)
				#get_title(j)
			
			return links


			#links = soup.findAll("a")
			#for data in links:
				#print(data['href'])





	except Exception as e:
		print(e)


links = [get_urls(url)]
for i in range(2,10):
	more_url = ("https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText="+search_text+"&page="+str(i))
	links.append(get_urls(more_url))

cringe_list = list()
for i,j in enumerate(links):
	for link in j:
		cringe_list.append(link)
	#print(j,i, sep = "\nCount:")
print(cringe_list,len(cringe_list),sep = "\nAmount:\n")


#FCKOFF NEED WEBDRIVER TO FAST or API REQ