import argparse
from passgen.core import generate_password

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="passgen",
        description="Генератор надёжных случайных паролей",
    )

    p.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="длина пароля (4–128 символов)",
    )

    g = p.add_argument_group("флаги символов")
    g.add_argument("--no-lower",   action="store_true", help="исключить строчные буквы")
    g.add_argument("--no-upper",   action="store_true", help="исключить заглавные буквы")
    g.add_argument("--no-digits",  action="store_true", help="исключить цифры")
    g.add_argument("--no-symbols", action="store_true", help="исключить спецсимволы")
    g.add_argument(
        "--exclude-similar",
        action="store_true",
        help="исключить похожие символы 0 O I l 1",
    )

    return p

def main() -> None:
    args = build_parser().parse_args()
    print(
        generate_password(
            length=args.length,
            use_lower=not args.no_lower,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            exclude_similar=args.exclude_similar,
        )
    )

if __name__ == "__main__":
    main()
