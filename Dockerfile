FROM tensorflow/tensorflow:latest-gpu

COPY . /app
WORKDIR /app
RUN python -m pip install -U garak

