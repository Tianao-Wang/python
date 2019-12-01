"""This program bases off the Monty Hall Problem, and uses the random built-in to pick random doors"""

import random

def get_all_door_list(num_of_doors):
    return [x for x in range(1, num_of_doors + 1)]

def pick_door(num_of_doors):
    door_list = get_all_door_list(num_of_doors)
    picked_door = random.choice(door_list)
    return picked_door

def host_open_door(guest_door, prize_door, num_of_doors):
    door_list = get_all_door_list(num_of_doors)
    door_list.remove(guest_door)
    if guest_door != prize_door:
        door_list.remove(prize_door)
    host_door = random.choice(door_list)
    return host_door

def guest_change_door(guest_door, host_door, change_door, num_of_doors):
    if change_door:
        door_list = get_all_door_list(num_of_doors)
        door_list.remove(host_door)
        door_list.remove(guest_door)
        guest_door = random.choice(door_list)
    return guest_door

def result(guest_door, prize_door):
    win = False
    if guest_door == prize_door:
        print("WE HAVE A WINNER!")
        win = True
    else:
        print("Sorry, better luck next time!")
    return win

def run_once(num_of_doors, change_door):
    prize_door = pick_door(num_of_doors)
    guest_door = pick_door(num_of_doors)
    host_door = host_open_door(guest_door, prize_door, num_of_doors)
    guest_door = guest_change_door(guest_door, host_door, change_door, num_of_doors)
    return result(guest_door, prize_door)

def main():
    num_of_doors = int(input("Enter how many doors you want: "))
    change_door = input("Do you want to change your door every time?(Y/N)")
    if change_door.upper() == "Y":
        change_door = True
    else:
        change_door = False
    run_times = int(input("Enter the amount of times you want to run the program: "))
    win_count = 0
    for x in range(0, run_times):
        win = run_once(num_of_doors, change_door)
        if win:
            win_count += 1
    print("Out of", run_times, "times, you won", win_count, "times")

if __name__ == '__main__':
    main()