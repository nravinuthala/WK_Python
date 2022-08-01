
scores = [0, 0]
current_score = 0
active_player = 0
playing = True

def init():
    scores = [0, 0]
    current_score = 0
    active_player = 0
    playing = True

def switch_player():
    current_score = 0
    active_player = 1 if active_player == 0 else 1