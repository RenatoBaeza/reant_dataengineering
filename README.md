# Data Engineering Project

A full-stack data engineering project that fetches weather data from a public API, processes it with pandas, stores it in Supabase, and visualizes it with React and Tremor.

## Features

- **Data Pipeline**: Python script that fetches weather data from Open-Meteo API
- **Data Processing**: Uses pandas for data transformation and cleaning
- **Database**: Stores processed data in Supabase (PostgreSQL)
- **Frontend**: React application with Vite and Tremor UI components for data visualization
- **CI/CD**: GitHub Actions workflows for automated data pipeline execution
- **Dockerized**: Full Docker support with docker-compose for easy deployment

## Project Structure

```
.
├── backend/              # Python data pipeline
│   ├── pipeline.py      # Main data pipeline script
│   ├── requirements.txt # Python dependencies
│   └── config.py        # Configuration settings
├── frontend/            # React application
│   ├── src/
│   ├── package.json
│   └── ...
├── .github/
│   └── workflows/       # GitHub Actions workflows
└── README.md

```

## Setup

### Prerequisites

- Python 3.8+ (or Docker)
- Node.js 16+ (or Docker)
- Supabase account (free tier)
- Docker and Docker Compose (optional, for containerized deployment)

### Backend Setup

1. Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Add your Supabase credentials
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Set up environment variables:
```bash
cp .env.example .env
# Add your Supabase credentials
```

### Supabase Setup

1. Create a new project on [Supabase](https://supabase.com)
2. Create the following table:
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

3. Get your project URL and anon key from Settings > API

## Usage

### Docker Deployment (Recommended)

1. Set up environment variables:
```bash
# Backend
cp backend/.env.example backend/.env
# Add your Supabase credentials to backend/.env

# Frontend
cp frontend/.env.example frontend/.env
# Add your Supabase credentials to frontend/.env
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

3. Access the application:
- Frontend: http://localhost:3000
- Backend pipeline runs automatically

### Docker Commands

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Run backend pipeline manually
docker-compose run backend python pipeline.py
```

## GitHub Actions

The project includes GitHub Actions workflows that:
- Run the data pipeline on a schedule (daily at 6 AM UTC)
- Can be triggered manually from the Actions tab

## Free Deployment

This project can be deployed completely free! 🚀

### Quick Deploy (Recommended)
1. **Frontend**: Deploy to [Vercel](https://vercel.com) in 2 minutes - see [QUICK_DEPLOY.md](QUICK_DEPLOY.md)
2. **Backend**: Already configured with GitHub Actions (just add secrets)
3. **Database**: Supabase free tier

### Deployment Options
- **Frontend**: [Vercel](https://vercel.com), [Netlify](https://netlify.com), or [Cloudflare Pages](https://pages.cloudflare.com)
- **Backend Pipeline**: GitHub Actions (already configured)
- **Full Stack**: [Railway](https://railway.app) or [Render](https://render.com)

📖 **See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions**  
⚡ **See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for 5-minute setup**

## License

MIT

