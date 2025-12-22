# Reant Data Engineering Project

A comprehensive full-stack data engineering project that demonstrates modern data pipeline architecture with ETL, data transformation, and visualization capabilities.

## 🚀 Features

- **Data Pipeline**: Python-based ETL pipeline that fetches weather data from Open-Meteo API
- **Data Processing**: Pandas-based data transformation and cleaning
- **Data Warehouse**: PostgreSQL database via Supabase with optimized schemas
- **Data Transformation**: dbt (data build tool) for analytics-ready data models
- **Frontend**: React application with Vite and Tremor UI for real-time data visualization
- **CI/CD**: GitHub Actions workflows for automated pipeline execution
- **Containerization**: Full Docker support with docker-compose for easy deployment
- **Analytics**: Built-in analytics tracking and reporting

## 📁 Project Structure

```
.
├── backend/                 # Python data pipeline
│   ├── pipeline.py         # Main ETL pipeline script
│   ├── config.py           # Configuration and settings
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Backend container definition
│   └── README.md           # Backend documentation
│
├── dbt/                    # dbt transformation project
│   ├── models/
│   │   ├── staging/        # Staging models (data cleaning)
│   │   ├── intermediate/   # Intermediate transformations
│   │   └── marts/          # Final analytics-ready tables
│   ├── dbt_project.yml     # dbt project configuration
│   ├── profiles.yml.example # Database connection template
│   └── README.md           # dbt documentation
│
├── frontend/               # React application
│   ├── src/                # Source code
│   ├── package.json        # Node dependencies
│   ├── Dockerfile          # Frontend container definition
│   └── README.md           # Frontend documentation
│
├── supabase/               # Database schemas
│   └── schema.sql          # Table definitions and indexes
│
├── .github/
│   └── workflows/          # GitHub Actions CI/CD
│
├── docker-compose.yml      # Multi-container orchestration
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**: Core programming language
- **Pandas**: Data processing and transformation
- **Supabase Python Client**: Database operations
- **Requests**: HTTP API calls

### Data Transformation
- **dbt**: SQL-based transformation framework
- **PostgreSQL**: Database engine (via Supabase)

### Frontend
- **React 18**: UI framework
- **Vite**: Build tool and dev server
- **Tremor**: UI component library
- **Supabase JS Client**: Real-time data fetching

### Infrastructure
- **Docker & Docker Compose**: Containerization
- **Supabase**: Backend-as-a-Service (PostgreSQL + API)
- **GitHub Actions**: CI/CD automation

## 📋 Prerequisites

- **Python 3.8+** (or Docker)
- **Node.js 16+** (or Docker)
- **Supabase account** (free tier works)
- **Docker & Docker Compose** (optional, for containerized deployment)
- **dbt** (for data transformations)

## 🚦 Quick Start

### Option 1: Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd reant_dataengineering
   ```

2. **Set up environment variables**:
   ```bash
   # Backend
   cp backend/.env.example backend/.env
   # Edit backend/.env with your Supabase credentials
   
   # Frontend
   cp frontend/.env.example frontend/.env
   # Edit frontend/.env with your Supabase credentials
   ```

3. **Set up Supabase database**:
   - Create a project on [Supabase](https://supabase.com)
   - Run the SQL from `supabase/schema.sql` in the SQL Editor
   - Get your project URL and anon key from Settings > API

4. **Start services**:
   ```bash
   docker-compose up --build
   ```

5. **Access the application**:
   - Frontend: http://localhost:3000
   - Backend pipeline runs automatically

### Option 2: Local Development

#### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Supabase credentials
python pipeline.py
```

#### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env
# Edit .env with your Supabase credentials
npm run dev
```

#### dbt Setup

```bash
cd dbt
pip install dbt-postgres

# Configure database connection
# Copy profiles.yml.example to ~/.dbt/profiles.yml (or %USERPROFILE%\.dbt\profiles.yml on Windows)
# Edit with your Supabase database credentials

# Test connection
dbt debug

# Run transformations
dbt run
dbt test
```

See [dbt/README.md](dbt/README.md) for detailed dbt setup instructions.

## 📚 Documentation

- **[SETUP.md](SETUP.md)**: Detailed setup instructions
- **[DOCKER.md](DOCKER.md)**: Docker-specific documentation
- **[DEPLOYMENT.md](DEPLOYMENT.md)**: Deployment guides
- **[QUICK_DEPLOY.md](QUICK_DEPLOY.md)**: Quick deployment guide
- **[backend/README.md](backend/README.md)**: Backend pipeline documentation
- **[frontend/README.md](frontend/README.md)**: Frontend application documentation
- **[dbt/README.md](dbt/README.md)**: dbt transformation documentation

## 🔄 Data Flow

```
Open-Meteo API
    ↓
Backend Pipeline (Python)
    ↓
Supabase (PostgreSQL) - Raw Data
    ↓
dbt Transformations
    ↓
Analytics-Ready Tables
    ↓
Frontend Dashboard (React)
```

## 🧪 Running Tests

### Backend
```bash
cd backend
python -m pytest  # If tests are added
```

### dbt
```bash
cd dbt
dbt test  # Run data quality tests
```

## 🐳 Docker Commands

```bash
# Build images
docker-compose build

# Start services in background
docker-compose up -d

# View logs
docker-compose logs -f
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up --build

# Run backend pipeline manually
docker-compose run backend python pipeline.py
```

## 🚀 Deployment

This project can be deployed completely free! 🎉

### Quick Deploy (Recommended)

1. **Frontend**: Deploy to [Vercel](https://vercel.com) in 2 minutes
   - See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for instructions

2. **Backend**: Use GitHub Actions (already configured)
   - Add `SUPABASE_URL` and `SUPABASE_KEY` to GitHub Secrets
   - Workflow runs daily at 6 AM UTC or can be triggered manually

3. **Database**: Supabase free tier
   - Already set up with your Supabase project

4. **dbt**: Run locally or in CI/CD
   - Can be integrated into GitHub Actions
   - Or run on a schedule using GitHub Actions

### Deployment Options

- **Frontend**: [Vercel](https://vercel.com), [Netlify](https://netlify.com), [Cloudflare Pages](https://pages.cloudflare.com)
- **Backend Pipeline**: GitHub Actions (already configured)
- **Full Stack**: [Railway](https://railway.app), [Render](https://render.com)
- **dbt**: GitHub Actions, [dbt Cloud](https://www.getdbt.com/product/cloud), or local execution

📖 **See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions**  
⚡ **See [QUICK_DEPLOY.md](QUICK_DEPLOY.md) for 5-minute setup**

## 🔧 Configuration

### Environment Variables

#### Backend (.env)
```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
```

#### Frontend (.env)
```env
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
```

#### dbt (profiles.yml)
See [dbt/profiles.yml.example](dbt/profiles.yml.example) for database connection configuration.

## 📊 Database Schema

The project uses two main tables:

1. **weather_data**: Stores weather observations
   - Location, temperature, humidity, wind speed, timestamp

2. **analytics**: Tracks frontend events
   - Event type, timestamp, user agent, referrer

See [supabase/schema.sql](supabase/schema.sql) for complete schema definitions.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Open-Meteo](https://open-meteo.com/) for free weather API
- [Supabase](https://supabase.com) for backend infrastructure
- [dbt](https://www.getdbt.com/) for data transformation framework
- [Tremor](https://www.tremor.so/) for UI components

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the documentation in each component's README
- Review the setup guides in the root directory

---

**Built with ❤️ for modern data engineering**
