"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from last_hope import app

@app.route('/')


class Move:
    def __init__(self, player_name, move_type, timestamp):
        self.player_name = player_name
        self.move_type = move_type
        self.timestamp = timestamp

def rate_move(move):
    if move.move_type == "banish":
        return 3  # Banish moves are generally considered more effective
    elif move.move_type == "land_on_luck_card":
        return 2  # Luck card moves have some impact on the game
    else:
        return 1  # Other moves have a smaller impact

def extract_info(move_list):
    # Initialize the result dictionary
    result = {
        "num_banish_moves": 0,
        "num_luck_card_moves": 0
    }
    
    # Loop through the move list and count the number of banish and luck card moves
    for move in move_list:
        if move.move_type == "banish":
            result["num_banish_moves"] += 1
        elif move.move_type == "land_on_luck_card":
            result["num_luck_card_moves"] += 1
    return result

@app.route("/dashboard")
def dashboard():
    # Retrieve the move data from the database or a file
    moves = get_moves()
    
    # Calculate the statistics and pass them to the template
    num_moves = len(moves)
    num_banish_moves = sum(1 for move in moves if move.move_type == "banish")
    num_luck_card_moves = sum(1 for move in moves if move.move_type == "land_on_luck_card")
    return render_template("dashboard.html", num_moves=num_moves, num_banish_moves=num_banish_moves, num_luck_card_moves=num_luck_card_moves)

@app.route("/report")
def report():
    # Retrieve the move data from the database or a file
    moves = get_moves()
    
    # Process the move data using the analysis functions
    move_ratings = [rate_move(move) for move in moves]
    move_info = extract_info(moves)
    
    # Generate the report
    report = generate_report(move_ratings, move_info)
    
    # Pass the report data to the template
    return render_template("report.html", report=report)
if __name__ == '__main__':
    app.run()