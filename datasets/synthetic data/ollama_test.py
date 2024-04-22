import ollama
response = ollama.chat(model='llama3:8b', messages=[
  {
    'role': 'user',
    "content": f"List the top 10 common typos or spelling mistakes of the word computer. Don't o\
... utput anything else other than the comma separated list of common typos. Don't provide any other context. Don't include the input word in the list. Don't include synynoms of the input words as misspelled words. Don't output any notes or remarks",
  },
])
print(response['message']['content'])