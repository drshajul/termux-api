# termux-api

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://github.com/shajul/termux.git)

> termux-api is here, made with :heart:

## What is termux-api?
> termux-api is a python module to access the [termux-api](https://wiki.termux.com/wiki/Termux:API)
> To ease the access of these beautiful api's which 
> can be really useful for IOT projects deploying using your own android phone.
> This module is heavily inspired by https://github.com/azwyane/pimux

## Why to use termux-api?
> For every pythonist and enthusiast termux-api can really ease hardware and software
> access through termux-api.

## Special thanks
  This module is heavily inspired by https://github.com/azwyane/pimux 

> This project is originally located at [termux-api](https://github.com/shajul/termux-api)

## Table of Contents
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Features](#Features)
- [Contributing](#Contributing)

## Requirements

- Termux app
- Termux-api (both app and package)
- Python

## Installation

🚀&nbsp; To install in your local machine follow the steps below:

### Method-1

You can always get the latest version of termux-api maintained here in the github.
> To get the latest feature:
- Clone this repo to your local machine(termux) using `https://github.com/shajul/termux-api.git`

Goto to your terminal and type:

```sh
git clone https://github.com/shajul/termux-api.git
pip install wheel
```

Now add this to site packages by first building by being where the setup.py is:
```
$ python3 setup.py sdist bdist_wheel

$ python3 -m pip install -e <path to termux-api main dir>
```

Finally, you have it installed.

### Method-2

**Install by pip**
> The stable version is available in the Pypi, which you can download by:

```
$ python3 -m pip install termux-api
```

## Run the project

> Now to run the termux-api type in your terminal:

```bash
$ python
>>> import termux
>>> termux.API.vibrate()

>>> help(termux.API) #for available methods
```
Avaliable modules are
API, Camera, Clipboard, Notification, Sensors, TTS, Wifi

OR

```bash
$ python
>>> from termux import <Module>
>>> API.vibrate()

>>> help(API) # for details of available methods

```

## Features

> It is a side project of making use of android sensors and IOT projects. 
> It has the feature of termux-api which can be easily used with
> python projects.

---

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

