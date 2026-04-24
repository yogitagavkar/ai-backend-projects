import re
from app.order_manager import OrderManager
from app.menu_loader import load_menu, find_item_by_name

order = OrderManager()
menu = load_menu()


def extract_quantity(text):
    match = re.search(r"\d+", text)
    return int(match.group()) if match else 1


def extract_modifiers(text):
    """
    Basic modifier extraction
    """
    modifiers = []

    if "less spicy" in text.lower():
        modifiers.append("less spicy")
    if "no onion" in text.lower():
        modifiers.append("no onion")
    if "extra cheese" in text.lower():
        modifiers.append("extra cheese")

    return modifiers


def format_menu():
    response = "\n🍽️ MENU\n"

    for cat in menu["categories"]:
        response += f"\n🔹 {cat['name']}\n"
        for item in cat["items"]:
            response += f"- {item['name']} (₹{item['price']}): {item['description']}\n"

    return response


def handle_chat(user_input):
    user_input_lower = user_input.lower()

    if "menu" in user_input_lower:
        return str(format_menu())   # ✅ ensure string

    if "bill" in user_input_lower:
        return order.calculate_bill()  # dict OK

    item = find_item_by_name(user_input)

    if item:
        qty = extract_quantity(user_input)
        modifiers = extract_modifiers(user_input)

        return order.add_item(
            item["name"],
            qty,
            item["price"],
            modifiers
        )

    return "Sorry, I didn’t understand."