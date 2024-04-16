# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# EXPOSE 3009
# Run climbing-stairs.py when the container launches
CMD ["python", "climbing_stairs.py", "5"]
