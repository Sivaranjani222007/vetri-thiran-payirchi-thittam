import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def update_workout_plan(original_plan, feedback):
    prompt = f"""
Update the following workout plan based on the user's feedback.

Original Plan:
{original_plan}

User Feedback:
{feedback}

Return the complete updated 7-day workout plan.

Keep the plan safe, beginner-friendly, age-appropriate and general.
Include warm-up, main activity, cooldown/recovery and suitable rest days.
Do not recommend extreme exercise, rapid weight loss or restrictive dieting.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"
