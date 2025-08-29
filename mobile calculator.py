"""
 MOBILE CALCULATOR v1.0
Автор: [snowwyknk]
Описание: Универсальный калькулятор на Python Interpretator для мобильных устройств
Особенности: красивое оформление, все базовые опции
Лицензия: MIT - свободное использование
"""
print("🧮 УНИВЕРСАЛЬНЫЙ КАЛЬКУЛЯТОР")
print("=" * 45)
print()

# ЧИСЛА
a = 15
b = 30 
c = 60

print(f"🔢 РАБОЧИЕ ЧИСЛА: a = {a}, b = {b}, c = {c}")
print("💡 Чтобы изменить числа, отредактируй значения выше!")
print()

def показать_раздел(название):
    print()
    print(f"📋 {название}")
    print("=" * 40)

# 1. БАЗОВЫЕ ОПЕРАЦИИ
показать_раздел("БАЗОВЫЕ ОПЕРАЦИИ")

print("➕ СЛОЖЕНИЕ:")
print(f"  {a} + {b} = {a + b}")
print(f"  {a} + {c} = {a + c}") 
print(f"  {b} + {c} = {b + c}")
print(f"  {a} + {b} + {c} = {a + b + c}")
print()

print("➖ ВЫЧИТАНИЕ:")
print(f"  {a} - {b} = {a - b}")
print(f"  {a} - {c} = {a - c}")
print(f"  {b} - {c} = {b - c}")
print(f"  {a} - {b} - {c} = {a - b - c}")
print()

print("✖️ УМНОЖЕНИЕ:")
print(f"  {a} × {b} = {a * b}")
print(f"  {a} × {c} = {a * c}")
print(f"  {b} × {c} = {b * c}")
print(f"  {a} × {b} × {c} = {a * b * c}")
print()

print("➗ ДЕЛЕНИЕ:")
print(f"  {a} ÷ {b} = {a / b:.2f}")
print(f"  {a} ÷ {c} = {a / c:.2f}")
print(f"  {b} ÷ {c} = {b / c:.2f}")

# 2. СПЕЦИАЛЬНЫЕ ОПЕРАЦИИ
показать_раздел("СПЕЦИАЛЬНЫЕ ОПЕРАЦИИ")

print("🎯 ОСТАТОК ОТ ДЕЛЕНИЯ:")
print(f"  {a} % {b} = {a % b}")
print(f"  {a} % {c} = {a % c}")
print(f"  {b} % {c} = {b % c}")
print()

print("🔢 ЦЕЛАЯ ЧАСТЬ:")
print(f"  {a} // {b} = {a // b}")
print(f"  {a} // {c} = {a // c}")
print()

print("⚡ СТЕПЕНИ:")
print(f"  {a}² = {a ** 2}")
print(f"  {b}² = {b ** 2}") 
print(f"  {c}² = {c ** 2}")
print(f"  {a}³ = {a ** 3}")
print()

print("📐 КОРНИ:")
print(f"  √{a} = {a ** 0.5:.2f}")
print(f"  √{b} = {b ** 0.5:.2f}")
print(f"  √{c} = {c ** 0.5:.2f}")

print("📐 ТРИГОНОМЕТРИЯ (в радианах):")
print(f"  sin({a}) = {__import__('math').sin(a):.3f}")
print(f"  cos({b}) = {__import__('math').cos(b):.3f}")

# 3. ДРОБИ И ПРОЦЕНТЫ
показать_раздел("ДРОБИ И ПРОЦЕНТЫ")

print("🔢 ДРОБИ:")
print(f"  {a}/{b} = {a/b:.3f}")
print(f"  {a}/{c} = {a/c:.3f}")
print(f"  {b}/{c} = {b/c:.3f}")
print()

print("🔄 ОБРАТНЫЕ ДРОБИ:")
print(f"  1/{a} = {1/a:.4f}")
print(f"  1/{b} = {1/b:.4f}")
print(f"  1/{c} = {1/c:.4f}")
print()

print("📊 ПРОЦЕНТЫ:")
print(f"  {a} от {b} = {(a/b)*100:.1f}%")
print(f"  {b} от {c} = {(b/c)*100:.1f}%")
print(f"  25% от {a} = {a*0.25}")
print(f"  50% от {b} = {b*0.5}")
print(f"  75% от {c} = {c*0.75}")

# 4. КОМБИНИРОВАННЫЕ ОПЕРАЦИИ
показать_раздел("КОМБИНИРОВАННЫЕ ОПЕРАЦИИ")

print("🔗 КОМБИНАЦИИ:")
print(f"  ({a} + {b}) × {c} = {(a+b)*c}")
print(f"  ({a} × {c}) + {b} = {(a*c)+b}")
print(f"  ({b} + {c}) ÷ {a} = {(b+c)/a:.2f}")
print(f"  {a}² + {b}² = {(a**2) + (b**2)}")
print()

print("🎯 СЛОЖНЫЕ ВЫРАЖЕНИЯ:")
print(f"  ({a} + {b}) × ({c} - {a}) = {(a+b)*(c-a)}")
print(f"  {a} × {b} ÷ {c} = {a*b/c:.2f}")
print(f"  √({a}×{b}) = {(a*b)**0.5:.2f}")

# 5. ИТОГИ И ФАКТЫ
показать_раздел("ИТОГИ И ФАКТЫ")

sum_all = a + b + c
product_all = a * b * c
average = sum_all / 3

print("📊 СВОДКА:")
print(f"  Сумма всех чисел: {sum_all}")
print(f"  Произведение всех чисел: {product_all}")
print(f"  Среднее арифметическое: {average:.2f}")
print()

print("💡 ИНТЕРЕСНЫЕ ФАКТЫ:")
print(f"  {a} - {'чётное' if a%2==0 else 'нечётное'}")
print(f"  {b} - {'чётное' if b%2==0 else 'нечётное'}")
print(f"  {c} - {'чётное' if c%2==0 else 'нечётное'}")
print(f"  {a} > {b} на {a-b}")
print(f"  {b} < {c} в {c/b:.1f} раз")
print()

print("🎯 ДЕЛИМОСТЬ:")
print(f"  {a} делится на {b}: {'✅' if a%b==0 else '❌'}")
print(f"  {a} делится на {c}: {'✅' if a%c==0 else '❌'}")
print(f"  {b} делится на {c}: {'✅' if b%c==0 else '❌'}")

print()
print("=" * 45)
print("🎉 ВСЕ ВЫЧИСЛЕНИЯ ЗАВЕРШЕНЫ!")
print(f"💡 Чтобы изменить числа, отредактируй a, b, c в начале кода")
print("🚀 Перезапусти программу для новых вычислений!")
print("👾" * 15)

print("\n🎲 СЛУЧАЙНЫЕ ПРИМЕРЫ:")
import random
for i in range(3):
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    op = random.choice(['+', '-', '*', '/'])
    print(f"  {x} {op} {y} = {eval(f'{x}{op}{y}'):.2f}")

