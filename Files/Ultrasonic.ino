#include <NewPing.h>                    //library for ultarsonic sensor

#define TRIGGER_PIN D1                 //defining pin number of trigger
#define ECHO_PIN D2                    //defining pin number of echo

NewPing sonar(TRIGGER_PIN, ECHO_PIN);  // creating object of NewPing

unsigned int dist;                     //defining variables 
unsigned int uS ;

void setup() {
 Serial.begin(9600);                  //starting the serial communication
 pinMode(TRIGGER_PIN,OUTPUT);        //set trigger pin for output
 pinMode(ECHO_PIN,INPUT);            //set echo pin for input
}


void loop() {

  digitalWrite(TRIGGER_PIN,LOW);      //stop previous wave for fresh start
  
  uS = sonar.ping();                  //Sends a ping , returns the echo time in microseconds
  
  Serial.print("Distance: ");
  dist=(uS / US_ROUNDTRIP_CM);        //calculating the distance in cm 
  Serial.println(dist);
  delay(1500);                        //delay of 1.5 sec before running loop next time time 
  
  
}
