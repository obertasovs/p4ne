from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet =  wb['Data']
def getvalue(x): return x.value
l1=list(map(getvalue, sheet['A'][1:]))
l2=list(map(getvalue, sheet['B'][1:]))
l3=list(map(getvalue, sheet['C'][1:]))
l4=list(map(getvalue, sheet['D'][1:]))

#print(l1)
#print(l2)
#print(l3)

pyplot.plot(l1, l2, label="t_средняя")
pyplot.plot(l1, l3, label="t_дневная")
pyplot.plot(l1, l4, label="акт_солнца")
pyplot.show()

#print(list_x)
#rint(list_y)
#print(list_z)




