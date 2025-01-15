# IoT Phone App Back End

Josh Rimes (Student at Cardiff University)

Project start date: 29/01/24

This project builds upon a group project I was part of for my 'CM2211 - Internet of Things' module at Cardiff University. Not all the code is my own.

## Project overview

This project is an app that allows voice input when a physical button connected to a Raspberry Pi is pressed. The voice input is run through OpenAI's API and an AI generated answer is outputted back from the Raspberry Pi.

This is the backend code for the IoT phone app project. This should be installed on the Raspberry Pi and the LED button should be plugged into port D4 on the GrovePi+ board.

### Technologies:
- Python
- Shell
- Raspberry Pi 4
    - GrovePi+
    - LED Button

### How to run

Requires Python 3.6+

1. Run the install script `bash install.sh` (Do not run it as superuser, as this can cause issues)
2. Download the ffmpeg package. `sudo apt-get install ffmpeg`
3. Run the code by executing the run script `bash run.sh`


### Troubleshooting

Sometimes, configuring a local venv can fail. If this is the case, attempt to install the requirements to your global Python installation as well as the GrovePi library. More information on how to configure the GrovePi library can be found here <https://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/>
