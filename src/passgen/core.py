from secrets import choice

LOWER   = "abcdefghijklmnopqrstuvwxyz"
UPPER   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS  = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"
SIMILAR = set("0OIl1")

DEFAULT_ALPHABET = LOWER + UPPER + DIGITS + SYMBOLS

def build_alphabet(
    *,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    exclude_similar: bool = False,
) -> str:
    parts: list[str] = []
    if use_lower:
        parts.append(LOWER)
    if use_upper:
        parts.append(UPPER)
    if use_digits:
        parts.append(DIGITS)
    if use_symbols:
        parts.append(SYMBOLS)


    alphabet = "".join(parts)
    if exclude_similar:
        alphabet = "".join(ch for ch in alphabet if ch not in SIMILAR)
    if not alphabet:
        raise ValueError("Ошибка: все группы символов отключены")
    return alphabet

def generate_password(
        length: int = 12,
        *,
        alphabet: str | None = None,
        use_lower: bool = True,
        use_upper: bool = True,
        use_digits: bool = True,
        use_symbols: bool = True,
        exclude_similar: bool = False,
) -> str:
    if not 4 <= length <= 128:
        raise ValueError("Длина должна быть в диапазоне 4..128")

    if alphabet is None:
        alphabet = build_alphabet(
            use_lower=use_lower,
            use_upper=use_upper,
            use_digits=use_digits,
            use_symbols=use_symbols,
            exclude_similar=exclude_similar,
        )
    return "".join(choice(alphabet) for _ in range(length))