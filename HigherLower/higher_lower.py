import random
import os

import art, game_data


def main():
    os.system("cls")
    while True:
        start=input("Do you want to play Higher Lower? (y/n): ").lower()
        if start == "n":
            exit()
        elif start !="y":
            print("Invalid Input!")
            continue
        break
    os.system("cls")    
    game(0, None)    

def game(score, contin):
    print(art.logo)
    if contin == None:
        p1=random.choice(game_data.data)
    else:
        p1=contin
    p2=random.choice([item for item in game_data.data if item != p1])
    print(f"Name: {p1["name"]}; Description: {p1["description"]}; Nationality: {p1["country"]}")
    print(art.vs)
    print(f"Name: {p2["name"]}; Description: {p2["description"]}; Nationality: {p2["country"]}")
    print(f"\nYour current score is: {score}\n")
    choice=input("Enter the name of the person with Higher Followers: ")
    compare(p1, p2, choice, score)

def compare(p1, p2, choice, score):
    max="".join([p1["name"] if p1["follower_count"] > p2["follower_count"] else p2["name"]])
    dic=next((item for item in game_data.data if item.get("name")==max), None)
    if max == choice:
        print("Right answer!")
        os.system("cls")
        game(score+1, dic)
    else:
        print("Wrong answer!")
        again=[main() if input("Do you want to play again? (y/n): ").lower() == "y" else exit()]

main()        