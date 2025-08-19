import numpy as np
import os
import pandas as pd
import sklearn.naive_bayes 

data = [
    [1, 1, 1, 0, 'spam'],
    [1, 1, 0, 0, 'spam'],
    [0, 1, 1, 0, 'spam'],
    [1, 0, 1, 0, 'spam'],
    [0, 0, 0, 1, 'not_spam'],
    [0, 0, 1, 1, 'not_spam'],
    [0, 1, 0, 1, 'not_spam'],
    [1, 0, 0, 1, 'not_spam'],
]

df = pd.DataFrame(data, columns=['has_link', 'has_money_word', 'is_short', 'sender_known', 'label'])

