import arcade
import Inventory

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

def stats_display():
    """Displays resources and stats"""

    # resource displays
    arcade.draw_text(("Iron: ", Inventory.iron), 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 14)
    arcade.draw_text(("Nickel: ", Inventory.nickel), 20, SCREEN_HEIGHT - 60, arcade.color.WHITE, 14)
    arcade.draw_text(("Gold: ", Inventory.gold), 20, SCREEN_HEIGHT - 80, arcade.color.WHITE, 14)
    arcade.draw_text(("Copper: ", Inventory.copper), 20, SCREEN_HEIGHT - 100, arcade.color.WHITE, 14)
    arcade.draw_text(("Platinum: ", Inventory.platinum), 20, SCREEN_HEIGHT - 120, arcade.color.WHITE, 14)
    arcade.draw_text(("Unobtanium: ", Inventory.unobtanium), 20, SCREEN_HEIGHT - 140, arcade.color.WHITE, 14)

    # stats
    arcade.draw_text(("HP: ", Inventory.hp), 20, SCREEN_HEIGHT - 160, arcade.color.WHITE, 14)
    arcade.draw_text(("Shield: ", Inventory.hullShield), 20, SCREEN_HEIGHT - 180, arcade.color.WHITE, 14)
    arcade.draw_text(("Regen: ", Inventory.healthRegen), 20, SCREEN_HEIGHT - 200, arcade.color.WHITE, 14)

def inventory_display():
    pass