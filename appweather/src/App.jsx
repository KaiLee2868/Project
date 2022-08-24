import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { Container } from 'react-bootstrap';
import WeatherButton from './components/WeatherButton';
import WeatherBox from './components/WeatherBox';


import { ClipLoader } from 'react-spinners';


const cities = ['paris', 'new york', 'london', 'seoul'];
const API_KEY = 'b4a0b63fb0a27cc709f6ea5ecd5f5d7d';

function App() {
  const [loading, setLoading] = useState(false);
  const [city, setCity] = useState(null);
  const [weather, setWeather] = useState(null);
  const [apiError, setAPIError] = useState('');

  const getWeatherByCurrentLocation = async (lat, lon) => {
    console.log('current', lat, lon);
    
    try {
      let url = //units=metric 
        // let url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
        // `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}`;
        'http://api.openweathermap.org/data/2.5/weather?lat=39.983334&lon=-82.983330&appid=b4a0b63fb0a27cc709f6ea5ecd5f5d7d';
      //&units=metric
      const res = await fetch(url);
      const data = await res.json();
      setWeather(data);
      setLoading(false);
    } catch (err) {
      setAPIError(err.message);
      setLoading(false);
    }
  };

  const getCurrentLocation = () => {
    navigator.geolocation.getCurrentPosition((position) => {
      const { latitude, longitude } = position.coords;
      getWeatherByCurrentLocation(latitude, longitude);
      
    });
  };

  const getWeatherByCity = async () => {
    try {
      let url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}`;
      //&units=metric
      const res = await fetch(url);
      const data = await res.json();

      setWeather(data);
      console.log(data)
      setLoading(false);
    } catch (err) {
      console.log(err);
      setAPIError(err.message);
      setLoading(false);
    }
  };

  useEffect(() => {
    if (city == null) {
      setLoading(true);
      getCurrentLocation();
    } else {
      setLoading(true);
      getWeatherByCity();
    }
  }, [city]);

  const handleCityChange = (city) => {
    if (city === 'current') {
      setCity(null);
    } else {
      setCity(city);
    }
  };
  // console.log(weather.data)
  return (        
    <div className= {weather&& weather.weather[0].main}>
      
  
    <Container className=" vh-100">      
      {loading ? (
        <div className="w-100 vh-100 d-flex justify-content-center align-items-center">
          <ClipLoader color="#f86c6b" size={500} loading={loading} />
        </div>
      ) : !apiError ? (
        <div className="main-container">
          <WeatherBox weather={weather} />
          <WeatherButton
            cities={cities}
            handleCityChange={handleCityChange}
            selectedCity={city}
          />
        </div>
      ) : (
        apiError
      )}
    </Container>
    </div>
  );
};




export default App;
