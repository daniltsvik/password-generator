from pwgen.core import generate_password, DEFAULT_ALPHABET
import pytest

def test_length():
    assert len(generate_password(20)) == 20

@pytest.mark.parametrize("bad", [3, 129])
def test_invalid_length(bad):
    with pytest.raises(ValueError):
        generate_password(bad)

def test_chars_subset():
    pwd = generate_password(50)
    assert set(pwd) <= set(DEFAULT_ALPHABET)
