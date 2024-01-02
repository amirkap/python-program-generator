import os, subprocess
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")


def get_user_prompt():
    # Ask the user for the type of program they want to create
    user_input = input("What kind of program do you want to create? Enter your request: ") + "."
    return user_input
  
def get_full_prompt():
  extra_instructions = " Return only the code in the completion. \
   I don't want any other comments. Don't say 'here is your code' or similar remarks.."
  return (get_user_prompt() + extra_instructions)
    
def extract_code(response_content):
  # Define start and end expressions
    start_expression = '```python'
    end_expression = '```'

    # Find the starting index of the code block
    start_index = response_content.find(start_expression)

    # Find the ending index of the code block
    end_index = response_content.find(end_expression, start_index + len(start_expression))

    # Check if both expressions are found
    if start_index != -1 and end_index != -1:
        # Extract the code between start and end expressions
        code_block = response_content[start_index + len(start_expression):end_index].strip()
        return code_block
    else:
      code_block = response_content

    return code_block

def main():
  # Initialize OpenAI client with API key
  client = OpenAI(api_key=api_key, organization=org_id)
  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=1.3,
    messages=[
      {"role": "system", "content": "You are an expert Python developer, who is able to write clean and aesthetic code. Don't explain the code, just generate the code block itself."},
      {"role": "assistant", "content": "What kind of program do you want me to create? Enter your request: "},
      {"role": "user", "content": get_full_prompt()}
    ]
  )

  response_content = chat_completion.choices[0].message.content
  generated_code = extract_code(response_content)
  
  with open('generatedcode.py', 'w', encoding='utf-8') as file:
      file.write(generated_code)
  subprocess.run(['python', 'generatedcode.py'])    

if __name__ == "__main__":
    main()
