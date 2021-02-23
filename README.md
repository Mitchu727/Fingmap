# Fingmap
## Project within "Szkoła Orłów na PW" program at Warsaw Univeristy of Tecnology 
### Idea and inspiration
Inspiration of the project was an idea to create an electronic device at low cost that would give the user a possibility to control computer without touching anything - only by making proper gestures. That, hopefully, could make living nad dealing with electronic devices more intuitive and easier in the future.

### Approaches
During my researches and measurements I came up wih two approaches that could give promising results:
 - static - every time distance is measured, ML algorythms are used to predict the coordinates of the finger, then with the coordinates for every timestep, software should predict what gesture that was
 - dynamic - after registering that there was some movement in front of the sensors and it ended, data from that timespan is being processed to predict what gesture that was


## Current status 
At present I'm researching effectivity of three ML algorythms in predicting the coordinates of the finger (static way). For now I've got some promising results (about 90% for raw data from labeled file). In the near future I would like to implement them in such way that they would show the user the position of the finger (or brick) in real time using a picture/plot.

### Assumptions
In the beginning I've made several assumptions to my model:
 - only one finger can be in front of the sensors
 - the finger could be represented by a LEGO structure with 1.5 cm x 1.5cm base

### Hardware 
I'm using Arduino with three HC-SR04 distance sensors. In front of them there is a LEGO brick structure.


### Software 
The ouptuts of the serial port from Arduino are read by python scirpt and written to file. To determine the finger position three machine learning algorythms where implemented: SVM, Bayes and Neural Network.  

#### Polish comments
A lot of names or comments in the code are polish. If you are interested and don't speak this beautiful language, write and I'll translate this parts of codes to be fully english.