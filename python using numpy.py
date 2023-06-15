#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

#creating an array object
a=np.array([[1,2,3],[4,5,6]])

#printing 2D array
print(a)

#printing type of array
print("Array is of type: ",type(a))

#printing number of dimensions in array
print("No. of dimesions in array: ",a.ndim)

#printing shape of array 
print("Shape of array: ",a.shape)

#printing size of array
print("Size of array: ",a.size)


# In[2]:


import numpy as np
l = np.random.randint(10,100,10)
print(l)

#sum
sum=np.sum(l)
print("Sum of array:",sum)

#max min
Min,Max=np.min(l), np.max(l)
print(f"minimum of array is :{Min} and maximum of array is:{Max}")
        


# In[20]:


import numpy as np
m = np.random.randint(10,100,(3, 4))
print(m)

#aggregate funcions

print(f'''
1. sum of array:{np.sum(m)}
2. mimimum of array:{np.min(m)}
3. maximum of array:{np.max(m)}
4. sum of rows in array:{m.sum(axis=1)}
5. minimum of rows in array:{m.min(axis=1)}
6. maximum of rows in array:{m.max(axis=1)}
7. sum of coloumns in array:{m.sum(axis=0)}
8. minimum of coloumns in array:{m.min(axis=0)}
9. maximum of coloumns in array:{m.max(axis=0)}
10.product of array:{np.prod(m)}
11.mean of array:{np.mean(m)}
12.standard deviation of array:{np.std(m)}
13.variance of array:{np.var(m)}''')


# In[ ]:


import numpy as np
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s,Array type is complex:\n", d)
e = np.random.random((2, 2))
print ("\nA random array:\n", e)
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between 0 and5:\n", g)
                [5, 2, 4, 2],
                [1, 2, 0, 1]]) 
newarr = arr.reshape(2, 2, 3) 
print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()
print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)


# In[34]:


import numpy as np
x = np.array([5, 3, 1, 2, 4])

#np.sort
print("sorted list: ",np.sort(x),"\n")

#Argsort
print("sorted list shows the index:", np.argsort(x),"\n")

print("------2D ARRAY------")
m = np.random.randint(0,10,(4,6))
print(m)

#sort by coloumns
print("sorted array by coloumns:\n",np.sort(m, axis=0),"\n")

#sort by rows
print("sorted array by rows:\n",np.sort(m, axis=1),"\n")

#reverse order of sorting
print("reverse sorted array:\n",np.sort(-m),"\n")

#reverse order of sorting by index
print("reverse sorted array by index:\n",np.sort(-m,axis=0),"\n")


# In[1]:


import numpy as np

#sorting in charectors
arr = np.array(['Apple', 'Orange', 'Banana'])
print(np.sort(arr))

#sorting in boolean
arr1 = np.array([True, False, True])
print(np.sort(arr1))

#sorting in 2d elements
arr2 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr2))

#lexsort
a = np.array(['a','b','c','d','e'])
b = np.array([12,90,380,12,21])
ind = np.lexsort((a,b))
print(ind)


# In[ ]:


import numpy as np
arr = np.array([1, 2, 3, 4])

print(f'''
The array is : {arr}
To get First element of the array: \n{arr[0]}
To get second element of the array: \n{arr[1]}
To get third and fourth element from array and to add them: \n{arr[2] + arr[3]}
''')

arr2= np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(f'''
The array is: \n{arr2}
2nd element on 1st row: \n{arr2[0, 1]}
5th element on 2nd row: \n{arr2[1, 4]}
''')

arr3=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f'''
The array is: \n{arr3}
Access the third element of the second array of the first array: \n{arr3[0, 1, 2]}
Where elements are greater than 5: \n{np.where(arr3>5)}''')

obj = np.array([12,90,380,12,211])
print(obj)
print(obj.nonzero())

