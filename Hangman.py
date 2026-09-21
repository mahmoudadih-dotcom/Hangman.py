#استدعاء المكاتب 
import random
#اخيار الاعشوائي 
ch_random=random.choice(['man','women','child'])
#المتغيرات
token=6
guessing_basket=[]
b_ch_random=['_']*(len(ch_random))
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(" ".join(b_ch_random))
print(HANGMANPICS[0])
#لوب 
while '_' in b_ch_random and token>0:
    guess=input("what is your guess ? ")

#IF داخل لوب تحقق من توكن 
    if guess in guessing_basket:
        print('this is selected guess')
        continue
# ضافه الاخيار في القائمه
    guessing_basket.append(guess)
    if  guess not in ch_random:
        token-=1
    print(HANGMANPICS[6-token])
    for g in range(len(ch_random)):
        if ch_random[g]==guess:
           b_ch_random[g]=guess
    print(" ".join(b_ch_random))
    print(f"you have token {token} ")
if token==0:
    print("""

          you ❌ losse


""")
else:
    print("""

         you ✅ win


""")



