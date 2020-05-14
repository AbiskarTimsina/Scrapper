'''
WebScrapper v1
Sources: Newyork Times, My Republica
Date: 2020/05/14
Coded By: Abiskar Timsina

Libraries required: 
- requests { pip install requests}
- bs4 { pip install bs4 }


'''

#The files are stored in the ./classes directory
from classes.newyorktimes import GlobalNews
from classes.myrepublica import *

if __name__ == '__main__':
	
	global_news = GlobalNews().global_news()
	local_news = NagarikNews().local_news()
	political_news = NagarikNews().political_news()
	# All these are of return type; list
	
	print (f'{global_news} \n {local_news} \n {political_news}')