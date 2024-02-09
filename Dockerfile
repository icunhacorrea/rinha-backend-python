FROM python:3.11-slim

WORKDIR /

COPY rinhaapi/ rinhaapi/

COPY run_api.sh /

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN chmod +x run_api.sh

ENTRYPOINT ["./run_api.sh"]

