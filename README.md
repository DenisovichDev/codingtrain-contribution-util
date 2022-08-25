# Coding Train Contribution Porting Utility

This project was created to make the process of porting the contributions from the old
Coding Train Website to the new one a bit easier for the contributors. This python script
takes the old contribution metadata in markdown format as an input and creates individual
json files containing the metadata of each individual contributions (following the new
Gatsby format) that can now be copied into the `showcase` folder.

**Warning**: I am not a python programmer, there must be ways to do this better. In that case please let me know.

## How To Use

First clone this repo locally in your computer.

Open the old video metadata file from the website archive (located [here](https://github.com/CodingTrain/website-archive/blob/main/_CodingChallenges/)), and copy only the contributions part to a `txt` file inside the directory of this script. For example:
```txt
  - title: "Asteroid Field"
    author:
      name: "Bossy Smaxx"
      url: https://asteroidfield.glitch.me
    url: https://glitch.com/~asteroidfield
  - title: "Swifty Starfield"
    author:
      name: "Bob Voorneveld"
      url: "https://www.bobvoorneveld.nl"
    url: "https://github.com/bobvoorneveld/Coding-Challenges/tree/master/CC001-Starfield"
  - title: "Hyperdrive Engaged"
    author:
      name: "JurriaanD"
      url: "http://projects.jurriaan.be/starfield/"
    url: "https://github.com/JurriaanD/Starfield"
  - title: "ES6 Starfield"
    author: "Bjorn Van Acker"
    url: https://bjorvack.github.io/code-challenges/challenges/cc-001-starfield/
    source: https://github.com/bjorvack/code-challenges/tree/master/challenges/cc-001-starfield
```
Remember to be careful about not skipping any spaces in the beginning. This file should be the exact copy of the contributions metadata. 

Now run the command:
```bash
python3 main.py your_input_file.txt
```

You can also choose not to mention the input filename in the command line argument. In that case, simply name the text file `contrib.txt` and it will use it as the input by default. The command would be, simply:  

```bash
python3 main.py
```

Now you should see the json files appear in the `output` folder. Check them to be sure that the script worked correctly. Now you can copy the contents of the `output` folder to your `showcase` directory. Please note that the `.gitkeep` file is not to be copied into the `showcase` directory.  

To reuse this script again, make sure to clean the directory:
```bash
sudo rm -f output/*.json *.txt
```

If you are not using bash or another UNIX command line, you can also just manually delete the JSON and the input files, and you are good to go.

## Comments

- Make sure to always check the outout files before using them.
- The script converts the `video_id` property to a valid `url` property.
- The `source` property isn't used as discussed [here](https://github.com/CodingTrain/thecodingtrain.com/issues/244).
- There is absolutely no exception handling, I'm sorry!
- I would like to implement a way fetch the metadata directly from the website archive, but I feel like that would be a bit of an overkill
- This whole project was written entirely in a train, which is very appropriate, I feel.