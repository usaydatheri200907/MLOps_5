FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy frontend files
COPY ./index.html /app/index.html
COPY ./script.js /app/script.js
COPY ./style.css /app/style.css

# Expose port 8000
EXPOSE 8000

# Command to start the server
CMD ["python", "-m", "http.server", "8000"]
