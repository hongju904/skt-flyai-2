using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IoTDevice
{
    internal class DummySensor
    {
        private Random _Random = new Random();

        public WeatherModel GetWeatherModel(string deviceID)
        {
            WeatherModel weatherModel = new WeatherModel();

            weatherModel.DeviceID= deviceID;
            weatherModel.Temperature = _Random.Next(25, 32);
            weatherModel.Huminity = _Random.Next(60, 80);
            weatherModel.Dust = _Random.Next(1, 5) + weatherModel.Temperature;

            return weatherModel;
        }
    }
}
