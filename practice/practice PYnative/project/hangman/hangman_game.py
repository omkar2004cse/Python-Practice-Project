import random
import hangman_stages
friuts=['apple','mango','gavo','banana']
chosen_fruit=random.choice(friuts)
# print(chosen_fruit)
display=[]
lives=6
print("Fruit Name is:-")
for i in chosen_fruit:
    display+='_'
print(display)
game_over=False 
while not game_over:
    guess_letter=input("Guess a Letter:-").lower()
    for position in range(len(chosen_fruit)):
        letter=chosen_fruit[position]
        if letter==guess_letter:
            display[position]=guess_letter
    print(display)
    if guess_letter not in chosen_fruit:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose!!")
    if '_' not in display:
        game_over=True
        print("You Win")
    print(hangman_stages.stages[lives])