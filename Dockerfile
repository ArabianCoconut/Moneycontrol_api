FROM python:3.11.4-alpine

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "executable" ]
LABEL maintainer="Arabian Coconut"

# Set the working directory to /app
WORKDIR /app
COPY . /app
EXPOSE 5000

#Flask Environment Variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=ArabianCoconut

# Install packages specified in requirements.txt
# trunk-ignore(checkov/CKV2_DOCKER_4)
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt && \
    rm requirements.txt\
    python3 -m compileall .

# CD into Flask directory
WORKDIR /app/src

# Run Flask when the container launches
CMD ["flask","run"]