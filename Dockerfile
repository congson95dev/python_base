FROM python:3.8.13-slim-buster

# -p meaning created if the folder is not exists, if it does exists, then ignore this command
RUN mkdir -p /app
# copy current directory and main.py to /app/
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
# python main.py
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]