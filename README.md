To start the program, first make sure you have the keyboard library installed. To do this, run the command "pip install keyboard" in the VScode terminal.
If you want to check if keyboard is already downloaded, use the command "keyboard version."

I used the keyboard library to read everything entered on the keyboard, since this library is used to simulate and control the keyboard. Whether it's recording a combination or just displaying the letters, I first created a function that will run every time a key is pressed. Its purpose is to capture the name of the letter pressed. Here, the event parameter is used, which contains information about the key pressed event. In this case, we're interested in the name attribute of the event, which contains the name of the key.

Finally, we use keyboard.on_press, which is a function from the keyboard library that takes a callback function as an argument. In this case, on_press is the callback function.
Every time a key is pressed, on_press is 
And from there I just added a key to end the program with the esc key
