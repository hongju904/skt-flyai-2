using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;
using Microsoft.Azure.Devices;
using Microsoft.Azure.Devices.Client;

namespace IoTDevice
{
    internal class Program
    {
        private static System.Timers.Timer SensorTimer;
        private static DummySensor Sensor = new DummySensor();
        private const string DeviceConnectionString = "HostName=labuser20.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=OmVH5gcCH766etcTvItUfREhXQlNFWW07FnvLL47TMs=";
        private const string DeviceID = "Device1";
        private static DeviceClient SensorDevice = null;

        static void Main(string[] args)
        {
            SensorDevice = DeviceClient.CreateFromConnectionString(DeviceConnectionString, DeviceID);
            SetTimer();

            if (SensorDevice == null)
            {
                Console.WriteLine("Failed to create DeviceClient");
                SensorTimer.Stop();
            }
          

            Console.WriteLine("\nPress the Enter key to exit the application...\n");
            Console.WriteLine("The application started at {0:HH:mm:ss.fff}", DateTime.Now);
            Console.ReadLine();
        }

        private static void SetTimer()
        {
            SensorTimer = new System.Timers.Timer();
            SensorTimer.Interval = 2000;
            SensorTimer.Enabled= true;
            SensorTimer.AutoReset= true;

            SensorTimer.Elapsed += SensorTimer_Elapsed;
        }

        private static async void SensorTimer_Elapsed(object sender, ElapsedEventArgs e)
        {
            Console.WriteLine("The Elapsed event was rised at {0:HH:mm:ss.fff}", e.SignalTime);
            WeatherModel weatherModel = Sensor.GetWeatherModel("Device1");
            
            string json = Newtonsoft.Json.JsonConvert.SerializeObject(weatherModel);
            Console.WriteLine(json);

            Message eventmessage = new Message(Encoding.UTF8.GetBytes(json));
            await SensorDevice.SendEventAsync(eventmessage);
        }
    }
}
