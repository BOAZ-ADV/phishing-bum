def del_stop_words(text):

    # 불용어
    stopwords = ["도", "는", "다", "의", "가", "이", "은", "한", "에", "하", "고", "을", "를", "인", "듯", "과", "와", "네", "들", "듯", "지", "임", "게"]
    # 불용어 제거
    results = [text[i] for i in range(len(text)) if text[i] not in stopwords]

    return results

# sample code
'''
tr['tokenized_del_stopwords'] = tr['tokenize_txt'].apply(lambda x : del_stop_words(x))
'''