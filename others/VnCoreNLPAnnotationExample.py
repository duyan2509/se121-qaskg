import os
import time
from vncorenlp import VnCoreNLP

# Define the base directory
BASE_DIR = os.path.dirname(__file__)
VnCoreNLP_SERVER_DIR = os.path.join(BASE_DIR, 'VnCoreNLP')

# Path to the VnCoreNLP jar file
vncorenlp_path = os.path.join(VnCoreNLP_SERVER_DIR, 'VnCoreNLP-1.1.1.jar')

def simple_usage():
    vncorenlp_file = vncorenlp_path

    sentences = 'VTV đồng ý chia sẻ bản quyền World Cup 2018 cho HTV để khai thác. ' \
                'Nhưng cả hai nhà đài đều phải chờ sự đồng ý của FIFA mới thực hiện được điều này.'

    # Use only word segmentation
    with VnCoreNLP(vncorenlp_file, annotators="wseg") as vncorenlp:
        print('Tokenizing:', vncorenlp.tokenize(sentences))

    # Specify the maximum heap size
    with VnCoreNLP(vncorenlp_file, annotators="wseg", max_heap_size='-Xmx4g') as vncorenlp:
        print('Tokenizing:', vncorenlp.tokenize(sentences))

    # For debugging
    with VnCoreNLP(vncorenlp_file, annotators="wseg", max_heap_size='-Xmx4g', quiet=False) as vncorenlp:
        print('Tokenizing:', vncorenlp.tokenize(sentences))


def ner_with_vncorenlp(input_text):
    with VnCoreNLP(vncorenlp_path, annotators="wseg,pos,ner", max_heap_size='-Xmx4g') as vncorenlp:
        annotations = vncorenlp.annotate_text(input_text)

        named_entities = []
        for sentence in annotations['sentences']:
            for word_info in sentence:
                if 'nerLabel' in word_info and word_info['nerLabel'] != 'O':
                    named_entities.append({
                        'word': word_info['form'],
                        'ner_label': word_info['nerLabel']
                    })

    return named_entities


if __name__ == '__main__':
    simple_usage()
