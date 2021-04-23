def n_gram(sent, n):
    n_gram = []
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
    return n_gram

words1 = "paraparaparadise"
words2 = "paragraph"
if "se" in words1:
    print("True1")
if "se" in words2:
    print("True2")
X = set(n_gram(words1, 2))
Y = set(n_gram(words2, 2))
print(X)
print(Y)
union = X | Y
print(union)
union = X.union(Y)
print(union)
intersection = X & Y
print(intersection)
intersection = X.intersection(Y)
print(intersection)
difference = X - Y
print(difference)
difference = X.difference(Y)
print(difference)
difference = Y - X
print(difference)
difference = Y.difference(X)
print(difference)
s_difference = X.symmetric_difference(Y)
print(s_difference)
