Word = 'Ege'
Word = Word.lower()
list_add = []
list_add_second = []
k =  len(Word) - 1

for i in Word:
    if i == Word[k]:
        list_add.append(Word[k])
        list_add_second.append(i)
        k = k - 1

if list_add == list_add_second:
    print("It's Palidrome")
