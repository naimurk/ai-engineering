import os
from scraper import fetch_website_contents
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI
from reponseParse import responseParse
# import end


# dotenv 
load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
# print(api_key)


if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")




    message = "Hello, GPT! This is my first ever message to you! Hi!"





    openai = OpenAI()

  



ed = fetch_website_contents("https://naimurrahman.vercel.app/")



system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""



user_prompt_prefix = ed




messages = [
 
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix}
    ]


response = openai.chat.completions.create(model="gpt-6-luna", reasoning_effort="none", messages=messages) 
print(responseParse(response))