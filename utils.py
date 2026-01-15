def validate_input(user_input, valid_options):
    """Validate user input against list of valid options"""
    return user_input.lower() in valid_options

def format_score(user_score, computer_score):
    """Format score display"""
    return f"Player: {user_score} | Computer: {computer_score}"

def get_win_percentage(wins, total_games):
    """Calculate win percentage"""
    if total_games == 0:
        return 0
    return (wins / total_games) * 100