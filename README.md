# nish_history
Warning: Purely working branch: do not attempt to merge into main!

### Installation
```
$ pip install nish_history
```

### Usage
```
$ nh -s ls
keyword ls was used 481 times.
```

```
$ nh -t 3 -d 2024-07-17
cmd     cnt
pyenv   2456
cd      3472
git     3396 
```

### DevEnv setting
```
$ git clone <URL>
$ cd <PROJECT_NAME>
$ [pdm test|pytest]
$ pdm add -dG test pytest pytest-cov
```
