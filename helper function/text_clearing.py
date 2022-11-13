def text_clearing(text):

    hangul = re.compile('[^ ㄱ-ㅣㅏ-ㅣ가-힣]+') # 한글이 아닌 텍스트를 찾음
    
    return hangul.sub('', text).split() # 치환할 문자열, target text