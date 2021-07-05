import re

def replace_spam_words(text, spam_words):
    for i in spam_words:
        result = re.sub(i, "*" * len(i), text, 0, re.IGNORECASE)
        text = result
    return result

print(replace_spam_words("Hello, my friend. How are you?", ["my", "you"]))
    
    

