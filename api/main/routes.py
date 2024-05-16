"Routes module"

from flask import render_template, redirect, url_for, flash, jsonify
from main import app, Session
from main.models import Player, Highlight, Statistic, Relation, Match
from main.forms import PlayerForm, UpdatePlayerForm, MatchForm
from main.utils import save_picture
import base64



@app.route("/", methods = ["POST", "GET"])
def main():
    "Main func"
    return render_template("petro_united.html")

@app.route("/players", methods = ["POST", "GET"])
def players_page():
    "Hikes view"
    session = Session()
    players = session.query(Player).all()
    return render_template("players.html", players = players, title = "Players")


@app.route("/create/player", methods = ["POST", "GET"])
def create_player():
    "Create trail func"
    form = PlayerForm()
    if form.validate_on_submit():
        session = Session()
        picture = save_picture(form.picture.data)
        trail = Player(first_name = form.first_name.data,
            last_name = form.last_name.data, 
            nickname = form.nickname.data,
            position = form.position.data,
            picture = picture)
        session.add(trail)
        session.commit()
        flash("Player added", category="success")
        return redirect(url_for("players_page"))
    return render_template("add_player.html", title = "Add Player",
            form = form, legend = "Add Player")

@app.route("/player/<int:player_id>", methods = ["POST", "GET"])
def player_page(player_id):
    "Trail page"
    session = Session()
    player = session.query(Player).filter_by(player_id = player_id).first()
    image_file = url_for('static', filename = 'profile_pics/' + player.picture)
    return render_template("player_page.html", player = player, 
            title = f"{player.first_name + ' ' + player.last_name} page", image_file = image_file)

@app.route("/player/update/<int:player_id>", methods = ["POST", "GET"])
def update_player(player_id):
    "Trail page"
    session = Session()
    player = session.query(Player).filter_by(player_id = player_id).first()
    form = UpdatePlayerForm()
    if form.validate_on_submit():
        session = Session()
        player = session.query(Player).filter_by(player_id = player_id).first()
        player.first_name = form.first_name.data
        player.last_name = form.last_name.data
        player.position = form.position.data
        player.nickname = form.nickname.data
        if form.picture.data:
            player.picture = save_picture(form.picture.data)
        session.commit()
        flash("Player updated", category="success")
        return redirect(url_for("players_page", player=player))
    form.first_name.data = player.first_name
    form.last_name.data = player.last_name
    form.position.data = player.position
    form.nickname.data = player.nickname
    return render_template("add_player.html", legend = "Update Player", form = form)

@app.route("/player/delete/<int:player_id>", methods = ["POST", "GET"])
def delete_player(player_id):
    "Delete trail"
    session = Session()
    player = session.query(Player).filter_by(player_id = player_id).first()
    session.delete(player)
    session.commit()
    flash("Player Deleted", category="warning")
    return redirect(url_for("players_page"))

@app.route("/matches", methods = ["POST", "GET"])
def matches_page():
    "Hikes view"
    session = Session()
    matches = session.query(Match).all()
    return render_template("matches.html", matches = matches, title = "Matches")

@app.route("/create/match", methods = ["POST", "GET"])
def create_match():
    "Create trail func"
    form = MatchForm()
    session = Session()
    players = session.query(Player).all()
    choices = [(str(player.player_id), player.first_name + " " + player.last_name) for player in players]
    form.players.choices = choices
    if form.validate_on_submit():
        session = Session()
        print(form.players.data)
        match = Match(start_time = form.start_time.data,
            rival_team = form.rival_team.data,
            team_score = form.team_score.data,
            rival_score = form.rival_score.data
            )
        session.add(match)
        session.commit()
        for player_id in form.players.data:
            relation = Relation(player_id = int(player_id), match_id = match.match_id)
            session.add(relation)
        session.commit()
        flash("Match added", category="success")
        return redirect(url_for("matches_page"))
    return render_template("add_match.html", title = "Add Match",
            form = form, legend = "Create Match")

@app.route("/match/<int:match_id>", methods = ["POST", "GET"])
def match_page(match_id):
    "Trail page"
    session = Session()
    match = session.query(Match).filter_by(match_id = match_id).first()
    players = []
    relations = session.query(Relation).filter_by(match_id = match.match_id).all()
    for relation in relations:
        player = session.query(Player).filter_by(player_id = relation.player_id).first()
        players.append(player)
    return render_template("match_page.html", match = match, players = players,
            title = f"Match Petro United - {match.rival_team} page")

@app.route("/match/update/<int:match_id>", methods = ["POST", "GET"])
def update_match(match_id):
    "Hike page"
    session = Session()
    match = session.query(Match).filter_by(match_id = match_id).first()
    players_lst = []
    relations = session.query(Relation).filter_by(match_id = match_id).all()
    for relation in relations:
        players_lst.append(str(relation.player_id))
    form = MatchForm()
    players = session.query(Player).all()
    choices = [(str(player.player_id), player.first_name + " " + player.last_name) for player in players]
    form.players.choices = choices
    if form.validate_on_submit():
        match = session.query(Match).filter_by(match_id = match_id).first()
        match.start_time = form.start_time.data
        match.rival_team = form.rival_team.data
        match.team_score = form.team_score.data
        match.rival_score = form.rival_score.data
        for relation in relations:
            session.delete(relation)
        for player_id in form.players.data:
            relation = Relation(player_id = int(player_id), match_id = match.match_id)
            session.add(relation)
        session.commit()
        flash("Match updated", category="success")
        return redirect(url_for("match_page", match_id = match_id))
    form.start_time.data = match.start_time
    form.rival_team.data = match.rival_team
    form.team_score.data = match.team_score
    form.rival_score.data = match.rival_score
    form.players.data = players_lst
    return render_template("add_match.html", legend = "Update Match", form = form)

