# nish_history
Using CLI commands to search through .parquet form CLI history log

## Usage
```bash
$ nish-history -s ls
keyword ls was used 481 times.
```

```bash
$ nh -t 3 -d 2024-07-17
cmd     cnt
pyenv   2456
cd      3472
git     3396 
```

## Deploy
```bash
$ pip install git+https://github.com/NishNovae/my_history.git@0.1.0/simple

$ pip install git+https://github.com/NishNovae/my_history.git@main
```

## DevEnv setting
```bash
$ git clone <URL>
$ cd <PROJECT_NAME>
$ pyenv global clean
$ rm -rf .venv
$ pdm venv create
$ source .venv/bin/activate

$ pdm install
$ [pdm test | pytest]
$ pdm add -dG test pytest pytest-cov

# option
$ pdm init
$ pdm venv create
$ pdm add -dG test pytest pytest-cov
```

## Reference
- https://daobook.github.io/pdm/usage/dependency/
