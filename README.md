# ConsoleMusic
A custom python script to generate sweet sweet music based on lines of text

You will need to install pyAudio. You should be able to use `pip install pyaudio`, but if that doesn't work download the right wheel for your version from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually.

In it's current form the script just reads off of an existing file (output.txt by default, but you can point it any any file by passing it in in the console). 

That being said the `console-music.py` file is the less interesting one. `SoundLib.py` is way more fun, and contains support for playing notes, getting the notes in scales, and could be extended to do so much more if only somebody would put in the effort.
