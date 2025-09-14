# Obstacle-Avoiding-Robot

The goal of this project is to build a car-bot that can detect obstacles and avoid them. This is a micro controller based project which takes sensor inputs and controls motor outputs. We use an ultrasonic sensor to measure distance to an obstacle and control the motors using micro-python running on a Raspberry Pi Pico micro-controller.

Here are the components used:
* Raspberry Pi Pico
* L298N motor driver
* Ultra Sonic sensors
* Two motors
* Two wheels to attach to the motor
* Castor wheel for the front
* A spaces to adjust the height of the castor wheel
* A PCB to use as a chassis
* Two Lithium ion 18650 batteries and a case
* Switch for on-off 


 ## Note:
 
Using a bread board will allow you to experiment a lot more with the project. You can opt to solder the components once the project is reasonably working.

 Using a PCB as a chassis is convenient but not suggested because it does not hold all the components together for too long. When held together by hot glue, the castor wheel and motors do not stick strong enough to the PCB. If you are looking for a more sturdy design, use bolts and nuts to hold the components to the chase.

 Caution : Be sure to use a motor of the correct rating because if the current is too high for the motor, the armature may burn giving a very distinct burning smell. In that case, do not worry. Turn the bot off for sometime and let it cool down and it will run again.The bot can only run in short intervals of time and will need some time to cool down. This also greatly reduces its durability. If the current is too low, then the motor does not even turn on, so you may have to increase the number of batteries.

 Another suggested method of controlling the current through the motor is through PWM - This is a software solution to the problem. This is what is done in the code. This allows flexibility to use a variety of BO motors with two or three Lithium batteries.


 ## Images of the bot
![20250914_143543](https://github.com/user-attachments/assets/9cba1308-88c5-4382-abef-1cfbd9a1c47c)
![20250914_143656](https://github.com/user-attachments/assets/c34f1b98-f781-48e8-9433-90cfe758ddbb)
![20250914_143843](https://github.com/user-attachments/assets/19e9724d-c9be-4eed-835f-548d5a1ddeac)
