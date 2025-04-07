import json

with open('./data/chunked_texts_docx.json', 'r', encoding='utf-8') as f:
    chunks = json.load(f)

print(chunks)