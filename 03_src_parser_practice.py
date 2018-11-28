def get_movieSrc(m_title):
    title = m_title
    URL = "https://www.rottentomatoes.com/m/{title}/"
    content = requests.get(URL).text
    soup = BeautifulSoup(content,'html.parser')
    a_tags = soup.find('div',{'class':'center'})
    img_tag = a_tags.find('img',{"src":True})
    print(a_tag)
    if img_tag == None:
        img_tag = a_tags.find('img',{"data-src":True})
    result = img_tag.get('src')
    if result == "/assets/pizza-pie/images/poster_default.c8c896e70c3.gif":
        result = img_tag.get('data-src')
    elif result == None:
        result = img_tag.get('data-src')
