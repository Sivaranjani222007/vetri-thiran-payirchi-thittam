import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_fitness_plan(goal, intensity):
    prompt = f"""
Create a safe, beginner-friendly 7-day workout plan for a teenager.

Goal: {goal}
Intensity: {intensity}

For each day include:
- Warm-up (5–10 minutes)
- Main activity with simple exercise details
- Cooldown or recovery tip
- Suitable rest/recovery days

Do not give calorie targets or encourage weight loss.
Keep the plan age-appropriate, general and safety-focused.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"
