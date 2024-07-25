# nish_history
Using CLI commands to search through .parquet form CLI history log

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
$ pdm install
$ [pdm test|pytest]
$ pdm add -dG test pytest pytest-cov

# option
$ pdm add -dG test pytest pytest-cov
```

### Reference
- https://daobook.github.io/pdm/usage/dependency/
