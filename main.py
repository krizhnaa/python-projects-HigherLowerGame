import art
import game_data
import random

print(art.logo)

game_over = False
user_point = 0

opt = ['A','B']

opa = random.randint(0,len(game_data.data)-1)
opb = random.randint(0,len(game_data.data)-1)

print(f"Compare {opt[0]} : {game_data.data[opa]['name']}, a {game_data.data[opa]['description']}, from {game_data.data[opa]['country']}")
print(game_data.data[opa]['follower_count'])

print(art.vs)

print(f"Compare {opt[1]} : {game_data.data[opb]['name']}, a {game_data.data[opb]['description']}, from {game_data.data[opb]['country']}")
print(game_data.data[opb]['follower_count'])
user_inp = input("Who has the most followers, Option 'A' or 'B' : ")

if user_inp == opt[0] and game_data.data[opa]['follower_count'] > game_data.data[opb]['follower_count']:
    print("You are awarded a point")
    user_point+=1
elif user_inp == opt[1] and game_data.data[opb]['follower_count'] > game_data.data[opa]['follower_count']:
    print("You are awarded a point")
    user_point+=1
else:
    print("You Lose")
    print(f"Your total points are : {user_point}")
    game_over = True