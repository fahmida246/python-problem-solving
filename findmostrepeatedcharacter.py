sen = "this is a common interview question"

char_fre = {}
for i in sen:
    if i in char_fre:
        char_fre[i] += 1
    else:
        char_fre[i] = 1

# print(char_fre)

char_fre_sort = sorted(
    char_fre.items(), key=lambda item: item[1], reverse=True)
print(char_fre_sort[0])
