# Use an official lightweight Python image
# "slim" variants are smaller and more secure for production
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (Caching layer)
# This is a best practice. If requirements.txt doesn't change, 
# Docker uses the cached layer, making builds faster.
COPY requirements.txt .

# Install dependencies
# --no-cache-dir keeps the image size small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a non-root user to run the app
# This is a security best practice (Production Ready)
RUN useradd -m myuser
USER myuser

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
# "python" is the command, "app.py" is the argument
CMD ["python", "app.py"]