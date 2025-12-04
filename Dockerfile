FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY main.py .
COPY pyproject.toml .
COPY Data/ Data/
COPY Notebooks/ Notebooks/

# Expose Streamlit port
EXPOSE 8501

# Configure Streamlit
RUN mkdir -p ~/.streamlit && echo '[server]\nport = 8501\nheadless = true\nenableXsrfProtection = false\n[browser]\ngatherUsageStats = false' > ~/.streamlit/config.toml

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
