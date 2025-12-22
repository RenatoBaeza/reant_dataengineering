# Frontend - Weather Dashboard

React application built with Vite and Tremor UI components for visualizing weather data from Supabase.

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
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
```

## Building for Production

```bash
npm run build
```

Preview the production build:
```bash
npm run preview
```

The app will be available at [http://localhost:3000](http://localhost:3000)

## Features

- Real-time weather data visualization
- Interactive charts using Tremor components
- Responsive design
- Data refresh functionality
- Optimized production builds with Vite

