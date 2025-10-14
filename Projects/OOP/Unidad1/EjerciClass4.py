class SalesPerson:  
   
   total_revenue = 0
   nombre = []
   def __init__(self,name,age):
       self.name = name
       self.age = age
       self.sales_amount = 0

       SalesPerson.nombre.append(name)
 
   def make_sale(self,money):
       self.sales_amount += money

       SalesPerson.total_revenue += money
 
   def show(self):
       print("NOMBRE", self.name,"EDAD", self.age, "Hacer venta", self.sales_amount)

       
      
 
s1 = SalesPerson('Alumno 1', 25)
s2 = SalesPerson('Alumno 2', 22)
s3 = SalesPerson('Alumno 3', 27)
s4 = SalesPerson('Alumno 4', 45)
s5 = SalesPerson('Alumno 5', 18)
s6 = SalesPerson('Alumno 6', 10)
s7 = SalesPerson('Alumno 7', 32)
s8 = SalesPerson('Alumno 8', 28)
s9 = SalesPerson('Alumno 9', 25)
s10 = SalesPerson('Alumno 10', 55)
s11 = SalesPerson('Alumno 11',68 )
s12 = SalesPerson('Alumno 12', 45)
 
s1.make_sale(1000)
s1.make_sale(1200)
s2.make_sale(5000)
s3.make_sale(3000)
s3.make_sale(8000)
s4.make_sale(1000)
s4.make_sale(1200)
s5.make_sale(5000)
s6.make_sale(3000)
s7.make_sale(8000)
s8.make_sale(18000)
s9.make_sale(1100)
s10.make_sale(7000)
s11.make_sale(2000)
s12.make_sale(8000)
 
s1.show()
s2.show()
s3.show()
s4.show()
s5.show()
s6.show()
s7.show()
s8.show()
s9.show()
s10.show()
s11.show()
s12.show()

print(f"Total de venta {SalesPerson.total_revenue}")
print(f"Nombre de los alumnos {SalesPerson.nombre}")
