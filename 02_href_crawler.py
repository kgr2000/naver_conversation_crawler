import requests
import bs4
import re

url = 'https://phrase.dict.naver.com/detail.nhn?targetLanguage=cn'
response = requests.get(url).text
soup = bs4.BeautifulSoup(response, 'html.parser')

#BigCategory 리스트 생성
big_a_tags = soup.find('ul', {'class':'lst_snb'}).find_all('a')
li_big_href = []
for big_a_tag in big_a_tags:
    big_href_tag = big_a_tag.get('href')
    li_big_href.append(big_href_tag)

#MidCatergory 리스트 생성
mid_a_tags = soup.find('dl', {'class':'lst_sort'}).find('span', {'class':'inline'}).find_all('a')
li_mid_href = []
for mid_a_tag in mid_a_tags:
    mid_href_tag = mid_a_tag.get('href')
    li_mid_href.append(mid_href_tag)

#SmallCatergory 리스트 생성
sm_a_tags = soup.find('dl', {'class':'lst_sort sort_small'}).find('span', {'class':'inline'}).find_all('a')
li_sm_href = []
for sm_a_tag in sm_a_tags:
    sm_href_tag = sm_a_tag.get('href')
    li_sm_href.append(sm_href_tag)