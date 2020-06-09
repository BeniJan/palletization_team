### RUN THIS ON YOUR ARDUINO ###

Are you on:

*~ Linux*
    Install _pyfirmata_ on your desktop using pip: "pip install pyfirmata"
        In case of not having pip, install it by running "sudo apt-get install pip"

    To give _pyfirmata_ permissions to access arduino port run in your terminal: "sudo chmod a+rw /dev/ttyACM0"

    Open your Arduino IDE, access _pyfirmata_ examples, then open the _"StandardFirmata"_ example and upload it to your arduino.

    Then you are ready to go, just enter the desired shirt objects list in _shirtDisorderedList_ variable at *main.py*
    and run it by entering "python main.py" inside your terminal at the root of the project.

*~ Windows*
    Install _pyfirmata_ on your desktop by following this link [1] simple steps.

    Once this project was developed in linux, to run in windows you will need to change:
    "board = Arduino('/dev/ttyACM0')" to "board = Arduino(‘COM3’)"

    Open your Arduino IDE, access _pyfirmata_ examples, then open the _"StandardFirmata"_ example and upload it to your arduino.

    Then you are ready to go, just enter the desired shirt objects list in _shirtDisorderedList_ variable at *main.py*
    and run it by entering "python main.py" inside your terminal at the root of the project.