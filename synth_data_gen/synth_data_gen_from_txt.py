import os
import ollama
from groq import Groq

# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )


# def show_common_typos_groq(word):
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#             "role": "user",
#             "content": f"You're an expert on the English language and also an expert on the spelling mistkes english speakers make when they use a keyboard to type words. List the top five common spelling mistakes of the word {word}. Output only a comma separated list of the common spelling mistakes with the first one being the most common. Don't provide any other context. Don't include the given correct input word in the list. Don't include synynoms of the input words as misspelled words. Don't output any notes or remarks. The output list should contain non-words only",}
#         ],
#         model="llama3-8b-8192",
#     )

#     return chat_completion



def show_common_typos_ollama(word):
    response = ollama.chat(model='llama3', messages=[
        {
    'role': 'user',
    "content": f"List the top 10 common non-word spelling errors for the word '{word}'. These errors should be typos that do not form real English words and should be more than 1 characters long. Provide a comma-separated list of these errors only. Ensure the list does not include '{word}', synonyms of '{word}', or any additional text or explanation.",
    },])

    return response



source_file_path = "/Users/adel/adel/dev/training_data/auto-correct/100k_wikidictionary_most_used_english_words/cleaned/clean_wiki-100k.txt"
lines_count = 0
with open(source_file_path, "r") as file:
    for line in file:
        lines_count += 1
        #groq response
        # print(lines_count,line.strip(),": ",show_common_typos_groq(line.strip()).choices[0].message.content)

        #ollama response
        print(lines_count,line.strip(),": ",show_common_typos_ollama(line.strip())['message']['content'])


#Prompt


