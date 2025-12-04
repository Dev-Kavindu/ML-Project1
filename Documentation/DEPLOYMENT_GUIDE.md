# 🚀 Deployment Guide - Sales Prediction ML Application

**Deploy your Streamlit ML application to production in minutes!**

This guide covers multiple deployment options, from simple cloud hosting to enterprise solutions.

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure:

- ✅ Your `main.py` is finalized and tested locally
- ✅ All models (`model1.pkl`, `model2.pkl`) are in `Notebooks/` folder
- ✅ Dataset (`Advertising Budget and Sales.csv`) is in `Data/` folder
- ✅ `pyproject.toml` has all dependencies listed
- ✅ Application runs without errors locally: `streamlit run main.py`

---

## 🌐 Deployment Options

### **Option 1: Streamlit Cloud (RECOMMENDED - FREE & EASIEST)**

**Best for:** Quick deployment, small teams, learning projects

#### Step 1: Prepare Your Project
```powershell
# Create requirements.txt
pip freeze > requirements.txt
```

#### Step 2: Push to GitHub
```powershell
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit - ready for deployment"
git remote add origin https://github.com/YOUR_USERNAME/ml-project1.git
git push -u origin main
```

#### Step 3: Deploy on Streamlit Cloud
1. Visit: https://streamlit.io/cloud
2. Click **"New app"**
3. Choose **GitHub repository:** `YOUR_USERNAME/ml-project1`
4. Select **branch:** `main`
5. Set **Main file path:** `main.py`
6. Click **Deploy**

**Your app goes live in seconds!** 🎉

**URL Format:** `https://your-username-ml-project1.streamlit.app`

#### Advantages:
- ✅ Completely free
- ✅ Auto-deploys on GitHub push
- ✅ No server management
- ✅ HTTPS included
- ✅ Analytics dashboard

---

### **Option 2: Heroku (PAID - $7+/month)**

**Best for:** Production apps needing custom domains

#### Step 1: Create Heroku Account
- Visit: https://www.heroku.com/

#### Step 2: Install Heroku CLI
```powershell
# Windows - download from https://devcenter.heroku.com/articles/heroku-cli
# Or use Chocolatey:
choco install heroku-cli
```

#### Step 3: Create Deployment Files

**Create `requirements.txt`:**
```powershell
pip freeze > requirements.txt
```

**Create `Procfile` (no extension):**
```
web: streamlit run main.py
```

**Create `.streamlit/config.toml`:**
```toml
[server]
port = 8501
headless = true

[browser]
gatherUsageStats = false
```

#### Step 4: Deploy
```powershell
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

**Your app is live at:** `https://your-app-name.herokuapp.com`

---

### **Option 3: Docker + Azure/AWS/GCP (ENTERPRISE)**

**Best for:** Large organizations, custom requirements

#### Step 1: Create `Dockerfile`
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Step 2: Create `.dockerignore`
```
.git
.venv
__pycache__
*.pyc
.env
```

#### Step 3: Build and Test Locally
```powershell
# Build Docker image
docker build -t sales-prediction:latest .

# Run container
docker run -p 8501:8501 sales-prediction:latest

# Visit: http://localhost:8501
```

#### Step 4: Push to Cloud

**Azure Container Registry:**
```powershell
az acr build --registry myregistry --image sales-prediction:latest .
az container create --resource-group mygroup --name sales-app --image myregistry.azurecr.io/sales-prediction:latest --ports 8501 --cpu 1 --memory 1
```

**AWS ECR:**
```powershell
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_AWS_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com
docker tag sales-prediction:latest YOUR_AWS_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/sales-prediction:latest
docker push YOUR_AWS_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/sales-prediction:latest
```

**Google Cloud Run:**
```powershell
gcloud run deploy sales-prediction --source . --platform managed --region us-central1 --allow-unauthenticated
```

---

### **Option 4: PythonAnywhere (BEGINNER-FRIENDLY - FREE & PAID)**

**Best for:** Beginners wanting simple hosting

1. Visit: https://www.pythonanywhere.com/
2. Create free account
3. Upload your files
4. Set up web app configuration
5. Done!

---

### **Option 5: Render (MODERN & FREE)**

**Best for:** Modern deployment with GitHub integration

1. Visit: https://render.com/
2. Connect your GitHub repository
3. Create new Web Service
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `streamlit run main.py`
6. Deploy!

---

## 📦 Prepare `requirements.txt`

Your dependencies are essential for deployment:

```powershell
# Generate requirements.txt from your environment
pip freeze > requirements.txt
```

**Your `requirements.txt` should include:**
```
streamlit>=1.28.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
joblib>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
```

---

## 🔐 Environment Variables & Secrets

If your app needs API keys or credentials:

**Create `.streamlit/secrets.toml`:**
```toml
# API Keys (never commit this file!)
api_key = "your-secret-key"
database_url = "your-database-url"
```

**Add to `.gitignore`:**
```
.streamlit/secrets.toml
.env
```

**In your app (`main.py`):**
```python
import streamlit as st

# Access secrets securely
api_key = st.secrets["api_key"]
```

