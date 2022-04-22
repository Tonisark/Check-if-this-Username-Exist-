from logging import exception
from requests import  get 
import requests

def Username() :
    Username =  input("Give me Username > ")
    response = requests.get("https://instagram.com/" + Username + "/")
    if not(response.ok):
        print("Username not exist")
    else :
        print(f"https://instagram.com/{Username}/")


def checklist() -> None :
    print("Give me file path > ")
    filepath = input()
    base_link = "https://instagram.com/"
    with open (filepath , "r") as f :
        pages = f.read().split("\n")
        for i in pages :
            try :
                res = get(base_link + i)
                if res.ok :
                    print(base_link + i , "is valid")
                else :
                    print(base_link + i , "is not valid")
            except exception.connectionError as c_error :
                print(c_error)



def start() :
    print("For check 1 Account write 1\nFor check some accounts write 2")
    UsernameInput = int(input("<>> "))
    if UsernameInput == 1 :
        Username()
    elif UsernameInput == 2 : 
        checklist()
    

start()