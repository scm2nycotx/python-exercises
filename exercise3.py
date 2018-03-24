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
  

for k, v in numbers.items():
            print("Name:", k, "\tNumber:", v["Number"], "\te-mail:", v["e-mail"], "\tURL:", v["url"])
            break
        
        

else:
    print("{} was not found".format(name))
    return True