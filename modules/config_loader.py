import json


def load_game_config(rooms_path="data/rooms.json"):
    """Reads room, monster, and item data from configuration files."""
    try:
        with open(rooms_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error loading game config: {error}")
        return {}


def format_room_description(room):
    """Formats room descriptions, exits, items, and monsters for console display."""
    if not room:
        return "You are in an unknown void."

    lines = [
        f"\n=== {room.get('name', 'Unknown Room')} ===",
        room.get("description", "No description available."),
    ]

    exits = list(room.get("exits", {}).keys())
    lines.append(f"Exits: {', '.join(exits) if exits else 'None'}")

    items = room.get("items", [])
    if items:
        lines.append(f"Items here: {', '.join(items)}")

    monsters = room.get("monsters", [])
    if monsters:
        lines.append(f"Enemies present: {', '.join(monsters)}")

    return "\n".join(lines)
