# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:55:45 2019

@author: rabbitindamoon
"""
#Production Co
    
#    from collections import Counter 
import numpy as np
import pytz
import datetime
from datetime import timezone
import bisect
from time import gmtime, strftime
import pandas as pd
from scipy import stats
import re as re
import os
import io
import matplotlib.pyplot as plt
import collections
from collections import Counter
from calendar import month_name
import calendar
from time import strptime

##This is trying with only one file, in the loop below is trying with multiple files    
#    def parse(self, filename):
#        self.filename = open(filename, 'r')
#        self.line=self.filename.readlines()
    # opening  the file and saving the txt file in order to extract info for general stats.
#    myfile = open("tt0000001_full_movie_bio.dat", 'r', encoding='utf8') # open lorem.txt for reading text
#    lines = myfile.readlines()


#working diretories:
    
work_dir = "D:\Thesis\data\movie_bios"
#work_dir = "D:\Thesis\data\movie_bios_sub"
#work_dir = "D:\Thesis\data\movie_bios_sub_sub"


#save the number of files in work_dir so to know how big the dicitonary has to be.

#num_of_files_dir = len([name for name in os.listdir(work_dir) if os.path.isfile(os.path.join(work_dir, name))])

# creating dataframes in order to save the specific data from each text file.  

count = 0
count_series_vs_movies = 0
#creating list in order to create dictionaries.

year_list = list(range(1800,2019))
genre_list = ["Action", "Adult", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Film-Noir", "Game-Show", "History", "Horror", "Musical", "Music", "Mystery", "News", "Reality-TV", "Romance", "Sci-Fi", "Short", "Sport", "Talk-Show", "Thriller", "War", "Western"]
castnumber_list = list(range(0,200))
dirnum_list = list(range(0,200))
metacritic_list = list(range(0,101))

rating_lists = []
for i in np.arange(0, 10.1, 0.1):
    i = "%.1f" % i
    rating_lists.append(i)

#creating dictionaries in order to save inforamtion faster.
    
year_dic = { i : 0 for i in year_list } 
genre_dic = { i : 0 for i in genre_list }
castnumber_dic = { i : 0 for i in castnumber_list }
dirnum_dic = { i : 0 for i in dirnum_list}
metacritic_dic = { i : 0 for i in metacritic_list}
rating_dic = { i:0 for i in rating_lists}
movie_serie_dic =  {'movie' : 0, 'series' : 0}
movie_cast_alph = {'alph' : 0, 'no_alph' : 0}

#creatiing empty lists in order to save files that are missing certain data.

file_noyear= []
file_nogenre= []
file_cast101 = []
file_nodir = []
file_nocast = []
file_zerocast_len =[]
file_zerodir_len =[]
file_nometacritic = []
file_nometacritic2 = []
file_metacritic = []
file_dirplus2 = []
file_norating = []
file_norating2 = []
file_dir21 =[]
cast_alph = []
cast_nonalph = []
file_nomovie_id = []


#this are the ones we are going to use in the future to create dictionary or pandas dataframe..

#not ready to use this yet
#dictionary_cast = dict.fromkeys(range(num_of_files_dir)) 
movie_id = []
movie_cast = []
movie_dir = []
movie_meta = []
movie_rating = []
movie_star_ids = [] 
movie_genre = []
movie_year = []
movie_type = []
movie_filename = []
movie_gross = []

#movie_budget = [0] * 561291
budget_list = []
budget_indexes = []
gross_list = []
gross_indexes = []


movie_writer = []
movie_producer = []
movie_cine = []
movie_cast_order = []

movie_number_reviews_imdb = []
movie_number_reviews_critic = []
movie_budget = []
movie_date = []

months = {m.lower() for m in month_name[1:]}  # create a set of month names
spl_word = 'plot_keywords'
spl_word2 = 'Country'
spl_word1 = 'Production Co'
movie_plot_keywords = []
movie_country = []
movie_production_co = []
movie_review_count_user = []
##    year_dic[1980] =  year_dic[1980] +1 


#    rating_value_pd = pd.DataFrame()
#    metascore = pd.DataFrame()
#    country_pd = pd.DataFrame()

## try the above variables first then focus on the rest.
#    duration = None
#    gross = None
#    budget = None
#    runtime = None
#    cast_num = None
#    director_num = None
#    producers_num = None





#this is to open multiple text files one by one before going inside loop to read the text.    
for filename in os.listdir(work_dir):
    if filename.endswith(".dat"):
        
# =============================================================================
    #this is for checking only 10 files in directory
# #    for index in range(1, 10):
# #        name = "tt000000{index}_full_movie_bio.dat".format(index=index)
# #        print(name)
# =============================================================================

#       
        path = os.path.join(work_dir, filename)
        with io.open(path, mode="r", encoding="utf-8") as fd:
            movie_filename.append(filename)
            count+=1
            if count%100 == 0 :
                print(count)
            #creating year variable to save the title year of movie/series
            lines = fd.readlines()
            year = 0
            movieid= str()
            genre = str()
            cast = str()
            director = str()
            metascore = int()
            rating= float()
            type_film = str()
            star_ids = str()
            count3 = 0
            count_seriesVSmovies = 0
            gross = int()
            alph_order = 0
            release_year = int()
            #still need to add code to extract this below, not hard just lazy...
            number_reviews = int()
            producer = str() # Produced by, Series Produced by
            writer = str() # Writing Credits(in alphabetical order) , Series Writing Credits
            cine = str() # Series Cinematography by, Cinematography by
            review_count_imdb = int()
            review_count_critic = int() # this is not meta review counts, but the numebr of critics who reviewed the film, so it needs to be added to the other review.
            fecha = str()
            ano = []
            plot_keywords = str()
            country = str()
            production_company = str()
            review_count_user = int()
            film_type = 1
            budget = str()
#            music = str()  # Music by, 
#            sound = str() # Sound Department 
#            edit_film = str() # Film Editing by, Series Film Editing by
            
#checking if cast, director exist, otherwise save filename in order to manually check it   
#this is no longer necessary since its done in other script and files were deleted already.
# =============================================================================
#             
#             if any("Cast" in s for s in lines):
#                 continue
#             else:
#                 file_nocast.append(filename)
#                 
#             if any("director_ids" in s for s in lines):
#                 continue
#             else:
#                 file_nodir.append(filename)  
#                 
# =============================================================================
                
                
                
#adding values into dictionaries from the files that contain cast, director, genre, title year, metascore, rating value....                
            for i in range(len(lines)):
                #for title year
                count3 += 1 
                if lines[i].startswith('Production Co'):
                    line = lines[i]                    
                    production_company = line.split(spl_word1,1)[1] 
                    try:                    
                        production_company = production_company[:production_company.index("See")]
                        production_company = production_company.strip()
                    except:
                        production_company = production_company.strip()
                #find the movie id and save it in list.
                if lines[i].startswith('movie_id'):
                    line = lines[i]
                    movieid =  re.findall("tt[0-9]{7}",line)
                    if not movieid:
                        file_nomovie_id.append(fd)
                
                
                #finding the number of reviews for the imbd score for each movie    

                if lines[i].startswith('rating_count'):
                    line = lines[i]
                    review_count_imdb =  re.findall(r"[0-9]+",line)
                #finding the number of reviews for the imbd score for each movie    
                if lines[i].startswith('review_count_critic'):
                    line = lines[i]
                    review_count_critic =  re.findall(r"[0-9]+",line)    
                if lines[i].startswith('review_count_user'):
                    line = lines[i]
                    review_count_user =  re.findall(r"[0-9]+",line)                    
                # finding gross    \$[0-9]+
                if lines[i].startswith('Gross'):
                    line = lines[i]
                    line = line.replace(",", "")
                    line = line.replace("Gross", "")                        
                    line = " ".join(line.split()) 
                    gross =  re.findall("\$[0-9]+",line)   
                    if not gross:
                        gross = None
                    else:
                        gross= int(gross[0].replace("$", ""))
            


#Budget	None  gross_list  gross_indexes
                if lines[i].startswith('Budget'):
                    line = lines[i]
                    line = line.replace(",", "")
                    line = line.replace("Budget", "")                        
                    line = " ".join(line.split()) 
                    line = line.replace("(estimated)", "")  
                    budget = re.findall("\$[0-9]+",line)  
                    if not budget:
                        budget = None
                    else:
                        budget= int(budget[0].replace("$", ""))
# =============================================================================
#                     budget =  re.findall("\$[0-9]+",line)   
#                     if not budget:
#                         budget = None
#                     else:
#                         budget = int(gross[0].replace("$", ""))                        
# =============================================================================
                        
                #line = 'Release Date	 September 1896 (USA)    See more »  ' 
                if lines[i].startswith('Release Date'):
                    line = lines[i]
                    mes = next((word for word in line.split() if word.lower() in months), None)
                    ano = re.findall(r'\d{4}', line)
                    dia = re.findall(r'(\b\d{1,2}\b)', line)                    
                    if not mes:
                        mes = 1
                    else:   
                        mes = strptime(mes,'%B').tm_mon
                    
                    if not dia:
                        dia=1
                    else:
                        dia = int(dia[0])
                        
                    if not ano:
                        ano = year
                        if not ano:
                            continue
                        else:
                            ano = int(ano[0]) 
                            fecha = datetime.datetime(ano, mes, dia)
                            
                    else:
                        ano = int(ano[0])                
                        fecha = datetime.datetime(ano, mes, dia)
                   
                  
                # finds the title year and counts the number of movies in each year. (saving it iin dictionary for stats)   
                if lines[i].startswith('titleYear'):
                    year = re.findall('\d+', lines[i])
                     #we are doing this above in the relesed day, since we can also find this information there and relesead day is after titleYear.                
#                    if len(year) == 0:
#                        file_noyear.append(filename)
#                    else:    
#                        year = int(year[0])
#                        key = str(year)
#                        if key in year_dic.keys():
#                            year_dic[key] =  year_dic[key] + 1
    
                 # for genre, find the movie gneres then it counts and save information about the genre of movie.          
                if lines[i].startswith('genre') or lines[i].startswith('genre_tags'):
                    line = lines[i]
                    genre = line[10:len(line)]
                    genre = genre.split()
                    if not genre or genre[0] == "None": 
                        file_nogenre.append(filename)
                    else:
                        for i in range(len(genre)):
                            key = genre[i]
                            if key in genre_dic.keys():
                                genre_dic[key] =  genre_dic[key] + 1

                #gettiing cast and finding the files without cast              
                if lines[i].startswith('Cast') and not lines[i].startswith('Casting') : #and not lines[i].startswith('Cast') and not :  #  
                    line = lines[i]
                    cast = re.findall("nm[0-9]{7}",line)   
                    #film_type = '1'
                    #cast = cast.split()
                    
                #getting cast series  and finding the files without cast Series Cast          
                if lines[i].startswith('Series Cast') and not lines[i].startswith('Series Casting'):# or lines[i].startswith('Series Casting'): #or lines[i].startswith('Series cast') :                 
                        line = lines[i]
                        cast = re.findall("nm[0-9]{7}",line)
                        film_type = 0
                        #cast = cast.split()                           
                           
            
                #getting directors in all files, and finding the files without directors.    
                if lines[i].startswith('director_ids'): # director_ids
                    line = lines[i]
                    director = re.findall("nm[0-9]{7}",line)
                #getting case where it stars with Directed by, and director_ids is empty.        
                if lines[i].startswith('Directed by') and not director:
                    line = lines[i]
                    director = re.findall("nm[0-9]{7}",line)
                #getting directors in all files, and finding the files without directors.            
                if lines[i].startswith('Series Directed') and not director:
                    line = lines[i]
                    director = re.findall("nm[0-9]{7}",line)      
                    film_type = 0
  
  
                            
                            
                #Finding all metascore of all films/series and if it DNE then saving it.
                #saving all file-names without metascore.
                if lines[i].startswith('metascore'):
                    line = lines[i]
                    metascore = re.findall(r"[0-9]+",line)
                    
                    if not metascore or metascore[0]== 'None':
                        file_nometacritic.append(filename)                     
                    else:
                        key= int(metascore[0])
                        file_metacritic.append(filename)
                        if key in metacritic_dic.keys():
                            metacritic_dic[key] = metacritic_dic[key] + 1
                        else:
                            file_nometacritic2.append(filename)

                # finding all rating values and saving all that do not ahve onw
                if lines[i].startswith('rating_value'):
                    line = lines[i]
                    rating = re.findall(r"[-+]?[0-9]*\.?[0-9]*.$",line)
                    
                    if not rating or rating[0]== 'e':
                        file_norating.append(filename)
                        
                    else:
                        rating2 = float(rating[0])
                        #key= rating[0]
                        if str(rating2) in rating_dic.keys():
                            rating_dic[str(rating2)] = rating_dic[str(rating2)] + 1  
                        else:
                            file_norating2.append(filename)
 
#algo no funciona aca...en la que divide series y peliculas.!!!!!!!!!!!!!!!!
           
                if lines[i].startswith('title') and not lines[i].startswith('titleYear'):
                    line = lines[i]
                    
                    if 'Episode' in line:
                        film_type = 0
                    if 'Serie' in line:
                        film_type = 0
                    
                    #type_film = re.findall("\((.*?)\)",line)
                    #l = 'Episode'
                    #l2 = 'Series'
 
                   



# need to see if the actors in star_ids are the same that in cast. 
#it seems to be working now just need to re-check                                
                if lines[i].startswith('star_ids'):
                    line = lines[i]
                    star_ids = re.findall("nm[0-9]{7}",line)    
                #here we are waiting until we read the last line of the file oni order to compare star_ids with cast.   because cast is almost at the end of file and star_ids at the start.
                if  len(star_ids)!=0 and count3 == len(lines):                         
                    new_cast_list = cast[0:len(star_ids)]#.copy()
                    if star_ids == new_cast_list:
                        movie_cast_alph['no_alph'] = movie_cast_alph['no_alph'] + 1
                        cast_nonalph.append(filename)
                        alph_order = 1
                    else:
                        movie_cast_alph['alph'] = movie_cast_alph['alph'] + 1
                        cast_alph.append(filename)
                        alph_order = 0
                    
                        
               # saving the writers
                if lines[i].startswith('writer_ids'):
                    line = lines[i]
                    writer = re.findall("nm[0-9]{7}",line)        
                    
                if lines[i].startswith('Writing Credits') and not writer :
                    line = lines[i]
                    writer = re.findall("nm[0-9]{7}",line)


                if lines[i].startswith('Series Writing Credits') and not writer :
                    line = lines[i]
                    writer = re.findall("nm[0-9]{7}",line)  
                    film_type = 0
                    
                                      
                if lines[i].startswith('Cinematography by'):
                    line = lines[i]
                    cine = re.findall("nm[0-9]{7}",line)
                    
                if lines[i].startswith('Series Cinematography'):
                    line = lines[i]
                    cine = re.findall("nm[0-9]{7}",line)
                    film_type = 0
#Produced by, Series Produced by                    
                if lines[i].startswith('Produced by'):
                    line = lines[i]
                    producer = re.findall("nm[0-9]{7}",line) 
                if lines[i].startswith('Series Produced'):
                    line = lines[i]
                    producer = re.findall("nm[0-9]{7}",line)   
                    film_type = 0
                if lines[i].startswith('plot_keywords'):
                    line = lines[i]                   
                    plot_keywords = line.partition(spl_word)[2]
                    plot_keywords = " ".join(plot_keywords.split())
                	
                if lines[i].startswith('Country'):
                    line = lines[i]                   
                    country = line.partition(spl_word2)[2]
                    country = " ".join(country.split())
                    #country = [x.replace('|', ' ') for x in country]  #this is not working for some reason 
#here i am saving dictionary for series and movies.
            if film_type == 0:
                count_seriesVSmovies +=1
                movie_serie_dic['series'] = movie_serie_dic['series'] + 1  
            else:
                count_seriesVSmovies +=1
                movie_serie_dic['movie'] = movie_serie_dic['movie'] + 1  
#counting number of cast, directors in each filmand saving info.                       
            key1 = len(cast)
            

            if key1 ==0:
                file_zerocast_len.append(filename)
                
            if key1 in castnumber_dic.keys():
                castnumber_dic[key1] =  castnumber_dic[key1] + 1
                
            if key1 >100:
                file_cast101.append(filename)
                  
            #finding size directors   
            key2 = len(director)
            if key2==0:
                file_zerodir_len.append(filename)
                
            if key2 in dirnum_dic.keys():
                dirnum_dic[key2] = dirnum_dic[key2] + 1   
                                
            if key2>3:
                file_dirplus2.append(filename)
            
            if key2>20:
                file_dir21.append(filename) 
# here we are saving the year into the dictionary since there could be 2 places where year appears and or one could be missing, this was originally
# in the part for titleYear, but it was missing opportunity to use ano from release date.                
            if not year:
                if not ano:
                    file_noyear.append(filename)
                else:
                    year= ano
                    key = str(year)
                    if key in year_dic.keys():
                        year_dic[key] =  year_dic[key] + 1                             
            else:    
                year = int(year[0])
                key = str(year)
                if key in year_dic.keys():
                    year_dic[key] =  year_dic[key] + 1              
# finding all movies without directors and saving info. 
                
            
                                                 
            #here we will check if cast director exist, if not we save the file.
            if not director:
                file_nodir.append(filename)
            if not cast:
                file_nocast.append(filename)
#saving all info in lists, in order fusion them later.                    
            movie_genre.append(tuple([genre]))
            movie_id.append(movieid)
            movie_year.append(year)
            movie_cast.append(tuple([cast]))
            movie_dir.append(tuple([director]))
            movie_meta.append(metascore)
            movie_rating.append(rating)
            movie_star_ids.append(tuple([star_ids]))
            movie_type.append(film_type)  
            movie_gross.append(gross)
            movie_writer.append(writer)     
            movie_cine.append(cine)
            movie_producer.append(producer)   
            # 0 = alph and 1 = non-alph
            movie_cast_order.append(alph_order)
            #saving the number of reviews both for imbd and metacritic
            movie_number_reviews_imdb.append(review_count_imdb)
            movie_number_reviews_critic.append(review_count_critic)
            movie_date.append(fecha)
            movie_plot_keywords.append(plot_keywords)
            movie_country.append(country)
            movie_production_co.append(production_company)
            movie_review_count_user.append(review_count_user)
            movie_budget.append(budget)
            
# This part is finding if any movie is still missing cast. as it turns out around 540000 are missing cast.
movie_cast_empty = []
movie_director_empty = []
movie_gross_nonempty = []
for i in range(len(movie_cast)):
    if any(map(lambda x: any(x), movie_cast[i])) == False:  
        movie_cast_empty.append(i)
         
for i in range(len(movie_dir)):
    if any(map(lambda x: any(x), movie_dir[i])) == False:  
        movie_director_empty.append(i)    
                     
for i in range(len(movie_gross)):
    if type(movie_gross[i]) == int and movie_gross[i] != 0 :
        movie_gross_nonempty.append(i)	
        

#funciona de la misma manera pero es mas robusto!
# =============================================================================
# import numbers        
# movie_gross_prueba =  movie_gross.copy()
# movie_gross_nonempty_prueba=[]
# for i in range(len(movie_gross_prueba)):
#     if isinstance(movie_gross_prueba[i], numbers.Real) and movie_gross_prueba[i] != 0 :
#           movie_gross_nonempty_prueba.append(i)
# =============================================================================
        	

#creating a pandas data frame to save the information... adding all the columns into one dataframe
dfObj = pd.DataFrame()
#dfObj_short = pd.DataFrame()
#still need to add 'producer','writer'
dfObj = dfObj.assign(ID = movie_id, cast = movie_cast, director = movie_dir, producer = movie_producer, writer = movie_writer, 
                     cinematography = movie_cine , metacritic = movie_meta, imdbScore = movie_rating, boxOffice = movie_gross, budget = movie_budget,
                     genre = movie_genre, year = movie_year, movie_or_serie = movie_type, stars = movie_star_ids, 
                     alph0_nonalph1 = movie_cast_order, date_released = movie_date, country = movie_country, 
                     plot_keywords = movie_plot_keywords, no_reviews_imdb = movie_number_reviews_imdb, no_review_critics= movie_number_reviews_critic, 
                     no_review_user = movie_review_count_user, production_co = movie_production_co )
#dfObj_short = dfObj_short.assign(ID = movie_id, cast = movie_cast, director = movie_dir, producer = movie_producer, writer = movie_writer, cinematography = movie_cine , metacritic = movie_meta, imdbScore = movie_rating, boxOffice = movie_gross, genre = movie_genre, year = movie_year, MvsS = movie_type,
#                     stars = movie_star_ids, alphVSnonalph = movie_cast_order, date_realesed = movie_date)
# here I am trying to save the perfect data 
gross_perfect = dfObj.loc[movie_gross_nonempty]
actors_perfect = dfObj['cast'].loc[movie_gross_nonempty]
directors_perfect = dfObj['director'].loc[movie_gross_nonempty]
#gross_perfect.to_csv(r'D:\Thesis\code\19-10-17\gross_perfect.csv')
#rows_perfect_gross



movie_budget_nonempty = []
gross_perfect = gross_perfect.reset_index(drop = False)
import math
for i in range(len(gross_perfect['budget'])):
    if math.isnan(gross_perfect['budget'][i]) == True:
        pass
    else:
        movie_budget_nonempty.append(i)	

gross_budget_perfect = gross_perfect.loc[movie_budget_nonempty]

#here was the code to draw some of the information regarding the data.




contador = 0
  
movie_actor_dic = {}
movie_director_dic = {}
movie_writer_dic = {}
movie_producer_dic = {}


movie_actor_dic_perfect = {}
movie_director_dic_perfect = {}

#nm0000033_actor = []
#nm0000033_dir = []

# this counts the number of films an actor and director did and save it in a dictionary, the key is the actor number and the value is the 
#number of films, some are. Movie Cast need to be 
for i in range(len(movie_cast)):
    for j in range(len(movie_cast[i][0])):
        
        if movie_cast[i][0][j] not in movie_actor_dic.keys():
            movie_actor_dic[movie_cast[i][0][j]] = 1
        else:
            movie_actor_dic[movie_cast[i][0][j]] = movie_actor_dic[movie_cast[i][0][j]] + 1
            
#        if movie_cast[i][0][j] == 'nm0000033':
#            nm0000033_actor.append(movie_id[i])
        

# gross_perfect  actors_perfect
for i in range(len(movie_dir)):
    for j in range(len(movie_dir[i][0])):
        
        if movie_dir[i][0][j] not in movie_director_dic.keys():
            movie_director_dic[movie_dir[i][0][j]] = 1
        else:
            movie_director_dic[movie_dir[i][0][j]] = movie_director_dic[movie_dir[i][0][j]] + 1
            
#        if movie_dir[i][0][j] == 'nm0000033':
#            nm0000033_dir.append(movie_id[i])

# =============================================================================
# #checking for duplicates in filename_list_movie_nodir and saving the unique ones in unique_list2 for actor Alfred Hitchcock    
# uniq_hitch_list_cast = []
# uniq_hitch_set_cast = set()
# for item in nm0000033_actor:
#     item = item[0]
#     if item not in uniq_hitch_set_cast:
#          uniq_hitch_list_cast.append(item)
#          uniq_hitch_set_cast.add(item)
# 
# uniq_hitch_list_dir = []
# uniq_hitch_set_dir = set()
# for item in nm0000033_dir:
#     item = item[0]
#     if item not in uniq_hitch_set_dir:
#          uniq_hitch_list_dir.append(item)
#          uniq_hitch_set_dir.add(item)
# =============================================================================


#what im a creating here
actors_perfect2 = list(actors_perfect)
for i in range(len(actors_perfect2)):
    for j in range(len(actors_perfect2[i][0])):
        if actors_perfect2[i][0][j] in movie_actor_dic.keys():
            movie_actor_dic_perfect[actors_perfect2[i][0][j]] = movie_actor_dic[actors_perfect2[i][0][j]]

director_perfect2 = list(directors_perfect)
for i in range(len(director_perfect2)):
    for j in range(len(director_perfect2[i][0])):
        if director_perfect2[i][0][j] in movie_director_dic.keys():
            movie_director_dic_perfect[director_perfect2[i][0][j]] = movie_director_dic[director_perfect2[i][0][j]]

    
    





#creating pandas dataframe from dictionary in order to create quintiles.          
#pd.DataFrame(d)

movie_actor_dic_perfect_pd =pd.DataFrame(list(movie_actor_dic_perfect.items()))
movie_director_dic_perfect_pd =pd.DataFrame(list(movie_director_dic_perfect.items()))

movie_actor_dic_perfect_pd['quintile'] = pd.qcut(movie_actor_dic_perfect_pd[1], 10, labels=False, duplicates='drop')
movie_director_dic_perfect_pd['quintile'] = pd.qcut(movie_director_dic_perfect_pd[1], 10, labels=False, duplicates='drop')

#creating a datafrma that has aggregated the actors and directors in order to do possible random forest or some type of prediction.
rows_perfect_gross_aggregated = gross_perfect[['ID', 'stars', 'director', 'imdbScore', 'boxOffice']].copy()



#here we are creating a aggregating all the actors in each movie using the quintile in order to obtain one value for all actor per movie.    
actors_perfect_list = actors_perfect.values.tolist()
prueba1 = {}
movie_actor_dic_perfect_pd.columns = ['actor', 'no_movies', 'quintile']
actors_dic_qintile = dict(zip(movie_actor_dic_perfect_pd.actor, movie_actor_dic_perfect_pd.quintile))

aggregate_actors = []
agg_actor = 0
# loop to aggregate all values of cast in each movie to obtain one single value.
for i in range(len(actors_perfect_list)):
    agg_actor = 0
    divisor = 0
    for j in range(len(actors_perfect_list[i])):
        divisor = len(actors_perfect_list[i])
        if actors_perfect_list[i][0][j] in actors_dic_qintile.keys():  
            agg_actor = agg_actor + actors_dic_qintile[actors_perfect2[i][0][j]]
    agg_actor = agg_actor / divisor
    aggregate_actors.append(agg_actor)





movie_director_dic_perfect_pd.columns = ['director', 'no_movies', 'quintile']
director_dic_qintile = dict(zip(movie_director_dic_perfect_pd.director, movie_director_dic_perfect_pd.quintile))

aggregate_directors = []
agg_director = 0

for i in range(len(director_perfect2)):
    agg_director = 0
    divisor = 0
    for j in range(len(director_perfect2[i])):
        divisor = len(director_perfect2[i])
        if director_perfect2[i][0][j] in director_dic_qintile.keys():  
            agg_director = agg_director + director_dic_qintile[director_perfect2[i][0][j]]
    agg_director = agg_director / divisor
    aggregate_directors.append(agg_director)
    
    
    
    

#  File "D:/Thesis/code/19-10-29/anaconda/movie_txt_getinfo.py", line 669, in <module>
#    if actors_perfect_list[i][0][j] in actors_dic_qintile.keys():

#IndexError: string index out of range    
    
    
# =============================================================================
# #creating the dataframe to do random forest on...
# random_forest_data = pd.DataFrame()
# random_forest_data = rows_perfect_gross_aggregated.copy()
# del random_forest_data['stars']
# del random_forest_data['director']
# random_forest_data.insert(1, "cast", aggregate_actors, True) 
# random_forest_data.insert(2, "director", aggregate_directors, True) 
# 
# 
# #Changing ID to string in dataframe.. since right now is list.
# #random_forest_data['ID'] = random_forest_data['ID'].apply(lambda x: ','.join(map(str, x)))
# random_forest_data['imbdScore'] = random_forest_data['imbdScore'].apply(lambda x: ''.join(map(str, x)))
# random_forest_data['imbdScore'][567989] = '5.5'
# random_forest_data['imbdScore'] = random_forest_data['imbdScore'].astype(float)
# 
# 
# 
# 
# 
# #random_forest_data.to_csv(r'D:\Thesis\code\19-10-19\spyder\random_forest_data.csv')
#  #creating this in  order to save it as csv file.
# perfect_data = pd.DataFrame()
# perfect_data = rows_perfect_gross.copy()
# perfect_data['imbdScore'] = perfect_data['imbdScore'].apply(lambda x: ''.join(map(str, x)))
# perfect_data['imbdScore'][567989] = '5.5'
# perfect_data['imbdScore'] = perfect_data['imbdScore'].astype(float)
# 
# perfect_data['ID'] = perfect_data['ID'].apply(lambda x: ''.join(map(str, x)))
# perfect_data['metacritic'] = perfect_data['metacritic'].apply(lambda x: ''.join(map(str, x)))
# perfect_data['metacritic'].replace(" ", "")
# ##perfect_data['metacritic'] = perfect_data['metacritic'].astype(float)
# perfect_data['metacritic'] = pd.to_numeric(perfect_data['metacritic'], errors='coerce')
# 
# perfect_data = perfect_data.reset_index()
# 
# perfect_tuple_cast = rows_perfect_gross['cast'].copy()
# perfect_tuple_cast = perfect_tuple_cast.reset_index()
# perfect_tuple_cast = perfect_tuple_cast['cast']
# 
# 
# for i in range(len(perfect_tuple_cast)):
#     perfect_tuple_cast[i] = perfect_tuple_cast[i][0]
#     
# del perfect_data['cast']
# perfect_data.insert(1, "cast", perfect_tuple_cast, True) 
# 
# perfect_tuple_dir = perfect_data['director'].copy()
# for i in range(len(perfect_tuple_dir)):
#     perfect_tuple_dir[i] = perfect_tuple_dir[i][0]   
# del perfect_data['director']
# perfect_data.insert(2, "director", perfect_tuple_dir, True) 
# 
# 
# perfect_tuple_genre = perfect_data['genre'].copy()
# for i in range(len(perfect_tuple_genre)):
#     perfect_tuple_genre[i] = perfect_tuple_genre[i][0] 
# del perfect_data['genre']
# perfect_data.insert(10, "genre", perfect_tuple_genre, True) 
# 
# perfect_tuple_star = perfect_data['stars'].copy()
# for i in range(len(perfect_tuple_star)):
#     perfect_tuple_star[i] = perfect_tuple_star[i][0] 
# del perfect_data['stars']
# perfect_data.insert(13, "stars", perfect_tuple_star, True) 
# perfect_data.to_csv(r'D:\Thesis\code\perfect_data2.csv') 




#guardando el archivo de 
#dfObj.to_csv(r'D:\Thesis\code\data_unfixed_26-01-2020.csv')

# =============================================================================



#dfObj.to_csv(r'D:\Thesis\code\20-02-10\dfObj.csv')

# =============================================================================
# 
# gross_perfect2 = pd.DataFrame()
# gross_perfect2 = gross_perfect.copy()  
# gross_budget_perfect2 = pd.DataFrame()
# gross_budget_perfect2 = gross_budget_perfect.copy  
# gross_perfect['no_reviews_imdb'] = gross_perfect['no_reviews_imdb'].apply(lambda x: ''.join(map(str, x)))    
# for i in range(1909,len(gross_perfect['no_reviews_imdb'])):
#     if not gross_perfect['no_review_user'][i]:
#         gross_perfect['no_review_user'][i] = int(0)
#     else: 
#         gross_perfect['no_review_user'][i] = int(gross_perfect['no_review_user'][i][0])
#  
#        
# for i in range(len(gross_perfect['no_review_critics'])):
#     if not gross_perfect['no_review_critics'][i]:
#         gross_perfect['no_review_critics'][i] = int(0)
#     else: 
#         gross_perfect['no_review_critics'][i] = int(gross_perfect['no_review_critics'][i])
# 
# gross_perfect['no_review_critics'] = gross_perfect['no_review_critics'].apply(lambda x: ''.join(map(str, x)))    
# 
# 
# for i in range(len(gross_perfect['no_reviews_imdb'])):
#     if not gross_perfect['no_reviews_imdb'][i]:
#         gross_perfect['no_reviews_imdb'][i] = int(0)
#     else: 
#         gross_perfect['no_reviews_imdb'][i] = int(gross_perfect['no_reviews_imdb'][i])
# 
# gross_perfect['imdbScore'] = gross_perfect['imdbScore'].apply(lambda x: ''.join(map(str, x)))        
# 
# 
# gross_perfect['metacritic'] = gross_perfect['metacritic'].apply(lambda x: ''.join(map(str, x)))        
# 
# for i in range(len(gross_perfect['metacritic'])):
#     if not gross_perfect['metacritic'][i]:
#         gross_perfect['metacritic'][i] = int(gross_perfect['imdbScore'][i]*10)
#     else: 
#         gross_perfect['metacritic'][i] = int(gross_perfect['metacritic'][i])
# 
# 
# import cpi
# 
# gross_perfect2['adjusted_bo'] = gross_perfect2.apply(lambda x: cpi.inflate(x.boxOffice, x.year), axis=1)     
# gross_perfect2['tercile'] = pd.qcut(gross_perfect2['adjusted_bo'], 3, labels=False)
# gross_perfect2.to_csv(r'D:\Thesis\code\20-02-10\gross_perfect2.csv')
# 
# gross_budget_perfect2 = gross_perfect2.loc[movie_budget_nonempty]
# gross_budget_perfect2['adjusted_budget'] = gross_budget_perfect2.apply(lambda x: cpi.inflate(x.budget, x.year), axis=1)     
# gross_budget_perfect2.to_csv(r'D:\Thesis\code\20-02-10\gross_budget_perfect2.csv')
# 
# =============================================================================


