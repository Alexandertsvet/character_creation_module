from module1 import special_calculation

print("Основной модуль")
# Производим расчёты. 
coef = special_calculation(2, 5)
print(coef)  # asd 





def attack(char_name: str, char_class: str) -> str:
    """Attack calculeited."""
    ...


def defence(char_name: str, char_class: str) -> str:
    """Defend calculeited."""
    ...


def special(char_name: str, char_class: str) -> str:
    """Use special"""
    ...


def start_training(char_name: str, char_class: str) -> str:
    """Start training"""
    ...


def choice_char_class() -> str:
    """Choose class"""
    ...


def main() -> None:
    """Hellow"""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
