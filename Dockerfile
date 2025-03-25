# ใช้ Python image
FROM python:3.10-slim

# ตั้ง working directory
WORKDIR /app

# Copy โค้ดเข้าไป
COPY app/ /app/
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# รัน Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
