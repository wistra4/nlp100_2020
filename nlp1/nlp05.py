def n_gram(sent, n):
    sect = input("Is type of output letter or word ? : ")
    n_gram = []
    if sect == "letter":
        w_num = len(sent)
        surp = w_num%n
        s_num = int((w_num - surp)/n)
        start = 0
        end = n
        add = n
        for i in range(s_num):
            n_gram.append(sent[start:end])
            start += add
            end += add
        if surp > 0:
            n_gram.append(sent[start:])
        print(n_gram)
    elif sect == "word":
        w_list = sent.split(" ")
        w_num = len(w_list)
        surp = w_num%n
        s_num = int((w_num - surp)/n)
        start = 0
        end = n
        add = n
        for i in range(s_num):
            n_gram.append(" ".join(w_list[start:end]))
            start += add
            end += add
        if surp > 0:
            n_gram.append(" ".join(w_list[start:]))
        print(n_gram)
    else:
        print("error")

sent = "I am an NLPer"
n_gram(sent, 2)
