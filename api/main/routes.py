"Routes module"

import base64
import secrets
import os
import datetime
from flask import render_template, redirect, url_for, flash, jsonify, abort, request
from main import app, Session
from main.models import Player, Highlight, Statistic, Relation, Match
from main.forms import PlayerForm, UpdatePlayerForm, MatchForm, StatisticForm, HighlightForm
from main.utils import save_picture

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
    if not player:
        abort(404)
    image_file = url_for('static', filename = 'profile_pics/' + player.picture)
    return render_template("player_page.html", player = player, 
            title = f"{player.first_name + ' ' + player.last_name} page", image_file = image_file)

@app.route("/player/update/<int:player_id>", methods = ["POST", "GET"])
def update_player(player_id):
    "Trail page"
    session = Session()
    player = session.query(Player).filter_by(player_id = player_id).first()
    if not player:
        abort(404)
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
        return redirect(url_for("player_page", player_id = player.player_id))
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
    if not player:
        abort(404)
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
        statistic = Statistic(match_id = match.match_id)
        session.add(statistic)
        session.commit()
        flash("Match added", category="success")
        return redirect(url_for("matches_page"))
    form.team_score.data = 0
    form.rival_score.data = 0
    return render_template("add_match.html", title = "Add Match",
            form = form, legend = "Create Match")

@app.route("/match/<int:match_id>", methods = ["POST", "GET"])
def match_page(match_id):
    "Trail page"
    session = Session()
    match = session.query(Match).filter_by(match_id = match_id).first()
    if not match:
        abort(404)
    players = []
    statistic_id = int(match.statistics[0].statistic_id)
    relations = session.query(Relation).filter_by(match_id = match.match_id).all()
    for relation in relations:
        player = session.query(Player).filter_by(player_id = relation.player_id).first()
        players.append(player)
    return render_template("match_page.html", match = match, players = players,
            title = f"Match Petro United - {match.rival_team} page", statistic_id = statistic_id)

@app.route("/match/update/<int:match_id>", methods = ["POST", "GET"])
def update_match(match_id):
    "Hike page"
    session = Session()
    match = session.query(Match).filter_by(match_id = match_id).first()
    if not match:
        abort(404)
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

@app.route("/match/delete/<int:match_id>", methods = ["POST", "GET"])
def delete_match(match_id):
    "Delete match def"
    session = Session()
    match = session.query(Match).filter_by(match_id = match_id).first()
    if not match:
        abort(404)
    relations = session.query(Relation).filter_by(match_id = match_id).all()
    for relation in relations:
        session.delete(relation)
    statistic = session.query(Statistic).filter_by(match_id = match_id).first()
    session.delete(statistic)
    highlights = session.query(Highlight).filter_by(match_id = match_id).all()
    for highlight in highlights:
        os.remove("./main/static/highlights/" + highlight.video)
        session.delete(highlight)
    session.delete(match)
    session.commit()
    return redirect(url_for("matches_page"))

@app.route("/statistic/update/<int:statistic_id>", methods = ["POST", "GET"])
def update_statistic(statistic_id):
    "update statistic"
    session = Session()
    statistic = session.query(Statistic).filter_by(statistic_id=statistic_id).first()
    if not statistic:
        abort(404)
    form = StatisticForm()
    if form.validate_on_submit():
        statistic.hits_team = form.hits_team.data
        statistic.hits_rival = form.hits_rival.data
        statistic.hits_gate_team = form.hits_gate_team.data
        statistic.hits_gate_rival = form.hits_gate_rival.data
        statistic.falls_team = form.falls_team.data
        statistic.falls_rivals = form.falls_rivals.data
        statistic.yellow_cards_team = form.yellow_cards_team.data
        statistic.yellow_cards_rival = form.yellow_cards_rival.data
        statistic.red_cards_team = form.red_cards_team.data
        statistic.red_cards_rival = form.red_cards_rival.data
        statistic.offsides_team = form.offsides_team.data
        statistic.offsides_rivals = form.offsides_rivals.data
        statistic.corners_team = form.corners_team.data
        statistic.corners_rivals = form.corners_rivals.data
        session.commit()
        return redirect(url_for("match_page", match_id = statistic.match_id))
    form.hits_team.data = statistic.hits_team
    form.hits_rival.data = statistic.hits_rival
    form.hits_gate_team.data = statistic.hits_gate_team
    form.hits_gate_rival.data = statistic.hits_gate_rival
    form.falls_team.data = statistic.falls_team
    form.falls_rivals.data = statistic.falls_rivals
    form.yellow_cards_team.data = statistic.yellow_cards_team
    form.yellow_cards_rival.data = statistic.yellow_cards_rival
    form.red_cards_team.data = statistic.red_cards_team
    form.red_cards_rival.data = statistic.red_cards_rival
    form.offsides_team.data = statistic.offsides_team
    form.offsides_rivals.data = statistic.offsides_rivals
    form.corners_team.data = statistic.corners_team
    form.corners_rivals.data = statistic.corners_rivals
    return render_template("statistic_page.html", form = form, 
            legend = "Statistic Page", title = "Statistic Update")

@app.route("/match/highlights/<int:match_id>", methods = ["POST", "GET"])
def match_highlights_page(match_id):
    "Highlights page"
    session = Session()
    highlights = session.query(Highlight).filter_by(match_id = match_id).all()
    return render_template("highlights.html", highlights = highlights, match_id = match_id, legend = "Highlights")

