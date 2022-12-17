// Tristan Caetano
// Pi Remote Power
// Using Raspberry Pi to remotely turn on my server

// This script is run from the pi

// Including Libraries
#include <wiringPi.h>
#include <stdio.h>

// Defining output pin
#define PWR_PIN 0

// Function for turning on server
int main() {

    // Setting up wiringPi
    wiringPiSetup();

    // Setting the pin as output
    pinMode(PWR_PIN, OUTPUT);

    // Sending a brief signal
    digitalWrite(PWR_PIN, HIGH);
    delay(200);
    digitalWrite(PWR_PIN, LOW);

    return(0);

}