# Docker Guide

This guide explains how to use Docker with this project.

## Quick Start

1. **Set up environment variables:**
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   ```
   Then edit both `.env` files with your Supabase credentials.

2. **Start everything:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - Frontend: http://localhost:3000

## Docker Compose Files

### Production (`docker-compose.yml`)
- Optimized production builds
- Frontend served via Nginx
- Backend runs pipeline once and exits

### Development (`docker-compose.dev.yml`)
- Hot reload for both frontend and backend
- Volume mounts for live code changes
- Frontend runs on port 3000 with React dev server

## Building Individual Services

### Backend Only
```bash
cd backend
docker build -t weather-pipeline .
docker run --env-file .env weather-pipeline
```

### Frontend Only
```bash
cd frontend
docker build -t weather-dashboard .
docker run -p 3000:80 --env-file .env weather-dashboard
```

## Development Workflow

### Using Development Compose
```bash
# Start services with hot reload
docker-compose -f docker-compose.dev.yml up

# Run backend pipeline manually in dev container
docker-compose -f docker-compose.dev.yml exec backend python pipeline.py

# View logs
docker-compose -f docker-compose.dev.yml logs -f frontend
```

### Making Changes
- Frontend: Edit files in `frontend/src/` - changes reflect immediately
- Backend: Edit files in `backend/` - restart container or run manually

## Environment Variables

Both services require Supabase credentials:

**Backend (.env):**
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
```

**Frontend (.env):**
```
REACT_APP_SUPABASE_URL=https://your-project.supabase.co
REACT_APP_SUPABASE_ANON_KEY=your-anon-key
```

## Troubleshooting

### Container won't start
- Check that `.env` files exist and have correct values
- Verify Supabase credentials are correct
- Check logs: `docker-compose logs`

### Frontend shows connection errors
- Ensure Supabase URL and key are set correctly
- Check browser console for specific errors
- Verify Supabase table exists and RLS policies allow access

### Backend pipeline fails
- Check Supabase connection: `docker-compose logs backend`
- Verify table schema matches `supabase/schema.sql`
- Ensure network connectivity to Open-Meteo API

### Port already in use
- Change port mapping in `docker-compose.yml`:
  ```yaml
  ports:
    - "8080:80"  # Use port 8080 instead
  ```

## Production Deployment

For production deployment:

1. **Build production images:**
   ```bash
   docker-compose build
   ```

2. **Use environment variables from your hosting platform** (don't commit `.env` files)

3. **Consider using Docker secrets** for sensitive data

4. **Set up a reverse proxy** (nginx, traefik) in front of the frontend container

5. **Schedule backend runs** using cron or your orchestration platform's scheduler

## Image Sizes

- Backend: ~150MB (Python slim base)
- Frontend: ~25MB (Nginx alpine + built React app)

## Multi-stage Builds

The frontend uses a multi-stage build:
1. **Build stage**: Node.js image to compile React app
2. **Production stage**: Nginx alpine to serve static files

This results in a much smaller final image (~25MB vs ~500MB).

