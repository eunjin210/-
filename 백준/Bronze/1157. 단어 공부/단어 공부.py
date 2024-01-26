s= input().upper()
temp = list(set(s))
cnt_list = []
for i in temp:
    cnt = s.count(i)
    cnt_list.append(cnt)
if cnt_list.count(max(cnt_list))>1:
    print('?')
else:
    max_index=cnt_list.index(max(cnt_list))
    print(temp[max_index])
