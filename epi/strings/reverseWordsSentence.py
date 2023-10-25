def reverse_words(sentence):
    words = []
    ans = ""
    word= ""
    for char in sentence:
        if char != " ":
            word+=char
        else:
            words.append(word)
            word = ""
    if word != "":
        words.append(word)

    print(words)
    for i in range(len(words)-1,0,-1):
        ans+=words[i] + " "
    ans+=words[0]
    return ans

print(reverse_words("You're awesome!"))
