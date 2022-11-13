import ClassSample as clazz
import platform
import Configuraaaation as conf
s = clazz.Student("sampath", 12)
s.print_name()



x = platform.system()
print(x)
y = dir(platform)
print(y)

a = conf.person
print(a.get("name"))