import json 
@app.route("/api/get_all_player", methods = ["POST", "GET"])
def get_all_players():
    "Sends all players"
    session = Session()
    players = session.query(Player).all()
    player_dicts = []
    for player in players:
        with open('./main/static/profile_pics/' + player.picture, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        player_dicts.append({
            "player_id": player.player_id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "nickname": player.nickname,
            "position": player.position,
            "picture": encoded_image
    })
    json_data = json.dumps(player_dicts, indent=4)

# Write JSON data to a file
    with open("players_with_photos.json", "w") as json_file:
        json_file.write(json_data)
    return jsonify(player_dicts)

# @app.route("/hike/<int:hike_id>", methods = ["POST", "GET"])
# def hike_page(hike_id):
#     "Hike page"
#     session = Session()
#     hike = session.query(Hike).filter_by(hike_id = hike_id).first()
#     return render_template("hike_page.html", title = f"Hike_{hike_id} page", 
#             hike = hike)
    

# @app.route("/hike/delete/<int:hike_id>", methods = ["POST", "GET"])
# def delete_hike(hike_id):
#     "Delete hike"
#     session = Session()
#     hike = session.query(Hike).filter_by(hike_id = hike_id).first()
#     for hiker in hike.hikers:
#         session.delete(hiker)
#     session.delete(hike)
#     session.commit()
#     flash("Hike Deleted", category="warning")
#     return redirect(url_for("hikes_page"))

# @app.route("/hikers", methods = ["POST", "GET"])
# def hikers_page():
#     "Hikers page"
#     session = Session()
#     hikers = session.query(Hiker).all()
#     return render_template("hikers.html", title = "Hikers", hikers = hikers)

# @app.route("/create/hiker", methods = ["POST", "GET"])
# def create_hiker():
#     "Create hiker"
#     form = HikerForm()
#     session = Session()
#     hikes = session.query(Hike).all()
#     choices = [(str(hike.hike_id), "Hike - " + str(hike.hike_id)) for hike in hikes]
#     if not choices:
#         flash("There are no hikes available. Please add hikes before creating a hiker.", category="warning")
#         return redirect(url_for("create_hike"))
#     form.hikes.choices = choices
#     if form.validate_on_submit():
#         session = Session()
#         hiker = Hiker(first_name = form.first_name.data, last_name = form.last_name.data, 
#             age = form.age.data, gender = form.gender.data, 
#             experience_level = form.experience_level.data, hike_id = form.hikes.data)
#         session.add(hiker)
#         session.commit()
#         flash("Hike added", category="success")
#         return redirect(url_for("hikers_page"))
#     return render_template("add_hiker.html", form = form, legend = "Create Hiker")

# @app.route("/hiker/<int:hiker_id>", methods = ["POST", "GET"])
# def hiker_page(hiker_id):
#     "Hiker page"
#     session = Session()
#     hiker = session.query(Hiker).filter_by(hiker_id = hiker_id).first()
#     return render_template("hiker_page.html", title = f"Hiker_{hiker_id} page",
#                     hiker = hiker) 

# @app.route("/hiker/update/<int:hiker_id>", methods = ["POST", "GET"])
# def update_hiker(hiker_id):
#     "hiker page"
#     session = Session()
#     hiker = session.query(Hiker).filter_by(hiker_id = hiker_id).first()
#     form = HikerForm()
#     trails = session.query(Trail).all()
#     choices = [(str(trail.trail_id), trail.name) for trail in trails]
#     form.hikes.choices = choices
#     if form.validate_on_submit():
#         session = Session()
#         hiker = session.query(Hiker).filter_by(hiker_id = hiker_id).first()
#         hiker.first_name = form.first_name.data
#         hiker.last_name = form.last_name.data
#         hiker.age = form.age.data
#         hiker.gender = form.gender.data
#         hiker.experience_level = form.experience_level.data
#         hiker.hike_id = form.hikes.data
#         session.commit()
#         flash("Hiker updated", category="success")
#         return redirect(url_for("hiker_page", hiker_id=hiker_id))
#     form.first_name.data = hiker.first_name
#     form.last_name.data = hiker.last_name
#     form.age.data = hiker.age
#     form.gender.data = hiker.gender
#     form.experience_level.data = hiker.experience_level
#     form.hikes.data = str(hiker.hike_id)
#     return render_template("add_hiker.html", legend = "Update Hiker", form = form)

# @app.route("/hiker/delete/<int:hiker_id>", methods = ["POST", "GET"])
# def delete_hiker(hiker_id):
#     "Delete hike"
#     session = Session()
#     hiker = session.query(Hiker).filter_by(hiker_id = hiker_id).first()
#     session.delete(hiker)
#     session.commit()
#     flash("Hiker Deleted", category="warning")
#     return redirect(url_for("hikers_page"))
