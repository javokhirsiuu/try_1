from modul3_lesson14 import Rectangle

rec1 = Rectangle(12,8)
rec3 = Rectangle(5,9)
print(rec1.get_area(),rec3.get_area())

cir1 = Circle(9)
cir2 = Circle(99)

print(cir1.get_cir_area(),cir2.get_cir_area())
figures = [rec1,rec3,cir1,cir2]
if inheritance(figure,Circle):
    print(figures.get_cir_area)
else:
    print(figures.get_area)