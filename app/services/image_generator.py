import base64
import uuid
from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.agents.prompt_enhancer import enhance_prompt

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_image(user_prompt: str):

    # Enhance prompt
    enhanced_prompt = enhance_prompt(user_prompt)

    # Generate image
    result = client.images.generate(
        model="gpt-image-1",
        prompt=enhanced_prompt,
        size="1024x1024"
    )

    # Get base64 image
    image_base64 = result.data[0].b64_json

    # Decode image
    image_bytes = base64.b64decode(image_base64)

    # Create unique filename
    filename = f"generated_{uuid.uuid4().hex}.png"
    filepath = f"static/{filename}"

    # Save image locally
    with open(filepath, "wb") as f:
        f.write(image_bytes)

    return {
        "enhanced_prompt": enhanced_prompt,
        "image_url": f"http://127.0.0.1:8000/static/{filename}"
    }