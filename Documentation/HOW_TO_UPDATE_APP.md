# 🔄 How to Update Your Deployed App

**Your app is live at:** https://dev-kavindu-ml-project1.streamlit.app

This guide explains how to update your deployed application.

---

## ✨ The Magic: Auto-Deploy on GitHub Push

**The best part:** When you push changes to GitHub, your live app automatically updates!

**No manual redeployment needed!**

---

## 🚀 How to Update Your App (3 Steps)

### Step 1: Make Changes Locally
Edit your files in VS Code:
- Update `main.py` to change app logic
- Add new features
- Fix bugs
- Change colors/styling

**Example:** Let's say you want to add a new currency or change the interface.

```python
# Edit main.py locally
# Your changes here...
```

### Step 2: Commit and Push to GitHub
```powershell
# Navigate to project directory
cd d:\ML_Project1

# Stage all changes
git add .

# Commit with a message
git commit -m "Added new currency feature"

# Push to GitHub
git push origin main
```

### Step 3: Wait for Auto-Deployment
- GitHub receives your push ✓
- Streamlit Cloud detects changes ✓
- App automatically redeploys (2-5 minutes) ✓
- Your live app is updated! ✓

---

## 📊 Timeline of an Update

```
You: Make changes locally (5 min)
You: git add . && git commit -m "fix" && git push (30 seconds)
     ↓
GitHub: Receives your code (2 seconds)
     ↓
Streamlit Cloud: Detects changes (10 seconds)
     ↓
Streamlit: Pulls code from GitHub (5 seconds)
     ↓
Streamlit: Installs dependencies (30 seconds)
     ↓
Streamlit: Starts your app (15 seconds)
     ↓
Your Users: See updated app (2-5 minutes after push)
```

---

## 💡 Common Updates & How to Do Them

### 1. Fix a Bug
```powershell
# Edit the bug in main.py
# Test locally: streamlit run main.py
# Then push:
git add .
git commit -m "Fixed currency conversion bug"
git push origin main
# ✅ Live app is fixed in 2-5 minutes
```

### 2. Add a New Feature
```powershell
# Add new code to main.py
# Test locally
# Push:
git add .
git commit -m "Added quarterly predictions feature"
git push origin main
# ✅ New feature is live in 2-5 minutes
```

### 3. Update Dependencies
```powershell
# Update requirements.txt
pip freeze > requirements.txt
# Then push:
git add requirements.txt
git commit -m "Updated scikit-learn to latest version"
git push origin main
# ✅ Updated dependencies in 2-5 minutes
```

### 4. Change the Model
```powershell
# Replace model2.pkl with new trained model
# Push to GitHub:
git add .
git commit -m "Deployed improved ML model"
git push origin main
# ✅ New model is live in 2-5 minutes
```

### 5. Update Data
```powershell
# Add/update CSV in Data/ folder
git add .
git commit -m "Updated dataset with latest advertising data"
git push origin main
# ✅ App uses new data in 2-5 minutes
```

---

## 🎯 Git Workflow for Updates

### Daily Update Workflow
```powershell
# 1. Make your changes in VS Code
# (edit files, add features, fix bugs)

# 2. Check what changed
git status

# 3. Stage all changes
git add .

# 4. Commit with meaningful message
git commit -m "Description of your changes"

# 5. Push to GitHub
git push origin main

# 6. Check Streamlit Cloud dashboard to see deployment progress
```

### Useful Git Commands
```powershell
# See all changes you made
git diff

# See recent commits
git log --oneline -5

# Undo a commit (last commit only)
git reset --soft HEAD~1

# See what will be pushed
git status

# Push specific branch
git push origin main
```

---

## 📈 Monitor Your Deployment

### Check if App Updated
1. **Visit your app URL:**
   ```
   https://dev-kavindu-ml-project1.streamlit.app
   ```
2. **Refresh the browser** (F5 or Ctrl+Shift+R)
3. **Look for your changes**

### View Deployment Status
1. **Go to Streamlit Cloud Dashboard:**
   ```
   https://share.streamlit.io/
   ```
2. **Click your app**
3. **Check "Deployment" tab** for progress
4. **View logs** if there are errors

### Check App Logs
1. **Streamlit Cloud Dashboard**
2. **Your App → Manage app → Logs**
3. **Scroll to see recent updates**
4. **Look for errors or warnings**

---

## ⚠️ If Deployment Fails

### Issue: Deployment hangs or fails
```
Check:
1. Did you push to main branch? (not other branches)
2. Are all files saved?
3. Is requirements.txt up to date?
4. No syntax errors in main.py?
```

