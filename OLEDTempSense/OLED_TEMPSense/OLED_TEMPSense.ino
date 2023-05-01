//library calls
#include <Wire.h>             //--
#include <Adafruit_GFX.h>     //-- Allows interfacing with OLED 
#include <Adafruit_SSD1306.h> //--
#include <Adafruit_Sensor.h>  //|| Allows interfacing with DHT-type sensors
#include <DHT.h>              //||

//  https://randomnerdtutorials.com/guide-for-oled-display-with-arduino/

//defines OLED displays properties
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

//init display object (&Wire is used for l2c communication protocol, -1 is used as the OLED doesn't have a reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

//defines DHT Sensor type
#define DHTTYPE DHT11
#define DHTPIN 2


//init DHT object using prev definitions
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200); //init serial monitor for debugging
  dht.begin();          //init dht sensor

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3c) ){  //init OLED display
      Serial.println(F("SSD1306 allocation failed")  );
      for(;;);
    }

  delay(2000);                  //delay so display can init
  display.clearDisplay();       //clear display
  display.setTextColor(WHITE);  //text colour to white

}

void loop() {
  delay(5000);

  float t = dht.readTemperature();  //read temp & humidity
  float h = dht.readHumidity();

  if(isnan(h) || isnan(t)){         //error handling when readings cant be taken
      Serial.println("Failed to read from DHT sensor!");
    }

  //clear screen
  display.clearDisplay();

  //display temperature
  display.setTextSize(1);
  display.setCursor(0,0);
  display.print("Temperature: ");
  display.setTextSize(2);
  display.setCursor(0, 10);
  display.print(t);
  display.print(" ");
  display.setTextSize(1);
  display.cp437(true);
  display.write(167);
  display.setTextSize(2);
  display.print("C");
  Serial.println("TEMPERATURE: ");
  Serial.println(t);

  //display humidity
  display.setTextSize(1);
  display.setCursor(0, 35);
  display.print("Humidity:  ");
  display.setTextSize(2);
  display.setCursor(0, 45);
  display.print(h);
  display.print(" %");
  Serial.println("HUMIDITY: ");
  Serial.println(h);

  display.display();
}
