import re


def find_all_emails(text):
    all = re.findall(r'[a-zA-Z][a-zA-Z0-9_.]+@[a-z]+\.\w+\w', text)
     

    return all

print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'))



#(\w+\.?\w+]+@[\w*)\.?\w+]
