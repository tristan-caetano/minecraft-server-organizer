// Tristan Caetano
// Pi Remote Power
// Using Raspberry Pi to remotely turn on my server

// Including Libraries
#include <wiringPi.h>
#include <stdio.h>

// Defining output pin
#define PWR_PIN 0

// Function for turning on server
void main(void) {

    // Setting up wiringPi
    wiringPiSetup();

    // Setting the pin as output
    pinMode(PWR_PIN, OUTPUT);

    // Sending a brief signal
    digitalWrite(PWR_PIN, HIGH);
    delay(100);
    digitalWrite(PWR_PIN, LOW);

    return(void);

}