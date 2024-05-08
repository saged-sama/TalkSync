from CastAPI import CastAPI
from database import database
from datetime import datetime

app = CastAPI()
db = database("talksync.db")


# Auth



# Chat
@app.route("/post-message", "POST")
def post_message(req):
    try:
        chatID = req["body"]["chatID"]
        userID = req["body"]["userID"]
        message = req["body"]["message"]
        media = req["body"]["media"]

        date = datetime.now().strftime("%Y-%m-%%d %H:%M:%S")

        db.con.execute("insert into message(?, ?, ?, ?, ?)", [chatID, userID, message, media, date])

    except Exception as e:
        print(f"Error posting new Message: {e}")

app.listen(8000, cors=True)