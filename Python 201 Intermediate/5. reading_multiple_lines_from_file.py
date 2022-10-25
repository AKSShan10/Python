with open('5. email.txt','r') as emails:
    emails = emails.readlines()

for email in emails:
    print('Looking for a hotmail account')
    if "hotmail" in email:
        print(email)

for email in emails:
    if "gmail" in email:
        print(email)

for email in emails:
    if "gmail" in email:
        print(email.rstrip()) #strip helps to get rid of extra line