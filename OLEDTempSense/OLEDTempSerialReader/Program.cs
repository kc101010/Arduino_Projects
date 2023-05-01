using System;
using System.IO.Ports;
using System.IO;

// https://www.techcoil.com/blog/how-to-use-c-to-read-sensor-data-from-arduino-or-espx-via-serial-connection/ 

namespace OLEDTempSerialReader
{
    class Program
    {
        static void Main(string[] args)
        {

			Console.Title = "Arduino Sensor Reader";

			try
			{
				SerialPort port = new SerialPort();
				port.BaudRate = 115200;
				port.PortName = "COM5";
				port.Open();

				try
				{
					while (true) {
						string reading = port.ReadLine();
						DateTime now = DateTime.Now;
						Console.WriteLine(now + " :: " + reading);
						System.Threading.Thread.Sleep(500);

						try
						{
							File.AppendAllText("reading.txt" ,now + " :: " + reading);
						}
						catch (Exception er)
						{
							Console.WriteLine(er);
						}
					}
				}
				catch (Exception ex)
				{
					Console.WriteLine("Error reading serial port");
					Console.WriteLine(ex.ToString());
				}
			}
			catch (Exception ex)
			{
				Console.WriteLine("Error opening serial port");
				Console.WriteLine(ex.ToString());
			}

			Console.ReadLine();
        }
    }
}
