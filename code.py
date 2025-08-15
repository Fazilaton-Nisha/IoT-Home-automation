code for the project
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "2ro_L9gmugpg6FfbtZ4Il5QMxJqlHY34";
// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "AndroidAP3DEC";
char pass[] = "123456";
void setup()
{
// Debug console
Serial.begin(9600);
Blynk.begin(auth, ssid, pass);
// You can also specify server:
//Blynk.begin(auth, ssid, pass, "blynk-cloud.com", 80);
//Blynk.begin(auth, ssid, pass, IPAddress(192,168,1,100), 8080);
}
void loop()
{
Blynk.run();
}
BLYNK_WRITE(V0)
{
int pinValue = param.asInt(); // assigning incoming value from pin V1 to a variable
// You can also use:
// String i = param.asStr();
// double d = param.asDouble();
analogWrite(D0, pinValue);
Blynk.virtualWrite(V1, pinValue);
Serial.print("V0 Slider value is: ");
Serial.println(pinValue);
}