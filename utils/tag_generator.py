import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tags(product_name, product_description):
    prompt = f"Suggest 5 relevant tags for a product with the name '{product_name}' and description '{product_description}'"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    
    tags_text = response.choices[0].text.strip()
    tags = [tag.strip() for tag in tags_text.split(',')]
    return tags
