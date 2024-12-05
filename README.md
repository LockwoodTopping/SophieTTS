# SophieTTS
This is a TTS proof-of-concept for Sophie

SophieTTS is a Python script which utilizes Selenium to access online text-to-speech solutions and read aloud the text you input. It supports controlling the speed of speech and allows you to specify the browser you'd like to use (Chrome, Edge, or Safari).

Features:
Read aloud text using configured websites.
Customizable speech speed.
Prepend a wake word (default is "Alexa").
Choose the browser to run the script (Chrome, Edge, Safari).
Headless browser operation for background execution.


---------------------
--  Prerequisites  --

**Python**
If you don't have Python installed on your computer, follow these steps to download and install it:

Visit the official Python website.
Download the latest Python version (ensure it's version 3.6 or higher).
During installation, check the box that says "Add Python to PATH" (this will make it easier to run Python from the command line).
Complete the installation by following the on-screen instructions.
To verify that Python is installed correctly, open the Command Prompt and type:
  python --version
If Python is installed, it will show the version number, like Python 3.x.x.


--------------------------
--  Running the Script  --

1. Download the Repository
Go to the SophieTTS GitHub repository.
Click on the Code button and choose Download ZIP.
Extract the ZIP file to a folder on your computer.
Alternatively, if you have Git installed, you can clone the repository using:
  git clone https://github.com/LockwoodTopping/SophieTTS.git

2. Run the Script
To run the script, follow these steps:

    2.1 Navigate to the script folder (where SophieTTS.py is located) in the command prompt:
      cd path\to\your\folder\SophieTTS

    2.2 Run the script using Python:
      python SophieTTS.py -t "What is the weather?"
        - says "Alexa, what is the weather?" over the computer speakers


----------------
--  Examples  --

  python SophieTTS.py -t "Turn off the light."
  
    - says "Alexa, turn off the light."


  python SophieTTS.py -t "What is the Weather Today" -b edge
  
    - uses the edge browser to access the TTS site
    
    - says "Alexa, what is the weather Today."


  python SophieTTS.py -t "Play some music" --wake-word "Siri"
  
    - says "Siri, turn off the light."


  python SophieTTS.py -l
  
    - lists the available TTS sites configured in the script


  python SophieTTS.py -h
  
    - provides examples of how to use the script  



  ays "Alexa, turn off the light."
  
    - python SophieTTS.py -t "Turn off the light."


  uses the edge browser to access the TTS site. says "Alexa, what is the weather Today."
  
    - python SophieTTS.py -t "What is the Weather Today" -b edge


  says "Siri, turn off the light."
  
    - python SophieTTS.py -t "Play some music" --wake-word "Siri"


  lists the available TTS sites configured in the script
  
    - python SophieTTS.py -l


  provides examples of how to use the script
  
    - python SophieTTS.py -h  

------------------
--  Parameters  --

--text or -t: The text you want to be read aloud. This is required.

--speed or -spd: The speed of the TTS voice (default is 0.85). Valid values are between 0.5 and 2.0.

--browser or -b: Choose the browser to use for Selenium (options: chrome, edge, or safari). The default is chrome.

--site or -s: Choose the TTS site to use out of the configured site list (default is ttsmp3). Use --list-sites or -l to list all available configured TTS sites.

--wake-word or -w: The wake word to prepend to the text (default is "Alexa").

--list-sites or -l: List all available TTS sites.  


------------------
--  Known Bugs  --

The script currently outputs a line to the console saying "DevTools listening on port ...". This is a bug with Selenium which currently does not have a working solution for our application.
