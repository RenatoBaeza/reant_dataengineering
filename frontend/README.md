# Frontend - Weather Dashboard

React application built with Tremor UI components for visualizing weather data from Supabase.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

3. Add your Supabase credentials to `.env`:
```
REACT_APP_SUPABASE_URL=https://your-project.supabase.co
REACT_APP_SUPABASE_ANON_KEY=your-anon-key
```

## Running the Application

Start the development server:
```bash
npm start
```

The app will open at [http://localhost:3000](http://localhost:3000)

## Building for Production

```bash
npm run build
```

## Features

- Real-time weather data visualization
- Interactive charts using Tremor components
- Responsive design
- Data refresh functionality

