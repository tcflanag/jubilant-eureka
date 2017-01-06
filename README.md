# jubilant-eureka
ESP32 UDP testcase

Setup
----
1) Make sure to install the https://github.com/espressif/arduino-esp32 into the components directory as normal. (I last used d84d912)


2) Edit the apa102.cpp with your network info, and LED pin #

3) Edit the stress.py with the appropiate IP address and com port of the device under test


Fail Test
----
1) Run the stress.py

2) CPU Halt typically occurs in <20 minutes (Sometimes halt message doesn't apppear, though lights stop blinking)

Pass Test
----
1) Edit app_main in components/arduino/cores/esp32/main.cpp as follows and reflash
````
extern "C" void app_main()
{
	initArduino();
    xTaskCreatePinnedToCore(loopTask, "loopTask", 1024, NULL, 1, NULL, 1);
    //setup();
    //for(;;) {
        //loop();
    //}
}
````
2) Run the stress.py while monitoring the DUT's serial port

3) Observe no failures for multiple hours.

