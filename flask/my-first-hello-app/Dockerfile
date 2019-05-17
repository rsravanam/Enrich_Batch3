FROM python

RUN pip install flask

RUN mkdir /app

WORKDIR /app

COPY ./hello.py .

ENV FLASK_APP=hello.py

#EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["hello.py"]
