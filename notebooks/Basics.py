1+2
x=2
y=3
z=x+y
print(z)
import numpy as np

x = 'Hello, World!'
print(x)

l = [1, 2, 3, 4, 5]
print(l)
type(l)

#add 6 to the list
l.append(6)
print(l)

l[3]= 'Orange'
print(l)

l.pop()
print(l)

#if else statement
if 1<2:
    print("First")
else:
    print("Last")

#looping (print all even numbers from 0 to 11)
for i in range(1,12):
    if i % 2 == 0:
        print(i)

#convert list l into numpy array
a = np.array(l)
print(a)
print(type(a))
a.ndim

#create a two dimentional array
b = np.array([[1,2,3],[4,5,6]])
print(b)
b.ndim

#Remove Orange from the list
l.remove('Orange')
print(l)

a = np.delete(a,3)
print(a)

#Sum of all elements in array a
#convert string elements to float
a = a.astype(float)
print(np.sum(a))


#taking the square root of each element in array a
print(np.sqrt(a))

#generate random data from normal distribution
x = np.random.normal(0,1,1000)
x.shape

#Add some random noise to the data
y = x + np.random.normal(0,0.1,1000)

#Scatter plot
import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter plot of X vs Y')
plt.show()

#save the plot
plt.savefig('scatter_plot.png')