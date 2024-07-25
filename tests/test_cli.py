from nish_history.cli import hello_msg as msg

def test_hello():
    m = msg()
    # assert: testing part
    assert m == "hello"
