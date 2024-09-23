# Use the official Python image from the Docker Hub
FROM python:3.11.7-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Set the application directory
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy local code to the container image
COPY . ./

# Install production dependencies
RUN pip install -r requirements.txt

# Expose the port (optional but recommended for documentation purposes)
EXPOSE 5000

# Set the default port for Flask to use
ENV PORT 5000

# Run the web service on container startup
#CMD exec gunicorn --bind :5000 --workers 1 --threads 8 --timeout 0 main:app
CMD ["sh", "-c", "flask --app main.py run --host=0.0.0.0 --port=5000 & streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0"]
