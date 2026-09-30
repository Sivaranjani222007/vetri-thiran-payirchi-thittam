import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_nutrition_tip_with_flash(goal):
    prompt = f"""
Give one short, practical healthy nutrition or recovery tip
for a teenager.

Goal: {goal}

Keep it simple and age-appropriate.
Focus on balanced meals, hydration, fruits and vegetables,
protein-rich foods, whole grains, and healthy recovery habits.

Do not give calorie targets or restrictive diet advice.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print("Gemini nutrition error:", repr(e))
        return (
            "Stay hydrated and include a balanced variety of foods "
            "in your meals for healthy recovery."
        )
