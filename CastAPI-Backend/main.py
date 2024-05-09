from CastAPI import CastAPI
from datetime import datetime

def main():
    app = CastAPI()
    users = {
        'saged': ('sajid', 'notadoctor')
    }

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
            print(searchUser)
            results = []
            for username in users:
                if searchUser in username:
                    name, _ = users[username]
                    results.append({"username": username, "name": name})
                    print(searchUser, username)
            print(results)
            return (200, {
                "users": results
            })
        except Exception as e:
            return (500, {
                "message": "Could not search usernames"
            })

    # # Chat
    # @app.route("/post-message", "POST")
    # def post_message(req):
    #     try:
    #         chatID = req["body"]["chatID"]
    #         userID = req["body"]["userID"]
    #         message = req["body"]["message"]
    #         media = req["body"]["media"]

    #         date = datetime.now().strftime("%Y-%m-%%d %H:%M:%S")

    #         db.con.execute("insert into message values(?, ?, ?, ?, ?)", [chatID, userID, message, media, date])
    #         return (200, {
    #             "message": "successfully added message"
    #         })

    #     except Exception as e:
    #         print(f"Error posting new Message: {e}")
    #         return (400, {
    #             "message": "Could not add message"
    #         })

    # @app.route("/get-messages", "GET")
    # def get_messages(req):
    #     try:
    #         userId = req["body"]["userid"]

    #         db.con.execute("select * from message where userid = ?", [userId])
    #         message = db.con.fetchone()[0]
    #         return (200, {
    #             "message": message
    #         })
    #     except Exception as e:
    #         return (500, {
    #             "message": "paisi na"
    #         })

    app.listen(8000, cors=True)

main()