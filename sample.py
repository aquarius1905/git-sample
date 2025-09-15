def add_key_value(key, value, dct=None):
    if dct is None:
        dct = {}
    dct[key] = value
    return dct

print(add_key_value('a', 1))  # {'a': 1}
print(add_key_value('b', 2))


def predict_fn(input_data, model):
    global preprocessor
    
    # 入力データを前処理（例：トークン化など）する
    inputs = preprocessor.tokenize(input_data)
    
    # 推論時は勾配計算を無効化
    with torch.no_grad():
        outputs = model(inputs)
    
    return outputs