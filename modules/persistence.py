import json


def parse_save_file(filepath="savegame.json"):
    """Loads saved game data from a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def export_game_session(filepath, player_state, event_log):
    """Saves the completed adventure log and final stats to a file."""
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("=== UNDER THE BREWERY FLOOR - ADVENTURE SUMMARY ===\n\n")
        file.write(f"Player State: {player_state}\n\n")
        file.write("Event Log:\n")
        for event in event_log:
            file.write(f"- {event}\n")
