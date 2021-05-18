# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . app/

# Install any needed packages specified in requirements.txt
RUN pip install pandas
RUN npm install
RUN pip install streamlit

# Make port 80 available to the world outside this container
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]

# Run app.py when the container launches
CMD ["app.py"]



