import random
import string

password_repeat = int(input("Kaç adet şifre oluştursun(varsayılan 1): "))
if password_repeat < 1:
    password_repeat = 1
password_length = int(input("Şifrenizin uzunluğunu giriniz(sayı giriniz): "))
password_lower = input("Şifrenizin hepsi küçük mü olsun?(E-H): ").upper()
password_upper = input("Şifrenizin hepsi büyük mü olsun?(E-H): ").upper()
if password_lower == 'E' and password_upper == 'E':
    print("Hem büyük hem küçük olsunu işaretlediniz. Sırayla bir büyük bir küçük şekilde şifreyi oluşturacak")
password_word = string.ascii_letters + string.digits + string.punctuation

def password_create(password_repeat, password_lenght, password_lower, password_upper, password_word):
    file = open(str(password_repeat)+"_AdetSifre_.txt", "a")
    file.write(str(password_lenght)+" Uzunluğunda "+str(password_repeat)+" Adet Şifre oluşturdunuz\n")
    for i in range(password_repeat):
        newpassword=""
        password = 0
        iRandom = 0
        while(password < password_lenght):
            newword = password_word[random.randint(0, len(password_word)-1)]
            if password_lower == 'H' and password_upper == 'H' : newpassword=newpassword+newword
            elif password_lower == 'E' and password_upper == 'H' : newpassword=newpassword+newword.lower()
            elif password_upper == 'E' and password_lower == 'H' : newpassword=newpassword+newword.upper()
            elif password_lower == 'E' and password_upper=='E' :
                iRandom = 1 if iRandom == 0 else 0
                newpassword=newpassword+newword.upper() if iRandom == 0 else newpassword+newword.lower()
            if password >= 1 and (newpassword[password-1] == newpassword[password] or ord(newpassword[password-1])+32 == ord(newpassword[password]) or
                                ord(newpassword[password-1])-32 == ord(newpassword[password])):
                newpassword=newpassword[0:password-1]
                password-=1
                continue

            password+=1

        print(newpassword)
        file.write(newpassword+"\n")
    file.close()

password_create(password_repeat=password_repeat, password_lenght=password_length, password_lower=password_lower, password_upper=password_upper, password_word=password_word)
