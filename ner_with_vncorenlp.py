from vncorenlp import VnCoreNLP
import os
SERVER_HOST = "http://127.0.0.1"
SERVER_PORT = 9000
BASE_DIR = os.path.dirname(__file__)
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')


def ner_with_vncorenlp(input_text):
    # Kết nối VnCoreNLP server
    print("in")
    with VnCoreNLP(f"{SERVER_HOST}:{SERVER_PORT}", annotators="wseg,pos,ner") as vncore_client:
        # Thực hiện NER
        annotations = vncore_client.annotate(input_text)

        # Ghi nhận các thực thể nhận diện được
        named_entities = []
        for sentence in annotations['sentences']:
            for word_info in sentence:
                if 'nerLabel' in word_info and word_info['nerLabel'] != 'O':  # Nếu có nhãn thực thể
                    named_entities.append({
                        'word': word_info['form'],  # Từ/tổ hợp từ
                        'ner_label': word_info['nerLabel']  # Loại thực thể
                    })

        return named_entities


def read_txt(txt_file):
    file_path = os.path.join(DATA_PROCESSED_DIR, txt_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()



def extract_entities_from_all_files(processed_dir):
    entities_by_file = {}  # Kết quả sẽ lưu từng file và các entity tương ứng

    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(processed_dir):
        if filename.endswith('.txt'):  # Chỉ xử lý file .txt
            file_path = os.path.join(processed_dir, filename)  # Tạo đường dẫn đầy đủ
            input_text = read_txt(file_path)  # Đọc nội dung file

            # Thực hiện trích xuất NER (giả sử bạn có hàm ner_with_vncorenlp)
            entities = ner_with_vncorenlp(input_text)  # Hàm NER của bạn
            entities_by_file[filename] = entities  # Lưu kết quả với tên file

            print(f"Đã trích xuất entity từ file: {filename}")

    return entities_by_file  # Trả lại kết quả toàn bộ entity theo file


entities_results = extract_entities_from_all_files(DATA_PROCESSED_DIR)

for file, entities in entities_results.items():
    print(f"File: {file}")
    print(f"Entities: {entities}")
