# termux-api

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://github.com/shajul/termux-api)

termux-api is here, made with :heart:

## What is termux-api?
termux-api is a python module to access the [termux-api](https://wiki.termux.com/wiki/Termux:API)
This provides a way to get native access in Python to Android device functionality as API.

Most of the [termux-api implementations](https://wiki.termux.com/wiki/Termux:API) are directly available.
The API.generic() method gives direct access to any other method that has not yet been implemented.

## Special thanks
Thanks to termux and termux-api for making all this possible.
This module is heavily inspired by https://github.com/azwyane/pimux, though the code has been 
almost completely re-written and now is much more comprehensive.  
This project is originally located at [termux-api](https://github.com/shajul/termux-api)

## Table of Contents
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Features](#Features)
- [Contributing](#Contributing)

## Requirements

- Termux app
- Termux-api (both app and package)
- Python installed in termux ($ pkg install python)

## Installation

🚀&nbsp; Android install through termux:

### Method-1

**Install by pip**
The stable version is available in the Pypi, which you can download by:

```
$ python3 -m pip install termux-api
```

### Method-2

You can always get the latest version of termux-api maintained here in the github.
- Clone this repo to your local machine(termux) using `https://github.com/shajul/termux-api.git`

Goto to your terminal and type:

```sh
$ git clone https://github.com/shajul/termux-api.git
$ python3 -m pip install wheel
$ python3 -m pip install dist/termux_api*.whl
```

Or you can add this to site packages by first building it first:
```
$ python3 setup.py sdist bdist_wheel
$ python3 -m pip install -e <path to termux_api*.whl>
```

Finally, you have it installed.

## Run the project

Now to run the termux-api type in your terminal:

```bash
$ python
>>> import termux
>>> termux.API.vibrate()

>>> help(termux.API) #for available methods
```
Avaliable modules are
API, Camera, Clipboard, Media, Microphone, Notification, Scheduler, Sensors, Share, Telephony, TTS, UI, Wifi

OR

```bash
$ python
>>> from termux import <Module>
>>> API.vibrate()

>>> help(API) # for details of available methods

```

## Contributing

### Step 1

- Option 1
    - 🍴 Fork this repo!

- Option 2
    - 👯 Clone this repo to your local machine using `https://github.com/shajul/termux-api.git`

### Step 2

- HACK AWAY!

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/shajul/termux-api/compare" target="_blank">`https://github.com/shajul/termux-api/compare`</a>.


---

###  Found a bug? Missing a specific feature?
You can file an issue.
If you already found a solution to your problem, **I would love to review your pull request**!

