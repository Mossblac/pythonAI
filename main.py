import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_files import schema_write_file


def main():
    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    parser = argparse.ArgumentParser(description="a scripts with a verbose option")
    parser.add_argument("prompt")
    parser.add_argument("--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()

    prompt = args.prompt
   
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]), 
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
    )   # detrmine if a tool was used to call a function; if the tools=[available_functions] == True?
    x = response.usage_metadata.prompt_token_count
    y = response.usage_metadata.candidates_token_count

    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {x}")
        print(f"Response tokens: {y}")
        print(response.text)
    else:
        if response.function_calls:
            for function_call in response.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")
        else: print(response.text)


if __name__ == "__main__":
    main()