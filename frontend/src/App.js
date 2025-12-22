import React, { useState, useEffect } from 'react';
import { createClient } from '@supabase/supabase-js';
import {
  Card,
  Title,
  Text,
  Grid,
  Metric,
  Flex,
  BarChart,
  LineChart,
  DonutChart,
} from '@tremor/react';
import './App.css';

const supabaseUrl = process.env.REACT_APP_SUPABASE_URL;
const supabaseKey = process.env.REACT_APP_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseKey) {
  console.error('Missing Supabase configuration');
}

const supabase = supabaseUrl && supabaseKey 
  ? createClient(supabaseUrl, supabaseKey)
  : null;

function App() {
  const [weatherData, setWeatherData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchWeatherData();
  }, []);

  const fetchWeatherData = async () => {
    if (!supabase) {
      setError('Supabase not configured. Please set REACT_APP_SUPABASE_URL and REACT_APP_SUPABASE_ANON_KEY');
      setLoading(false);
      return;
    }

    try {
      setLoading(true);
      const { data, error: fetchError } = await supabase
        .from('weather_data')
        .select('*')
        .order('timestamp', { ascending: false })
        .limit(100);

      if (fetchError) throw fetchError;

      setWeatherData(data || []);
      setError(null);
    } catch (err) {
      console.error('Error fetching data:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Calculate statistics
  const latestData = weatherData.slice(0, 5); // Latest 5 records
  const avgTemperature = weatherData.length > 0
    ? (weatherData.reduce((sum, d) => sum + (d.temperature || 0), 0) / weatherData.length).toFixed(1)
    : 0;
  const avgHumidity = weatherData.length > 0
    ? (weatherData.reduce((sum, d) => sum + (d.humidity || 0), 0) / weatherData.length).toFixed(1)
    : 0;
  const avgWindSpeed = weatherData.length > 0
    ? (weatherData.reduce((sum, d) => sum + (d.wind_speed || 0), 0) / weatherData.length).toFixed(1)
    : 0;

  // Prepare chart data
  const locationData = latestData.reduce((acc, record) => {
    const loc = record.location;
    if (!acc[loc]) {
      acc[loc] = { location: loc, temperature: 0, humidity: 0, wind_speed: 0, count: 0 };
    }
    acc[loc].temperature += record.temperature || 0;
    acc[loc].humidity += record.humidity || 0;
    acc[loc].wind_speed += record.wind_speed || 0;
    acc[loc].count += 1;
    return acc;
  }, {});

  const chartData = Object.values(locationData).map(loc => ({
    location: loc.location,
    temperature: (loc.temperature / loc.count).toFixed(1),
    humidity: (loc.humidity / loc.count).toFixed(1),
    wind_speed: (loc.wind_speed / loc.count).toFixed(1),
  }));

  // Time series data for line chart
  const timeSeriesData = weatherData.slice(0, 20).reverse().map(record => ({
    date: new Date(record.timestamp).toLocaleTimeString(),
    temperature: record.temperature || 0,
    humidity: record.humidity || 0,
  }));

  if (loading) {
    return (
      <div className="App">
        <div className="container">
          <Text>Loading weather data...</Text>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="App">
        <div className="container">
          <Card>
            <Title>Error</Title>
            <Text>{error}</Text>
          </Card>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <div className="container">
        <Title className="main-title">Weather Data Dashboard</Title>
        <Text className="subtitle">Real-time weather data visualization</Text>

        {/* Key Metrics */}
        <Grid numItems={1} numItemsSm={2} numItemsLg={3} className="gap-6 mt-6">
          <Card>
            <Text>Average Temperature</Text>
            <Metric>{avgTemperature}°C</Metric>
          </Card>
          <Card>
            <Text>Average Humidity</Text>
            <Metric>{avgHumidity}%</Metric>
          </Card>
          <Card>
            <Text>Average Wind Speed</Text>
            <Metric>{avgWindSpeed} m/s</Metric>
          </Card>
        </Grid>

        {/* Charts */}
        <Grid numItems={1} numItemsLg={2} className="gap-6 mt-6">
          <Card>
            <Title>Temperature by Location</Title>
            <BarChart
              data={chartData}
              index="location"
              categories={["temperature"]}
              colors={["blue"]}
              valueFormatter={(value) => `${value}°C`}
            />
          </Card>

          <Card>
            <Title>Humidity by Location</Title>
            <DonutChart
              data={chartData}
              category="humidity"
              index="location"
              valueFormatter={(value) => `${value}%`}
              colors={["slate", "violet", "indigo", "rose", "cyan", "amber"]}
            />
          </Card>
        </Grid>

        <Card className="mt-6">
          <Title>Temperature & Humidity Over Time</Title>
          <LineChart
            data={timeSeriesData}
            index="date"
            categories={["temperature", "humidity"]}
            colors={["blue", "green"]}
            valueFormatter={(value) => 
              value > 50 ? `${value}%` : `${value}°C`
            }
            yAxisWidth={60}
          />
        </Card>

        {/* Latest Data Table */}
        <Card className="mt-6">
          <Title>Latest Weather Records</Title>
          <div className="table-container">
            <table className="data-table">
              <thead>
                <tr>
                  <th>Location</th>
                  <th>Temperature (°C)</th>
                  <th>Humidity (%)</th>
                  <th>Wind Speed (m/s)</th>
                  <th>Timestamp</th>
                </tr>
              </thead>
              <tbody>
                {latestData.map((record, idx) => (
                  <tr key={idx}>
                    <td>{record.location}</td>
                    <td>{record.temperature?.toFixed(1) || 'N/A'}</td>
                    <td>{record.humidity?.toFixed(1) || 'N/A'}</td>
                    <td>{record.wind_speed?.toFixed(1) || 'N/A'}</td>
                    <td>{new Date(record.timestamp).toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </Card>

        <Flex justifyContent="center" className="mt-6">
          <button onClick={fetchWeatherData} className="refresh-button">
            Refresh Data
          </button>
        </Flex>
      </div>
    </div>
  );
}

export default App;

