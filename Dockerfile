FROM python:3.9.0-slim

RUN apt-get -yq update && apt-get install -yq tk-dev git curl jq

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt -c constraints.txt

CMD ["/bin/bash"]
