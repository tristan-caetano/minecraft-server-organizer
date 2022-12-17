// Tristan Caetano
// Pi Remote Power
// Using Raspberry Pi to remotely turn on my server

#include <wiringPi.h>
#include <stdio.h>

#define PWR_PIN 0

void main(void) {

  wiringPiSetup();

  pinMode(PWR_PIN, OUTPUT);

  while(1){

    digitalWrite(PWR_PIN, HIGH);
    delay(100);
    digitalWrite(PWR_PIN, LOW);
    delay(100);
}