from secrets import choice

DEFAULT_ALPHABET = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "!@#$%^&*()-_=+[]{};:,.?"
)

def generate_password(length: int = 12, alphabet: str = DEFAULT_ALPHABET) -> str:
    if length < 4 or length > 128:
        raise ValueError("length must be in range 4..128")
    return "".join(choice(alphabet) for _ in range(length))
