lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        "name":"Ann",
        "numbers":{4,5,8,1,2}
    },
    {
        "name":"Bob",
        "numbers":{13,5,8}
        
    }]


player0=(players[0]["numbers"])
player0_name=players[0]["name"]
Lottery1=str(len(lottery_numbers.intersection(player0)))
print(player0_name+" got "+Lottery1+" numbers right")
player1=(players[1]["numbers"])
Lottery2=str(len(lottery_numbers.intersection(player1)))
print(players[1]["name"]+" got "+Lottery2+" numbers right")

#ALTERNATE
name = players[0]["name"]
numbers = players[0]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} numbers right.")
name = players[1]["name"]
numbers = players[1]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} numbers right.")