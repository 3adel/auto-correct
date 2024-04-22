import os
import ollama
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def show_common_typos_groq(word):
    chat_completion = client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": f"List the top 10 common typos or spelling mistakes of the word {word}. Don't o\
... utput anything else other than the comma separated list of common typos. Don't provide any other context. Don't include the input word in the list. Don't include synynoms of the input words as misspelled words. Don't output any notes or remarks",}
        ],
        model="llama3-8b-8192",
    )

    return chat_completion



def show_common_typos_ollama(word):
    response = ollama.chat(model='llama3:8b', messages=[
        {
    'role': 'user',
    "content": f"List the top 10 common typos or spelling mistakes of the word {word}. Don't o\
... utput anything else other than the comma separated list of common typos. Don't provide any other context. Don't include the input word in the list. Don't include synynoms of the input words as misspelled words. Don't output any notes or remarks",
    },])

    return response



file_path = "/Users/adel/adel/dev/playground/training data/auto-correct/sample.txt"
lines_count = 0
with open(file_path, "r") as file:
    for line in file:
        lines_count += 1
        #groq response
        #print(lines_count,line.strip(),": ",show_common_typos_groq(line.strip()).choices[0].message.content)

        #ollama response
        print(lines_count,line.strip(),": ",show_common_typos_ollama(line.strip())['message']['content'])


#Prompt




