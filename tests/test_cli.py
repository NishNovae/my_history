from nish_history.cli import hello_msg as msg
from nish_history.cli import cmd

def test_hello():
    m = msg()
    # assert: testing part
    assert m == "hello"

    cmd()
