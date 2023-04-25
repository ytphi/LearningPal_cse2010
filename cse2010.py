import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview" 
openai.api_base = os.getenv("OPENAI_API_BASE") # Your Azure OpenAI resource's endpoint value.
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    engine="cse2010-learning-pal", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
    messages=[
        {"role": "system", "content": "Assistant is an intelligent c++ lab tutor."},
        {"role": "user", "content": "What the derived class is and give an example"}
    ]
)

print(response)

print(response['choices'][0]['message']['content'])