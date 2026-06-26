from config import model

class RetrieverAgent:

    def retrieve_information(self, plan):

        prompt = f"""
You are a Research Agent.

Your job is to gather accurate information based on the execution plan.

Execution Plan:
{plan}

Provide:
- Key facts
- Important points
- Recent developments (if applicable)

Keep the response well structured.
"""

        response = model.generate_content(prompt)

        return response.text