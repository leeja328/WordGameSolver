f = open('/Users/jameslee/Desktop/words.txt', 'r')

content = f.read()

new = content.split("\n")

# new = ['red', 'bro', 'hellow', 'asdf', 'bored']

letters = input("Enter the letters ")
l = []
for x in letters:
    l.append(x)


d = []
# for word in new:
#     if l[0] in word and l[1] in word and l[2] in word and l[3] in word and l[4] in word and l[5] in word:
#         if len(word) <= 6:
#             print(word)

count = 0
leng = 0
lst = []
while count < len(new):
    while leng < len(new[count]):
        if new[count][leng] in l:
            d.append(new[count][leng])
            l.pop(l.index(new[count][leng]))
            leng += 1
        else:
            break
    for x in l:
        d.append(x)
    l = []
    for x in d:
        l.append(x)
    d = []
    if leng == len(new[count]) and len(new[count]) < 7 and len(new[count]) >= 3:
        lst.append(new[count])
        leng = 0
        count += 1
        
    else:
        leng = 0
        count += 1


lst.sort(key=len, reverse=True)
print(lst)





f.close()
