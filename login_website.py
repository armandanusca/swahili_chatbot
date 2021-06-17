import fbchat

def fbLogin(user, password):
    global client

    try:
        client=fbchat.Client(user,password)

    except:
        print("Login Failed")


    if client.isLoggedIn():
        print(client.uid)

    else:
        print("Client is not logged in")

def sendMessage(message):
    global client
    client.send(fbchat.Message(text=message), 100030265500881)


client=""

user = input("Enter username: ")
password = input("Enter password: ")

if __name__ == "__main__":
    fbLogin(user, password)
    #sendMessage("asdas")

