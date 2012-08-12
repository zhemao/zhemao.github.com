---
title: Programming an AVR Microcontroller
layout: post
---

This post details the process of compiling C code into an AVR hex file and
programming it onto an ATMega328 microcontroller using an Arduino Uno board
as the programmer. The information on how to do this was culled from several 
different sources online. 

# Step 1: Installing dependencies

Make sure you have the following pieces of software installed.

    arduino
    make
    avrdude
    avr-gcc
    avr-binutils

# Step 2: Setting up Arduino

Plug the Arduino into your computer and compile and upload the ArduinoISP
sketch. This should be under File -> Examples -> ArduinoISP.

# Step 3: Compiling and Linking the Code

Check out the source code from https://bitbucket.org/zhemao/ledblink

    git clone https://bitbucket.org/zhemao/ledblink.git

Compile the ledblink.c file into an object file using avr-gcc.

    avr-gcc -c -Os -Wall -DF_CPU=8000000 -mmcu=atmega328 ledblink.c

Note that -DF\_CPU is just passing in a preprocessor variable. You won't have
to do this if you are writing your own code. The -Os optimization flag tells
the compiler to optimize for a smaller executable. This is helpful when 
writing to a small microcontroller ROM.

Link the object file into an ELF executable
    
    avr-gcc -mmcu=atmega328 ledblink.o -o ledblink.elf

Convert the ELF executable into an AVR hex file

    avr-objcopy -O ihex -R .eeprom ledblink.elf ledblink.hex

You can do all of the above using the makefile by just running make with
no arguments.

# Step 3: Setting up the circuit.

Hook up the Uno to the ATMega328 according the [instructions](http://arduino.cc/en/Tutorial/ArduinoISP)
on the Arduino website. Hook up an LED in series with a resistor to the PD6 pin
on the ATMega328. This would be pin 12 (3rd from the bottom on the left side).
You can find the ATMega328 datasheet at http://www.atmel.com/Images/8271s.pdf.

# Step 4: Programming the Microcontroller

Make sure ArduinoISP is running properly, and then run the following command to
upload the hex file.

    avrdude -p m328p -P /dev/ttyACM0 -c avrisp -b 19200 -U flash:w:ledblink.hex

The -p flag denotes the chip number of the microcontroller (m328p corresponds to
ATMega328p). The -P flag is the device file for the serial port. It may be 
something different on your system. It is generally something linke 
/dev/ttyACMx or /dev/ttyUSBx, where x is a number. The -c flag is the name of 
the programmer, in this case ArduinoISP. The -b flag specifies the USB baud 
rate, which is 19200 Bd for the Arduino. And the -U flag just tells avrdude 
what file to program onto the microcontroller.

If you are successful, you should see something like [this](http://www.youtube.com/watch?v=-IjRGw39Iek&feature=plcp).

# Attributions

ArduinoISP instructions from [Arduino website](http://arduino.cc/en/Tutorial/ArduinoISP). 

Code and compilation instructions by [Limor Fried](http://www.ladyada.net/learn/proj1/blinky.html) (AKA Lady Ada).

Programmer instructions from [Kurt T](http://www.openhardwarehub.com/projects/43-Scavenger-Hunt-Beacon-Decoder-and-AVR-Programmer).

# Update

I've recently discovered that you can use avrdude to upload the hex file to the
microcontroller on the arduino itself through the arduino bootloader. For
instance, on an arduino uno, you could do the following

    avrdude -p m328p -P /dev/ttyACM0 -c arduino -b 115200 -U flash:w:ledblink.hex

The github repository has been update with these as the defaults.
