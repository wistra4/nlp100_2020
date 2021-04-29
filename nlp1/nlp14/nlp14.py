n_num = int(input('自然数を入力してください : '))
count = 0
with open('popular-names.txt', 'r') as f:
    for data in f:
        if count < n_num:
            # print(data)
            s_data = data.strip()
            # print(s_data)
            r_data = s_data.replace('\t',' ')
            print(r_data)
            count += 1
