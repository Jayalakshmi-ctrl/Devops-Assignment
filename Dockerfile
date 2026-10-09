# Step 1: Base Build Engine
FROM python:3.11-slim

# Step 2: Establish isolated execution landscape
WORKDIR /app

# Step 3: Layer dependencies to leverage Docker cache optimization
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Import Application codebase 
COPY . .

# Step 5: Enforce Non-Root Security Best Practices
RUN useradd -m devopsuser && chown -R devopsuser:devopsuser /app
USER devopsuser

# Step 6: Define execution metadata 
EXPOSE 5000

# Step 7: Run via web server interface
CMD ["python", "app.py"]
