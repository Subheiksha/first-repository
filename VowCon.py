a=str(input(""))
vow=["a","e","i","o","u"]
cons=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","u","v","w","x","y","z"]
if(a in cons):
    print("Consonant")
elif(a in vow):
    print("Vowel")
else:
   print("Invalid")
