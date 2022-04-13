"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route("/")
def start_here():
    """Display homepage."""

    return render_template("home.html")


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

@app.route("/greet")
def greet_person():
    # """Ask user if they would like to play."""

    return render_template("compliment.html")

@app.route("/game")
def show_madlib_form():
    """Asks the user if they want to play a game"""
    
    #render_template("compliment.html")
    game_decision = request.args.get("game")
    print(game_decision)
    if game_decision =='no': 
        return render_template("goodbye.html")
    else:   
        return render_template("game.html")
    

@app.route("/madlib")
def show_madlib():
    """Return the final madlib."""

    number = request.args.get("number")
    verb = request.args.get("verb")
    adverb = request.args.get("adverb")
    feeling = request.args.get("feeling")
    adjective = request.args.get("adjective")
    noun = request.args.get("noun")
    another_number = request.args.get("another-number")
    another_adjective = request.args.get("another-adjective")
    third_adjective = request.args.get("third-adjective")
    instructor_name = request.args.get("instructor-name")
    animal = request.args.get("animal")
    niche_topic = request.args.get("niche-topic")
    another_verb = request.args.get("another-verb")
    time_of_day = request.args.get("time-of-day")
    last_number = request.args.get("last-number")
    name = request.args.get("name")


    return render_template("madlib.html", 
                            number=number,
                            verb=verb,
                            adverb=adverb,
                            feeling=feeling,
                            adjective=adjective,
                            noun=noun,
                            another_number=another_number,
                            another_adjective=another_adjective,
                            third_adjective =third_adjective,
                            instructor_name=instructor_name,
                            animal = animal,
                            niche_topic = niche_topic,
                            another_verb = another_verb,
                            time_of_day = time_of_day,
                            last_number = last_number,
                            name=name
                            )
    
if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
