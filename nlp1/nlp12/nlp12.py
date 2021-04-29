c_list1 = []
c_list2 = []
with open('popular-names.txt', 'r') as r:
    for data in r:
        # print(data)
        s_data = data.strip()
        # print(s_data)
        r_data = s_data.replace('\t',' ')
        print(r_data)
        d_list =  r_data.split(" ")
        print(d_list)
        c_list1.append(d_list[0])
        c_list2.append(d_list[1])
    print(c_list1)
    print(c_list2)
with open('col1.txt', 'w') as f_c1:
    for c1 in c_list1:
        f_c1.write(c1+'\n')
with open('col2.txt', 'w') as f_c2:
    for c2 in c_list2:
        f_c2.write(c2+'\n')