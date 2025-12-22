# Setup Guide

Follow these steps to set up the complete data engineering project.

## 1. Supabase Setup

1. Go to [Supabase](https://supabase.com) and create a free account
2. Create a new project
3. Once your project is ready, go to Settings > API
4. Copy your Project URL and anon/public key
5. In the SQL Editor, run the following to create the table:

```sql
CREATE TABLE weather_data (
  id SERIAL PRIMARY KEY,
  location VARCHAR(255),
  temperature FLOAT,
  humidity FLOAT,
  wind_speed FLOAT,
  timestamp TIMESTAMP DEFAULT NOW()
);
```

## 2. Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Edit `.env` and add your Supabase credentials:
```
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-key-here
```

6. Test the pipeline:
```bash
python pipeline.py
```

## 3. Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env` file:
```bash
cp .env.example .env
```

4. Edit `.env` and add your Supabase credentials:
```
VITE_SUPABASE_URL=https://your-project-id.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key-here
```

5. Start the development server:
```bash
npm start
```

The app will open at http://localhost:3000

## 4. GitHub Actions Setup

1. Go to your GitHub repository
2. Navigate to Settings > Secrets and variables > Actions
3. Add the following secrets:
   - `SUPABASE_URL`: Your Supabase project URL
   - `SUPABASE_KEY`: Your Supabase anon key

4. The workflow will automatically run daily at 6 AM UTC, or you can trigger it manually from the Actions tab

## 5. Verify Everything Works

1. Run the backend pipeline to populate data:
```bash
cd backend
python pipeline.py
```

2. Check your Supabase dashboard to see the data in the `weather_data` table

3. Start the frontend and verify the dashboard displays the data:
```bash
cd frontend
npm start
```

## Troubleshooting

### Backend Issues
- Make sure your `.env` file is in the `backend` directory
- Verify your Supabase credentials are correct
- Check that the table was created correctly in Supabase

### Frontend Issues
- Ensure your `.env` file is in the `frontend` directory
- Make sure environment variables start with `VITE_`
- Clear browser cache if data doesn't appear
- Restart the dev server after changing `.env` variables

### GitHub Actions Issues
- Verify secrets are set correctly in GitHub
- Check the Actions tab for error logs
- Ensure the workflow file is in `.github/workflows/`

