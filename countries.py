'''
Scatter of Global Surface Temperature of Different Countries
@author: Suyash Shivaji Phatak
Date: 22/05/2020
'''

# Importing Librarires
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()

# Reading Data From CSV
df = pd.read_csv('datasets/State.csv')

# Renaming the Columns
df.rename(columns={
    'dt':'date',
    'AverageTemperature':'Temperature',
    'AverageTemperatureUncertainty': 'Uncertainty'
    }, inplace=True)

# Checking Names of Columns
print('____________________________________________________________')
print('\nCorrected Column Name:\n')
print(df.columns)


# Displaying Small Data
print('____________________________________________________________')
print('Displaying 1st 10 Data:\n')
print(df.head(10))

# Displaying Rows and Columns
print('____________________________________________________________')
print('\n Displaying Rows and Columns:')
print('\n(Rows, Coulmns) : ',df.shape)

# Displaying Information of Data
print('____________________________________________________________')
print('\nInformation of DataSet :\n')
print(df.info())

# Displaying Sum of Null Values
print('____________________________________________________________')
print('\nChecking for Null Values:\n')
print(df.isna().sum())

''' Method for Replacing Null Values'''
# Getting 2 Rows Which Have Null Values
Temp = df['Temperature']
Temp_ut = df['Uncertainty']

# Taking Mean
Temp_mean = Temp.mean()
Tempct_mean = Temp_ut.mean()

# Replacing Null Values with Mean
Temp.fillna(Temp_mean, inplace=True)
Temp_ut.fillna(Tempct_mean, inplace=True)
'''Method End'''

# Displaying Sum of Null Values After Calling Method
print('____________________________________________________________')
print('\nChecking for Null Values After Applying Method of Replacing Null Values with Mean Value:\n')
print(df.isna().sum())

# Displaying all the counts
print('____________________________________________________________')
print('\nDescribing the Dataset:\n')
print(df.describe(include='all'))   

# Differenciating Columns by Countries

# Just Uncomment in right place to see individual countries or all
# I Prefer individual because it has larger number of data such that difficult to computer to handle fast

'''1.Brazil Start
is_brazil = df['Country']=='Brazil'
Brazil = df[is_brazil]
print('__________________________________________________________________')
print('\n(Rows, Columns) of Brazil:')
print(Brazil.shape)

# Plotting Graph for Brazil 
brazil_dates = Brazil['date']
brazil_temp = Brazil['Temperature']

# Seperating Figures
plt.figure(1)

# Plotting first points 
plt.plot(brazil_dates, brazil_temp, 'o', color = 'r',label = 'Scatter')

# Naming the x axis
plt.xlabel('Dates (Currently Not Showable)')

# Naming the y axis 
plt.ylabel('Brazil\'s Surface Temperature')

# Giving a title to graph 
plt.title('Brazil Surface Air Temperature Scatter')

# Showing the plot
plt.show()
Brazil End'''






'''2.Russia Start
is_russia = df['Country']=='Russia'
Russia = df[is_russia]
print('__________________________________________________________________')
print('\n(Rows, Columns) of Russia:')
print(Russia.shape)

# Plotting Graph for Russia 
russia_dates = Russia['date']
russia_temp = Russia['Temperature']

# Seperating Figures
plt.figure(2)

# Plotting first points 
plt.plot(russia_dates, russia_temp, '*' , color='b',label = 'Curve')

# Naming the x axis
plt.xlabel('Dates (Currently Not Showable)')

# Naming the y axis 
plt.ylabel('Surface Temperature')

# Giving a title to graph 
plt.title('Russia Surface Air Temperature Scatter')

# Showing the plot
plt.show()
 Russia End'''








'''3.China Start
is_china = df['Country']=='China'
China = df[is_china]
print('__________________________________________________________________')
print('\n(Rows, Columns) of China:')
print(China.shape)

# Plotting Graph for China 
china_dates = China['date']
china_temp = China['Temperature']

# Seperating Figures
plt.figure(3)

# Plotting first points 
plt.plot(china_dates, china_temp, '+' , color='g',label = 'Scatter')

# Naming the x axis
plt.xlabel('Dates (Currently Not Showable)')

# Naming the y axis 
plt.ylabel('Surface Temperature')

# Giving a title to graph 
plt.title('China Surface Air Temperature Scatter')

# Showing the plot
plt.show()
China End'''






'''4.India Start
is_india = df['Country']=='India'
India = df[is_india]
print('__________________________________________________________________')
print('\n(Rows, Columns) of India:')
print(India.shape)

# Plotting Graph for India 
india_dates = India['date']
india_temp = India['Temperature']

# Seperating Figures
plt.figure(4)

# Plotting first points 
plt.plot(india_dates, india_temp, '+' , color='c',label = 'Scatter')

# Naming the x axis
plt.xlabel('Dates (Currently Not Showable)')

# Naming the y axis 
plt.ylabel('Surface Temperature')

# Giving a title to graph 
plt.title('India Surface Air Temperature Scatter')

# Showing the plot
plt.show()
India End'''






'''5.Australia Start
is_australia = df['Country']=='Australia'
Australia = df[is_australia]
print('__________________________________________________________________')
print('\n(Rows, Columns) of Australia:')
print(Australia.shape)

# Plotting Graph for Australia 
australia_dates = Australia['date']
australia_temp = Australia['Temperature']

# Seperating Figures
plt.figure(5)

# Plotting first points 
plt.plot(australia_dates, australia_temp, '.' , color='m',label = 'Scatter')

# Naming the x axis
plt.xlabel('Dates (Currently Not Showable)')

# Naming the y axis 
plt.ylabel('Surface Temperature')

# Giving a title to graph 
plt.title('Australia Surface Air Temperature Scatter')

# Showing the plot
plt.show()
Australia End'''





'''6.United States Start
is_US = df['Country']=='United States'
US = df[is_US]
print('__________________________________________________________________')
print('\n(Rows, Columns) of United States:')
print(US.shape)

# Plotting Graph for US 
US_dates = US['date']
US_temp = US['Temperature']

# Seperating Figures
plt.figure(6)

# Plotting first points 
plt.plot(US_dates, US_temp, '.' ,color='y',label = 'Scatter')

# Naming the x axis
plt.xlabel('Dates (Currently Not Showable)')

# Naming the y axis 
plt.ylabel('Surface Temperature')

# Giving a title to graph 
plt.title('United States Surface Air Temperature Scatter')

# Showing the plot
plt.show()
United States End'''




'''7.Canada Start
is_canada = df['Country']=='Canada'
Canada = df[is_canada]
print('__________________________________________________________________')
print('\n(Rows, Columns) of Canada:')
print(Canada.shape)

# Plotting Graph for Canada 
canada_dates = Canada['date']
canada_temp = Canada['Temperature']

# Seperating Figures
plt.figure(7)

# Plotting first points 
plt.plot(canada_dates, canada_temp, '.' , color='k',label = 'Scatter')

# Naming the x axis
plt.xlabel('Dates (Currently Not Showable)')

# Naming the y axis 
plt.ylabel('Surface Temperature')

# Giving a title to graph 
plt.title('Canada Surface Air Temperature Scatter')

# Showing the plot
plt.show()
Canada End'''
