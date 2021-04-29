c_list = []
with open('popular-names.txt', 'r') as r:
    for data in r:
        # print(data)
        s_data = data.strip()
        # print(s_data)
        r_data = s_data.replace('\t',' ')
        # print(r_data)
        d_list =  r_data.split(" ")
        # print(d_list)
        c_list.append(d_list[0])
    c_set = set(c_list)
    print(c_set)