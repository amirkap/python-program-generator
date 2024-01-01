import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")

# Initialize OpenAI client with API key
client = OpenAI(api_key=api_key, organization=org_id)
chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  temperature=1.3,
  messages=[
    {"role": "system", "content": "You are an expert Python developer, who is able to write clean and aesthetic code. Don't explain the code, just generate the code block itself."},
    {"role": "user", "content": "Create a Pong game in Python. Return only the code in the completion. I don't want any other comments. Don't say 'here is your code' or similar remarks.."}
  ]
)

print(chat_completion.choices[0].message.content)

