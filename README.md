# Behave Edx Tests.

## Description:
This repo shows usage the concept of Behavior-driven Development (BDD) with Behave, Selenium WebDriver and Python.

### Tests was implementing and running on:

* System: Linux Ubuntu 16.04 LTS
* Browsers: Firefox 54, Chrome 60.0.3112.90
* Selenium WebDriver: 3.4.3
* Behave: 1.2.5
* Python: 3.5.2

### To Run Tests - Linux Ubuntu way:

1.Clone/Download project: https://github.com/MaBlaGit/SeleniumPageObjectPatternExample

2.Install __virtialenvwrapper__
```
 $ pip install virtualenvwrapper
```
3.Run virtualenvwrapper and create hermetic virtualenv for the project

```
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv --python=/usr/bin.python3.5 name-of-virtualenv
$ workon name-of-virtualenv
```

4.Go to  __BehaveEdxTests__ folder and project to the PYTHONPATH of current active virtualenv

```
$ add2virtualenv .
```
5.Install requred modules

```
$ make deps
```

6.Download drivers, unpack , make executable and copy to /usr/local/bin: 

__geckodriver__: https://github.com/mozilla/geckodriver/releases


__chromedriver__: https://sites.google.com/a/chromium.org/chromedriver/

(example below shows how add to path __geckodriver__)

```
tar -xvzf geckodriver-v0.11.1-linux64.tar.gz
rm geckodriver-v0.11.1-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/
```

### Running tests

In order to run tests in the __BehaveEdxTests__ folder run command
```
$ behave
```
In order to run selected scenarios, use __--tags__ attribute:
```
$ behave --tags=test_1
```

