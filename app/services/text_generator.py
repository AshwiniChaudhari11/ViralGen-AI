from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.prompts.personas import PERSONAS
from app.prompts.platforms import PLATFORM_TEMPLATES

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_marketing_copy(product, platform, persona):

    system_prompt = PERSONAS.get(persona.lower())
    platform_prompt = PLATFORM_TEMPLATES.get(platform.lower())

    if not system_prompt or not platform_prompt:
        return "Invalid persona or platform"

    final_prompt = f"""
{platform_prompt}

Product Details:
{product}

Generate marketing copy now.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content