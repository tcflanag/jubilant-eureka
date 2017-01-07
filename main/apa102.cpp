#include "Arduino.h"
#include <WiFi.h>
#include <WiFiUDP.h>


// WiFi network name and password:
const char * networkName = "Bill.Wi.The.Science.Fi";
const char * networkPswd = "ScienceRules1";


const int LED_PIN = 5;

WiFiUDP Udp;

void setup()
{
    // Initilize hardware:
    Serial.begin(115200);
    pinMode(LED_PIN, OUTPUT);

    WiFi.begin(networkName, networkPswd);

    digitalWrite(LED_PIN, LOW); // LED offnn
    Udp.begin(0x1936);
}

void loop()
{

    char packetBuffer[2000];
    int noBytes = Udp.parsePacket();
    String received_command = "";
    if ( noBytes ) {

        // We've received a packet, read the data from it
        Udp.read(packetBuffer,noBytes); // read the packet into the buffer
        digitalWrite(LED_PIN, !digitalRead(LED_PIN));

    }
}



