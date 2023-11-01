import art
import game_data
import random

print(art.logo)

opa = random.randint(0,len(game_data.data)-1)
opb = random.randint(0,len(game_data.data)-1)

print(f"Compare A : {game_data.data[opa]['name']}, a {game_data.data[opa]['description']}, from {game_data.data[opa]['country']}")

print(art.vs)

print(f"Compare B : {game_data.data[opb]['name']}, a {game_data.data[opb]['description']}, from {game_data.data[opb]['country']}")

user_inp = input("Choose your option : ")