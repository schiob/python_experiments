
# coding: utf-8

# In[1]:

from pylab import imshow, show
import mahotas
import mahotas.demos
wally = mahotas.demos.load('Wally')
imshow(wally)
show()


# In[2]:

wfloat = wally.astype(float)
r,g,b = wfloat.transpose((2,0,1))


# In[3]:

w = wfloat.mean(2)


# In[4]:

pattern = np.ones((24,16), float)
for i in xrange(2):
    pattern[i::4] = -1


# In[5]:

v = mahotas.convolve(r-w, pattern)


# In[6]:

mask = (v == v.max())
mask = mahotas.dilate(mask, np.ones((48,24)))


# In[7]:

wally -= .8*wally * ~mask[:,:,None]


# In[8]:

imshow(wally)
show()


# In[ ]:



