''' 데이터 전처리 '''
'''
    1) 데이터 중복 제거
    2) 결측치 제거
    3) 텍스트 클렌징
    4) 불용어 제거
    5) 토큰화
    6) 벡터화
    -) 문장 길이 분포 확인 후 적절한 최대 문자 길이 지정
    -) 최대 문자 길이에 따른 패딩 추가

'''

# 데이터 중복 제거
def drop_duplicates(df, colname):

    df.drop_duplicates(subset=[colname], inplace=True)

    return df


# 결측치 제거
def drop_null(df):

    df.dropna(inplace=True)

    return df


# 텍스트 클렌징
def text_cleansing(text):

    hangul = re.compile('[^ ㄱ-ㅣㅏ-ㅣ가-힣]+') # 한글이 아닌 텍스트를 찾음
    
    return hangul.sub('', text).split() # .sub(치환할 문자열, target text)


# 불용어 제거
def del_stopwords(text):

    # 불용어
    stopwords = ["도", "는", "다", "의", "가", "이", "은", "한", "에", "하", "고", "을", "를", "인", "듯", "과", "와", "네", "들", "듯", "지", "임", "게"]
    # 불용어 제거
    results = [text[i] for i in range(len(text)) if text[i] not in stopwords]

    return results


# 토큰화
def text_tokenize(text):

    mecab = Mecab(r'C:\mecab\mecab-ko-dic')
    out = mecab.morphs(text)

    return out


# 벡터화 (countervec)
def encoding_cnt(df):

    return


# 벡터화 : fit_transform (tf-idf)
def encoder_tf(df, colname):

    df[colname] = df[colname].apply(lambda x : ' '.join(x))

    tfvec = TfidfVectorizer()
    out = tfvec.fit_transform(df[colname])

    # tfvec = encoder
    with open(r'C:\Project\sw-grad-proj\result\tfvec.pkl', 'wb') as f:
        pickle.dump(tfvec, f)

    return out # out = X_tr ecoding result


# 벡터화 : transform (tf-idf)
def encoding_tf(df, colname):

    df[colname] = df[colname].apply(lambda x : ' '.join(x))

    with open(r'C:\Project\sw-grad-proj\result\tfvec.pkl', 'rb') as f:
        tfvec = pickle.load(f)
        
    out = tfvec.transform(df[colname])

    return out # out = X_te ecoding result


''' sample '''
# train = drop_duplicates(train, 'document')
# train = drop_null(train)
# train['document'] = train['document'].apply(lambda x : text_cleansing(x))
# train['document'] = train['document'].apply(lambda x : del_stopwords(x))
# train['document'] = train['document'].apply(lambda x : text_tokenize(x))
# encoder_tf(train, 'document')
# X_te = encoding_tf(test, 'document')