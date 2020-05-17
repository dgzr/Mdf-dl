# usr/bin/py3
# Tuul ampas gan ,gak usah di clone
# start : minggu 17 05 2020 , 23:32:20 WIB
# done  : senin 17 05 2020, 00:01:22 WIB
import argparse,re
import requests as r
from sys import argv
from os import system
from tqdm import tqdm
from bs4 import BeautifulSoup as bs

h = '\033[1;32m'
b = '\033[1;34m'
p = '\033[1;37m'

class MediaFire(object):
	def __init__(self,url,path):
		self.url = url
		self.path = path
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		self.main()
	def main(self):
		try:
			_o = r.get(self.url,headers=self.headers).text
			_u = re.search(r'href\=\"(http:\/\/download\d+.mediafire\.com.*?)">',_o).group(1) # search url content
			_x = bs(_o,'html.parser').find('div',class_='filename').text.replace(' ','_') # search file name
			si = re.search(r'<span\>(\d.*?)\<\/span\>',_o).group(1) # search size file
			_up = re.search(r'<li\>Uploaded\:\ \<span\>(.*?)\</',_o).group(1)
			print(f' {b}[{p}*{b}] {p}Size File     : {si} ')
			print(f' {b}[{p}*{b}] {p}File Uploaded : {_up}')
			print(f' {b}[{p}*{b}] {p}Downloading Content ')
			za_ = r.get(_u,stream=True)
			prog_ = tqdm(total=int(za_.headers.get('content-length', 0)), unit='B', unit_scale=True)
			with open(self.path+_x, 'wb') as f:
				for cos_ in za_.iter_content(1024):
					prog_.update(len(cos_))
					f.write(cos_)
			prog_.close()
			print(f' {b}[{p}*{b}] {p}Okay File Saved As : {_x}')
		except Exception as eror:
			print(f'Error :=> {str(eror)}')
			
try:
	_y = argparse.ArgumentParser(description='Ezz-Kun © 2020\nA Simple MediaFire Downloader',formatter_class=argparse.RawTextHelpFormatter)
	_y.add_argument('-u','--url',help='url file to download',metavar='')
	_y.add_argument('-p','--path',help='path save file example:/sdcard/',metavar='')
	_gs = _y.add_argument_group('Additional')
	_gs.add_argument('-c','--contact',help='Contact Author Script',action='store_true')
	_gs.add_argument('-v','--version',help='show this script version',action='store_true')
	_q = _y.parse_args()
	if _q.url and _q.path:
		MediaFire(_q.url,_q.path)
	elif _q.contact:
		system('xdg-open https://instagram.com/aditiaze_07')
	elif _q.version:
		print('Versi : 00000000000000000')
	else:
		print(f'''Usage : python {argv[0]} -h for show all options''')
except EOFError:
	pass
