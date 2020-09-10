all: test

test:
	pytest -v --capture=no tests

download-kdd-data:
	python anomaly_detection/download_kdd_data.py

format:
	black anomaly_detection tests

lint:
	pytest -v --flake8 tests

freeze:
	pip freeze -r requirements.txt | tee constraints.txt
