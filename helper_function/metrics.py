from sklearn.metrics import accuracy_score, f1_score

def metrics(y, pred):

    acc = accuracy_score(y, pred)
    f1 = f1_score(y, pred, average='macro')

    return round(acc, 5), round(f1, 5)