from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def enhance_prompt(user_prompt: str):

    system_prompt = """
You are an expert AI image prompt engineer.

Convert simple product descriptions into highly detailed,
photorealistic prompts suitable for AI image generation.

Include:
- lighting
- environment
- camera style
- realism
- advertisement quality
Keep response under 60 words.
Return ONLY the improved prompt.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content