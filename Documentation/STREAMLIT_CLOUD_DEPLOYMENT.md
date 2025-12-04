# 🚀 Streamlit Cloud Deployment - Step by Step

**Deploy your Sales Prediction ML app to Streamlit Cloud in 5 minutes!**

> ✅ Your code is already pushed to GitHub. Now let's deploy it live!

---

## ✅ Pre-Deployment Checklist

Before starting, verify:

- ✅ Code pushed to GitHub: **Dev-Kavindu/ML-Project1**
- ✅ Branch: **main**
- ✅ Files present:
  - `main.py` ✓
  - `requirements.txt` ✓
  - `Notebooks/model2.pkl` ✓
  - `Data/Advertising Budget and Sales.csv` ✓

**Status: All verified! Ready to deploy.**

---

## 🎯 Deployment Steps (5 MINUTES)

### Step 1: Go to Streamlit Cloud
```
Visit: https://streamlit.io/cloud
```

### Step 2: Sign Up or Login
- Click **"Sign up"** (if new) or **"Sign in"** (if existing)
- **Recommended:** Use your GitHub account
  - Click **"Continue with GitHub"**
  - Authorize Streamlit to access your repositories

### Step 3: Deploy New App
- After signing in, you'll see the dashboard
- Click **"New app"** button (top-right or center of page)

### Step 4: Select Your Repository
In the deployment dialog:
- **Repository:** Select `Dev-Kavindu/ML-Project1`
- **Branch:** Select `main` (should be default)
- **Main file path:** Enter `main.py`

### Step 5: Deploy!
- Click the **"Deploy"** button
- Wait 30-60 seconds for deployment to complete

---

## 🎉 Your App is Live!

Once deployment completes, you'll see:

```
✓ Deployment successful
✓ Your app URL: https://ml-project1-5gwnorma9jbmdvkblm97ct.streamlit.app
```

**Share this URL with anyone to let them use your app!**

---

## 📊 What to Expect

### Initial Load (First Time)
- Streamlit Cloud installs dependencies from `requirements.txt`
- Models load from `Notebooks/` folder
- App initializes Streamlit UI

### Performance
- **First load:** 30-60 seconds (normal)
- **Subsequent loads:** 2-5 seconds (cached)
- **Predictions:** Instant (< 1 second)

### URL Format
```
https://[custom-deployment-url].streamlit.app

Your URL: https://ml-project1-5gwnorma9jbmdvkblm97ct.streamlit.app
```

---

## ✨ Using Your Live App

1. **Visit your URL** in any browser
2. **Select currency** from dropdown
3. **Enter advertising budgets:**
   - TV budget
   - Radio budget
   - Newspaper budget
4. **Click "🔮 Predict Sales"**
5. **See prediction** with visualization

---

## 🔄 Auto-Deploy on Updates

**Best part:** Every time you push to GitHub, your app automatically updates!

```powershell
# Make changes locally
# Commit and push
git add .
git commit -m "Updated feature X"
git push origin main

# ✅ App automatically redeploys within 2-5 minutes!
```

---

## 🎯 Streamlit Cloud Dashboard

Your dashboard shows:

- **App Status:** Running ✓
- **Memory & CPU Usage**
- **Logs:** Debug issues
- **Settings:** Configure app behavior
- **Sharing:** Share your app URL
- **Analytics:** Track visitors (optional)

---

## 🐛 Troubleshooting

### Issue: "Repository not accessible"
**Solution:** 
1. Go to GitHub → Settings → Applications
2. Authorize Streamlit to access your repos
3. Try again

### Issue: "Module not found error"
**Solution:**
1. Check `requirements.txt` has all dependencies
2. Push changes: `git push origin main`
3. Streamlit will auto-redeploy

### Issue: "Model not found"
**Solution:**
1. Verify file path in `main.py` is relative:
   ```python
   model = joblib.load("Notebooks/model2.pkl")  # ✓ Correct
   ```
