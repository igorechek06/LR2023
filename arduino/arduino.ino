#include <Servo.h>

Servo myservo;
String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(9600);
  myservo.attach(3);
}

void loop() {
  if (stringComplete) {
    if (inputString == "-1") {
      myservo.write(98);
    } else if (inputString == "1") {
      myservo.write(86);
    } else if (inputString == "0") {
      myservo.write(92);
    }
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char) Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
      Serial.flush();
    } else {
      inputString += inChar;
    }
  }
}