with open('popular-names.txt', 'r') as r:
    with open('popular-names_space.txt', 'w', newline="") as w:
        for data in r:
            # print(data)
            s_data = data.strip()
            # print(s_data)
            r_data = s_data.replace('\t',' ')
            print('\n'+r_data)
            # f.write('\n'+r_data)
            w.write(r_data+'\n')