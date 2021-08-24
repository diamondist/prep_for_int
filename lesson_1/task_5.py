"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию
должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Необходимо в главной функции реализовать вложенную функцию подсчета процентов
для пополняемой суммы. Примем, что клиент вносит средства в последний день
каждого месяца, кроме первого и последнего. Например, при сроке вклада в 6
месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает
сумму дополнительно внесеннх средств (с процентами), а главная функция — общую
сумму по вкладу на конец периода.
"""

from task_4 import PRODUCTS


def deposit_calculator(summ, period, addition):
    def addition_calc(add, add_summ, add_period):
        return add_summ + add * (add_period - 2)

    if period not in (6, 12, 24):
        print('Wrong period!')
        return
    if summ < 1000 or summ > 1000000:
        print('Wrong amount!')
        return
    for product in PRODUCTS:
        if product['begin_sum'] <= summ <= product['end_sum']:
            period_proc = product[period] * period / 12
            summ = addition_calc(addition, summ, period)
            return summ + summ * period_proc / 100


if __name__ == '__main__':
    print(deposit_calculator(1000, 12, 2))
