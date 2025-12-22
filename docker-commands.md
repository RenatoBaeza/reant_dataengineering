# Quick Docker Commands Reference

## Production Commands

```bash
# Build and start all services
docker-compose up --build

# Start in detached mode (background)
docker-compose up -d --build

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f frontend
docker-compose logs -f backend

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Rebuild specific service
docker-compose build backend
docker-compose build frontend

# Run backend pipeline manually
docker-compose run backend python pipeline.py
```

## Development Commands

```bash
# Start development environment
docker-compose -f docker-compose.dev.yml up --build

# Start in detached mode
docker-compose -f docker-compose.dev.yml up -d --build

# Execute command in running container
docker-compose -f docker-compose.dev.yml exec backend python pipeline.py
docker-compose -f docker-compose.dev.yml exec frontend npm test

# View logs
docker-compose -f docker-compose.dev.yml logs -f

# Stop development environment
docker-compose -f docker-compose.dev.yml down
```

## Individual Service Commands

```bash
# Build backend only
cd backend
docker build -t weather-pipeline .
docker run --env-file .env weather-pipeline

# Build frontend only
cd frontend
docker build -t weather-dashboard .
docker run -p 3000:80 --env-file .env weather-dashboard
```

## Maintenance Commands

```bash
# List running containers
docker ps

# List all containers
docker ps -a

# Remove unused images
docker image prune

# Remove unused volumes
docker volume prune

# Remove everything (containers, images, volumes)
docker system prune -a --volumes

# View container resource usage
docker stats

# Inspect container
docker inspect <container-name>

# Access container shell
docker exec -it <container-name> /bin/sh
```

