import random

user_total = 0
bot_total = 0

def roll_dice():
    return random.randint(1, 6)

for round in range(1, 4):
    input(f"Round: {round} - Press Enter to roll!")
    
    user_roll = roll_dice()
    bot_roll = roll_dice()
    
    user_total += user_roll
    bot_total += bot_roll
    
    print(f"You: {user_roll}")
    print(f"PC: {bot_roll}")
    print(f"You: {user_total} | PC: {bot_total}\n")

print(f"You: {user_total} | PC: {bot_total}")

if user_total > bot_total:
    print("You Win!!")
elif user_total < bot_total:

    print("PC win!!")
else:
    print("It's a tie!")
