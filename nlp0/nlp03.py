sent = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
w_list = sent.split(" ")
n_list = []
for words in w_list:
    words = words.strip(",")
    words = words.strip(".")
    w_num = len(words)
    n_list.append(w_num)
print(n_list)