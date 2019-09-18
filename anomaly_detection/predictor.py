import pickle


class PredictionResult(dict):
    def __init__(self, is_anomaly, score, is_error, message):
        dict.__init__(
            self, is_anomaly=is_anomaly, score=score, is_error=is_error, message=message
        )


class Predictor(object):
    def __init__(self) -> None:
        self.trainer = None

    def load(self, filename):
        with open(filename, mode="rb") as f:
            self.trainer = pickle.load(f)

    def predict(self, features):
        # trainerを使って賢く分類するようにしましょう
        return PredictionResult(
            is_anomaly=False, score=0.0, is_error=False, message=None
        )
