from CastAPI import CastAPI
from database import database
from datetime import datetime

app = CastAPI()
db = database("talksync.db")


# Auth
@app.route("/sign-up", "POST")
def register(req):
    try:
        username = req["body"]["username"]
        password = req["body"]["password"]
        name = req["body"]["name"]

        db.con.execute("insert into user (username, password, name) values(?, ?, ?)", [username, password, name])
        return (200, {
            "message": "Successfully registered new user"
        })
    except Exception as e:
        print("Could not register new ID: ", e)
        return (500, {
            "message": "Could not add new user"
        })

@app.route("/log-in", "POST")
def register(req):
    try:
        username = req["body"]["username"]
        password = req["body"]["password"]

        db.con.execute("select count(*) from user where username = ? and password = ?", [username, password])
        if db.con.fetchone()[0] > 0:
            return (200, {
                "message": "Successful log in"
            })
        else:
            return (401, {
                "message": "Unauthorized"
            })
    except Exception as e:
        print("Could not log in: ", e)
        return (500, {
            "message": "Could not log in"
        })

# Chat
@app.route("/post-message", "POST")
def post_message(req):
    try:
        chatID = req["body"]["chatID"]
        userID = req["body"]["userID"]
        message = req["body"]["message"]
        media = req["body"]["media"]

        date = datetime.now().strftime("%Y-%m-%%d %H:%M:%S")

        db.con.execute("insert into message values(?, ?, ?, ?, ?)", [chatID, userID, message, media, date])
        return (200, {
            "message": "successfully added message"
        })

    except Exception as e:
        print(f"Error posting new Message: {e}")
        return (400, {
            "message": "Could not add message"
        })

app.listen(8000, cors=True)