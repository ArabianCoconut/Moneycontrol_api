FROM python:3.11.4-alpine
LABEL Author="Arabian Coconut"

# Set the working directory to /app
WORKDIR /app
COPY . /app
EXPOSE 5000

#Flask Environment Variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=CoconutMagic

# Install packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt && \
    rm requirements.txt

# CD into Flask directory
WORKDIR /app/Src

# Run Flask when the container launches
CMD ["flask","run"]