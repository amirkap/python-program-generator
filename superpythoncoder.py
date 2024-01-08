import os, subprocess, random, sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")


PROGRAMS_LIST = [
    '''Create a program that given two strings str1 and str2, prints all interleavings of the given
    two strings. You may assume that all characters in both strings are
    different.Input: str1 = "AB",  str2 = "CD"
    Output:
        ABCD
        ACBD
        ACDB
        CABD
        CADB
        CDAB
    Input: str1 = "AB",  str2 = "C"
    Output:
        ABC
        ACB
        CAB  ''',
    "Create a program that checks if a number is a palindrome",
    "Create a program that finds the kth smallest element in a given binary search tree." ,
    "Create a program that recursively generates all permutations of a given list of unique integers.",
    '''You are given the heads of two sorted linked lists list1 and list2.
Create a program that merges the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
  Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
  Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order. Don't forget unittests.''',
]

def get_random_program():
    return random.choice(PROGRAMS_LIST)

def get_user_prompt():
    # Ask the user for the type of program they want to create
    user_input = input("\nTell me, which program would you like me to code for you? If you don't have an idea, just press enter and I will choose a random program.\n")
    return user_input
  
def get_full_prompt():
  extra_instructions =   ". Also, please include unit tests that check the logic of the program using 5 different inputs and expected outputs."  \
  "Make sure you have a main method for your program. Run tests first and then run the actual program I asked you to create." \
  "Return only the code in the completion. " \
  "I don't want any other comments. " \
  "Don't say 'here is your code' or similar remarks." \
   
  user_input = get_user_prompt()
  if not user_input:
    user_input = get_random_program()
    print(user_input)

  return user_input + extra_instructions 

def write_program_to_file(generated_code):
    with open('generatedcode.py', 'w', encoding='utf-8') as file:
        file.write(generated_code)    
            
def extract_code(response_content):
  # Define start and end expressions
    start_expression = '```python' if '```python' in response_content else '```' 
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

def write_and_execute_program(generated_code):
  with open('generatedcode.py', 'w', encoding='utf-8') as file:
      file.write(generated_code)
  subprocess.run([sys.executable, 'generatedcode.py']) 
  
def main():
  successful = False
  # Initialize OpenAI client with API key
  client = OpenAI(api_key=api_key, organization=org_id)
  conversation = [
      {"role": "system", "content": "You are an expert Python developer, who is able to write clean and aesthetic code. Don't explain the code, just generate the code block itself." \
       "You always remember to add unit tests to every program you create."},
      {"role": "assistant", "content": "Tell me, which program would you like me to code for you? If you don't have an idea, just press enter and I will choose a random program."},
      {"role": "user", "content": get_full_prompt()}
      ]

  for i in range(5):
    print("Attempt number " + str(i+1) + ":\n")
    chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation
  )
    response_content = chat_completion.choices[0].message.content
    generated_code = extract_code(response_content)
    write_program_to_file(generated_code)
    try:
      subprocess.run([sys.executable, 'generatedcode.py'], stderr=subprocess.PIPE, check=True, text=True)
      successful = True
      break
    except subprocess.CalledProcessError as e:
        print(f"Error running main program! Error:\n{e.stderr}")
        conversation.append({"role": "assistant", "content": generated_code})
        conversation.append( {"role": "user", "content": "I got this error:\n" + e.stderr + 
        "\nPlease fix the code you gave me and show the whole code fixed." \
        "Return only the fixed code in the completion. " \
        "I don't want any other comments. " \
        "Don't say 'here is your code' or similar remarks."})
        
  if not successful:
    print("Code generation FAILED")
  else:
    print("Code creation completed successfully !")
    subprocess.call(['open', 'generatedcode.py'])
    
if __name__ == "__main__":
    main()
