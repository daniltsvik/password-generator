import argparse
import shlex
import sys
import pyperclip          

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
    g.add_argument("--exclude-similar", action="store_true", help="исключить похожие символы 0 O I l 1")

    p.add_argument("--copy", action="store_true",
                   help="скопировать пароль в буфер обмена")
    return p

def print_custom_help(parser: argparse.ArgumentParser) -> None:
    lines = parser.format_help().splitlines()
    try:
        first_blank = lines.index("")         
    except ValueError:
        first_blank = 0
    print("\n".join(lines[first_blank + 1:]))

def print_and_copy(pwd: str, do_copy: bool) -> None:
    print(pwd)
    if do_copy and pyperclip:
        try:
            pyperclip.copy(pwd)
            print("Пароль скопирован в буфер обмена.")
        except pyperclip.PyperclipException:
            print("Буфер обмена недоступен", file=sys.stderr)

def generate_once(args) -> str:
    return generate_password(
        length=args.length,
        use_lower=not args.no_lower,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols,
        exclude_similar=args.exclude_similar,
    )

def merge_inline_flags(line: str, args, parser) -> bool:
    """
    Пытается распарсить `line` как аргументы CLI и обновить `args`.
    Возвращает True, если параметры изменены, False если строка пуста.
    """
    if not line:
        return False                     
    try:
        new_args = parser.parse_args(shlex.split(line))
        vars(args).update(vars(new_args)) 
    except SystemExit:                
        print("Неверные флаги, введите -h для справки")
    return True

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not sys.stdin.isatty():
        print_and_copy(generate_once(args), args.copy)
        return
    
    print_custom_help(parser)
    print("\nEnter — сгенерировать пароль / q — выход")

    try:
        while True:
            line = input("> ").strip()
            low  = line.lower()

            if low in {"q", "quit", "exit"}:
                break
            if low in {"-h", "--help"}:
                print_custom_help(parser)
                continue

            changed = merge_inline_flags(line, args, parser)
            if not line or changed:
                print_and_copy(generate_once(args), args.copy)

    except KeyboardInterrupt:
        pass
    print("\nЗавершение")


if __name__ == "__main__":
    main()