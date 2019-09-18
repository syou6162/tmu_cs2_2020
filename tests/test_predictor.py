import unittest
import pickle
from anomaly_detection.trainer import Trainer
from anomaly_detection.predictor import Predictor


class TestPredict(unittest.TestCase):
    def setUp(self):
        self.model_filename = "my_model_file.bin"
        with open("data/train.pickle", mode="rb") as f:
            self.train_data = pickle.load(f)["features"]
        trainer = Trainer()
        trainer.train(self.train_data)
        trainer.save(self.model_filename)

    def test_predict(self):
        predictor = Predictor()
        predictor.load(self.model_filename)
        result = predictor.predict([1, 2, 3])

        assert result["is_anomaly"] is False
        assert result["is_error"] is False
        assert result["score"] == 0.0
        assert result["message"] is None

    # 様々な入力ケースに対してテストを書いていきましょう
