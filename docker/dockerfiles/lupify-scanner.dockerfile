FROM python:3

WORKDIR /lupify-scanner

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install netaddr
RUN pip install pymongo

COPY ./lupify-scanner /lupify-scanner

CMD [ "python", "/lupify-scanner/lupify-scanner.py" ]