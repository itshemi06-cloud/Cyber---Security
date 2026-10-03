import string

print("=====Password Stregth Cheker=====")

password = input("Enter your password :")

score = 0

if len(password) >8:
    score +=1

    if any(char.isupper() for char in password):
        score +=1


if any(char.isdigit() for char in password):
                score +=1

if any(char in  string.punctuation for char in password):
                score +=1

                print("\nPassword Analysis")

                if score <= 2:
                        print("Password Strength : weak")

                elif score ==3 or score == 4 :
                       print("Password Strengh : mediam")  

                else : 
                        print("Password Strengh : Strong")      