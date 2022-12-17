import pandas as pd

def make_dataset():

    # 데이터 로드
    df = pd.read_csv(r'C:\Project\phishing_bum\phishing-bum\data\fin.csv')

    # X, y
    X = df['txt']
    y = df['label']
    # print(f'X, y shape : {X.shape}, {y.shape}\n')

    return X, y