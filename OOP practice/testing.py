import Date 
import Person

pablo = Date.Date(22,7,1997)
# laura = Date.Date(2,8,2001)
#f = Date.Date(2,13,1920)
#g = Date.Date(92,10,1950)
#i = Date.Date(12,4,92)
# print(Date.Date.getDMY(pablo,6514))
# print(pablo + 15)
# print(pablo - 20)
# print(pablo)
# print(laura.difference_between_dates(pablo))

Pableto = Person.Person("Pablo",pablo , 654431416, "M")
print(Pableto.get_age())