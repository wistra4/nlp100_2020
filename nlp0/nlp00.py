words = "stressed"
r_words = ""
w_num = len(words)
for i in range(w_num):
    r_words += words[w_num-i-1]
print(r_words)