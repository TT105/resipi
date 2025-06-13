import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# JSONファイルから食材と料理名のデータを読み込む
def load_data():
    with open("matched_meals_50.json", "r", encoding="utf-8") as f:
        return json.load(f)

recipes = load_data()

# 食材にマッチする料理名を提案
@app.route("/suggest", methods=["POST"])
def suggest_meals():
    input_data = request.get_json()
    input_ingredients = input_data.get("ingredients", [])

    suggestions = []
    for recipe in recipes:
        if all(ingredient in input_ingredients for ingredient in recipe["ingredients"]):
            suggestions.append(recipe["meal"])

    return jsonify({"suggestions": suggestions})

if __name__ == "__main__":
    app.run(debug=True)
