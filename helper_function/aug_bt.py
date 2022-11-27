import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import API_KEY

# based papago api
def papago_get_translate(text, In_lang, Out_lang):

    client_id = API_KEY.GET_TRANSLATE_ID()
    client_secret = API_KEY.GET_TRANSLATE_KEY()

    data = {'text' : text,       # text
            'source' : In_lang,  # Input lang
            'target': Out_lang}  # Output lang

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {'X-Naver-Client-Id' : client_id,
              'X-Naver-Client-Secret' : client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if rescode == 200:
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data

    else:
        print('Error Code : {0}'.format(rescode))


# based Pororo library
def Pororo_get_translate(text, In_lang, Out_lang):

    # 뽀로로 라이브러리 실험 해보기!
    
    return

def Pororo_en_to_ko():

    return

def Pororo_ko_to_en():

    return

def Pororo_en_to_jp():

    return

def Pororo_jp_to_en():

    return

def BT(df):

    return