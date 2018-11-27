import requests
import bs4

#url 분류
url = "https://phrase.dict.naver.com/detail.nhn"
big_no = 3
mid_no = 21
sm_no = 145
param = {
        "bigCategoryNo": big_no,
        "middleCategoryNo": mid_no,
        "smallCategoryNo": sm_no,
        "targetLanguage":"cn"
}
header = {'User-Agent' : 'Mozilla/5.0', 'referer' : 'http://naver.com'}

#코드 추출
response = requests.get(url, params=param, headers=header).text
soup = bs4.BeautifulSoup(response,"html.parser")

#토픽 추출
topic = soup.find("ul", {"class":"lst_area"}).text
print(topic)
# cont_kor = soup.find("div", "dic_cont").find_all("span", {"class":"info_txt"})
# cont_ch = soup.find("div", "dic_cont").find_all("span", {"class":"info_txt2"})
#
# #한국어 대화 리스트 만들기
# cont_li_kor = []
# for li_kor in cont_kor:
#     cont_li_kor.append(li_kor.text.strip())
# #print(cont_li_kor)
#
# #중국어 대화 리스트 만들기
# cont_li_ch = []
# for li_ch in cont_ch:
#     cont_li_ch.append(li_ch.text.strip())
# #print(cont_li_ch)

