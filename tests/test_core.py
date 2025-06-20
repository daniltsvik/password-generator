from passgen.core import generate_password
import pytest

# тест 1 фильтр только цифры                                            
# при отключении букв и символов пароль обязан состоять из одних цифр
def test_filter_digits():
    pwd = generate_password(
        30,
        use_lower=False,
        use_upper=False,
        use_digits=True,
        use_symbols=False,
    )
    assert pwd.isdigit()


# тест 2 ошибка при пустом алфавите                                        
# если отключить все группы символов, генератор должен вывести ValueError
def test_empty_alphabet():
    with pytest.raises(ValueError):
        generate_password(
            10,
            use_lower=False,
            use_upper=False,
            use_digits=False,
            use_symbols=False,
        )
