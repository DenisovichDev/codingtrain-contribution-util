# Coding Train Contribution Porting Utility

**Work in progress**

This project was created to make the process of porting the contributions from the old
Coding Train Website to the new one a bit easier for the contributors. This python script
takes the old contribution metadata in markdown format as an input and creates individual
json files containing the metadata of each individual contributions (following the new
Gatsby format) that can now be copied into the `showcase` folder.

Warning: I am not a python programmer, there must be ways to do this better. In that case please let me know.

## How To Use

Open the old video metadata file from the website archive (located [here](https://github.com/CodingTrain/website-archive/blob/main/_CodingChallenges/)), and copy only the contributions part to a txt file inside the directory of this script. For example:
```txt
  - title: "Asteroid Field"
    author:
      name: "Bossy Smaxx"
      url: "https://asteroidfield.glitch.me"
    url: "https://glitch.com/~asteroidfield"
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
    author:
      name: "Bjorn Van Acker"
      url: "https://bjorvack.github.io/code-challenges/"
    url: "https://bjorvack.github.io/code-challenges/challenges/cc-001-starfield/"
    source: "https://github.com/bjorvack/code-challenges/tree/master/challenges/cc-001-starfield"
```
Remember to be careful about not skipping any spaces in the beginning. This file should be the exact copy of the contributions metadata. Name this file `contrib.txt`.  

Now run the script:
```bash
python3 main.py
```
Now you should see the json files appear in the directory. Check them to be sure that the script worked correctly.  

To reuse this script again, make sure to clean the directory:
```bash
sudo rm -f *.json *.txt
```

## Comments

- This is a work in progress, should be finished in a day or two.
- Currently doesn't support the `video_id` format for `url` link, I'll add it in a moment.