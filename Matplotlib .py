#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# In[1]:


pip install matplotlib


# In[2]:


import matplotlib 
print(matplotlib.__version__)


# # Matplotlib Pyplot - 

# In[4]:


import matplotlib.pyplot as plt


# # Draw a line in a diagram from position (0,0) , to (6,250)

# In[6]:


import matplotlib.pyplot as plt
import numpy as np
xpoint = np.array([0,6])
ypoint = np.array([0,250])
plt.plot(xpoint , ypoint)
plt.show()


# # Matplotlib Ploting - Plot function is used to draw points in a diagram.It drwas a line from point to point.

# In[7]:


import matplotlib.pyplot as plt
import numpy as np
xpoint = np.array([1,8])
ypoint = np.array([3,10])
plt.plot(xpoint , ypoint)
plt.show()


# In[8]:


import matplotlib.pyplot as plt
import numpy as np
xpoint = np.array([1,8])
ypoint = np.array([3,10])
plt.plot(xpoint , ypoint , 'o')
plt.show()


# # Multiple Points 

# In[9]:


import matplotlib.pyplot as plt
import numpy as np
xpoint = np.array([1,2,6,8])
ypoint = np.array([3,8,1,10])
plt.plot(xpoint , ypoint )
plt.show()


# In[10]:


import matplotlib.pyplot as plt
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint )
plt.show()


# # Matplotlib Markers

# In[12]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , '*' )
plt.show()


# In[14]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , 'o:r' )
plt.show()


# In[15]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , 'hotpink' )
plt.show()


# # Markers Size

# In[16]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , marker = 'o' , ms = 20 )
plt.show()


# # Marker Color

# In[17]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , marker = 'o' , ms = 20 , mec = 'r' )
plt.show()


# # Marker Face color

# In[18]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , marker = 'o' , ms = 20 , mfc = 'r' )
plt.show()


# # Entire Marker

# In[19]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , marker = 'o' , ms = 20 , mfc = 'g' , mec = 'r' )
plt.show()


# # Matplotlib Line

# In[21]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , linestyle = 'dashed' )
plt.show()


# In[22]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , linestyle = ':' )
plt.show()


# In[23]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , color = 'hotpink' )
plt.show()


# # Lines Width

# In[24]:


import matplotlib.pyplot as plt 
import numpy as np
ypoint = np.array([3,8,1,10])
plt.plot( ypoint , linewidth = '20.5' )
plt.show()


# # Multiple Line

# In[31]:


import matplotlib.pyplot as plt 
import numpy as np
y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])
plt.plot(y1 , color = 'hotpink' )
plt.plot(y2 , color = 'r')
plt.show()


# # Matplotlib Labels and Title

# In[34]:


import matplotlib.pyplot as plt 
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y)
plt.xlabel('Average Pulse')
plt.ylabel('Calories')
plt.show()


# In[35]:


import matplotlib.pyplot as plt 
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y)
plt.title('Sports Data')
plt.xlabel('Average Pulse')
plt.ylabel('Calories')
plt.show()


# # Font Properties for Titles and Labels

# In[42]:


import matplotlib.pyplot as plt 
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
font1 = {'family' : 'serif' , 'color' : 'hotpink' , 'size' : 20}
font2 = {'family' : 'serif' , 'color' : 'g' , 'size' : 10}
plt.title('Sports Data' , fontdict = font1 )
plt.xlabel('Average Pulse' , fontdict = font2)
plt.ylabel('Calories' , fontdict = font2)
plt.plot(x,y)
plt.show()


# # Matplotlib Grid

# In[43]:


import matplotlib.pyplot as plt 
import numpy as np
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y)
plt.grid()
plt.xlabel('Average Pulse')
plt.ylabel('Calories')
plt.show()


# # Matplotlib Subplot

# In[47]:


import matplotlib.pyplot as plt 
import numpy as np
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)


# In[48]:


import matplotlib.pyplot as plt 
import numpy as np
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,1,1)
plt.plot(x,y)
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2,1,2)
plt.plot(x,y)


# # Matplot Scatterplot

# In[50]:


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y , color = 'r')
plt.show()


# # Matplotlib Bargraph

# In[54]:


x = np.array(["A" , "B" , "C" , "D"])
y = np.array([3,8,1,10])
plt.bar(x,y , color = 'hotpink')
plt.show()


# In[57]:


x = np.array(["A" , "B" , "C" , "D"])
y = np.array([3,8,1,10])
plt.bar(x,y , width = 0.1)
plt.show()


# In[59]:


x = np.array(["A" , "B" , "C" , "D"])
y = np.array([3,8,1,10])
plt.barh(x,y , color = 'r' , height = 0.1)
plt.show()


# # Matplotlib Histogram  - Histogram is  used for Frequency Distribution

# In[61]:


import numpy as np
x = np.random.normal(170,10,250)
print(x)


# In[64]:


import matplotlib.pyplot as plt 
import numpy as np
x = np.random.normal(170,10,250)
plt.hist(x , color = 'r')
plt.show()


# # Matplotlib Piechart

# In[68]:


y  = np.array([35,25,25,15])
plt.pie(y)
plt.show()


# In[77]:


y  = np.array([35,25,25,15])
labels = my_labels= (['Apple' , 'Banana' , 'Cherry' , 'Grapes'])
color = my_colors = ['r' , 'b' , 'k' , 'g']
plt.pie(y,labels = my_labels , colors = my_colors)
plt.show()
y,labels
plt.show()


# # Pie Chart Explode

# In[78]:


y  = np.array([35,25,25,15])
labels = my_labels= (['Apple' , 'Banana' , 'Cherry' , 'Grapes'])
explode = my_explode = [0.2,0,0,0]
color = my_colors = ['r' , 'b' , 'k' , 'g']
plt.pie(y,labels = my_labels , colors = my_colors , explode = my_explode)
plt.show()
y,labels
plt.show()


# # Pie Chart Shadow

# In[80]:


y  = np.array([35,25,25,15])
labels = my_labels= (['Apple' , 'Banana' , 'Cherry' , 'Grapes'])
explode = my_explode = [0.2,0,0,0]
color = my_colors = ['r' , 'b' , 'k' , 'g']
plt.pie(y,labels = my_labels , colors = my_colors , explode = my_explode , shadow = True)
plt.show()
y,labels
plt.show()


# # Pie Chart Legend

# In[86]:


import matplotlib.pyplot as plt
import numpy as np
y  = np.array([35,25,25,15])
labels = my_labels= (['Apple' , 'Banana' , 'Cherry' , 'Grapes'])
color = my_colors = ['r' , 'b' , 'k' , 'g']
plt.pie(y,labels = my_labels , colors = my_colors)
plt.legend()
plt.show()


# In[ ]:




