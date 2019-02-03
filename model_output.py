from keras.models import model_from_json
from keras.preprocessing import text, sequence
import numpy
import pandas as pd
import os
import csv
import indexer


def predict_output(topics_data):
    # test = pd.read_csv(file)
    test = topics_data
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
    loaded_model.compile(loss='binary_crossentropy',
                         optimizer='adam', metrics=['accuracy'])

    # final_ans = test['id']

    y_pred = loaded_model.predict(x_test, batch_size=1024)

    counter = 0
    result = -1

    links = []

    with open('ans.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)

        for counter, row in enumerate(y_pred):
            max_value = max(row)
            max_index = list(row).index(max_value)

            if max_value < 0.03:
                result = 0
                links.append(test['id'][counter])
                # print(0)
            else:
                if(max_index == 0):
                    # print(1)
                    result = 1
                elif(max_index == 1):
                    # print(2)
                    result = 2
                elif(max_index == 2):
                    # print(3)
                    result = 3
                elif(max_index == 3):
                    # print(4)
                    result = 4
                elif(max_index == 4):
                    # print(5)
                    result = 5
                else:
                    # print(6)
                    result = 6
            writer.writerow([test['id'][counter], result])
            indexer.insert_element(test['id'][counter], result)
            # counter = counter + 1
    
    writeFile.close()
    print("Uncensored links")
    return links
