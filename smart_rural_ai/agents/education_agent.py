import random

class EducationAgent:

    def process(self, query):

        intro = [
            "Let me explain this simply:",
            "Here’s an easy explanation:",
            "Breaking it down:"
        ]

        examples = [
            "Think of it like a real-world system.",
            "Imagine it like a structured process.",
            "Compare it with daily life examples."
        ]

        return f"""
🎓 Education Agent

{random.choice(intro)}
{query}

{random.choice(examples)}
"""