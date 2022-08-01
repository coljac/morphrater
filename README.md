# Lensrater

Application for quickly classifying images.

## Installation

First, `pip3 install pyqt5` - the dependency can't at this stage be installed via setuptools. Then:

`python setup.py install`

## Usage

`morphrater <directory containing images>`

The application will create a scores.csv in the directory upon exit.

## Usage

|  |  |
|---------------|--------|
| Next image | right, j |
| Prev image | left, k |
| Forward/back 10 images | pgup/pgdn |
| First/last image | Home/End |
| Save and quit | Esc |
| Classify Irregular | 0, ~ |
| Classify Elliptical | 1 |
| Classify Disk | 2 |
| Classify Disk+Bulge | 3 |
| Classify Discard | 4 |
| Increase score | Space |



