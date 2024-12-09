# Use Python official image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
