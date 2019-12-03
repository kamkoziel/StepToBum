 Step to Bum 
=========
# About
Final project on the subject of _Biomedical Engineering in practice_. 

The application is used to record the sound signal of the test person's steps
 and the emission of the acoustic disorder. For proper operation, the microphone 
 connected to the computer should be placed close enough to the subject's legs. 
 The examined person should wear headphones connected to the computer so that 
 the sound signal can be played.
 
 The application allows you to make an acoustic signal automatically or when you click the button. The method of signal emission is set in the Audio menu of the Menu bar. The broadcasting time is set in Settings.

Non-automatic mode allows you to control the time only based on the LCD timer. (to change)
 
###### Todo
- saving the sound emission time in the file name of the recording
- improving the look of GUI
- ....

#### Author 
Kamil Kozieł

email: kkoziel@outlook.com

## Prepare virtual environment

First step to run application is create new python virtual environment

``` python
python3 -m venv venv
```
Next you have to active your environment
``` python
venv\Scripts\activate.bat
``` 
## Install requirements packages
``` bash
(venv) (...)> pip install (pathTo_StepToBum)\requirements.txt
```
#### PyAudio install 
If you have problem with PyAudio package install you should check: [PyAudio install problem].

## Running app
To run app you should run you command prompt from StepToBum directory and then type:
``` bash
(venv) (...)> python steup.py
```
### IMPORTANT NOTE!
 
Before using the application for the first time, make sure everything 
has been properly configured. To do this, choose File -> Settings,
 from the menu bar.


Based on [PROJECT] 

[PyAudio install problem]:(https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-my-python-how-to-do-it)
[PROJECT]:(https://flothesof.github.io/pyqt-microphone-fft-application.html)