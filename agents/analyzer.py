from config import model

class AnalyzerAgent:

    def analyze(self, research):

        prompt = f"""
You are an Analysis Agent.

Analyze the following research and generate a concise summary.

Research:
{research}

Instructions:
- Summarize in 5-8 bullet points.
- Keep it clear and professional.
"""

        response = model.generate_content(prompt)

        return response.text