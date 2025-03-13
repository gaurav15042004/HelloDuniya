sentence = "This is a common interview question"
sentence = sentence.lower()
sentence_chars = list(sentence)

sorted_chars = sorted(sentence_chars)

count_table=[]
for i in range(0, len(sorted_chars)):
    x = sorted_chars.count(sorted_chars[i])
    index = [sorted_chars[i], x]
    if index not in count_table:
        count_table.append(index)

count_table.sort(key=lambda x: x[1], reverse = True)
largest = count_table

for large in largest:
    if largest[0][1]> largest[1][1]:
        print(largest[0][0])
    else: print(f" The most occurred character in the sentence was {largest[1][0]}, Which appeared {largest[1][1]} times")
    break