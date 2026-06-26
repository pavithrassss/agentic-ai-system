from config import model

class PlannerAgent:
    def create_plan(self, user_task):
        prompt = f"""
You are a planning agent.

Break the following user request into clear, ordered execution steps.

User Request:
{user_task}

Rules:
- Return only the numbered steps.
- Keep the steps short and clear.
- Do not explain anything else.
"""

        response = model.generate_content(prompt)

        return response.text