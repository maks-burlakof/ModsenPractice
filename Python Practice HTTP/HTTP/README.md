# ExpressJS Weather API

This project is an Express.js application that provides a set of API endpoints to get weather information from the OpenWeather API. Additionally, it includes a simple "Hello World" endpoint.

## Endpoints

- GET / - this page  
- POST / - example post request  
- PATCH / - example patch request  
- PUT / - example put request  
- DELETE / - example delete request  
- GET /hello - returns "Hello, World!"  
- GET /weather/city/:name - Fetch weather data by city name.  
- GET /weather/cityid/:id - Fetch weather data by city ID.  
- GET /weather/coordinates?lat=latitude&lon=longitude - Fetch weather data by geographic coordinates.

## Prerequisites

- Node.js (>= 12.x)
- npm (>= 6.x)
- An OpenWeather API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/maks-burlakof/ModsenPractice.git
   cd "Python Practice HTTP/HTTP/"
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add the following environment variables:

   ```bash
   cp .env.example .env
   ```

   ```plaintext
   OPENWEATHER_API_KEY="your_openweather_api_key"
   ```

4. **Start the server:**

   ```bash
   DEBUG=myapp:* npm start
   ```
