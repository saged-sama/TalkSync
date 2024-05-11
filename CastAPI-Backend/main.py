from CastAPI import CastAPI
from datetime import datetime
import mimetypes

def read_file_info(file_name):
    mtype, _ = mimetypes.guess_type(file_name)
    if mtype is None:
        mtype = "application/octet-stream"

    with open(file_name, "rb") as file:
        content = file.read()
    
    flength = len(content)

    return {
        "isbin": True,
        "mimetype": mtype,
        "content-length": flength,
        "file": content
    }

def main():
    app = CastAPI()
    users = {
        'saged': ('sajid', 'notadoctor', "files-profilepic-image.jpeg")
    }
    chats = {}

    @app.route("/set-profile-picture", "POST")
    def saveimage(req):
        username = req["body"]["username"]
        image = bytes(map(int, req["body"]['image'].split(',')))
        ext = req["body"]["type"].split("/")[-1]
        imageDir = f"files/profilepic/{username}.{ext}"

        with open(imageDir, "wb") as file:
            file.write(image)
        
        return (200, {
            "image": imageDir
        })

    # Auth
    @app.route("/sign-up", "POST")
    def register(req):
        try:
            print(req["body"])
            username = req["body"]["username"]
            password = req["body"]["password"]
            name = req["body"]["name"]
            image = req["body"]["image"].replace("/", "-")

            users[username] = (name, password, image)
            print(users)
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

            _, pss, __ = users[username]
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
    
    @app.route("/get-users", "GET")
    def get_users(req):
        try:
            results = []
            for username in users:
                name, _, image = users[username]
                results.append({"username": username, "name": name, "image": image})
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
            # print(chatID)
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
        
    @app.route("/get-image-path", "GET")
    def get_image_path(req):
        username = req["query"]["username"]
        _, __, imagepath = users[username]

        return(200, {
            "imagepath": imagepath
        })

    @app.route("/get-file", "GET")
    def get_image(req):
        path = req["query"]["path"].replace("-", "/")
        # print(path)
        body = read_file_info(path)
        # print(body)
        # print(body["mimetype"], body["content-length"])
        return (200, body)

    app.listen(8000, cors=True)

main()