count = 0
with open('popular-names.txt') as f:
    for line in f:
        count += 1
print(count)

print(sum([1 for line in open('popular-names.txt')]))