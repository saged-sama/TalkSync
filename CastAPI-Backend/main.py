from CastAPI import CastAPI
from datetime import datetime

def main():
    app = CastAPI()
    users = {
        'saged': ('sajid', 'notadoctor')
    }
    chats = {}

    # Auth
    @app.route("/sign-up", "POST")
    def register(req):
        try:
            username = req["body"]["username"]
            password = req["body"]["password"]
            name = req["body"]["name"]

            users[username] = (name, password)

            return (200, {
                "message": "Successfully registered new user"
            })
        except Exception as e:
            print("Could not register new ID: ", e)
            return (500, {
                "message": "Could not add new user"
            })

    @app.route("/log-in", "POST")
    def login(req):
        try:
            username = req["body"]["username"]
            password = req["body"]["password"]

            _, pss = users[username]
            if password == pss:
                return (200, {
                    "message": "login successful"
                })
            else:
                return (401, {
                    "message": "unauthorized"
                })
        except Exception as e:
            print("Could not log in: ", e)
            return (500, {
                "message": "Could not log in"
            })
        
    @app.route("/search-username", "GET")
    def search_username(req):
        try:
            searchUser = req["query"]["user"]
            results = []
            for username in users:
                if searchUser in username:
                    name, _ = users[username]
                    results.append({"username": username, "name": name})
            return (200, {
                "users": results
            })
        except Exception as e:
            print("Could not search usernames: ", e)
            return (500, {
                "message": "Could not search usernames"
            })
    
    @app.route("/get-users", "GET")
    def get_users(req):
        try:
            results = []
            for username in users:
                name, _ = users[username]
                results.append({"username": username, "name": name})
            return (200, {
                "users": results
            })
        except Exception as e:
            print("Could not get users: ", e)
            return (500, {
                "message": "Could not search users"
            })
            

    # Chat
    @app.route("/add-message", "POST")
    def add_message(req):
        try:
            chatID = req["query"]["chatID"]
            # print(req["body"])
            message = req["body"]["message"]
            sender = req["body"]["sender"]
            image = req["body"]["image"]
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if chatID not in chats:
                chats[chatID] = [{
                    "sender": sender,
                    "time": date,
                    "message": message,
                    "image": image,
                }]
                sender, receiver = chatID.split("-")
                chatID = receiver + "-" + sender
                chats[chatID] = [{
                    "sender": sender,
                    "time": date,
                    "message": message,
                    "image": image,
                }]
            else:
                chats[chatID].append({
                    "sender": sender,
                    "time": date,
                    "message": message,
                    "image": image,
                })
                sender, receiver = chatID.split("-")
                chatID = receiver + "-" + sender
                chats[chatID].append({
                    "sender": sender,
                    "time": date,
                    "message": message,
                    "image": image,
                })
            # print(chats[chatID])
            return (200, {
                "messages": chats[chatID]
            })

        except Exception as e:
            print(f"Error posting new Message: {e}")
            return (400, {
                "message": "Could not add message"
            })

    @app.route("/get-messages", "GET")
    def get_messages(req):
        try:
            chatID = req["query"]["chatID"]
            print(chatID)
            if chatID not in chats:
                messages = []
            else:
                messages = chats[chatID]
            # print(messages)
            if len(messages) == 0:
                return (400, {
                    "messages": "Not Found"
                })
            return (200, {
                "messages": messages
            })
        except Exception as e:
            return (500, {
                "message": "paisi na"
            })

    app.listen(8000, cors=True)

main()