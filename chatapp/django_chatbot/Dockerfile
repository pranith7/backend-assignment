# Use an official Python runtime as a parent image
FROM python:3.10-alpine 

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE django_chatbot.settings

# Create and set the working directory
WORKDIR /app

# Copy the project code into the container
COPY requirements.txt /app/requirements.txt
# Install postgres client
RUN apk add --update --no-cache postgresql-client
# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev

# Remove dependencies
RUN apk del .tmp-build-deps

# Install project dependencies
RUN pip install -r requirements.txt 
COPY . /app/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# # Set work directory
# WORKDIR /code

# # Install dependencies
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# # Copy project
# COPY . .

