# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:32:53 2020
#aca estoy creando el codigo para obtener los datos para poder tener 3-4-5 peliculas con que entrenar
y para predecir la pelicula numero 4-5-6 respectivamente. 
pero en este archivo vamos a generar 4 peliculas y predecir la numero 5
@author: rabbitindamoon
"""
import pandas as pd
#import numpy as np
#import cpi
import re as re



# =============================================================================
# 
# dfObj = pd.read_csv("D:/Thesis/code/gross_perfect_19_10_29.csv")
#    
# dataset_500k = dfObj.copy()  
# dataset_500k = dataset_500k.reset_index(drop=True)
# dataset_500k['metacritic'] = dataset_500k['metacritic'].apply(lambda x: ''.join(map(str, x)))
# for i in range(len(dataset_500k['metacritic'])):
#     try:
#         dataset_500k['metacritic'][i] = float(dataset_500k['metacritic'][i])
#     except:
#         dataset_500k['metacritic'][i] = float(dataset_500k['imdbScore'][i]*10)    
# 
# 
# #here we are jsut uploading the data that we are gonna use, this should be done using the definition..
# #    dataset_12k = pd.read_csv("D:/Thesis/code/perfect_data_yearsfixed.csv")
# #    dataset_500k['metacritic'] = dataset_500k['metacritic'].apply(literal_eval)
# #    type(dataset_500k['metacritic'][0] )
# #    print(type(dataset_500k.at[0, 'metacritic'])) #this shows that the change from string to list worked
# #print(type(dataset_12k.at[0, 'ID']))
# #    dataset_12k['metacritic'][14][0]  # this shows re-confirms that it worked the change...
#    
# #here is were deleted all the films that did not contained metacritic.
# # =============================================================================
# #     #this worked, it deleted all empty lists from metacritic and saved it in data.
# #     data = dataset_12k[(dataset_12k['metacritic'].str.len() != 0) | (dataset_12k['metacritic'].str.len() != 0)]
# #     # elimina los parentesis de las lsitas para poder tener solo un valor para metacritic
# #     data['metacritic'] = data['metacritic'].apply(lambda x: ''.join(map(str, x)))
# #     #this worked, making the values in metacritic float values.
# #     data['metacritic'] = data['metacritic'].astype(float)
# # =============================================================================
#    
# #    data = dataset_12k.copy()
# #reindexing data since few items were deleted, old index is deleteded .
# #    data = data.reset_index(drop = True)
# #dropping index that was saved 
# try:
#     dataset_500k = dataset_500k.drop(['Unnamed: 0'], axis=1)
# except:
#     pass
# 
# #cambiando de string a lista imdb score column
# #    data['imdbScore'] = data['imdbScore'].apply(literal_eval)
# #this worked, it deleted all empty lists from metacritic and saved it in data.
# #    data = data[(data['imdbScore'].str.len() != 0) | (data['imdbScore'].str.len() != 0)]
# # elimina los parentesis de las lsitas para poder tener solo un valor para metacritic
# dataset_500k['imdbScore'] = dataset_500k['imdbScore'].apply(lambda x: ''.join(map(str, x)))
# #this worked, making the values in metacritic float values.
# 
# #finding all imdb score with 'e' values
# dataset_500k_imdb_evalue =[]
# for i in range(len(dataset_500k['imdbScore'])):
#     if dataset_500k['imdbScore'][i] == 'e':
#         dataset_500k_imdb_evalue.append(i)
#     else:
#         pass
# 
# #deleting all rows where imdb score is 'e'
# dataset_500k_imdb_e_value_id= []
# for i in dataset_500k_imdb_evalue:
#     dataset_500k_imdb_e_value_id.append(dataset_500k['ID'][i])
# dataset_500k = dataset_500k.drop(dataset_500k.index[dataset_500k_imdb_evalue])    
# dataset_500k = dataset_500k.reset_index(drop=True)
# 
# 
# 
# dataset_500k['imdbScore'] = dataset_500k['imdbScore'].astype(float)
# 
#     
# #    print(type(data.at[0, 'imdbScore'])) #this shows that the change from string to list worked
# #print(type(dataset_12k.at[0, 'ID']))
# type(dataset_500k['imdbScore'][14])  # this shows re-confirms that it worked the change...
# 
# 
# 
# dataset_500k['ID'] = dataset_500k['ID'].apply(lambda x: ''.join(map(str, x)))
# dataset_500k['ID'] = dataset_500k['ID'].apply(literal_eval)  
# 
# 
# type(dataset_500k['date_released'][0])
# #now we are sorting the data by  data using the date_realesed that is misspelled here, but in the new run is correctly spelled.
# #data_prueba = data.copy()
# #    data['date_realesed'] = pd.to_datetime(data['date_realesed'])
# 
# dataset_500k.sort_values('date_released', inplace=True, ascending=True)
# dataset_500k = dataset_500k.reset_index(drop = True)
#     
#     #data_prueba.to_csv(r'D:\Thesis\code\dataset_metacritic_19_10_30.csv')
#     #######################################################
#      
#      #here we create a new column with the adjusted prices according to inflation using 2019 as the year 
# #    data['adjusted'] = data.apply(lambda x: cpi.inflate(x.boxOffice, x.year), axis=1)     
# #    data['tercile'] = pd.qcut(data['adjusted'], 3, labels=False)
# #    data['tercile'].value_counts()
# 
# #    data['metacritic'] = data['metacritic'].apply(lambda x: ''.join(map(str, x)))
#     
#     #this worked, making the values in metacritic float values.
#     #aca estoy poniendo imdb score en todos los metacritics que no tienen numero y haciendo que el resto sean float
# 
#  
# 
# 
# ############################################################################################################################## 
#             
# # =============================================================================
# #    rows_no_cast = pd.DataFrame()
# #    rows_no_cast_position = []
# #     #here I am checking the films that have no cast.
# #     for cast_missing_index in range(len(data_8k)):
# #         cast_1 = data_8k['cast'][cast_missing_index]
# #         cast_1 = re.findall("nm[0-9]{7}",cast_1)
# #         if cast_1 == []:
# #             temp_row = data_8k.iloc[cast_missing_index]
# #             rows_no_cast= rows_no_cast.append(data_8k.iloc[cast_missing_index])
# #             rows_no_cast_position.append(cast_missing_index)
# # =============================================================================
# ##############################################################################################################################   
# 
# 
# 
# 
# =============================================================================
import numpy as np



import json
dataset_6k = pd.read_csv("D:/Thesis/code/20-02-10/gross_budget_perfect2.csv")
with open('D:/Thesis/code/20-01-30/production_co_movies_500k_0.json') as json_file:
    production_co_movies_500k = json.load(json_file)
# =============================================================================
# 
# #for no_reviews_imdb!!!!
# dataset_500k['no_reviews_imdb'] = dataset_500k['no_reviews_imdb'].apply(literal_eval)
# print(type(dataset_500k.at[0, 'no_reviews_imdb'])) #this shows that the change from string to list worked
# dataset_500k['no_reviews_imdb'] = dataset_500k['no_reviews_imdb'].apply(lambda x: ''.join(map(str, x)))
# #this worked, making the values in metacritic float values.
# dataset_500k['no_reviews_imdb'] = dataset_500k['no_reviews_imdb'].astype(int)
# 
# 
# # for no_review_critic
# dataset_500k['no_review_critics'] = dataset_500k['no_review_critics'].apply(literal_eval)
# dataset_500k['no_review_user'] = dataset_500k['no_review_user'].apply(literal_eval)
# 
# for index_i in range(len(dataset_500k['no_review_critics'])):
#     
#     try:
#         dataset_500k['no_review_critics'][index_i] = int(dataset_500k['no_review_critics'][index_i][0])
#     except:
#         dataset_500k['no_review_critics'][index_i] = 0
#         
#     try: 
#         dataset_500k['no_review_user'][index_i] = int(dataset_500k['no_review_user'][index_i][0])
#     except:
#         dataset_500k['no_review_user'][index_i] = 0
# 
# 
# 
# print(type(dataset_500k.at[0, 'no_review_critics'])) #this shows that the change from string to list worked
# for index_i in range(len(dataset_500k['no_review_critics'])):
#     if not dataset_500k['no_review_critics'][index_i]:
#         dataset_500k['no_review_critics'][index_i] = 0
#     else:
#         dataset_500k['no_review_critics'][index_i] = int(dataset_500k['no_review_critics'][index_i][0])
#     
#     if not dataset_500k['no_review_user'][index_i]:
#         dataset_500k['no_review_user'][index_i] = 0
#     else:
#         dataset_500k['no_review_user'][index_i] = int(dataset_500k['no_review_user'][index_i][0])
# 
# 
# =============================================================================




#dataset_500k['no_review_critics'] = dataset_500k['no_review_critics'].replace('', 0, inplace=True)
#res = {k: v for k, v in production_co_movies_500k.items() if v > 1}
#res.pop('')
#res.pop('None')
#production_co_movies_500k = dict.fromkeys(res, 0)




def dictionary_actor_bo_puntaje(dataset, production_co_movies_500k):
    '''    data set need to be uploaded and cast, director needs to be a list of strings, 
    need to explain more as we go along'''    
    # creando dictionarios para cada actor.  En uno se va a guardar lsitas de listas de todas las peliculas
    # y en otra se va a guardar average score para el actor
#    dictionario_de_prueba = []
    data_8k = dataset
    data = dataset.copy()
    actors_dictionary = {}
    actors_rating_bo = {}
    actors_num_movies = {}
    # creando dictionario para los directores, donde se guarda un average para todos los directores.
    directors_dictionary = {}
    directors_rating_bo = {}
    directors_num_movies= {}
    actors_dictionary2 = {}
    # creando dictionario para guardar la informacion de escritores:
    writer_dictionary = {}
    writer_rating_bo = {}
    writer_num_movies = {}
    
    producer_dictionary = {}
    producer_rating_bo = {}
    producer_num_movies = {}
    
#    star_dictionary = {}
    star_rating = {}
    star_num_movies = {}
    #dataset_puntaje = pd.DataFrame(dataset_puntaje,columns=['movie_id', 'cast', 'director', 'producer', 'writer', 
    #                                                        'cinematography','metacritic','imdb_score','boxOffice',
    #                                                        'actor_score_1', 'stars', 'adjusted'])
    
    cinematography_dic = {}
    cinematography_rating = {}
    cinematography_num_movies = {}
    
    dataset_list = []
    star_list_test = []
    
    #production_co_movies_500k
    
    
    actors_dictionary_binary_values = {}
    #tratando cosas #probando cosas aca
#    data_list  = data.values.tolist()
#    data_cast = data['cast'].tolist()
#    adjusted = data_8k['adjusted'][0]
#    star_si_no = str()
#    directors_num_movies['santiago'] = [1]
#    directors_num_movies['santiago'].append(1)
#    directors_num_movies['santiago'].append(1)
#    len(directors_num_movies['santiago'])
#    sum(directors_num_movies['santiago'])
#    lista_provisoria = list(directors_num_movies['santiago'])
#    lista_provisoria = lista_provisoria[0:2]



# la listas de listas necesita tener lo sigueinte:
# [movie_id, imbd_score, metacritic, director_score_until_now, 
# imbd_avg_score_of_movies_so_far(this is for the actor score, if it DNE then use average score of star_ids), 
#                                       binary_star (if it appears as feature actor, in star_ids 0-no, 1-yes)]   
 



       
       
    #here finding total average for each actor in order to use info in case there is no info regarding actor previews expirience.
    # also finding a total average for each director in order to use info in case there is no info regarding actor previews expirience.           
    imdb_total = data_8k['imdbScore'].sum()
    metacritic_total = data_8k['metacritic'].sum()
    meta_average = metacritic_total / len(data_8k['metacritic'])
    imdb_average = imdb_total / len(data_8k['imdbScore'])

    for i_1 in range(len(data_8k)):
        cast_1 = data_8k['cast'][i_1]
        cast_1 = str(cast_1)
        cast_1 = re.findall("nm[0-9]{7}",cast_1)
    
        dir_1 = data_8k['director'][i_1]
        dir_1 = str(dir_1)
        dir_1 = re.findall("nm[0-9]{7}",dir_1)
        
        writer_1 = data_8k['writer'][i_1]
        writer_1 = str(writer_1)
#        if type(writer_1) == float:
#            data_8k['writer'][i_1] = []
#            writer_1 = str(
        writer_1 = re.findall("nm[0-9]{7}",writer_1)
        
        producer_1 =  data_8k['producer'][i_1]
        producer_1 = str(producer_1)

        
        if type(producer_1) == float:
            data_8k['producer'][i_1] = str('[]')
            producer_1 = str('[]')
        producer_1 = re.findall("nm[0-9]{7}",producer_1)


        cinematography_1 = data_8k['cinematography'][i_1]
        cinematography_1 = str(cinematography_1)
# =============================================================================
#         if type(cinematography_1) == float:
#             data_8k['cinematography'][i_1] = str('[]')
#             cinematography_1 = str('[]')
# =============================================================================
        cinematography_1 = re.findall("nm[0-9]{7}", cinematography_1)   

#        box_office =  int(data_8k['adjusted'][i_1])
        
        imdb_1 = float(data_8k['imdbScore'][i_1])
        metacritic_1 = int(data_8k['metacritic'][i_1])
        # llendo por la lista de actores de cada pelicula.
        for j_1 in cast_1:
            # viendo si el actor esta en la lista de actores y guardando el rating accumulado
            # guardando el numero de peliculas que el actor hizo y de acuerdo a eso 
            if j_1 not in actors_rating_bo.keys():
                actors_rating_bo[j_1] = [imdb_1]
                actors_num_movies[j_1] = 1
            else:
                actors_rating_bo[j_1].append(imdb_1)
                actors_num_movies[j_1] = actors_num_movies[j_1] + 1
# this is created in order to get info for stars...
        for j_5 in cast_1:
            # viendo si el actor esta en la lista de actores y guardando el rating accumulado
            # guardando el numero de peliculas que el actor hizo y de acuerdo a eso 
            if j_5 not in star_rating.keys():
                star_rating[j_5] = [metacritic_1]
                star_num_movies[j_5] = 1
            else:
                star_rating[j_5].append(metacritic_1)
                star_num_movies[j_5] = star_num_movies[j_5] + 1                
                
        # llendo por la lista de directores de cada pelicula y creando dictionario para poder obtener un puntaje para cada peli.  
        for j_2 in dir_1:
            # viendo si el director esta el la lista de directores y guardando el rating accumulado
            # guardando el numero de peliculas que el director hizo hizo y de acuerdo a eso
            if j_2 not in directors_rating_bo.keys():
                directors_rating_bo[j_2] = [imdb_1]
                directors_num_movies[j_2] = 1
            else:
                directors_rating_bo[j_2].append(imdb_1)
                directors_num_movies[j_2] = directors_num_movies[j_2] + 1  
                
        # llendo por la lsita de escritores de cada pelicula, si el escritor esta en la lsita entonces 
#        if len(writer_1) != 0:
        for j_3 in writer_1:
            if j_3 not in writer_rating_bo.keys():
                writer_rating_bo[j_3] = [imdb_1]
                writer_num_movies[j_3] = 1
            else:
                writer_rating_bo[j_3].append(imdb_1)
                writer_num_movies[j_3] = writer_num_movies[j_3] + 1
        # llendo por la lista de productores de cada pelicula, si el productor esta en la lsita entonces 
        for j_4 in producer_1:
            if j_4 not in producer_rating_bo.keys():
                producer_rating_bo[j_4] = [imdb_1]
                producer_num_movies[j_4] = 1
            else:
                producer_rating_bo[j_4].append(imdb_1)
                producer_num_movies[j_4] = producer_num_movies[j_4] + 1
#        if len(cinematography_1) != 0:
        for j_6 in cinematography_1:
            if j_6 not in cinematography_rating.keys():
                cinematography_rating[j_6] = [imdb_1]
                cinematography_num_movies[j_6] = 1
            else:
                cinematography_rating[j_6].append(imdb_1)
                cinematography_num_movies[j_6] = cinematography_num_movies[j_6] + 1            
         
       
    # aca necesito divdir el average de cada actor por el numero de peliculas y asi realmente obtener el average real.    
    # quizas no encesito esta informacion, quizas esta informacion la estoy creando mas abajo automaticamente.
        #creating a list of it then I can save it in a dataframe in orter to retrive it later.
        
  













#  2nd part!!!!!!!!!!!!!



      
    star_1_list1 = []
    star_2_list2 = []
    star_3_list3 = []
    cast_score_total_list = []
    cinematography_score_total_list = []    
    director_score_total_list = []
    writer_score_total_list = []
    producer_score_total_list = []
    star_1_list = []
    star_2_list = []
    star_3_list = []
    list_movie_bo = []
    cast_score_total_list = []
    cinematography_score_total_list = []  
    production_company_list = []
#    index_wo_stars = []
    # here we loop over all films to save information regarding each movie for each actor.
    #can check if is is correct by checking the number of films each actor has and compared it by the number of list of lists for each actor.        
    for i in range(len(data_8k)):
        movie_id = data_8k['ID'][i]
        #movie_id = re.findall("tt[0-9]{7}",movie_id) 
#        movie_id = movie_id[0]
        #getting row cast from dataframe
        cast =  data_8k['cast'][i]
        cast = str(cast)
        cast = re.findall("nm[0-9]{7}",cast)    
        len_cast = len(cast)
        binary_star_list_temp = []
        actors_score_movie_temp = []
        
        director = data_8k['director'][i]
        director = str(director)
        director = re.findall("nm[0-9]{7}",director)
        
        writer = data_8k['writer'][i]
        writer = str(writer)
        writer = re.findall("nm[0-9]{7}",writer)
        producer = data_8k['producer'][i]
        producer = str(producer)
        producer = re.findall("nm[0-9]{7}",producer)
        
        #getting row-stars  dataframe
        stars = data_8k['stars'][i]
        stars = str(stars)
        stars = re.findall("nm[0-9]{7}",stars)
        
        cinematography = data_8k['cinematography'][i]
        cinematography = str(cinematography)
        cinematography = re.findall("nm[0-9]{7}",cinematography)

        meta = data_8k['metacritic'][i]
        imdb = data_8k['imdbScore'][i]
        
        no_reviews_imdb = data_8k['no_reviews_imdb'][i]
        no_reviews_critics = data_8k['no_review_critics'][i]
        no_reviews_users = data_8k['no_review_user'][i]
        
        
        
        budget = data_8k['adjusted_budget'][i]
        box_office =  data_8k['adjusted_budget'][i]
        #adjusted
#        b_o = data_8k['adjusted'][i] 
#        tercile = data_8k['tercile'][i]
        #unadjusted to inflation
#        b_o = data_8k['boxOffice'][i]         
        director_score = 0
        writer_score = 0
        producer_score = 0
        cinematography_score = 0        
        cast_score_total = 0


        
        #Production company part.!
        #list_production_co_movie_ttx = 
#        star_1 = data_8k['stars'][i_1]
        try:
            list_production_co_movie_ttx = [x.strip() for x in data_8k['production_co'][i].split(',')]
        except:
            list_production_co_movie_ttx = []
        score_productions_co_temp = 1
        score_productions_co = 1
        for i_pro in list_production_co_movie_ttx:
            if i_pro not in production_co_movies_500k.keys():
                score_productions_co = 1
            else:
                score_productions_co_temp = production_co_movies_500k[i_pro]
                production_co_movies_500k[i_pro] = production_co_movies_500k[i_pro] + 1
                if score_productions_co_temp > score_productions_co:
                    score_productions_co = score_productions_co_temp



        number_cinematography_movie = len(cinematography)
        #loop para encontrar el puntaje del cinematografos en la pelicula i.
        if len(cinematography) > 0:
            for i_cinematography in cinematography:
                #creando variable de puntaje de cada escritos en la pelicula i.
                cinematography_s = int()
                #creando lista provisoria para guardar info de cada pelicula i para cada escritos i_writer.
                lista_provisoria_cinematography =  list()
                #loop para ver si el escritor ya existe en writer_dictionary.
                #si escritor no existe, entonces calculamos el average del escritor con average de adjusted de todas las peliculas.
                if i_cinematography not in cinematography_dic.keys():
                    cinematography_s = imdb_average
                # si no vemos cuantas peliculas hizo hasta el momento de esta pelicula i y usando la suma de imdb_score hasta esta pelicula i dividimos por el numero de pelculas hasta i y usamos este everage como nuevo puntaje de director.
                else:
                    length_of_movies_cinematography_thus_far = len(cinematography_dic[i_cinematography])
                    lista_provisoria_cinematography = list(cinematography_rating[i_cinematography])
                    lista_provisoria_cinematography = lista_provisoria_cinematography[0: length_of_movies_cinematography_thus_far]
                    cinematography_s = sum(lista_provisoria_cinematography) / len(lista_provisoria_cinematography)
            #aca genero un nuevo dictionario para poder usar esta infromacion en el futuro si es necesario.
            
                list_movie_cinematography = [movie_id, imdb, meta, cinematography_s]
                if i_cinematography not in cinematography_dic.keys():
                   cinematography_dic[i_cinematography] = [list_movie_cinematography]
                else:
                    cinematography_dic[i_cinematography].append(list_movie_cinematography)            
        #sumando los puntajes de los 2 escritores para obtener un valor unico.
                cinematography_score = cinematography_score + cinematography_s
        #dividiendo el puntaje de los 2 escritores por el numero de escritores para obtener el puntaje total de escritores para la pelicula i
    
            cinematography_score = cinematography_score / number_cinematography_movie
    
        # si es que la lsita de escritores esta vacia entonces uso los directores de la pelicula para generar un puntaje para el escritor.
        else:
            number_cinematography_movie = len(director)
            for i_cinematography in director:
                #creando variable de puntaje para director i_dir de pelicula i.
                cinematography_s = int()  
                #creando lista provisoria para guardar info de cada pelicula i  para cada director i_dir
                lista_provisoria_cinematography = list()
                # loop para ver si director ya existe en directors_dictionary.
                #si director no existe, entonces calculando el average del director con la suma de imdb score de todas las peliculas hechas por el dividiendo por el numero de peliculas hechas por el.
                if i_cinematography not in directors_dictionary.keys():
                    cinematography_s = imdb_average
                # de lo contrario viendo cuantas peliculas hizo hasta el momento de pelicula i y usando la suma de imdb_score hasta pelicula i dividiendo por el numero de peliculas hasta i y usando este average como nuevo puntaje de director.
                else:
                    length_of_movies_cinematography_thus_far = len(directors_dictionary[i_cinematography])
                    lista_provisoria_cinematography = list(directors_rating_bo[i_cinematography])
                    lista_provisoria_cinematography = lista_provisoria_cinematography[0: length_of_movies_cinematography_thus_far]
                    cinematography_s = sum(lista_provisoria_cinematography) / len(lista_provisoria_cinematography)
        #sumando los puntajes de los 2 escritores para obtener un valor unico.
                cinematography_score = cinematography_score + cinematography_s
        #dividiendo el puntaje de los 2 escritores por el numero de escritores para obtener el puntaje total de escritores para la pelicula i
            
            try:
                cinematography_score = cinematography_score / number_cinematography_movie
            except ZeroDivisionError:
                cinematography_score = imdb_average



        
# informacion de escrito en pelicula i                  
        #creando los valores necesarios para los escritores de la pelicula y asi poder guardar un valor para cada uno.
        number_writers_movie = len(writer)
        #loop para encontrar el puntaje del escritos en la pelicula i.
        if len(writer) > 0:
            for i_writer in writer:
                #creando variable de puntaje de cada escritos en la pelicula i.
                writer_s = int()
                #creando lista provisoria para guardar info de cada pelicula i para cada escritos i_writer.
                lista_provisoria_writer =  list()
                #loop para ver si el escritor ya existe en writer_dictionary.
                #si escritor no existe, entonces calculamos el average del escritor con average de adjusted de todas las peliculas.
                if i_writer not in writer_dictionary.keys():
                    writer_s = imdb_average
                # si no vemos cuantas peliculas hizo hasta el momento de esta pelicula i y usando la suma de imdb_score hasta esta pelicula i dividimos por el numero de pelculas hasta i y usamos este everage como nuevo puntaje de director.
                else:
                    length_of_movies_writer_thus_far = len(writer_dictionary[i_writer])
                    lista_provisoria_writer = list(writer_rating_bo[i_writer])
                    lista_provisoria_writer = lista_provisoria_writer[0: length_of_movies_writer_thus_far]
                    writer_s = sum(lista_provisoria_writer) / len(lista_provisoria_writer)
            
            #aca genero un nuevo dictionario para poder usar esta infromacion en el futuro si es necesario.
                list_movie_writer = [movie_id, imdb, meta, writer_s, score_productions_co]    
                if i_writer not in writer_dictionary.keys():
                    writer_dictionary[i_writer] = [list_movie_writer]
                else:
                    writer_dictionary[i_writer].append(list_movie_writer)            
        #sumando los puntajes de los 2 escritores para obtener un valor unico.
                writer_score = writer_score + writer_s
        #dividiendo el puntaje de los 2 escritores por el numero de escritores para obtener el puntaje total de escritores para la pelicula i

            writer_score = writer_score / number_writers_movie

        # si es que la lsita de escritores esta vacia entonces uso los directores de la pelicula para generar un puntaje para el escritor.
        else:
            number_writers_movie = len(director)
            for i_writer in director:
                #creando variable de puntaje para director i_dir de pelicula i.
                writer_s = int()  
                #creando lista provisoria para guardar info de cada pelicula i  para cada director i_dir
                lista_provisoria_writer = list()
                # loop para ver si director ya existe en directors_dictionary.
                #si director no existe, entonces calculando el average del director con la suma de imdb score de todas las peliculas hechas por el dividiendo por el numero de peliculas hechas por el.
                if i_writer not in directors_dictionary.keys():
                    writer_s = imdb_average
                # de lo contrario viendo cuantas peliculas hizo hasta el momento de pelicula i y usando la suma de imdb_score hasta pelicula i dividiendo por el numero de peliculas hasta i y usando este average como nuevo puntaje de director.
                else:
                    length_of_movies_writer_thus_far = len(directors_dictionary[i_writer])
                    lista_provisoria_writer = list(directors_rating_bo[i_writer])
                    lista_provisoria_writer = lista_provisoria_writer[0: length_of_movies_writer_thus_far]
                    writer_s = sum(lista_provisoria_writer) / len(lista_provisoria_writer)
        #sumando los puntajes de los 2 escritores para obtener un valor unico.
                writer_score = writer_score + writer_s
        #dividiendo el puntaje de los 2 escritores por el numero de escritores para obtener el puntaje total de escritores para la pelicula i
            try:
                writer_score = writer_score / number_writers_movie
            except ZeroDivisionError:
                writer_score = imdb_average
        
            

            
           

# informacion de productor en pelicula i
        number_producers_movie = len(producer)
        #loop para encontrar el puntaje del escritos en la pelicula i.
        if len(producer) > 0:
            for i_producer in producer:
                #creando variable de puntaje de cada escritos en la pelicula i.
                producer_s = int()
                #creando lista provisoria para guardar info de cada pelicula i para cada escritos i_writer.
                lista_provisoria_producer =  list()
                #loop para ver si el escritor ya existe en writer_dictionary.
                #si escritor no existe, entonces calculamos el average del escritor con la suma del puntaje imdb de todas las peliculas hechas por el dividiendo por el numero de peliculas hechas por el mismo.
                if i_producer not in producer_dictionary.keys():
                    producer_s = imdb_average
                # si no vemos cuantas peliculas hizo hasta el momento de esta pelicula i y usando la suma de imdb_score hasta esta pelicula i dividimos por el numero de pelculas hasta i y usamos este everage como nuevo puntaje de director.
                else:
                    length_of_movies_producer_thus_far = len(producer_dictionary[i_producer])
                    lista_provisoria_producer = list(producer_rating_bo[i_producer])
                    lista_provisoria_producer = lista_provisoria_producer[0: length_of_movies_producer_thus_far]
                    producer_s = sum(lista_provisoria_producer) / len(lista_provisoria_producer)
                
                list_movie_producer = [movie_id, imdb, meta, producer_s, score_productions_co]
            #aca genero un nuevo dictionario para poder usar esta infromacion en el futuro si es necesario.
                if i_producer not in producer_dictionary.keys():
                    producer_dictionary[i_producer] = [list_movie_producer]
                else:
                    producer_dictionary[i_producer].append(list_movie_producer)            
        #sumando los puntajes de los 2 escritores para obtener un valor unico.
                producer_score = producer_score + producer_s
        #dividiendo el puntaje de los 2 escritores por el numero de escritores para obtener el puntaje total de escritores para la pelicula i           
            
            producer_score = producer_score / number_producers_movie

        # si es que la lsita de escritores esta vacia entonces uso los directores de la pelicula para generar un puntaje para el escritor.
        else:
            number_producer_movie = len(director)
            for i_producer in director:
                #creando variable de puntaje para director i_dir de pelicula i.
                producer_s = int()  
                #creando lista provisoria para guardar info de cada pelicula i  para cada director i_dir
                lista_provisoria_producer = list()
                # loop para ver si director ya existe en directors_dictionary.
                #si director no existe, entonces calculando el average del director con la suma de imdb score de todas las peliculas hechas por el dividiendo por el numero de peliculas hechas por el.
                if i_producer not in directors_dictionary.keys():
                    producer_s = imdb_average
                # de lo contrario viendo cuantas peliculas hizo hasta el momento de pelicula i y usando la suma de imdb_score hasta pelicula i dividiendo por el numero de peliculas hasta i y usando este average como nuevo puntaje de director.
                else:
                    length_of_movies_producer_thus_far = len(directors_dictionary[i_producer])
                    lista_provisoria_producer = list(directors_rating_bo[i_producer])
                    lista_provisoria_producer = lista_provisoria_producer[0: length_of_movies_producer_thus_far]
                    producer_s = sum(lista_provisoria_producer) / len(lista_provisoria_producer)
        #sumando los puntajes de los 2 escritores para obtener un valor unico.
                producer_score = producer_score + producer_s
        #dividiendo el puntaje de los 2 escritores por el numero de escritores para obtener el puntaje total de escritores para la pelicula i
            
            try:
                producer_score = producer_score / number_producer_movie
            except ZeroDivisionError:
                producer_score = imdb_average       
        
#informacion de director en pelicula i         
        #necesito crear algo para poder guardar un valor para director pero no puedo utilizar la misma tecnica que para actor
        #ya que no estoy guardando 
        # guardando el numero total de directores de la pelicula i 
        number_directors_movie = len(director)
        #list_movie_dir = [index_movie, b_o, imbd_score, meta, dir_avg]
        #loop para encontrar el puntaje de cada director en la pelicula i.
        for i_dir in director:
            #creando variable de puntaje para director i_dir de pelicula i.
            d_s = int()  
            #creando lista provisoria para guardar info de cada pelicula i  para cada director i_dir
            lista_provisoria_dir = list()
            # loop para ver si director ya existe en directors_dictionary.
            #si director no existe, entonces calculando el average del director con la suma de imdb score de todas las peliculas hechas por el dividiendo por el numero de peliculas hechas por el.
            if i_dir not in directors_dictionary.keys():
                d_s = imdb_average
            # de lo contrario viendo cuantas peliculas hizo hasta el momento de pelicula i y usando la suma de imdb_score hasta pelicula i dividiendo por el numero de peliculas hasta i y usando este average como nuevo puntaje de director.
            else:
                length_of_movies_dir_thus_far = len(directors_dictionary[i_dir])
                lista_provisoria_dir = list(directors_rating_bo[i_dir])
                lista_provisoria_dir = lista_provisoria_dir[0: length_of_movies_dir_thus_far]
                d_s = sum(lista_provisoria_dir) / len(lista_provisoria_dir)
            
            list_movie_dir = [movie_id, imdb, meta, d_s, score_productions_co]
            #aca genero un nuevo dictionario para poder usar esta infromacion en el futuro si es necesario.
            if i_dir not in directors_dictionary.keys():
                directors_dictionary[i_dir] = [list_movie_dir]
            else:
                directors_dictionary[i_dir].append(list_movie_dir)
            
            director_score = director_score + d_s
#            director_score = director_score / number_directors_movie
        # dividiendo el puntaje total de los directores de la pelicula por el numero de directores en la pelicula,         
        
        try:
            director_score = director_score / number_directors_movie
        except ZeroDivisionError:
            director_score = imdb_average       
        





        
        star_score_list = []
        for j_star_bo in stars: 
            star_score = int()           
            lista_provisoria_stars = list()
            #for k in range(i_mas1):
            if j_star_bo not in actors_dictionary.keys():
                star_score = meta_average
            else: 
                length_of_movies_star_thus_far = len(actors_dictionary[j_star_bo])
                lista_provisoria_stars = list(star_rating[j_star_bo])
                lista_provisoria_stars = lista_provisoria_stars[0: length_of_movies_star_thus_far]
                star_score = sum(lista_provisoria_stars) / len(lista_provisoria_stars)             
            star_score_list.append(star_score) 
        
#informacion de actores en pelicula i.
        # necesito crear esta lista por ahora.
        #list_movie = [index_movie, b_o, imdb_score, meta, dir_avg, actor_score, binary_star]

                
        for j in cast:
            # necesito guardar el rating de cada actor aca, tambien el de cada director. para luego guardar la lista            
            #length_of_movies_director_thus_far = len(directors_dictionary[cast])
            #contador = 0
            actor_score = int()           
            lista_provisoria = list()
            #for k in range(i_mas1):
            if j not in actors_dictionary.keys():
                actor_score = imdb_average
            else: 
                length_of_movies_actor_thus_far = len(actors_dictionary[j])
                lista_provisoria = list(actors_rating_bo[j])
                lista_provisoria = lista_provisoria[0: length_of_movies_actor_thus_far]
                actor_score = sum(lista_provisoria) / len(lista_provisoria)
            
            cast_score_total = cast_score_total + actor_score
                        # finding if actor is a featured actor by checking list of star_ids
            if j in stars:
                binary_star = 1
            else:
                binary_star = 0
            actors_score_movie_temp.append(actor_score)
            binary_star_list_temp.append(binary_star)

            list_movie_bo_actor = [movie_id, imdb, meta, actor_score, director_score, writer_score, producer_score, budget, box_office, binary_star]
            
            if j not in actors_dictionary.keys():
                actors_dictionary[j] = [list_movie_bo_actor]
            else:
                actors_dictionary[j].append(list_movie_bo_actor)

            
#            list_movie_bo_actor = [movie_id, imdb, meta, actor_score, director_score, writer_score, producer_score, cinematography_score, score_productions_co, binary_star]
# =============================================================================
#             try:
#                 list_movie_bo_actor = [movie_id, imdb, meta,actor_score, cast_score_total, director_score, writer_score, producer_score, cinematography_score, star_score_list[0], star_score_list[1], star_score_list[2], score_productions_co]
# 
#             except IndexError:          
#                 if len(star_score_list) == 1:
#                     list_movie_bo_actor = [movie_id, imdb, meta, cast_score_total, director_score, writer_score, producer_score, cinematography_score, star_score_list[0], meta_average, meta_average, score_productions_co]
#                     star_1_list.append(star_score_list[0])
#                     star_2_list.append(meta_average)
#                     star_3_list.append(meta_average)
#                 elif len(star_score_list) == 2:
#                     list_movie_bo_actor = [movie_id, imdb, meta, cast_score_total, director_score, writer_score, producer_score, cinematography_score, star_score_list[0], star_score_list[1], meta_average, score_productions_co]
# 
#                 else:
#                     list_movie_bo_actor = [movie_id, imdb, meta, cast_score_total, director_score, writer_score, producer_score, cinematography_score, meta_average, meta_average, meta_average, score_productions_co]
# 
#     
#             
# =============================================================================      
        try:
            cast_score_total = cast_score_total / len_cast
        except ZeroDivisionError:
            cast_score_total = imdb_average
                
                
            ###########################################################################
            #here we are creating the list for a movie for an actor, this will be saved as a list for each actor in order to create the list of lists.
            #list_movie = [movie_id, b_o, imdb, meta, director_score, actor_score, writer_score, binary_star]
        try:
            list_movie_bo = [movie_id, imdb, meta, cast_score_total, director_score, writer_score, 
                             producer_score, cinematography_score, star_score_list[0], star_score_list[1], star_score_list[2], score_productions_co, budget, box_office]
            star_1_list = star_score_list[0]
            star_2_list = star_score_list[1]
            star_3_list = star_score_list[2]
            star_1_list1.append(star_1_list)
            star_2_list2.append(star_2_list)
            star_3_list3.append(star_3_list)
        except IndexError:          
            if len(star_score_list) == 1:
                list_movie_bo = [movie_id, imdb, meta, cast_score_total, director_score, writer_score, 
                                 producer_score, cinematography_score, star_score_list[0], meta_average, meta_average, score_productions_co, budget, box_office]
                star_1_list = star_score_list[0]
                star_2_list = meta_average
                star_3_list = meta_average
                star_1_list1.append(star_1_list)
                star_2_list2.append(star_2_list)
                star_3_list3.append(star_3_list)
            elif len(star_score_list) == 2:
                list_movie_bo = [movie_id, imdb, meta, cast_score_total, director_score, writer_score, 
                                 producer_score, cinematography_score, star_score_list[0], star_score_list[1], meta_average, score_productions_co, budget, box_office]
                star_1_list = star_score_list[0]
                star_2_list = star_score_list[1]
                star_3_list = meta_average
                star_1_list1.append(star_1_list)
                star_2_list2.append(star_2_list)
                star_3_list3.append(star_3_list)
            else:
                list_movie_bo = [movie_id, imdb, meta, cast_score_total, director_score, writer_score, 
                                 producer_score, cinematography_score, meta_average, meta_average, meta_average, score_productions_co, budget, box_office]
                star_1_list = meta_average
                star_2_list = meta_average
                star_3_list = meta_average
                star_1_list1.append(star_1_list)
                star_2_list2.append(star_2_list)
                star_3_list3.append(star_3_list)

                
        #         no_reviews_imdb  no_reviews_critics  no_reviews_users
                
        for i_2cast in range(len(cast)):
            list_movie_actor = [movie_id, imdb, meta, actors_score_movie_temp[i_2cast], cast_score_total, director_score, writer_score, producer_score, 
                             cinematography_score, star_1_list, star_2_list, star_3_list, score_productions_co, no_reviews_imdb, no_reviews_critics,
                             no_reviews_users, budget, box_office, binary_star_list_temp[i_2cast]]
#            dictionario_de_prueba.append(list_movie_actor)
            if cast[i_2cast] not in actors_dictionary2.keys():
                actors_dictionary_binary_values[cast[i_2cast]] = [binary_star_list_temp[i_2cast]]
                actors_dictionary2[cast[i_2cast]] = [list_movie_actor]
            else:
                actors_dictionary2[cast[i_2cast]].append(list_movie_actor)
                actors_dictionary_binary_values[cast[i_2cast]].append(binary_star_list_temp[i_2cast])

                
            #this save the list inside list of the movie information pertaining to actor

        #here i need to get info and pu it into the dataframe.
        star_list_test.append(star_score_list)
        dataset_list.append(list_movie_bo)
        cinematography_score_total_list.append(cinematography_score)
        director_score_total_list.append(director_score)
        writer_score_total_list.append(writer_score)
        producer_score_total_list.append(producer_score)
        cast_score_total_list.append(cast_score_total)    
        production_company_list.append(score_productions_co)
        
    
    
   
    data['cast_score'] = cast_score_total_list
    data['director_score'] = director_score_total_list
    data['writer_score'] = writer_score_total_list
    data['producer_score'] = producer_score_total_list
    data['cinematography_score'] = cinematography_score_total_list
    data['production_co_score'] = production_company_list
    data['star_1'] = star_1_list1
    data['star_2'] = star_2_list2
    data['star_3'] = star_3_list3
    
    #actor_dictionary_bo = actors_dictionary.copy()
    return actors_dictionary,actors_dictionary2, dataset_list, data, actors_dictionary_binary_values, production_co_movies_500k #, star_list_test, data_8k, index_wo_stars , data


actor_dictionary_6k,actor_dictionary2_6k, dataset_list_6k, data, actors_dictionary2_binary_values, production_co_movies_6k2 = dictionary_actor_bo_puntaje(dataset_6k, production_co_movies_500k)




#dataset_500k.to_csv(r'D:\Thesis\code\20-02-04\dataset_500k.csv') 
# =============================================================================
# import json
# json = json.dumps(actor_dictionary2_500k)
# f = open("actor_dictionary2_500k_20-02-04.json","w")
# f.write(json)
# f.close()
# 
# json = json.dumps(actors_dictionary2_binary_values)
# f = open("actors_dictionary2_binary_values_20-02-04.json","w")
# f.write(json)
# f.close()
# 
# 
# =============================================================================

# =============================================================================
# dataset_500k.to_csv(r'D:\Thesis\code\20-01-30\dataset_500k_31-01-20-0011.csv') 
# #need to save the dictionary with all the prodcutions company 
# import json
# json = json.dumps(production_co_movies_500k)
# f = open("production_co_movies_500k.json","w")
# f.write(json)
# f.close()
# =============================================================================




#dfObj = pd.DataFrame(dataset_list, columns = ['ID' , 'b_o', 'imdb', 'metacritic', 'cast_score', 'director_score', 'writer_score', 'producer_score', 'star_1', 'star_2', 'star_3', 'tercile']) 


# =============================================================================
# import json
# json = json.dumps(actor_dictionary_bo)
# f = open("actor_dictionary_bo.json","w")
# f.write(json)
# f.close() 
# =============================================================================

# =============================================================================
# cinematography_try = dataset['cinematography'][31]
# cinematography_try2 = re.findall("nm[0-9]{7}", cinematography_try)   
#         except TypeError :
#             cinema_errors.append(i_1)
#             cinematography_1 = []
# 
# type(dataset['cinematography'][70])
# =============================================================================





