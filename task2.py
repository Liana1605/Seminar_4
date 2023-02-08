#Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
#подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
#содержится в этом тексте.
#Input:  She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
#shells on the sea shore I'm sure that the shells are sea shore shells
#Output: 13

#text = input('Введите текст: ')
#print(text)

#text = text.split()
#print(text)

#text = set(text)
#print(text)
#print(f'В нашем тексте {len(text)} уникальных слов')

#или

text = input('Введите текст: ')
text = text.split()
new_list = []

for word in text:
    if not word in new_list:
        new_list.append(word)

print(f'В нашем тексте {len(new_list)} уникальных слов')