---

## 🎯 Deployment Comparison

| Platform | Cost | Setup Time | Ease | Best For |
|----------|------|-----------|------|----------|
| **Streamlit Cloud** | FREE | 5 min | ⭐⭐⭐⭐⭐ | Learning, Small projects |
| **Heroku** | $7/mo | 15 min | ⭐⭐⭐⭐ | Production apps |
| **Docker + AWS** | Varies | 30 min | ⭐⭐⭐ | Enterprise |
| **PythonAnywhere** | FREE/Paid | 10 min | ⭐⭐⭐⭐ | Beginners |
| **Render** | FREE/Paid | 10 min | ⭐⭐⭐⭐⭐ | Modern apps |

---

## 🚀 Quick Start: Deploy to Streamlit Cloud (30 SECONDS)

**Fastest way to go live:**

1. **Commit your code to GitHub**
   ```powershell
   git add .
   git commit -m "Ready for deployment"
   git push
   ```

2. **Go to:** https://streamlit.io/cloud

3. **Click:** "New app"

4. **Select:** Your GitHub repo & `main.py`

5. **Click:** "Deploy"

**Done! Your app is now live! 🎉**

---

## ✅ Post-Deployment Verification

After deployment, test your application:

- [ ] App loads without errors
- [ ] All UI elements visible
- [ ] Currency selector works
- [ ] Input fields accept values
- [ ] Predictions generate correctly
- [ ] Visualizations display properly
- [ ] Performance is acceptable

---

## 🐛 Troubleshooting Deployment

### **Issue: ModuleNotFoundError**
```
Solution: Ensure all dependencies are in requirements.txt
pip freeze > requirements.txt
git push
```

### **Issue: Model Not Found**
```
Solution: Verify file paths in main.py are relative
✓ model = joblib.load("Notebooks/model2.pkl")
✗ model = joblib.load("C:\Users\...\model2.pkl")
```

### **Issue: App Takes Too Long to Load**
```
Solution: Optimize model loading with caching
@st.cache_resource
def load_model():
    return joblib.load("Notebooks/model2.pkl")
```

### **Issue: Port Already in Use**
```powershell
# On Streamlit Cloud, this is handled automatically
# Locally, use:
streamlit run main.py --server.port 8502
```

---

## 📈 Monitoring & Maintenance

### Streamlit Cloud Dashboard
- View app analytics
- Check deployment status
- View error logs
- Reboot app if needed

### Enable Auto-Deploy
```
GitHub Integration → Enable "Deploy on Push"
```

### Monitor Performance
```python
import time
import streamlit as st

start = time.time()
# Your code here
elapsed = st.write(f"⏱️ Took {time.time() - start:.2f}s")
```

---

## 💡 Pro Tips

### 1. **Use Streamlit Secrets for Credentials**
```python
# Don't do this:
api_key = "abc123xyz"

# Do this:
api_key = st.secrets["api_key"]
```

### 2. **Cache Your Model**
```python
@st.cache_resource
def load_model():
    return joblib.load("Notebooks/model2.pkl")

model = load_model()  # Loads only once
```

### 3. **Add Loading Indicators**
```python
with st.spinner("Loading model..."):
    model = joblib.load("Notebooks/model2.pkl")
```

### 4. **Monitor Logs**
```powershell
# Streamlit Cloud: View in dashboard
# Heroku: heroku logs --tail
# Docker: docker logs container_id
```

---

## 🔗 Deployment URLs After Going Live

| Platform | URL Format |
|----------|-----------|
| Streamlit Cloud | `https://username-projectname.streamlit.app` |
| Heroku | `https://your-app-name.herokuapp.com` |
| Render | `https://your-app-name.onrender.com` |
| Azure | `https://your-app-name.azurewebsites.net` |
| AWS | Custom domain available |

---

## 📞 Getting Help

### Resources
- [Streamlit Deployment Docs](https://docs.streamlit.io/deploy/streamlit-cloud)
- [Heroku Python Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- [Docker Documentation](https://docs.docker.com/)
- [Render Deployment Guide](https://render.com/docs)

### Common Questions
- **Q: Is my model secure?** A: Yes, models are encrypted in transit
- **Q: Can I use custom domain?** A: Yes (on paid plans)
- **Q: What about HTTPS?** A: Included on all platforms
- **Q: How to scale?** A: Upgrade plan for more resources

---

## ✨ You're Ready to Deploy!

**Choose your platform and go live today:**

1. **Easiest:** Streamlit Cloud (recommended for most users)
2. **Professional:** Heroku or Render
3. **Enterprise:** Docker + AWS/Azure/GCP
4. **Learning:** PythonAnywhere or Render

**Next Steps:**
1. ✅ Ensure `requirements.txt` is updated
2. ✅ Test app locally one more time
3. ✅ Push to GitHub
4. ✅ Deploy to your chosen platform
5. ✅ Share your live URL!

---

**Happy Deploying! 🚀**

*Last Updated: December 5, 2025*  
*For more details, see other documentation files in this folder.*
