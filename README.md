# ESC204 Team 0112C Zombie Fire MQTT Publisher

Team 0112C: Atharv KudChadKar, Charlie Martinez, Derek Chen, Han Fang, Oscar Low, Rooney Cheung

This repository contains the MQTT publisher onboard the Raspberry Pi Pico W that gathers underground environment data through BME680 and SEN0114 sensors.

## Prerequisites

You have a Pico W and you have downloaded and copied the `.uf2` file to the device.

## Setup

Install all the dependencies listed in the `project.dependencies` section in `pyproject.toml` by copying the relevant files/directories into the Pico W.

Clone the repository by running:

```sh
git clone https://github.com/derkychen/esc204-zombie-fire-mqtt-publisher.git
```

Copy the packages and modules in the `tools.setuptools` section in `pyproject.toml` from where the repository was cloned to the Pico W's root directory, replacing the default, empty `code.py`.

## Run subscriber

Write `code.py` or press Ctrl-D in the serial console.
