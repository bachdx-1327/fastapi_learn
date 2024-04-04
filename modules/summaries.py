import os
import pathlib
import textwrap
from dotenv import load_dotenv

# load_dotenv('..env', override=True)

# GOOGLE_API_KEY="AIzaSyB14Nzpol0htZ85pIvtlvm780UtgRYEM7Q"


# model = 

def summary_f(model, text = None):
    # print(model)
    # print(text)
    if text is None:
        raise ValueError("Text is required")
    
    prompt = """
    Summeries upper text to 1 - 2 sentences, give me the main idea of this text. 
    """
    contents = [
        text,
        prompt,
    ]

    responses = model.generate_content(contents, stream=True)
    text_s = ""
    for response in responses:
        text_s += response.text
    return text_s
