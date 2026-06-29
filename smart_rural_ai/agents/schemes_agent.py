import json

class SchemesAgent:

    def process(self, query):

        with open("mcp/scheme_db.json", "r") as f:
            data = json.load(f)

        result = "\n".join([f"- {k}: {v}" for k, v in data.items()])

        return f"""
🏛️ Government Schemes

{result}
"""