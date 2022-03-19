#-------------------------------------------------------
#------------------Mason Skinner------------------------
#--------------External Files Summative-----------------
#-----------------March 19, 2022------------------------
#-------------------------------------------------------

#-------------------------Imports-----------------------
import time
import random
#------------------------------------------------------

#---------------------Functions-------------------------
def create_user():#used to create user saves and adds them to the saves list
    print("What is your name?")
    name = input('> ').lower()
    saves = open('saves.txt', 'a')
    saves.write(f'{name}\n')
    saves.close()
    file_name = name + '.txt'
    save_file = open(file_name, 'w')
    save_file.write(f"name,{name},highest_score,0,total_score,0")
    save_file.close()
    
def load_user(): #used to load the user save file you want
    saves = open('saves.txt', 'r')
    names = saves.read()
    saves.close()
    file_found = False
    while file_found == False:#this loop makes sure the user pics a real file
        try:
            print(names)
            print("Which user would you like to load?")
            user = input('> ').lower()
            file_name = user + '.txt'
            save_file = open(file_name, 'r')
            file_found = True
        except FileNotFoundError:
            print("That save does not exist!\n")
    save = save_file.read().split(',')
    item = 0
    while item < (len(save)):
        user_info[save[item]] = save[item + 1]
        item = item + 2
    save_file.close()
    return file_name

def main():
    print("Would you like too create or load a user?")
    x = input('> ').lower()
    if x == 'load':
        filename = load_user()
    elif x == 'create':
        create_user()
        filename = load_user()
    print(f"{user_info['name']}, are you ready to get your lucky number?!")
    input('> ')
    print("Well here it is!")
    lucky_number = random.randint(1, 1000000)
    print(f"Your number is {lucky_number}!")
    time.sleep(2)
    if lucky_number > int(user_info['highest_score']):
        user_info['highest_score'] = str(lucky_number)
        print("Congrats thats your new highest number!")
    else:
        print(f"Not quite, your highest number is still {user_info['highest_score']}")
    user_info['total_score'] = int(user_info['total_score']) + lucky_number
    print(f"Your total score is {user_info['total_score']}!")
    user_info['total_score'] = str(user_info['total_score'])
    save_game = open(filename, 'w')
    save_game.write(f"name,{user_info['name']},")
    save_game.write(f"highest_score,{user_info['highest_score']},")
    save_game.write(f"total_score,{user_info['total_score']}")
    save_game.close()
    time.sleep(2)
    print("Come back tomorrow to increase your score!")
#-------------------------------------------------------

#----Variables----
user_info = {}
#-----------------

#----Main Code----
main()