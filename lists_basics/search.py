n = int(input())
searched_word = input()
words_list = []
for i in range(n):
    word = input()
    words_list.append(word)

print(words_list)

for i in range(len(words_list) -1, -1, -1):
    element = words_list[i]
    if searched_word not in element:
        words_list.remove(element)


print(words_list)