#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
}



void loop() { // run over and over
  if (Serial.available()) {
    char ch = Serial.read();
    mySerial.write(ch);
  }else if (mySerial.available()) {
    Serial.write(mySerial.read());
  }

}
