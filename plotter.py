# Your code to create majestic plots goes in here!
import numpy
import pandas as pd
import matplotlib.pylab as plt

iris= pd.read_csv('iris.data', header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_lenght', 'petal_width', 'species']

#boxplot
iris.columns = ['sepal_length', 'sepal_width', 'petal_lenght', 'petal_width', 'species']
columns= ['sepal_length', 'sepal_width', 'petal_lenght', 'petal_width']
plt.boxplot(iris[columns],
            labels= columns)
plt.ylabel('cm')
plt.title('Iris deminsions')
plt.savefig('box_plots.png')        


#scatterplot
species_name= iris['species'].unique()
  
for species_name in set(iris['species']):
    plt.scatter(iris['petal_lenght'],
                iris['petal_width'],
                label = species_name,
                s= 8)
plt.legend()
plt.ylabel('petal_length')
plt.xlabel('petal_width')
plt.title('petal size')
plt.savefig('scatter_plot.png')

#subplots
fig, axes= plt.subplots(1,2)
fig.set_size_inches(10,10)
#right subplot
axes[1].boxplot(iris[columns],
            labels= columns)
axes[1].set_ylabel('cm')
axes[1].set_title('Iris deminsions')

#left plot
for species_name in set(iris['species']):
    axes[0].scatter(iris['petal_lenght'],
                iris['petal_width'],
                label = species_name,
                s= 8)
axes[0].legend()
axes[0].set_ylabel('petal_length')
axes[0].set_xlabel('petal_width')
axes[0].set_title('petal size')
plt.savefig('subplots.png')
plt.show()
