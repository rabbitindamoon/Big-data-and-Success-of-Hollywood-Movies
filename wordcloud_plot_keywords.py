# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:20:10 2020
Here I am gonna try to do all the data information fro the thesis.
@author: rabbitindamoon
"""
from wordcloud import WordCloud, STOPWORDS
import nltk
import matplotlib.pyplot as plt 
import pandas as pd
# lets start with word cloud for the plot words.
# movie_plot_keywords
plot_keywords_corpus_list = list()
plot_keywords_corpus = str()
for i in movie_plot_keywords:
    if i == 'None':
        pass
    else:
        plot_keywords_corpus_list.append(i)

plot_keywords_corpus = ' '.join(plot_keywords_corpus_list)
# None

###
#This is for word cloud.
title_wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', height=2000, width=4000).generate(plot_keywords_corpus)
plt.figure(figsize=(16,8))
plt.imshow(title_wordcloud)
plt.axis('off')
plt.show()



# here I will try to plot the year and the countries 
# =============================================================================
# import seaborn as sns
# sns.set()
# df.set_index('App').T.plot(kind='bar', stacked=True)
# =============================================================================

dfObj = dfObj.assign(country = movie_country)
#creating a df for year and country.
df_country_year = pd.DataFrame()
country_unique_key = country_dictionary_total.keys()
year_dictionary = {}
contador_anos = 0

for i in range(len(dfObj['year'])):
    if dfObj['year'][i] == []:
        dfObj['year'][i] = ''
        if dfObj['year'][i] not in year_dictionary.keys():
            year_dictionary[dfObj['year'][i]] = 1
        else:
            year_dictionary[dfObj['year'][i]] = year_dictionary[dfObj['year'][i]] + 1
    else:
        if dfObj['year'][i] not in year_dictionary.keys():
            year_dictionary[dfObj['year'][i]] = 1
        else:
            year_dictionary[dfObj['year'][i]] = year_dictionary[dfObj['year'][i]] + 1        
    contador_anos = contador_anos + 1 

year_unique_key = year_dictionary.keys()



# here creating data frames to show countries and numebr of movies per year.
countries_list_toshow= ['USA', 'UK', 'France', 'Canada', 'Germany', 'India', 'Japan', 'Italy', 'Spain', 'Australia', 'West Germany', 'Mexico', 'Sweden', 'Turkey', 'Soviet Union', 'Netherlands', 'Hong Kong', 'Brazil', 'Denmark']

import numpy
country_unique_key = list(country_unique_key)
country_unique_key.sort()
year_unique_key = list(year_unique_key)
year_unique_key.sort(key=int)
colxrow = numpy.zeros(shape=(len(year_unique_key),len(country_unique_key)))
df_country_year = pd.DataFrame(colxrow,columns=country_unique_key)
df_country_year.index = year_unique_key


colxrow2 = numpy.zeros(shape=(len(year_unique_key), len(countries_list_toshow)))
df_country_year_toshow = pd.DataFrame(colxrow2 ,columns=countries_list_toshow)
df_country_year_toshow.index = year_unique_key
for i in range(len(dfObj['country'])):
    if dfObj['year'][i] == '':
        pass
    else: 
        if '|' in movie_country[i]:
            country = dfObj['country'][i].split('|')
            for c in country:
                if c not in countries_list_toshow:
                    pass
                else:                    
                    df_country_year_toshow[c][dfObj['year'][i]] = df_country_year_toshow[c][dfObj['year'][i]] + 1
        else:
            if dfObj['country'][i] not in countries_list_toshow:
                pass
            else:
                df_country_year_toshow[dfObj['country'][i]][dfObj['year'][i]] = df_country_year_toshow[movie_country[i]][dfObj['year'][i]] + 1
            

#df_country_year['Total_year'] =  df_country_year.sum(axis=1)
#df_country_year = df_country_year.drop(['Russian', 'German'], axis=1)
# Plot
import matplotlib.pyplot as plt
import seaborn as sns                

#['USA', 'UK', 'France', 'Canada', 'Germany', 'India', 'Japan', 'Italy', 'Spain', 'Australia', 'West Germany', 'Mexico', 'Sweden', 'Turkey', 
# 'Soviet Union', 'Netherlands', 'Hong Kong', 'Brazil', 'Denmark']

x= df_country_year_toshow[40: len(df_country_year_toshow)-2].index  #since the date are the same in both tables I only have 1 x
y1=df_country_year_toshow['USA'][40: len(df_country_year_toshow)-2]
y2=df_country_year_toshow['UK'][40: len(df_country_year_toshow)-2]
y3=df_country_year_toshow['France'][40: len(df_country_year_toshow)-2]
y4=df_country_year_toshow['Canada'][40: len(df_country_year_toshow)-2]
y5=df_country_year_toshow['Germany'][40: len(df_country_year_toshow)-2]
y6=df_country_year_toshow['India'][40: len(df_country_year_toshow)-2]
y7=df_country_year_toshow['Japan'][40: len(df_country_year_toshow)-2]
y8=df_country_year_toshow['Italy'][40: len(df_country_year_toshow)-2]
y9=df_country_year_toshow['Spain'][40: len(df_country_year_toshow)-2]
y10=df_country_year_toshow['Australia'][40: len(df_country_year_toshow)-2]
y11=df_country_year_toshow['West Germany'][40: len(df_country_year_toshow)-2]
y12=df_country_year_toshow['Mexico'][40: len(df_country_year_toshow)-2]
y13=df_country_year_toshow['Sweden'][40: len(df_country_year_toshow)-2]
y14=df_country_year_toshow['Turkey'][40: len(df_country_year_toshow)-2]
y15=df_country_year_toshow['Soviet Union'][40: len(df_country_year_toshow)-2]
y16=df_country_year_toshow['Netherlands'][40: len(df_country_year_toshow)-2]
y17=df_country_year_toshow['Hong Kong'][40: len(df_country_year_toshow)-2]
y18=df_country_year_toshow['Brazil'][40: len(df_country_year_toshow)-2]
y19=df_country_year_toshow['Denmark'][40: len(df_country_year_toshow)-2]

###
plt.figure(figsize=(15,8))
plt.stackplot(x,y1,label="USA")
plt.stackplot(x,y2,label="UK")
plt.stackplot(x,y3,label="France")
plt.stackplot(x,y4,label="Canada")
plt.stackplot(x,y5,label="Germany")
plt.stackplot(x,y6,label="India")
plt.stackplot(x,y7,label="Japan")
plt.stackplot(x,y8,label="Italy")

plt.title("Number of movies top countries from 1930 to 2016")
plt.legend(loc='upper left', title="Countries")
plt.legend()
plt.show()






##
# Basic stacked area chart.
x= df_country_year_toshow[40: len(df_country_year_toshow)-2].index
#y = [df_country_year_toshow['USA'][40: len(df_country_year_toshow)-2],df_country_year_toshow['UK'][40: len(df_country_year_toshow)-2], df_country_year_toshow['France'][40: len(df_country_year_toshow)-2
#     df_country_year_toshow['Canada'][40: len(df_country_year_toshow)-2], df_country_year_toshow['Germany'][40: len(df_country_year_toshow)-2],df_country_year_toshow['India'][40: len(df_country_year_toshow)-2]
#     y7=df_country_year_toshow['Japan'][40: len(df_country_year_toshow)-2], y8=df_country_year_toshow['Italy'][40: len(df_country_year_toshow)-2]]
pal = sns.color_palette("Set2")
plt.stackplot(x,y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19,labels= ['USA', 'UK', 'France', 'Canada', 'Germany', 'India', 'Japan', 'Italy', 'Spain', 
                        'Australia', 'West Germany', 'Mexico', 'Sweden', 'Turkey', 'Soviet Union', 'Netherlands', 
                        'Hong Kong', 'Brazil', 'Denmark'], 
              colors=pal, alpha=0.8, baseline='zero')
plt.grid()
plt.xlabel('Year')
plt.ylabel('Number of movies')
plt.xlim(1930, 2016)
plt.legend(loc='upper left')
plt.show()
#############################################################################

sns.set()
df_country_year_toshow[60:len(df_country_year_toshow)-3][:].plot(kind='area', stacked=True)


#################################################################################

#transforming dictionaries country_dictionary_total into a dataframe.
country_dictionary_total_df = pd.DataFrame(list(country_dictionary_total.items()),columns = ['Country','Number of Movies']) 
#dropping 'None', 'Russian', 'German', that are not really anything
country_dictionary_total_df = country_dictionary_total_df.drop([42, 98, 64])

##############################################################################

#Aca voy a poner number of movies in each genre por cada año...


genre_list2 = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Game-Show', 
               'History', 'Horror', 'Musical', 'Music', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 
               'Thriller', 'War', 'Western']


colxrow2 = numpy.zeros(shape=(len(year_unique_key), len(genre_list2)))
df_genre_year_toshow = pd.DataFrame(colxrow2 ,columns=genre_list2)
df_genre_year_toshow.index = year_unique_key

# movie_year
# movie_genre
for i in range(len(movie_genre)):
    if movie_year[i] == '':
        pass
    else:
        if len(movie_genre[i])==0 :
                    pass
        else:
            for j in range(len(movie_genre[i][0])):
                if movie_genre[i][0][j] not in genre_list2:
                    pass
                else:
                    df_genre_year_toshow[movie_genre[i][0][j]][movie_year[i]] = df_genre_year_toshow[movie_genre[i][0][j]][movie_year[i]] + 1



sns.set(style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)
df_genre_year_toshow[75:len(df_genre_year_toshow)-2][:].plot(kind='bar', stacked=True)
#sns.set(xlabel='Year', ylabel='Number of Movies', title='Movie Genre for Years')
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.title("Movie Genre for each Years") # You can comment this line out if you don't need title
plt.show(fig)

#df_genre_year_toshow.to_csv(r'D:\Thesis\code\df_genre_year_toshow.csv')


#listo!!!!!!!!!!!!














################################################################################


#Now country of origin of films.. need to take into account 
country_dictionary_total = {}
counter = 0
indexes_nocountry = []
for i in range(len(movie_country)):
    if '|' in movie_country[i]:
        countries = movie_country[i].split('|')
        for c in countries:
            if c not in country_dictionary_total.keys():
                country_dictionary_total[c] = 1
            else:
                country_dictionary_total[c] = country_dictionary_total[c] + 1
    else:
        if  movie_country[i].startswith('Production'):#'Production' in movie_country[i]:# or country.startswith('Filming') or country.startswith('Goofs') or country.startswith('Production') or country.startswith('Trivia') or country.startswith('Also Known') or len(country) == 0:
            indexes_nocountry.append(i)
        elif movie_country[i] not in country_dictionary_total.keys():
            country_dictionary_total[movie_country[i]] = 1
        else:
            country_dictionary_total[movie_country[i]] = country_dictionary_total[movie_country[i]] + 1 
     
        
        
        
        
        
#saving the file names in order to scrape sites.            
movie_scraping_country_filename = [] 
for i in range(len(indexes_nocountry)):
    movie_scraping_country_filename.append(movie_id[indexes_nocountry[i]][0])



#made copy just in case
movie_country_copy = movie_country.copy()
#movie_country_missing
#cheanging the values for correct ones in list of movie_country.
for found_country in range(len(movie_country_missing)):
    movie_country[indexes_nocountry[found_country]] = movie_country_missing[found_country]
   # indexes_nocountry
   # movie_country




#saving infor in order to check and use later
movie_scraping_country_index = pd.DataFrame()
movie_scraping_country_index = movie_scraping_country_index.assign(movie_nocountry_index = indexes_nocountry, movie_nocountry_id = movie_scraping_country_filename)

len(movie_scraping_country_filename) # = 8
#just printing to check and in some cases change the name manually
movie_id[14752]    
    
print(movie_scraping_country_index['movie_nocountry_index'][63])
print(movie_scraping_country_index['movie_nocountry_id'][63])
#186391
print(movie_country[457881])
movie_country[457881] = 'USA'










# =============================================================================
# 
# movie_country[27478] = 'France'
# dfObj.iloc[27478]
# tt0052370
# 
# 
# 
# movie_country[42177] = 'USA'
# dfObj.iloc[42177]
# tt0070552
# 
# =============================================================================


#dfObj['boxOffice'][21725] = int(11884)
#dfObj.iloc[21725]




#df_country_year.to_csv(r'D:\Thesis\code\df_country_year.csv')
#df_country_year_toshow.to_csv(r'D:\Thesis\code\df_country_year_toshow.csv')







#trying to recreate map with countries here... not going so well.

# =============================================================================
# country_dictionary_total_df.to_csv(r'D:\Thesis\code\country_dictionary_total_df.csv')
# 
# 
# import plotly
# import plotly.offline as py
# import plotly.graph_objs as go
# import plotly.tools as tls
# import warnings
# data = [ dict(
#         type = 'choropleth',
#         locations = country_dictionary_total_df['Country'],
#         locationmode = 'country names',
#         z = country_dictionary_total_df['Number of Movies'],
#         text = country_dictionary_total_df['Country'],
#         colorscale = [[0,'rgb(255, 255, 255)'],[1,'rgb(255, 0, 0)']],
#         autocolorscale = False,
#         reversescale = False,
#         marker = dict(
#             line = dict (
#                 color = 'rgb(180,180,180)',
#                 width = 0.5
#             ) ),
#         colorbar = dict(
#             autotick = False,
#             tickprefix = '',
#             title = 'Production Countries'),
#       ) ]
# 
# layout = dict(
#     title = 'Production Countries for Motion Pictures',
#     geo = dict(
#         showframe = False,
#         showcoastlines = False,
#         projection = dict(
#             type = 'Mercator'
#         )
#     )
# )
# 
# fig = dict( data=data, layout=layout )
# plt.show(fig)
# #py.iplot( fig, validate=False, filename='d3-world-map' )
# 
# =============================================================================
string = 'A.J.O.Z. Films,        Gaumont,        Les Magnifiques'
string2 = 'Gaumont'
mylist = [x.strip() for x in string2.split(',')]

#production company
production_company_dic = {}
for i in range(len(dfObj['production_co'])):
    mylist = [x.strip() for x in dfObj['production_co'][i].split(',')]
    for j in range(len(mylist)):
        if mylist[j] not in production_company_dic.keys():
            production_company_dic[ mylist[j]] = 1
        else:
            production_company_dic[ mylist[j]] = production_company_dic[ mylist[j]] + 1






# density plots 
            
            
sns.distplot(dataset_12k['boxOffice'], hist = False, kde = True, kde_kws = {'shade': True, 'linewidth': 3})
dataset_12k['boxOffice'].plot(
    kind='box',
    figsize=(12,8)
)