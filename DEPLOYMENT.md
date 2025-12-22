# Free Deployment Guide

This guide covers multiple free deployment options for your data engineering project.

## Overview

Your project consists of:
- **Backend**: Python data pipeline (runs periodically)
- **Frontend**: React/Vite application
- **Database**: Supabase (already free tier)

## Deployment Options

### Option 1: GitHub Actions + Vercel/Netlify (Recommended)

**Best for**: Separate deployment of pipeline and frontend

#### Backend Pipeline
- **Platform**: GitHub Actions (already configured)
- **Cost**: Free for public repositories
- **Setup**: Already done! The workflow runs daily at 6 AM UTC

#### Frontend
- **Platform**: Vercel or Netlify
- **Cost**: Free tier
- **Setup**: See sections below

---

### Option 2: Railway (Full Stack)

**Best for**: Simple full-stack deployment

- **Cost**: Free tier with $5 credit/month
- **Setup**: Deploy both backend and frontend
- **Limitations**: Sleeps after inactivity (free tier)

---

### Option 3: Render (Full Stack)

**Best for**: Reliable free hosting

- **Cost**: Free tier
- **Setup**: Deploy both services
- **Limitations**: Sleeps after 15 minutes of inactivity

---

## Detailed Deployment Instructions

### Frontend: Vercel (Recommended)

Vercel offers excellent free hosting for React/Vite applications.

#### Steps:

1. **Push your code to GitHub** (if not already done)

2. **Install Vercel CLI** (optional, or use web interface):
   ```bash
   npm i -g vercel
   ```

3. **Deploy via Web Interface**:
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub
   - Click "New Project"
   - Import your repository
   - Set root directory to `frontend`
   - Add environment variables:
     - `VITE_SUPABASE_URL`
     - `VITE_SUPABASE_ANON_KEY`
   - Click "Deploy"

4. **Deploy via CLI**:
   ```bash
   cd frontend
   vercel
   ```
   Follow the prompts and add environment variables when asked.

5. **Configure Build Settings**:
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`

#### Environment Variables in Vercel:
- Go to Project Settings > Environment Variables
- Add:
  ```
  VITE_SUPABASE_URL=your_supabase_url
  VITE_SUPABASE_ANON_KEY=your_supabase_key
  ```

#### Custom Domain (Optional):
- Vercel provides a free `.vercel.app` domain
- You can add a custom domain in project settings

---

### Frontend: Netlify

Alternative to Vercel with similar features.

#### Steps:

1. **Go to [netlify.com](https://netlify.com)**
   - Sign up with GitHub

2. **Deploy**:
   - Click "Add new site" > "Import an existing project"
   - Connect your GitHub repository
   - Configure:
     - Base directory: `frontend`
     - Build command: `npm run build`
     - Publish directory: `frontend/dist`

3. **Add Environment Variables**:
   - Go to Site settings > Environment variables
   - Add:
     ```
     VITE_SUPABASE_URL=your_supabase_url
     VITE_SUPABASE_ANON_KEY=your_supabase_key
     ```

4. **Redeploy** after adding environment variables

---

### Frontend: Cloudflare Pages

Another excellent free option.

#### Steps:

1. **Go to [pages.cloudflare.com](https://pages.cloudflare.com)**
   - Sign up/login

2. **Connect Repository**:
   - Click "Create a project"
   - Connect GitHub repository

3. **Configure Build**:
   - Framework preset: Vite
   - Build command: `npm run build`
   - Build output directory: `dist`
   - Root directory: `frontend`

4. **Add Environment Variables**:
   - Go to Settings > Environment variables
   - Add your Vite environment variables

---

### Full Stack: Railway

Deploy both backend and frontend together.

#### Steps:

1. **Go to [railway.app](https://railway.app)**
   - Sign up with GitHub

2. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"

3. **Deploy Frontend**:
   - Add service > GitHub repo
   - Select your repository
   - Root directory: `frontend`
   - Build command: `npm install && npm run build`
   - Start command: `npm run preview`
   - Add environment variables:
     ```
     VITE_SUPABASE_URL=your_url
     VITE_SUPABASE_ANON_KEY=your_key
     ```

4. **Deploy Backend** (Optional):
   - Add another service
   - Root directory: `backend`
   - Start command: `python pipeline.py`
   - Add environment variables:
     ```
     SUPABASE_URL=your_url
     SUPABASE_KEY=your_key
     ```

5. **Configure Cron Job** (for scheduled pipeline runs):
   - Use Railway's cron service or keep GitHub Actions

---

### Full Stack: Render

Similar to Railway, good free tier.

#### Steps:

1. **Go to [render.com](https://render.com)**
   - Sign up with GitHub

2. **Deploy Frontend**:
   - New > Static Site
   - Connect repository
   - Settings:
     - Build Command: `cd frontend && npm install && npm run build`
     - Publish Directory: `frontend/dist`
   - Add environment variables

3. **Deploy Backend** (Optional):
   - New > Background Worker
   - Connect repository
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python pipeline.py`
   - Add environment variables

---

## GitHub Actions (Backend Pipeline)

Your backend pipeline is already configured to run via GitHub Actions!

### Current Setup:
- Runs daily at 6 AM UTC
- Can be triggered manually
- Free for public repositories

### To Modify Schedule:
Edit `.github/workflows/data-pipeline.yml`:
```yaml
schedule:
  - cron: '0 6 * * *'  # Change this to your preferred time
```

### Manual Trigger:
- Go to Actions tab in GitHub
- Select "Data Pipeline" workflow
- Click "Run workflow"

---

## Recommended Setup

### For Most Users:
1. **Backend**: Keep GitHub Actions (already configured)
2. **Frontend**: Deploy to Vercel (easiest, best performance)

### For Full Control:
1. **Backend**: Railway or Render
2. **Frontend**: Vercel or Netlify

---

## Environment Variables Checklist

Make sure to set these in your deployment platform:

### Frontend:
- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`

### Backend:
- `SUPABASE_URL`
- `SUPABASE_KEY`

---

## Post-Deployment Checklist

- [ ] Frontend is accessible and loads
- [ ] Environment variables are set correctly
- [ ] Frontend can connect to Supabase
- [ ] GitHub Actions workflow runs successfully
- [ ] Data appears in Supabase after pipeline runs
- [ ] Dashboard displays data correctly

---

## Troubleshooting

### Frontend shows blank page:
- Check browser console for errors
- Verify environment variables are set (must start with `VITE_`)
- Ensure build completed successfully
- Check that Supabase RLS policies allow public read

### Environment variables not working:
- Vite requires variables to start with `VITE_`
- Restart/redeploy after adding variables
- Check variable names match exactly

### GitHub Actions failing:
- Verify secrets are set in repository settings
- Check workflow file syntax
- Review action logs for specific errors

### CORS issues:
- Supabase handles CORS automatically
- If issues persist, check Supabase project settings

---

## Cost Comparison

| Platform | Free Tier | Limitations |
|----------|-----------|-------------|
| **Vercel** | ✅ Unlimited | 100GB bandwidth/month |
| **Netlify** | ✅ Unlimited | 100GB bandwidth/month |
| **Cloudflare Pages** | ✅ Unlimited | Unlimited bandwidth |
| **Railway** | ✅ $5 credit/month | Sleeps after inactivity |
| **Render** | ✅ Free | Sleeps after 15 min |
| **GitHub Actions** | ✅ Free (public repos) | 2000 min/month |

---

## Next Steps

1. Choose your deployment platform
2. Follow the specific instructions above
3. Set environment variables
4. Deploy and test
5. Monitor your deployments

For questions or issues, check the platform's documentation or GitHub issues.

