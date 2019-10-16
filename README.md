# Jenkins Arduino Minion

This is a side project made at work for having [this thing](https://www.amazon.com/Despicable-Me-BEE-DO-Fireman-Minion/dp/B00JGPIZFC) go BEE-DOO whenever a Jenkins job failed.

## Requirements
- Jenkins
- A PC that is not being used
- [This thing](https://www.amazon.com/Despicable-Me-BEE-DO-Fireman-Minion/dp/B00JGPIZFC)
- An Arduino
- A breadboard
- A soldering gun
- An optocoupler
- Maybe some resistors, I don't know
- Patience

## Usage

Well, you need to wire the Arduino on PIN 11 (or a PIN of your choice) to a breadboard with the optocoupler that provides power to the minions internal wiring (basically closing the circuit, mimicing what the button does on his chest).
After that, connect the Arduino to a PC and run the python script. Make sure to adjust the Jenkins hosts and conditions. 

Good luck.

## Disclaimer
If your workplace goes up in flames, I'm not responsible.
