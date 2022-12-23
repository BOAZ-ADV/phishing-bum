from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold

from helper_function import preprocessing
from helper_function import aug_bt
from helper_function import metrics
import dataset

from lightgbm import LGBMClassifier

import pandas as pd
import numpy as np
import re
import pickle
import time

from tqdm import tqdm
tqdm.pandas() # progress

import warnings
warnings.filterwarnings('ignore')


# start train.py
print('\n== start train.py ==')

# load data
X, y = dataset.make_dataset()

# model list
model_list = []


def train(X, y, model='LGBM'):

    kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    k = kfold.get_n_splits(X, y)
    # print(f'split k : {k}')
    cnt_kfold = 1
    best_acc, best_f1 = 0, 0 # to save best model

    # == k-fold idx ==
    for tr_idx, val_idx in kfold.split(X, y):

        # k-fold
        print(f'\n== K-FOLD {cnt_kfold} ==\n')
        print(f'TRAIN : {tr_idx}')   # kfold train index
        print(f'VALID : {val_idx}')  # kfold test index

        # == split ==
        X_tr, X_val = X.iloc[tr_idx], X.iloc[val_idx]
        y_tr, y_val = y.iloc[tr_idx], y.iloc[val_idx]
        X_tr, X_val, y_tr, y_val = pd.DataFrame(X_tr), pd.DataFrame(X_val), pd.DataFrame(y_tr), pd.DataFrame(y_val)

        # == tr aug ==
        out = pd.concat([X_tr, y_tr], axis=1)
        out_en = out[out['label'] == 1].copy()
        print(out_en)
        return
        out_en['txt'] = X_tr['txt'].progress_apply(lambda x : aug_bt.BT_ko2en(x))
        out_en['txt'] = out_en['txt'].apply(lambda x : aug_bt.BT_en2ko(x))
        out_en_y = pd.DataFrame({'label' : [1] * len(out_en)}) # y_tr.copy()
        # print('Done. (aug)')
        
        # tr concat : origin + aug
        X_tr_aug = pd.concat([X_tr, out_en], ignore_index=True)
        y_tr_fin = pd.concat([y_tr, out_en_y], ignore_index=True)
        # print('Done. (concat)')
        
        # == tr preprocessing ==
        X_tr_aug['txt'] = preprocessing.drop_duplicates(X_tr_aug['txt'])                    # 데이터 중복 제거
        X_tr_aug['txt'] = preprocessing.drop_null(X_tr_aug['txt'])                          # 결측치 제거
        X_tr_aug['txt'] = X_tr_aug['txt'].apply(lambda x : preprocessing.text_cleansing(x)) # 텍스트 킄렌징
        X_tr_aug['txt'] = X_tr_aug['txt'].apply(lambda x : preprocessing.text_tokenize(x))  # 토큰화
        X_tr_aug['txt'] = X_tr_aug['txt'].apply(lambda x : preprocessing.del_stopwords(x))  # 불용어 제거
        X_tr_fin = preprocessing.encoder_tf(X_tr_aug['txt'])                                # X_tr_fin & fit_transform tf-idf encoder 생성
        # print('Done. (tr preprocessing)')

        # == val preprocessing ==
        X_val['txt'] = preprocessing.drop_duplicates(X_val['txt'])
        X_val['txt'] = preprocessing.drop_null(X_val['txt'])
        X_val['txt'] = X_val['txt'].apply(lambda x : preprocessing.text_cleansing(x))
        X_val['txt'] = X_val['txt'].apply(lambda x : preprocessing.text_tokenize(x))
        X_val['txt'] = X_val['txt'].apply(lambda x : preprocessing.del_stopwords(x))
        X_val_fin = preprocessing.encoding_tf(X_val['txt'])
        # print('Done. (val preprocessing) \n')

        # == train model ==
        clf = LGBMClassifier()
        clf.fit(X_tr_fin, y_tr_fin) # , callbacks=[tqdm_callback])

        # == eval model ==
        pred = clf.predict(X_val_fin)
        acc, f1 = metrics.metrics(y_val, pred)
        print(f'tr acc, f1 : {acc}, {f1}')
        time.sleep(0.5)
        # print('Done. (train/eval model) \n')

        # == check best model == 
        if f1 > best_f1:
            # == save best model and vectorizer ==
            best_f1 = f1
            best_acc = acc
            best_model = clf
            pickle.dump(best_model, open(r'C:\Project\phishing_bum\phishing-bum\result\best_f1_model.pkl', 'wb')) # save best model
            preprocessing.save_encoder_tf(X_tr_aug['txt']) # save best encoder
            
        cnt_kfold += 1

    return


''' sample '''
train(X, y)