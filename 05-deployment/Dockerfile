# Use the provided base image
FROM agrigorev/zoomcamp-model:2025

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml .
COPY predict.py .

# Install dependencies using uv
RUN pip install uv && uv pip install --system .

# Expose the API port
EXPOSE 9696

# Run FastAPI app with Uvicorn
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
