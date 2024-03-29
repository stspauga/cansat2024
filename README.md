# **ASU CANSAT 2024**

### Summary
The mission involves designing a Cansat, composed of a container and a probe, to simulate a planetary landing sequence. The Cansat will be launched to an altitude of 670 to 725 meters and deployed at apogee, facing uncontrolled orientation and substantial shock forces, which it must withstand. Following deployment, it will descend via parachute at 15 m/s. At 500 meters, it will release a probe, which employs a heat shield as an aerobraking device to slow down to 20 m/s or less, without using a parachute or similar device. At 200 meters altitude, the probe will deploy a parachute to reduce its speed to 5 m/s until landing. Post-landing, the probe will self-right and raise a flag, while a video camera pointing downward records the descent.

### Software Role
The job of the software team includes the following:
1. Establish a connection between ground control (the computer) and the radio on board the rocket
2. Ensure each on board sensor is communicating with the SD card/XBEE radio on board the rocket
3. Ensure the onboard XBEE radio is sending data packets to ground control XBEE radio at 1 Hz
4. Process data by parsing the information in the packet and writing it to a few different locations in real time
5. Take data and display as line graphs in real time
6. Create custom commands to enter into the terminal that activate certain modes and sensors
7. Mitigate processor resets by creating an option to do the following:
  - Upon computer power on, start all processes to establish connection, process data and display graphs
  - Upon computer power on, look to external hard drive to determine if data has already been recorded and if so begin from there and go forward

### Running these files on your local computer
To run the software, take a look at the Makefile. It will have the keywords to enter in your terminal. For example to run GUI.py and writeToCSV.py, type in the terminal "make CUSTOMCOMMAND". The rest are shown in the Makefile.

### Steps to adhere to 'custom commands' requirement
1. In the terminal enter "open ~/.bshrc" or "open ~./zshrc" depending on what you use
2. Make a new alias for any of the custom keywords in the Makefile as such
3. alias CMD="make -C /path/to/your/repository CUSTOMCOMMAND"
4. Now if you enter CMD in the terminal, it will automatically run the scripts within the scope of CUSTOMCOMMAND in the Makefile.

   
