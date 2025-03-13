sentence = "This is a common interview question"
sentence = sentence.lower()
chars = {}
for char in sentence:
    if char in chars:
        chars[char]+=1
    else:
        chars[char]=1
sorted_chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
print(f"The most occurring character is: {sorted_chars[0][0]}, which appears {sorted_chars[0][1]} times")
