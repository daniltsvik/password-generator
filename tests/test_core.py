from pwgen.core import generate_password

def test_length():
    assert len(generate_password(20)) == 20
