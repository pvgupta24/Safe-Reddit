from keras.models import model_from_json
from keras.preprocessing import text, sequence
import numpy
import pandas as pd
import os

def predict_output(file):
    test = pd.read_csv(file)
    maxlen = 100
    max_features = 30000
    X_test = test["comment_text"].fillna("fillna").values
    tokenizer = text.Tokenizer(num_words=max_features)
    tokenizer.fit_on_texts(list(X_test))
    X_test = tokenizer.texts_to_sequences(X_test)
    x_test = sequence.pad_sequences(X_test, maxlen=maxlen)

    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    y_pred = loaded_model.predict(x_test, batch_size=1024)
    results = {}
    count = 0 
    for row in y_pred:
        max_value = max(row)
        max_index = list(row).index(max_value)
        if max_value < 0.03:
            print(0)
        else:
            if(max_index ==0):
                print(1)
            elif(max_index ==1):
                print(2)
            elif(max_index==2):
                print(3)
            elif(max_index==3):
                print(4)
            elif(max_index==4):
                print(5)
            else:
                print(6)
