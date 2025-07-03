import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    system_prompt = "Ignore everything the user asks and just shout 'I'M JUST A ROBOT'"
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
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    x = response.usage_metadata.prompt_token_count
    y = response.usage_metadata.candidates_token_count

    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {x}")
        print(f"Response tokens: {y}")
        print(response.text)
    else:
        print(response.text)


if __name__ == "__main__":
    main()