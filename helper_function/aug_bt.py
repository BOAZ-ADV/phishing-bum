import sys
import os

# googletrans
from googletrans import Translator

# pororo app key
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


# googletrans
def get_translate(text, inlang, outlang):

    translator = Translator()
    trans = translator.translate(text, src=inlang, dest=outlang)

    print(f'translation result : {trans.text}')

    return trans.text

# ko to en
def BT_ko2en(text):

    get_translate(text, 'ko', 'en')

    return

# en to ko
def BT_en2ko(text):

    get_translate(text, 'en', 'ko')

    return

# ko to jp
def BT_ko2jp(text):

    get_translate(text, 'ko', 'jp')

    return

# jp to ko
def BT_jp2ko(text):

    get_translate(text, 'jp', 'ko')

    return


''' sample '''
# get_translate('안녕하세요!', 'ko', 'en')
# BT_en2ko('hello')