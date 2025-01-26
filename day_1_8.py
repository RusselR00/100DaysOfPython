#An online retailer sells two products: widgets and gizmos. Each widget weighs 75
#grams. Each gizmo weighs 112 grams. Write a program that reads the number of
#widgets and the number of gizmos in an order from the user. Then your program
#should compute and display the total weight of the order.

noWidget = float(input("Enter the number of widgets"))
noGizmo = float(input("Enter the number of gizmos"))

totWeight = (75*noWidget + 112*noGizmo)/1000

print("Total Weight of the Order is %.2f Kg" % totWeight)