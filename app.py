import os
from flask import Flask, render_template, request, redirect, url_for
from db import get_player, add_player, add_match, add_skin

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/player", methods=["POST"])
def query_player():
    name = request.form["name"]
    player = get_player(name)
    return render_template("player.html", name=name, player=player)

@app.route("/add_player", methods=["GET", "POST"])
def add_player_route():
    if request.method == "POST":
        name = request.form["name"]
        level = int(request.form["level"])
        win_rate = float(request.form["win_rate"])
        success = add_player(name, level, win_rate)
        return redirect(url_for("index"))
    return render_template("add_player.html")

@app.route("/add_match", methods=["GET", "POST"])
def add_match_route():
    if request.method == "POST":
        name = request.form["name"]
        result = request.form["result"]
        hero = request.form["hero"]
        kills = int(request.form["kills"])
        deaths = int(request.form["deaths"])
        success = add_match(name, result, hero, kills, deaths)
        return redirect(url_for("index"))
    return render_template("add_match.html")

@app.route("/add_skin", methods=["GET", "POST"])
def add_skin_route():
    if request.method == "POST":
        name = request.form["name"]
        skin = request.form["skin"]
        success = add_skin(name, skin)
        return redirect(url_for("index"))
    return render_template("add_skin.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