@app.route("/match/highlight/add/<int:match_id>", methods = ["POST", "GET"])
def highlight_add(match_id):
    "Add highlight"
    form = HighlightForm()
    if form.validate_on_submit():
        session = Session()
        file = form.video.data
        old_name, file_extension = os.path.splitext(file.filename)
        old_name = f'{old_name}{file_extension}'
        filename = secrets.token_hex(20)
        file_name = "./main/static/highlights/" + f'{filename}{file_extension}'
        file.save(file_name)
        highlight = Highlight(title = form.title.data, video = f'{filename}{file_extension}', match_id = match_id)
        session.add(highlight)
        session.commit()
        return redirect(url_for("match_highlights_page", match_id = match_id))
    return render_template("add_highlight.html", title = "Add Highlight", 
        legend = "Add Highlight", form = form)

@app.route("/match/highlight/delete/<int:highlight_id>", methods = ["POST", "GET"])
def highlight_delete(highlight_id):
    "Highlight id"
    session = Session()
    highlight = session.query(Highlight).filter_by(highlight_id=highlight_id).first()
    if not highlight:
        abort(404)
    match_id = highlight.match_id
    os.remove("./main/static/highlights/" + highlight.video)
    session.delete(highlight)
    session.commit()
    return redirect(url_for("match_highlights_page", match_id = match_id))

@app.route("/api/get_all_player", methods = ["POST", "GET"])
def get_all_players():
    "Sends all players"
    session = Session()
    players = session.query(Player).all()
    player_dicts = {"Attacker": [], "Midfielder": [], "Defender": [], "Goalkeeper": []}
    for player in players:
        with open('./main/static/profile_pics/' + player.picture, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        player_dicts[player.position].append({
            "player_id": player.player_id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "nickname": player.nickname,
            "picture": encoded_image
        })
    return jsonify([player_dicts])

@app.route("/api/get_recent_highlights", methods = ["POST", "GET"])
def get_recent_highlights():
    "Sends all players"
    session = Session()
    highlights = session.query(Highlight).all()
    highlights_dicts = []
    for highlight in highlights:
        video_ref = url_for('static', filename = 'highlights/' + highlight.video)
        highlights_dicts.append({
            "highlight_id": highlight.highlight_id,
            "title": highlight.title,
            "date": highlight.match.start_time,
            "video": video_ref
        })
    highlights_dicts.sort(key = lambda elem: elem["date"])
    return jsonify(highlights_dicts[:6])

@app.route("/api/get_all_matches", methods = ["POST", "GET"])
def get_all_matches():
    "Sends all matches"
    session = Session()
    matches = session.query(Match).all()
    matches_dict = []
    for match in matches:
        today = datetime.datetime.now()
        json_obj = {
            "match_id": match.match_id,
            "rival_team": match.rival_team,
            "team_score": match.team_score,
            "rival_score": match.rival_score,
            "start_time": match.start_time,
            "ongoing": today < match.start_time
        }
        matches_dict.append(json_obj)
    return jsonify(matches_dict)

@app.route("/api/get_closest_ongoing_match", methods = ["POST", "GET"])
def get_closest_ongoing_match():
    "Sends all matches"
    session = Session()
    matches = session.query(Match).all()
    matches_dict = []
    for match in matches:
        today = datetime.datetime.now()
        if today < match.start_time:
            json_obj = {
                "match_id": match.match_id,
                "rival_team": match.rival_team,
                "team_score": match.team_score,
                "rival_score": match.rival_score,
                "start_time": match.start_time
            }
            matches_dict.append(json_obj)
    matches_dict.sort(key = lambda elem: elem["start_time"])
    return jsonify(matches_dict[0])

@app.route("/api/get_match_info_by_id", methods = ["POST", "GET"])
def get_match_info_by_id():
    "Get Match info By Id"
    data = request.json
    match_id = data["match_id"]
    session = Session()
    match = session.query(Match).filter_by(match_id = match_id).first()
    matches_dict = {"Match": {}, "Highlights": [], "Statistic": {}, "Players": []}
    today = datetime.datetime.now()
    json_obj = {
        "match_id": match.match_id,
        "rival_team": match.rival_team,
        "team_score": match.team_score,
        "rival_score": match.rival_score,
        "start_time": match.start_time,
        "ongoing": today < match.start_time
    }
    matches_dict["Match"] = json_obj
    statistic = match.statistics[0]
    stats = {
        "hits_team": statistic.hits_team,
        "hits_rival": statistic.hits_rival,
        "hits_gate_team": statistic.hits_gate_team,
        "hits_gate_rival": statistic.hits_gate_rival,
        "falls_team": statistic.falls_team,
        "falls_rivals": statistic.falls_rivals,
        "yellow_cards_team": statistic.yellow_cards_team,
        "yellow_cards_rival": statistic.yellow_cards_rival,
        "red_cards_team": statistic.red_cards_team,
        "red_cards_rival": statistic.red_cards_rival,
        "corners_team": statistic.corners_team,
        "corners_rivals": statistic.corners_rivals
    }
    matches_dict["Statistic"] = stats
    relations = session.query(Relation).filter_by(match_id = match_id).all()
    players = []
    for relation in relations:
        players.append(session.query(Player).filter_by(player_id = relation.player_id).first())
    for player in players:
        with open('./main/static/profile_pics/' + player.picture, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        matches_dict["Players"].append({
            "player_id": player.player_id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "nickname": player.nickname,
            "picture": encoded_image
        })
    for highlight in match.highlights:
        video_ref = url_for('static', filename = 'highlights/' + highlight.video)
        matches_dict["Highlights"].append({
            "highlight_id": highlight.highlight_id,
            "title": highlight.title,
            "date": highlight.match.start_time,
            "video": video_ref
        })
    return jsonify(matches_dict)
