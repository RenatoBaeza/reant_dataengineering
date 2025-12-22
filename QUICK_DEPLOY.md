# Quick Deploy Guide (5 Minutes)

The fastest way to deploy your project for free.

## Step 1: Deploy Frontend to Vercel (2 minutes)

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push
   ```

2. **Go to [vercel.com](https://vercel.com)**
   - Click "Sign Up" → Use GitHub
   - Click "Add New Project"
   - Import your repository

3. **Configure Project**:
   - Root Directory: Leave empty (or set to `frontend` if Vercel doesn't auto-detect)
   - Framework Preset: Vite (should auto-detect)
   - Build Command: `cd frontend && npm run build` (or just `npm run build` if root is frontend)
   - Output Directory: `frontend/dist` (or `dist` if root is frontend)

4. **Add Environment Variables**:
   - Click "Environment Variables"
   - Add:
     ```
     VITE_SUPABASE_URL = your_supabase_url_here
     VITE_SUPABASE_ANON_KEY = your_supabase_key_here
     ```

5. **Deploy**:
   - Click "Deploy"
   - Wait 1-2 minutes
   - Your app is live! 🎉

## Step 2: Configure GitHub Actions (Already Done!)

Your backend pipeline is already configured! Just add secrets:

1. **Go to your GitHub repository**
2. **Settings** → **Secrets and variables** → **Actions**
3. **Add secrets**:
   - `SUPABASE_URL`: Your Supabase project URL
   - `SUPABASE_KEY`: Your Supabase anon key

4. **Test the workflow**:
   - Go to **Actions** tab
   - Click **Data Pipeline**
   - Click **Run workflow** → **Run workflow**

## Step 3: Verify Everything Works

1. **Check your Vercel deployment**:
   - Visit your Vercel URL (e.g., `your-project.vercel.app`)
   - Dashboard should load (may show "No data" initially)

2. **Run the pipeline**:
   - Go to GitHub Actions
   - Manually trigger the workflow
   - Wait for it to complete

3. **Refresh your dashboard**:
   - Data should now appear!

## That's It! 🎉

Your project is now deployed:
- ✅ Frontend: Live on Vercel
- ✅ Backend: Running via GitHub Actions (daily at 6 AM UTC)
- ✅ Database: Supabase (free tier)

## Next Steps (Optional)

- **Custom Domain**: Add your domain in Vercel settings
- **Change Schedule**: Edit `.github/workflows/data-pipeline.yml`
- **Monitor**: Check Vercel analytics and GitHub Actions logs

## Troubleshooting

**Frontend shows blank page?**
- Check browser console (F12)
- Verify environment variables in Vercel
- Make sure variables start with `VITE_`

**No data showing?**
- Run GitHub Actions workflow manually
- Check Supabase dashboard for data
- Verify RLS policies allow public read

**Need help?** See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

