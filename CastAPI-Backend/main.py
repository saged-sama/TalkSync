from CastAPI import CastAPI

app = CastAPI()

@app.route("/post-message", "POST")
def post_message(req):
    message = f"Received your message '{req['body']['message']}'"
    return (200, {
        "message": message,
        "query": req["query"]
    })

app.listen(8000, cors=True)