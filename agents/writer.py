from config import model

class WriterAgent:

    def write_post(self, summary):

        prompt = f"""
You are a Content Writer.

Using the summary below, write a professional LinkedIn post.

Summary:
{summary}

Requirements:
- Professional tone
- Around 150 words
- Add relevant hashtags
"""

        response = model.generate_content(prompt)

        return response.text