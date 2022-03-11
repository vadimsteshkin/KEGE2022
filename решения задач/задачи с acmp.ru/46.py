from decimal import *
number = Decimal("2.7182818284590452353602875")
print(number.quantize(Decimal('1.000')))