def is_spam_words(text, spam_words, space_around=False):
         
    text = text.lower()
    for i in range(len(spam_words)):
        spam_words[i] = spam_words[i].lower()             
    for j in spam_words:
        if text.find(j) == -1:
            continue
        elif text.find(j) != -1 and space_around == True:
            if j == text.find(j):
                return True
            else:
                return False
        elif text.find(j) != -1 and space_around == False:
            if j != text.find(j):
                return True
            else:
                return False

  
print(is_spam_words("Молох", ["лох"], False))