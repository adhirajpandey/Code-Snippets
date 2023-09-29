import openai
import os
from dotenv import load_dotenv

load_dotenv()


openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_base = os.getenv("BASE_URL")
openai.api_key = os.getenv("API_KEY")

DEPLOYED_MODEL_NAME = "MyStatus"

def gen_response(prompt):
    response = openai.ChatCompletion.create(
        engine=DEPLOYED_MODEL_NAME,
        messages=[{"role": "system", "content": prompt}],
        temperature=0.5,
        max_tokens=950,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    response = response["choices"][0]["message"]["content"]

    return response


print(gen_response("Who are you?"))