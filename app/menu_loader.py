import json
from functools import lru_cache
from pathlib import Path

MENU_PATH = Path("menu_data/menu.json")


@lru_cache()
def load_menu():
    """
    Load menu from JSON file with caching.
    This avoids re-reading file on every API call.
    """
    if not MENU_PATH.exists():
        raise FileNotFoundError("menu.json not found in /data folder")

    with open(MENU_PATH, "r", encoding="utf-8") as f:
        menu = json.load(f)

    return menu


def get_all_items_flat():
    """
    Flatten menu for fast lookup
    """
    menu = load_menu()
    items = []

    for category in menu.get("categories", []):
        for item in category.get("items", []):
            item_copy = item.copy()
            item_copy["category"] = category["name"]
            items.append(item_copy)

    return items


def find_item_by_name(name: str):
    """
    Case-insensitive item search
    """
    items = get_all_items_flat()

    name = name.lower()

    for item in items:
        if item["name"].lower() in name:
            return item

    return None