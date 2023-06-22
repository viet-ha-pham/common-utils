import os
import math
from collections import Counter

def calculate_idf(corpus_dir):
    # Lấy danh sách tất cả các tài liệu trong thư mục corpus_dir
    all_files = [os.path.join(corpus_dir, f) for f in os.listdir(corpus_dir) if f.endswith('.txt')]

    # Đếm số lượng tài liệu
    num_docs = len(all_files)

    # Tạo một bộ đếm chung cho tất cả các tài liệu
    word_counts = Counter()

    # Đếm số lần xuất hiện của các từ trong từng tài liệu
    for file in all_files:
        with open(file, 'r', encoding='utf-8') as f:
            words_in_doc = set(f.read().lower().split())
            word_counts.update(words_in_doc)

    # Tính idf cho từng từ
    idf_values = {}
    for word, count in word_counts.items():
        idf_values[word] = math.log(num_docs / count)

    return idf_values
