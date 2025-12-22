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

## Docker Compose

The `docker-compose.yml` file provides:
- Optimized production builds
- Frontend served via Vite preview server
- Backend runs pipeline once and exits

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
docker run -p 3000:3000 --env-file .env weather-dashboard
```

Note: The frontend uses Vite's preview server for production serving.

## Environment Variables

Both services require Supabase credentials:

**Backend (.env):**
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
```

**Frontend (.env):**
```
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
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
    - "8080:3000"  # Use port 8080 instead
  ```

## Production Deployment

For production deployment:

1. **Build production images:**
   ```bash
   docker-compose build
   ```

2. **Use environment variables from your hosting platform** (don't commit `.env` files)

3. **Consider using Docker secrets** for sensitive data

4. **Set up a reverse proxy** (nginx, traefik, caddy) in front of the frontend container (optional)

5. **Schedule backend runs** using cron or your orchestration platform's scheduler

## Image Sizes

- Backend: ~150MB (Python slim base)
- Frontend: ~150MB (Node.js alpine with Vite preview server)

## Build Process

The frontend uses Vite for:
- Optimized production builds
- Built-in preview server for production serving

