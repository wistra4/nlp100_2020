sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
w_list = sent.split(" ")
n_list = []
for words in w_list:
    words = words.strip(",")
    words = words.strip(".")
    n_list.append(words)
w_num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}
order = 1
for words in n_list:
    if order in w_num:
        word = words[0]
    else:
        word = words[:2]
    dic[word] = order
    order += 1
print(dic)