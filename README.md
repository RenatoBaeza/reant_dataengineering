# Data Engineering Project

A full-stack data engineering project that fetches weather data from a public API, processes it with pandas, stores it in Supabase, and visualizes it with React and Tremor.

## Features

- **Data Pipeline**: Python script that fetches weather data from Open-Meteo API
- **Data Processing**: Uses pandas for data transformation and cleaning
- **Database**: Stores processed data in Supabase (PostgreSQL)
- **Frontend**: React application with Tremor UI components for data visualization
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
# Production build
docker-compose up --build

# Development mode with hot reload
docker-compose -f docker-compose.dev.yml up --build
```

3. Access the application:
- Frontend: http://localhost:3000
- Backend pipeline runs automatically

### Local Development

#### Run Data Pipeline Locally

```bash
cd backend
pip install -r requirements.txt
python pipeline.py
```

#### Run Frontend Locally

```bash
cd frontend
npm install
npm start
```

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

# Development mode
docker-compose -f docker-compose.dev.yml up
```

## GitHub Actions

The project includes GitHub Actions workflows that:
- Run the data pipeline on a schedule (daily)
- Run tests
- Deploy the frontend (optional)

## License

MIT

