from sklearn.datasets import fetch_kddcup99
import pickle

features, labels = fetch_kddcup99(subset="http", return_X_y=True)
labels = list(map(lambda label: 0 if label == b"normal." else 1, labels))

NUM_OF_TRAINING_EXAMPLES = 50000

# 先頭のNUM_OF_TRAINING_EXAMPLES件を学習データに、それ以降をテストデータとする

with open("data/train.pickle", mode="wb") as f:
    pickle.dump(
        {
            "features": features[:NUM_OF_TRAINING_EXAMPLES],
            "labels": labels[:NUM_OF_TRAINING_EXAMPLES],
        },
        f,
    )

with open("data/test.pickle", mode="wb") as f:
    pickle.dump(
        {
            "features": features[NUM_OF_TRAINING_EXAMPLES:],
            "labels": labels[NUM_OF_TRAINING_EXAMPLES:],
        },
        f,
    )