### Solution
```powershell
# Check what files changed
git status

# See the actual changes
git diff

# If something is wrong, revert
git reset HEAD .

# Undo last commit
git reset --soft HEAD~1

# Try again
git add .
git commit -m "Fixed deployment issue"
git push origin main
```

### View Error Logs
1. Streamlit Cloud Dashboard
2. Your App name
3. "Manage app" → "Logs" tab
4. Read the error message
5. Fix the issue in your code
6. Push again

---

## 🔄 Update Frequency Guidelines

**How often should you update?**

| Scenario | Frequency | Notes |
|----------|-----------|-------|
| Bug fixes | ASAP | Push immediately |
| Minor features | Weekly | Batch small updates |
| Major features | Bi-weekly | Test thoroughly first |
| Experiments | Daily (during dev) | Use branches for testing |
| Production updates | Monthly | Plan ahead, test everything |

---

## 🎓 Best Practices for Updates

### ✅ Do This
- ✅ Test changes locally first: `streamlit run main.py`
- ✅ Write meaningful commit messages: `git commit -m "Added temperature feature"`
- ✅ Push only to `main` branch when ready
- ✅ Check logs after deployment
- ✅ Monitor your app performance
- ✅ Keep `requirements.txt` updated

### ❌ Don't Do This
- ❌ Push broken code to main
- ❌ Commit without testing locally
- ❌ Use vague messages like "update" or "fix"
- ❌ Delete files without backup
- ❌ Change model path without testing
- ❌ Ignore error messages

---

## 🚀 Quick Update Commands

### Copy-Paste These

**For quick fixes:**
```powershell
git add . && git commit -m "Quick fix" && git push origin main
```

**For feature updates:**
```powershell
git add . && git commit -m "Added new feature: [description]" && git push origin main
```

**For bug fixes:**
```powershell
git add . && git commit -m "Fixed bug: [description]" && git push origin main
```

**For model updates:**
```powershell
git add . && git commit -m "Updated ML model with better performance" && git push origin main
```

---

## 📊 Deployment Success Checklist

After each deployment, verify:

- [ ] Code pushed to GitHub successfully
- [ ] Streamlit Cloud shows "Deployment running"
- [ ] No errors in logs
- [ ] App URL loads (may take 2-5 minutes)
- [ ] Your changes are visible
- [ ] All features work correctly
- [ ] No performance issues
- [ ] Ready for users!

---

## 🎯 Workflow Summary

```
Local Development
    ↓
Test with: streamlit run main.py
    ↓
Make changes work perfectly
    ↓
git add .
    ↓
git commit -m "Description"
    ↓
git push origin main
    ↓
Wait 2-5 minutes
    ↓
Visit https://dev-kavindu-ml-project1.streamlit.app
    ↓
Refresh browser (F5)
    ↓
See your updates live!
```

---

## 💡 Pro Tips

### Tip 1: Use Branches for Testing
```powershell
# Create a test branch
git checkout -b feature/new-currency

# Make changes, commit, push
git push origin feature/new-currency

# When ready, merge to main
git checkout main
git merge feature/new-currency
git push origin main
```

### Tip 2: Keep Model Files Small
- Large model files take longer to deploy
- Consider compressing or optimizing

### Tip 3: Monitor Dependencies
- Update dependencies carefully
- Test locally before pushing
- Document version requirements

### Tip 4: Use Meaningful Commit Messages
```
Good:     "Added support for EUR currency"
Better:   "Feature: Added 5 new currencies (EUR, GBP, CHF, SEK, NOK)"
Bad:      "update", "fix", "changes"
```

---

## 📞 Troubleshooting Quick Links

| Issue | Solution |
|-------|----------|
| App won't deploy | Check logs → Fix errors → Push again |
| Changes not showing | Hard refresh browser (Ctrl+Shift+R) or wait longer |
| Model errors | Verify model path in main.py is correct |
| Dependency errors | Update requirements.txt and push |
| Performance issues | Check Streamlit Cloud dashboard for resource usage |

---

## ✨ Final Checklist for Updates

Before each update, ask yourself:

1. ✅ Have I tested locally?
2. ✅ Are all files saved?
3. ✅ Is my commit message clear?
4. ✅ Am I pushing to main branch?
5. ✅ Have I updated requirements.txt if needed?

If YES to all, then:
```powershell
git add . && git commit -m "Your message" && git push origin main
```

**Done!** Your app will update automatically! 🎉

---

**Your app is deployed and live!** 🚀

Every push to GitHub = Automatic update to production

Simple as that! 

**Happy updating!**

*Last Updated: December 5, 2025*
