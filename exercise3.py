def playagain():
    while(True):
        user_input = input("Do you want to play again (Y or N)? ")
        if(user_input == 'Y'):
            print("ok")
        elif(user_input == 'N'):
            return False
        else:
            print("Invalid input.")
        
if __name__ == "__main__":
  playagain()