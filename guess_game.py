from random import choice
import time
colors = ['red','blue','yellow','gray','white','green','black','pink','purple','brown']
print("I choose the colors that i'll write them!")
print(colors)
start = time.time()
a = input("guess the color that in my mind! \n")
counter = 1
b = choice(colors)
while a != b:
    counter += 1
    a = input("no.try again \n")
    elapsed = time.time() - start
    if elapsed > 30 or counter > 6:
        break

if a==b:
    if counter == 1:
        print(f"nice!\nyou guessed with {counter} guess")
    elif counter > 1 and counter < 7:
        print(f"not so bad!\nyou guessed with {counter} guesses")
    else:
        print(f"6 wrong guesses! you lost! the answer was: {b}")
else:
    if counter > 6:
       print(f"6 wrong guesses! you lost! the answer was: {b}")
    else:
        print(f'game over.your time is over!the answer was: {b}')
        print("that's okay.you can try again!!")