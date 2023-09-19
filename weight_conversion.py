weight = int(input('Weight: '))
unit = input('lb or kg: ')
if unit == 'lb':
    conversion = weight * 0.45
    print(f'{conversion} in kilograms')
else:
    conversion = weight / 0.45
    print(f'{conversion} in pounds')
