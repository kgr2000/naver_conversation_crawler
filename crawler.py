import requests
import bs4
import re
import random

                    #####href 추출
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
href_load = 0
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
    href_load += 1
    print("href 추출 중:"+ str(href_load) + "/112")
                    #####href 추출 끝

                    #####간체, 번체 리스트 만들기
f = open('chi_stt.txt', 'r', encoding='utf8')
#총 2495개
lines = f.readlines()
li_sim = []
li_tra = []

#간체자 리스트 만들기
for sim in lines :
    li_sim.append(sim[2])
#번체자 리스트 만들기
for tra in lines :
    li_tra.append(tra[4])

                    #####간체, 번체 리스트 만들기 끝



for url_href in li_sm_href:
#url 분류
    url = "https://phrase.dict.naver.com/"+url_href
    #url = 'https://phrase.dict.naver.com/detail.nhn?bigCategoryNo=2&middleCategoryNo=32&categoryTypeCode=0&targetLanguage=cn'
    header = {'User-Agent' : 'Mozilla/5.0', 'referer' : 'http://naver.com'}

    #코드 추출
    response = requests.get(url, headers=header).text


    soup = bs4.BeautifulSoup(response,"html.parser")

    #토픽 추출
    topic = soup.find("ul", {"class":"lst_area"}).text

    cont_kor = soup.find("div", "dic_cont").find_all("span", {"class":"info_txt"})
    cont_ch = soup.find("div", "dic_cont").find_all("span", {"class":"info_txt2"})

    #한국어 대화 리스트 만들기
    cont_li_kor = []
    cont_li_kor_ran = []
    for li_kor in cont_kor:
        cont_li_kor.append(li_kor.text.strip())


    #중국어 대화 리스트 만들기&간체를 번체로 변경
    cont_li_ch_sim = []
    cont_li_ch_tra = []
    for li_ch in cont_ch:
        li_ch_text = li_ch.text.strip()
        cont_li_ch_sim.append(li_ch_text)
        len_li_ch_text = range(len(li_ch_text))
        for le_ch_num in len_li_ch_text :
            if li_ch_text[le_ch_num] in li_sim :
                li_ch_text = re.sub(li_ch_text[le_ch_num], li_tra[li_sim.index(li_ch_text[le_ch_num])], li_ch_text)
                    #(print(li_ch_text[le_ch_num], li_sim.index(li_ch_text[le_ch_num]), li_tra[li_sim.index(li_ch_text[le_ch_num])])
            else :
                continue
        cont_li_ch_tra.append(li_ch_text)

    for cont_li_kor_num in range(len(cont_li_kor)) :
        spl_cont_li_kor = re.split("\s", cont_li_kor[cont_li_kor_num])
        ran_cont_li_kor = random.sample(spl_cont_li_kor, len(spl_cont_li_kor))
        cont_li_kor_ran.append(ran_cont_li_kor)

    print(topic)
    a = range(len(cont_li_kor))
    for b in a:
        print(cont_li_kor[b])
        print(cont_li_kor_ran[b])
        print(cont_li_ch_tra[b])