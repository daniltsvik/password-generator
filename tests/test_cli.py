import subprocess
import sys
import textwrap


def run_cli(*args: str) -> str:
    res = subprocess.run(
        [sys.executable, "-m", "passgen.cli", *args],
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:                         
        raise RuntimeError(textwrap.dedent(f"""
            CLI завершился с кодом {res.returncode}
            stderr:
            {res.stderr}
        """))
    return res.stdout.strip()                        

# тест 1 проверяем значение по умолчанию                                    
# по умолчанию программа должена сгенерировать один пароль длиной 12 символов       
def test_cli_default_length():
    out = run_cli()                                 
    assert len(out) == 12                           

# тест 2 работа флагов исключения спецсимволов                                  
# ожидаем что длина 12 и строка содержит только буквы и цифры           
def test_cli_custom_flags():
    out = run_cli("-l", "12", "--no-symbols")
    assert len(out) == 12 and out.isalnum()
