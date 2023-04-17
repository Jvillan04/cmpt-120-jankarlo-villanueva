# import the flask package for making rest apis.
from flask import Flask
from flask import *
import uuid
from movies import movies


# create an instance of a Flask object.
app = Flask(__name__)
movies = []


@app.route("/", methods=["GET"])
def hello_world():
    '''
    This is our base route. When visited, we get the text "Hello, world!"
    '''
    return "Hello, world!"


@app.route("/api/movies", methods=["GET", "POST"])
def handle_movies():
    # GET & POST method logic
    """
    This function returns a Response object back containing all
    of stored movies and reviews back to the caller on the web.
    """
    if request.method == "GET":
        # previous GET logic
        response_body = movies

    titles = request.args.getlist("title")

        # only get the movies that have the same title as the query parameter.
    if titles:
        response_body = [movie for movie in movies if movie["title"] in titles]

        return jsonify(response_body)

    elif request.method == "POST":
        # new POST logic
        request_body = request.get_json()
        if request_body is None:
            return Response("Bad request", 400)
        if request_body["title"] is None:
            return Response("Bad request", 400)
        for mov in movies:
            if mov["title"] == request_body["title"]:
                return Response("Already exists", 409)
    else:
        data = request.json
        movies.append({
            "uuid": str(uuid.uuid4()),
            "title": data["title"],
            "review": data["review"]
        })
        return Response("Created", 201)

# This function below is not the same as the function above


@app.route("/api/movies/<mid>", methods=["GET", "DELETE"])
def handle_movie(mid: str) -> Response:
    if request.method == "GET":
        for m in movies:
            if m['uuid'] == mid:
                return jsonify(m)
        return Response("Not found", 404)
    elif request.method == "DELETE":
        for m in movies:
            if m['uuid'] == mid:
                movies.remove(m)
                return Response("No content", 204)
        return Response("Not found", 404)

#mid means move id
# run our application
if __name__ == '__main__':
    app.run()