email = input("Enter Email Text: ")

keywords = ["verify", "password", "bank", "click", "urgent", "winner"]

phishing = False

for word in keywords:
    if word in email.lower():
        phishing = True
        break

if phishing:
    print("Phishing Email Detected")
else:
    print("Safe Email")