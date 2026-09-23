from getpass import getpass
from google import genai


api_key = getpass("Paste your API key and press Enter: ")


client = genai.Client(api_key=api_key)


def ask(question):
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=question,
    )
    return interaction.output_text

print(ask("What is a Python dictionary?"))