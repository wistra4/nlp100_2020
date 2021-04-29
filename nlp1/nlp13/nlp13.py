c1_list = []
c2_list = []
with open('col1.txt', 'r') as col1:
    for c1 in col1:
        s_c1 = c1.strip()
        c1_list.append(s_c1)
    print(c1_list)
with open('col2.txt', 'r') as col2:
    for c2 in col2:
        s_c2 = c2.strip()
        c2_list.append(s_c2)
    print(c2_list)
with open('marge.txt', 'w') as m:
    if len(c1_list) == len(c2_list):
        for i in range(len(c1_list)):
            m.write(c1_list[i]+'\t'+c2_list[i]+'\n')
    else:
        print('error')