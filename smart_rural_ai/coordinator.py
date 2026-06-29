from agents.safety_agent import SafetyAgent
from agents.agriculture_agent import AgricultureAgent
from agents.education_agent import EducationAgent
from agents.schemes_agent import SchemesAgent


class CoordinatorAgent:

    def __init__(self):
        self.safety = SafetyAgent()
        self.agriculture = AgricultureAgent()
        self.education = EducationAgent()
        self.schemes = SchemesAgent()

    # SMART ROUTING
    def route(self, query):
        q = query.lower()

        if any(w in q for w in ["crop", "farm", "soil", "plant", "dry", "yellow"]):
            return "agriculture"

        if any(w in q for w in ["scheme", "loan", "pm", "government", "scholarship"]):
            return "schemes"

        if any(w in q for w in ["what is", "explain", "define", "dbms", "study", "how"]):
            return "education"

        return "education"

    def handle(self, query):

        if not self.safety.is_safe(query):
            return "⚠️ Query blocked by Safety Agent."

        intent = self.route(query)

        reasoning = f"🧠 Detected Intent: {intent.upper()}"

        if intent == "agriculture":
            response = self.agriculture.process(query)

        elif intent == "education":
            response = self.education.process(query)

        elif intent == "schemes":
            response = self.schemes.process(query)

        else:
            response = "Cannot process request."

        return reasoning + "\n\n" + response