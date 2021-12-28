
import requests
from flask import redirect, render_template, request, session
from functools import wraps
import food


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def complexSearch(foodname):
    """Look up quote for symbol."""

    # Contact API
    try:
        url = f"https://api.spoonacular.com/recipes/complexSearch?query={foodname}&minCarbs=0&minProtein=0&minCalories=0&minFat=0&number=1&minSugar=0&apiKey=fae840d1e0ac4a73a10dcddb3537deab"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        food = response.json()
        return {
            
            "id": food["results"][0]["id"],
            "title": food["results"][0]["title"],
            "image": food["results"][0]["image"],
            "nutrition": food["results"][0]["nutrition"]['nutrients']
        }
    except (KeyError, TypeError, ValueError):
        return None

def Search(foodname):
    """Look up quote for symbol."""

    # Contact API
    try:
        url = f"https://api.spoonacular.com/food/search?query={foodname}&number=2&apiKey=fae840d1e0ac4a73a10dcddb3537deab"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        food = response.json()
        return {
            "food": food["results"],
            "id": food["results"][0]["id"],
            "title": food["results"][0]["title"],
            "image": food["results"][0]["image"],
            "nutrition": food["results"][0]["nutrition"]['nutrients']
        }
    except (KeyError, TypeError, ValueError):
        return None