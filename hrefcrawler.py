import requests
import bs4
import re

url = 'https://phrase.dict.naver.com/detail.nhn?targetLanguage=cn'
response = requests.get(url).text
soup = bs4.BeautifulSoup(response, 'html.parser')

li_big_href = []
li_mid_href = []
li_sm_href = []

#BigCategory 리스트 생성
big_a_tags = soup.find('ul', {'class':'lst_snb'}).find_all('a')
for big_a_tag in big_a_tags:
    big_href_tag = big_a_tag.get('href')
    li_big_href.append(big_href_tag)

for big_page_num in li_big_href:
    big_res = requests.get('https://phrase.dict.naver.com/'+big_page_num).text
    big_soup = bs4.BeautifulSoup(big_res, 'html.parser')

    # #MidCatergory 리스트 생성
    mid_a_tags = big_soup.find('dl', {'class':'lst_sort'}).find('span', {'class':'inline'}).find_all('a')
    for mid_a_tag in mid_a_tags:
        mid_href_tag = mid_a_tag.get('href')
        li_mid_href.append(mid_href_tag)

for mid_page_num in li_mid_href:
    try:
        mid_res = requests.get('https://phrase.dict.naver.com/'+mid_page_num).text
        mid_soup = bs4.BeautifulSoup(mid_res, 'html.parser')

        #SmallCatergory 리스트 생성
        sm_a_tags = mid_soup.find('dl', {'class':'lst_sort sort_small'}).find('span', {'class':'inline'}).find_all('a')
        for sm_a_tag in sm_a_tags:
            sm_href_tag = sm_a_tag.get('href')
            li_sm_href.append(sm_href_tag)

    except:
        pass
