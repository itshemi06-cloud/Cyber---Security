import hashlib

print("=====Hash Generator=====")

text = input("Enter the text to generate hash :")

sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print("SHA-256 Hash : ", sha256_hash)