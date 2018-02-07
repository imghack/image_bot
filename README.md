# image_bot

Release notes:
0.0.1-beta version
0.0.1-alpha will be at 08.02.2018

### Build status [![Build Status](https://travis-ci.org/imghack/image_bot.svg?branch=master)](https://travis-ci.org/imghack/image_bot) [![Coverage Status](https://coveralls.io/repos/github/imghack/image_bot/badge.svg?branch=master)](https://coveralls.io/github/imghack/image_bot?branch=master)

### Install packages

``` pip3 install -r requirements.txt ```

### Run basic app

``` python3 main.py ```

and run mongod to enable db saving

``` mongod ```

### Unit tests
To install unit tests
``` 
pip install pytest 
pip install pytest-cov
```
and to run it 
``` python -m pytest ```
or 
``` python unittest discover ```

or you can add coverage flag to see code coverage =)

``` python -m pytest --cov="./" ```
