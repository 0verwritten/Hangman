# Hangman: intresting game on python
```
 _   _
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/
```
## Navigation
[Prewiew](#Preview) <br />
[Getting started](#Getting-started)

## Preview

### Console

![](https://github.com/TheSimpleWriter/Hangman/blob/master/images/Screen%20Shot%202019-08-18%20at%2021.38.26.png)
![](https://github.com/TheSimpleWriter/Hangman/blob/master/images/Screen%20Shot%202019-08-18%20at%2021.38.02.png)

### Graphical

![](https://github.com/TheSimpleWriter/Hangman/blob/master/images/Screen%20Shot%202019-08-18%20at%2021.37.41.png)
![](https://github.com/TheSimpleWriter/Hangman/blob/master/images/Screen%20Shot%202019-08-18%20at%2021.36.42.png)

## Getting started

here is how to [install](#How-to-install-game) or [play without installation](#How-to-run-game-without-installation)

1. First you have to before other steps clone this reporitory with : ```git clone https://github.com/TheSimpleWriter/Hangman.git```

2. Then you have to go to graphical or console folder with: ```cd Hangman/<folder>```

### How to run game without installation

#### Console variant

3. Install required modules with pip3 (package managment for python3): ```pip3 install -r requirements.txt```
4. Run game with: ```python3 main.py```

#### Graphical interface

3. Install required modules with pip3 (package managment for python3): ```pip3 install -r requirements.txt```
4. Than you can run app with: ```fbs run```
- or you can compile app with: ```fbs freeze```

### How to install game

#### Console variant

3. Install required modules with pip3 (package managment for python3): ```pip3 install -r requirements.txt```
4. Run game with: ```python3 main.py```
5. Compile game: ```pyinstaller -F main.py```
6. Your app will be in ```dist``` folder, to rename output file run this 
> For Windows
``` rename dist/main.exe Hangman.exe ```
> For Mac OS/Linux
``` mv dist/main ```

7. If you want to run this game from terminal/cmd(for windows) try this:

> For Windows

+ right click my computer
+ click Properties
+ click Advanced System Settings
+ click Environment Variables
+ In the bottom pane find Path, select it and click Edit
+ after the last ;, add the full path to the folder containing Hangman.exe (in this case you must add C:\Program Files (x86)\Hangman\bin\, also note the \ at the end)

>For Linux
```
cp dist/main /usr/local/bin/hangman
ln -s /home/username/programs/bluegriffon/EXECUTABLE.sh /usr/local/bin/hangman

```

> For MacOS
```
cp dist/main /usr/local/bin/hangman
```

#### Graphical interface

3. Install required modules with pip3 (package managment for python3): ```pip3 install -r requirements.txt```
4. Than you can run app with: ```fbs run```
- and then you can compile app with: ```fbs freeze```
5. To install you have to run: ```fbs installer```
6. Follow fbs function instruction
