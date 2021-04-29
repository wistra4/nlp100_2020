n_num = int(input('自然数を入力してください : '))
count = 0
s_count = 0
with open('popular-names.txt', 'r') as f:
    for data in f:
        count += 1
    # print(count)
with open('popular-names.txt', 'r') as f:
    for data in f:
        # print(data)
        s_data = data.strip()
        # print(s_data)
        r_data = s_data.replace('\t',' ')
        # print(count-n_num)
        # print(s_count)
        if s_count < count-n_num:
            pass
        else:
            print(r_data)
        s_count += 1
