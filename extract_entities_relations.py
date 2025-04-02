import os
import json
from vncorenlp import VnCoreNLP

BASE_DIR = os.path.dirname(__file__)
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
VnCoreNLP_SERVER_DIR = os.path.join(BASE_DIR, 'VnCoreNLP')
vncorenlp_path = os.path.join(VnCoreNLP_SERVER_DIR, 'VnCoreNLP-1.1.1.jar')

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_entities_and_relations(input_text):
    with VnCoreNLP(vncorenlp_path, annotators="wseg,pos,ner,parse", max_heap_size='-Xmx4g') as vncorenlp:
        annotations = vncorenlp.annotate(input_text)

        named_entities = []
        dependency_relations = []

        for sentence in annotations['sentences']:
            entities = []
            for word_info in sentence:
                if word_info['nerLabel'] != 'O':
                    entities.append({
                        'word': word_info['form'],
                        'ner_label': word_info['nerLabel'],
                        'index': word_info['index']
                    })
                    named_entities.append(entities[-1])

            for word_info in sentence:
                head_index = word_info['head']
                if head_index > 0:
                    head_word_info = sentence[head_index - 1]
                    dependency_relations.append({
                        'head': head_word_info['form'],
                        'dependent': word_info['form'],
                        'relation': word_info['depLabel']
                    })

    return named_entities, dependency_relations

def process_all_files(processed_dir):
    results = {}

    for filename in os.listdir(processed_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(processed_dir, filename)
            input_text = read_txt(file_path)

            entities, relations = extract_entities_and_relations(input_text)
            results[filename] = {
                'entities': entities,
                'relations': relations
            }

            print(f" Extracted from file: {filename}")

    return results

if __name__ == '__main__':
    extracted_data = process_all_files(DATA_PROCESSED_DIR)

    output_file = os.path.join(BASE_DIR,'data','extracted', 'extracted_data.json')
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(extracted_data, json_file, ensure_ascii=False, indent=4)

    print(f"\n Results saved to: {output_file}")
