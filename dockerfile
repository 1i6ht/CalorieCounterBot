FROM python:3.8
WORKDIR /app
RUN pip install ast
RUN pip install requests
RUN pip install python-telegram-bot
RUN pip install typing

COPY ..
CMD ["python", "tel-bot.py"]