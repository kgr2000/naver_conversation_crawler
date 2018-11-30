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

print(li_sim)
print(li_tra)