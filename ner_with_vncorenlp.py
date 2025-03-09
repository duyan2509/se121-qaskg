from vncorenlp import VnCoreNLP
import os
SERVER_HOST = "http://127.0.0.1"
SERVER_PORT = 9000
BASE_DIR = os.path.dirname(__file__)
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
VnCoreNLP_SERVER_DIR = os.path.join(BASE_DIR, 'VnCoreNLP')
vncorenlp_path = os.path.join(VnCoreNLP_SERVER_DIR, 'VnCoreNLP-1.1.1.jar')

def ner_with_vncorenlp(input_text):
    with VnCoreNLP(vncorenlp_path, annotators="wseg,pos,ner", max_heap_size='-Xmx4g') as vncorenlp:
        annotations = vncorenlp.annotate(input_text)

        named_entities = []
        for sentence in annotations['sentences']:
            for word_info in sentence:
                if 'nerLabel' in word_info and word_info['nerLabel'] != 'O':
                    named_entities.append({
                        'word': word_info['form'],
                        'ner_label': word_info['nerLabel']
                    })

    return named_entities


def read_txt(txt_file):
    file_path = os.path.join(DATA_PROCESSED_DIR, txt_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()



def extract_entities_from_all_files(processed_dir):
    entities_by_file = {}

    for filename in os.listdir(processed_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(processed_dir, filename)
            input_text = read_txt(file_path)

            entities = ner_with_vncorenlp(input_text)
            entities_by_file[filename] = entities

            print(f"Đã trích xuất entity từ file: {filename}")

    return entities_by_file

if __name__ == '__main__':
    entities_results = extract_entities_from_all_files(DATA_PROCESSED_DIR)
    for file, entities in entities_results.items():
        print(f"File: {file}")
        print(f"Entities: {entities}")
