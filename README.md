# jubilant-eureka
ESP32 UDP testcase

Setup
----
1) This works on arduino, or IDF+Arduino 

2) Tested with latest as of Jan 7:
	arduino-esp32 7cef2e2
	esp-idf 8e4a8e1

3) Edit the apa102.cpp with your network info, and LED pin #

4) Edit the stress.py with the appropiate IP address and com port of the device under test


Fail Test
----
1) Run the stress.py

2) CPU Halt typically occurs in <20 minutes (Sometimes halt message doesn't apppear, though lights stop blinking)

Pass Test
----
1) Edit app_main in components/arduino/cores/esp32/main.cpp as follows and reflash (or hardware\espressif\esp32\cores\esp32\main.cpp for Arduino)

````
diff --git a/cores/esp32/main.cpp b/cores/esp32/main.cpp
index c2300b4..49f0932 100644
--- a/cores/esp32/main.cpp
+++ b/cores/esp32/main.cpp
@@ -15,7 +15,7 @@ void loopTask(void *pvParameters)
 extern "C" void app_main()
 {
     initArduino();
-    xTaskCreatePinnedToCore(loopTask, "loopTask", 4096, NULL, 1, NULL, 1);
+    xTaskCreatePinnedToCore(loopTask, "loopTask", 4096, NULL, 1, NULL, 0);
 }

 #endif

````
2) Run the stress.py while monitoring the DUT's serial port

3) Observe no failures for multiple hours.

