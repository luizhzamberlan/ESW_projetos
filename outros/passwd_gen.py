# import 
import string
import random

def useing_key():
  char = ((string.ascii_letters)+(string.ascii_uppercase)+(string.digits)+(string.hexdigits)+(string.punctuation))
  key_words=(list(char))
  return key_words
key_words2 = (useing_key())

while True:
  # a for password lenth:  ########
  print("")
  while True:
    try:
      a=int(input("Enter The Password Leanth : "))
      break
    except:
      print('Error: command not found')
      print('Try to type a number!')
  print("")
  #b for asking n times pasword
  while True:
    try:
      b = int(input("How many password would you like : "))
      break
    except:
      print('Error: command not found')
      print('Try to type a number!')
  print("")
  print("")
  # This first for loop 
  for x in range(0,b):
    password=""
    #second for loop
    for x in range(0,a):
      pasword_Gen = random.choice(key_words2)
      password = (password + pasword_Gen)
    print(""*100)
    print("|                                  ")
    print(f"|Your Password =  {password}")
    print("|"+""*100)
  
  print("")
  # To exit
  while True:
    r = input("Do you want to try again?[Y/N] ").strip().lower()
    if r not in "yn":
      print("Error: command not found")
    else:
      if r == "n":
        exit()
      else:
        break
