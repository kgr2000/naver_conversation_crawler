import requests
import bs4

response = requests.get("https://phrase.dict.naver.com/detail.nhn?bigCategoryNo=2&middleCategoryNo=21&smallCategoryNo=145&targetLanguage=cn").text
soup = bs4.BeautifulSoup(response,"html.parser")
#토픽 추출
topic = soup.find("ul", {"class":"lst_area"}).text
cont_kor = soup.find("div", "dic_cont").find_all("span", {"class":"info_txt"})
cont_ch = soup.find("div", "dic_cont").find_all("span", {"class":"info_txt2"})

#한국어 대화 리스트 만들기
cont_li_kor = []
for li_kor in cont_kor:
    cont_li_kor.append(li_kor.text.strip())
#print(cont_li_kor)

#중국어 대화 리스트 만들기
cont_li_ch = []
for li_ch in cont_ch:
    cont_li_ch.append(li_ch.text.strip())
#print(cont_li_ch)

