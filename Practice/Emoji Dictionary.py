def emoji_dictionary():
    input1 = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "☹️",
        "dick": "🍆",
        "ass": "🍑"
    }
    output = ""
    for input in input1:
        output += emojis.get(input, input)
    return output

message = input("What's up? ")
print(emoji_dictionary())