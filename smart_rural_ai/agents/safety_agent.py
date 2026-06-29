class SafetyAgent:

    def is_safe(self, query):
        banned = ["hack", "weapon", "illegal", "attack", "kill"]

        for b in banned:
            if b in query.lower():
                return False

        return True