2. Ensure model file exists in your GitHub repo
3. Check logs for detailed error

### Issue: "App not responding"
**Solution:**
1. Streamlit Cloud → Settings → Reboot app
2. Or redeploy: Push new commit to GitHub

---

## 📊 Monitor Your App

### View Logs
```
Streamlit Cloud Dashboard
  → Your App
  → Manage App
  → Logs tab
```

### Check Performance
```
Dashboard → Settings → Advanced Settings
Monitor resource usage and response times
```

### Share Analytics
```
Dashboard → Settings → Public Analytics
Enable to track visitors and usage
```

---

## 🔐 Security & Secrets

If your app needs secrets (API keys, database URLs):

### Option 1: Using Streamlit Secrets
1. Go to your app settings in Streamlit Cloud
2. Click **"Secrets"**
3. Add secrets in TOML format:
   ```toml
   database_url = "postgresql://..."
   api_key = "sk_live_..."
   ```

### Option 2: GitHub Secrets (CI/CD)
```yaml
# In your workflow
env:
  API_KEY: ${{ secrets.API_KEY }}
```

**For this project:** No secrets needed (public model & data)

---

## 📱 Mobile & Device Testing

Your app works on:
- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Tablet (iPad, Android tablets)
- ✅ Mobile (iPhone, Android phones)

**Responsive design handled automatically by Streamlit!**

---

## 🚀 Advanced: Custom Domain

**Want a custom domain?** (e.g., `myapp.com`)

1. **Streamlit Community Cloud:** Not supported (free plan)
2. **Streamlit for Teams:** Supported (paid)
3. **Alternative:** Use DNS service like Cloudflare

---

## ✅ Post-Deployment Checklist

After deployment, test:

- [ ] App loads at your URL
- [ ] All UI elements visible
- [ ] Currency selector works
- [ ] Can enter budget values
- [ ] Predictions generate correctly
- [ ] Visualizations display
- [ ] No console errors
- [ ] Mobile view works
- [ ] Page loads in < 10 seconds

---

## 📈 Scaling & Upgrades

### Current (Community Cloud)
- **Cost:** FREE ✓
- **Resources:** Limited (512 MB RAM, 1 CPU)
- **Concurrent users:** ~10-20
- **Uptime:** ~99%

### Future (Streamlit for Teams)
- **Cost:** $30/month+
- **Resources:** More memory & CPU
- **Concurrent users:** 100+
- **Features:** Custom domains, priority support

---

## 🎓 Next Steps After Deployment

1. **Share your URL** with friends/colleagues
2. **Get feedback** from real users
3. **Monitor logs** for any issues
4. **Make improvements** based on feedback
5. **Update GitHub** → Auto-deploys to Streamlit Cloud

---

## 📞 Support

### Streamlit Cloud Docs
- https://docs.streamlit.io/deploy/streamlit-cloud

### Getting Help
- Streamlit Cloud Dashboard → Help
- Streamlit Community Forum: https://discuss.streamlit.io/
- Stack Overflow: Tag `streamlit`

---

## 🎉 Success!

Your app is now live on the internet! 

```
🌍 URL: https://dev-kavindu-ml-project1.streamlit.app
📱 Works on all devices
⚡ Auto-updates when you push to GitHub
🎯 Shared with your team/users
✨ Production ready!
```

---

## 📝 Deployment Record

| Item | Value |
|------|-------|
| **Platform** | Streamlit Cloud |
| **App Name** | ML-Project1 |
| **Repository** | Dev-Kavindu/ML-Project1 |
| **Branch** | main |
| **Main File** | main.py |
| **Cost** | FREE |
| **Status** | ✅ Deployed |
| **Live URL** | https://ml-project1-5gwnorma9jbmdvkblm97ct.streamlit.app |

---

**Congratulations! 🎊 Your ML project is now live on the internet!**

*Last Updated: December 5, 2025*
