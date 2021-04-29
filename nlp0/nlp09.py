import random
sent = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
w_list = sent.split(" ")
n_list = []
for words in w_list:
    words = words.strip(",")
    words = words.strip(".")
    w_num = len(words)
    l_list = []
    l_count = 1
    s_letters = ''
    if w_num > 4:
        for l_num in range(w_num-2):
            l_list.append(words[l_count])
            l_count += 1
        # print(l_list)
        r_list = random.sample(l_list, w_num-2)
        # print(r_list)
        for s_num in range(w_num-2):
            s_letters += r_list[s_num]
        words = words[0] + s_letters + words[-1]
    else:
        pass
    n_list.append(words)
# print(n_list)
sent = " ".join(n_list)
print(sent)
    
    