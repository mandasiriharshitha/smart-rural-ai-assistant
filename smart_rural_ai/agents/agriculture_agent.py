import random
from mcp.weather_tool import get_weather

class AgricultureAgent:

    def process(self, query):

        weather = get_weather()

        tips = [
            "Maintain proper irrigation",
            "Use organic fertilizers",
            "Check soil nutrients",
            "Monitor pest activity"
        ]

        return f"""
🌾 Agriculture Agent

Weather: {weather['condition']} | {weather['temp']}

Advice:
- {random.choice(tips)}
"""