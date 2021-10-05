x0 = int(input("enter the center x coordinate"))
y0 = int(input("enter the initial y coordinate"))

r = int(input("enter the radius of the circle"))

# two lists for maintaining the coordinates of the consecutive circle
x_cor = []
y_cor = [] 

# intially appending the input point into the their respective list
x_cor.append(x0)
y_cor.append(r)
p_list = [] # a list to store the values of the decsion parameters

# step:1
x0 = 0
y0 = r

# step:2 let's calculate the decsion parameter
p = 3 - 2 * r 

# step:3 let's loop through the conditions now

for i in range(10):
    if p<0:
        x1 = x0 + 1
        y1 = y0
        p1 = p + 4 * x1 + 6
        x_cor.append(x1)
        y_cor.append(y1) 
        p_list.append(p1)
        x0 = x1
        y0 = y1
        p = p1
    else:
        x1 = x0 + 1
        y1 = y0 - 1
        p1 = p + 4*(x1-y1)+10
        x_cor.append(x1)
        y_cor.append(y1)
        p_list.append(p1)
        x0 = x1
        y0 = y1
        p = p1 
    
print(x_cor)
print(y_cor)

# now, we will use the matplotlib library to plot the points

import matplotlib.pyplot as plt 
plt.plot(x_cor, y_cor)
plt.show()