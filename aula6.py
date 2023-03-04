# conversão ou coerção de tipos
#type convertion, typecasting, coercion

#str to int
print("{} is the type {}".format(int('1'), type(int('1'))))

#str to float
print("{} is the type {}".format(float('1'), type(float('1'))))

#str to bool
print("{} is the type {}".format(bool(' '), type(bool(' ')))) # filled str == True
print("{} is the type {}".format(bool(''), type(bool('')))) # empty str == False

#int to str
print("{} is the type {}".format(str(1), type(str(1))))
