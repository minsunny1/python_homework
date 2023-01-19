# 5.4
print('# 5.4')
letter = str('''Dear {salutation} {name},\n
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially near any
{animals}.\n
Send us your receipt and {amount} for shipping and handling. We will send you
another {product} that, in our tests, is {percent}% less likely to have {verbed}.\n
Thank you for your support.
Sincerely,
{spokesman}
{job_title}''')


# 5.5
print('# 5.5')
print(letter.format(salutation='Hi', name='minsun', product='note', verbed='used', room='house', animals='dog', amount='amount', percent=10, spokesman='homin', job_title='job'))

# 5.6
print('# 5.6')
English_submarine = "Boaty McBoatface"
Australian_racehorse = "Horsey McHorseface"
Swedish_train = "Trainy McTrainface"
str1 = "Duck"
str2 = "Gourd"
str3 = "Spitz"
print('%sy Mc%sface' % (str1, str1))
print('%sy Mc%sface' % (str2, str2))
print('%sy Mc%sface' % (str3, str3))

# 5.7
print('# 5.7')
print('{}y Mc{}sface'.format(str1, str1))
print('{}y Mc{}face'.format(str2, str2))
print('{}y Mc{}face'.format(str3, str3))

# 5.8
print('# 5.8')
print(f'{str1}y Mc{str1}sface')
print(f'{str2}y Mc{str2}face')
print(f'{str3}y Mc{str3}face''')

