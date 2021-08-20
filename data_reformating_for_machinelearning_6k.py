# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 09:32:48 2019
Aca voy a crear el DataFrame para los actores y las peliculas, hay dos cosas que necesito buscar,  
peliculas 000 0 y peliculas  000 1 ya que solo estoy viendo cuando un actor pasa de ser 'not features'  a 'featured'
eventualmente podria usar una lista mas grande de actore, considerando que podria extender el tema de featured a mas actores,  de 3 a 5.
game changer, 
eso lo haria cuando termine esta parte y la parte donde estoy tratando de predecir box Office, 
tambien podria tratar de ver los datos de 


Ahora puedo usar esto en machine learning...              
@author: rabbitindamoon
"""
import pandas as pd

#to upload saved dictionary.
# # to open pickel load...
# with open('actor_dictionary_2020-01-21.p', 'rb') as fp:
#     data = pickle.load(fp)  

def data_reformating_for_machinelearning_6k(actors_dictionary):           
    # here we are creating a list of lists for all actors.
    #each row contains 2 entries ine with the actors id and the other with all the movie information creates and carreer trajectory of actor.
    dictlist = []
    dict_list1 = []
    dict_list2 = []
    actors_dictionary_10plus = {}

    actors_data_000_0_list = []
    actors_data_111_0_list = []    
    actors_data_001_0_list = []  
    actors_data_011_0_list = [] 
    actors_data_110_0_list = []
    actors_data_010_0_list = []
    actors_data_100_0_list = []
    actors_data_101_0_list = []     
    
    actors_data_xxx_x_list = []

    actors_data_000_1_list = []
    actors_data_111_1_list = []    
    actors_data_001_1_list = []  
    actors_data_011_1_list = [] 
    actors_data_110_1_list = []
    actors_data_010_1_list = []
    actors_data_100_1_list = []
    actors_data_101_1_list = []    
#    actors_data_4_1_list = []
#    actors_data_5_1_list = []

    #moving the data from dictionary to lisst in order to put information in dataframe.
    for key, value in actors_dictionary.items():
        temp = [key, value]
        dictlist.append(temp)
        dict_list1.append(value)
        dict_list2.append(key)
    #Now  I need to create the format for the data with many columns with the information needed. and grabbing the last value as the predictor either 0 or 1.
    # firstly we only need the actors with 10 movies or more.
    actors_dictlist_plus10 = []
    actor_id_plus10 = []
    for i in  range(len(dictlist)):
        length = len(dictlist[i][1])
        if length>3:
            actors_dictionary_10plus[dict_list2[i]] = dictlist[i][1]
            actors_dictlist_plus10.append(dictlist[i][1])
            actor_id_plus10.append(dict_list2[i])
    
    #grabing 3 films at the time and saving the inrformation regarding the film.
    column_names =  ['movie_id', 'imdb', 'meta', 'actors_score', 'cast_score_total', 
                 'director_score', 'writer_score', 'producer_score', 'cinematography_score', 'star_1_list', 
                 'star_2_list', 'star_3_list', 'score_productions_co', 'no_reviews_imdb', 'no_reviews_critics',
                 'no_reviews_users',  'budget', 'box_office','binary_star_list_temp[i_2cast]']
    for i in range(len(actors_dictlist_plus10)):       
        j_2 = 1
        j_3 = 2
        j_4 = 3      
        for j_1 in range(len(actors_dictlist_plus10[i])-3):
            actor_id = [actor_id_plus10[i]]
            movie_1 = actors_dictlist_plus10[i][j_1][1:]
            id_1 = [actors_dictlist_plus10[i][j_1][0]]
            binary_1 = actors_dictlist_plus10[i][j_1][18]
            movie_2 = actors_dictlist_plus10[i][j_2][1:]
            id_2 = [actors_dictlist_plus10[i][j_2][0]]
            binary_2 = actors_dictlist_plus10[i][j_2][18]
            movie_3 = actors_dictlist_plus10[i][j_3][1:]
            id_3 =[ actors_dictlist_plus10[i][j_3][0]]
            binary_3 = actors_dictlist_plus10[i][j_3][18]
            movie_4 = [actors_dictlist_plus10[i][j_4][18]]
            id_4 = [actors_dictlist_plus10[i][j_4][0]]
            binary_4 = actors_dictlist_plus10[i][j_4][18]
#            temp_list = movie_1 + movie_2 + movie_3 + movie_4
            if(binary_1 == 0 and binary_2 == 0 and binary_3 == 0 and binary_4 == 0):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_000_0_list.append(temp_list_2)
            elif(binary_1 == 1 and binary_2 == 1 and binary_3 == 1 and binary_4 == 0):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_111_0_list.append(temp_list_2)
            elif(binary_1 == 0 and binary_2 == 0 and binary_3 == 1 and binary_4 == 0):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_001_0_list.append(temp_list_2)
            elif(binary_1 == 0 and binary_2 == 1 and binary_3 == 1 and binary_4 == 0):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_011_0_list.append(temp_list_2)
            elif(binary_1 == 1 and binary_2 == 1 and binary_3 == 0 and binary_4 == 0):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_110_0_list.append(temp_list_2)
            elif(binary_1 == 0 and binary_2 == 1 and binary_3 == 0 and binary_4 == 0):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_010_0_list.append(temp_list_2)
            elif(binary_1 == 1 and binary_2 == 0 and binary_3 == 0 and binary_4 == 0):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_100_0_list.append(temp_list_2)
            elif(binary_1 == 1 and binary_2 == 0 and binary_3 == 1 and binary_4 == 0):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_101_0_list.append(temp_list_2)

                
            elif(binary_1 == 0 and binary_2 == 0 and binary_3 == 0 and binary_4 == 1):
                temp_list_1 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_000_1_list.append(temp_list_1)
                
            elif(binary_1 == 1 and binary_2 == 1 and binary_3 == 1 and binary_4 == 1):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_111_1_list.append(temp_list_2)  
                
            elif(binary_1 == 0 and binary_2 == 0 and binary_3 == 1 and binary_4 == 1):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_001_1_list.append(temp_list_2)  
                
            elif(binary_1 == 0 and binary_2 == 1 and binary_3 == 1 and binary_4 == 1):
                temp_list_2 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_011_1_list.append(temp_list_2)   
                
            elif(binary_1 == 1 and binary_2 == 1 and binary_3 == 0 and binary_4 == 1):
                temp_list_1 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_110_1_list.append(temp_list_1)
                
            elif(binary_1 == 0 and binary_2 == 1 and binary_3 == 0 and binary_4 == 1):
                temp_list_1 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_010_1_list.append(temp_list_1)

            elif(binary_1 == 1 and binary_2 == 0 and binary_3 == 0 and binary_4 == 1):
                temp_list_1 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_100_1_list.append(temp_list_1)
                
            elif(binary_1 == 1 and binary_2 == 0 and binary_3 == 1 and binary_4 == 1):
                temp_list_1 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_101_1_list.append(temp_list_1)

            else:
                temp_list_3 = actor_id + id_1 + id_2 + id_3 + id_4 + movie_1 + movie_2 + movie_3 + movie_4
                actors_data_xxx_x_list.append(temp_list_3)
            #saving tem data into list to make a dataframe after.
#            actors_data_3_1_list.append(temp_list)
            #updating indices to go one more
            j_2 = j_2 + 1
            j_3 =  j_3 + 1
            j_4 = j_4 + 1
          
# =============================================================================
#     for i in range(len(actors_dictlist_plus10)):
#         j_2 = 1
#         j_3 = 2
#         j_4 = 3
#         j_5 = 4
#     #grabbing 4 films at the time and saving the information ragarding the filsm            
#         for j_1 in range(len(actors_dictlist_plus10[i])-4):            
#             actor_id = [actor_id_plus10[i]]
#             movie_1 = actors_dictlist_plus10[i][j_1][1:]
#             id_1 = [actors_dictlist_plus10[i][j_1][0]]
#             movie_2 = actors_dictlist_plus10[i][j_2][1:]
#             id_2 = [actors_dictlist_plus10[i][j_2][0]]
#             movie_3 = actors_dictlist_plus10[i][j_3][1:]
#             id_3 = [actors_dictlist_plus10[i][j_3][0]]
#             movie_4 = actors_dictlist_plus10[i][j_4][1:]
#             id_4 = [actors_dictlist_plus10[i][j_4][0]]
#             movie_5 = [actors_dictlist_plus10[i][j_5][16]]
#             id_5 = [actors_dictlist_plus10[i][j_5][0]]
# #            temp_list = movie_1 + movie_2 + movie_3 + movie_4
#             temp_list2 = actor_id + id_1 + id_2 + id_3 + id_4 + id_5 + movie_1 + movie_2 + movie_3 + movie_4 + movie_5
#             #saving tem data into list to make a dataframe after.
# 
#             actors_data_4_1_list.append(temp_list2)
#             #updating indices to go one more
#             j_2 = j_2 + 1
#             j_3 =  j_3 + 1
#             j_4 = j_4 + 1
#             j_5 = j_5 + 1
#  
#     for i in range(len(actors_dictlist_plus10)):
#         j_2 = 1
#         j_3 = 2
#         j_4 = 3
#         j_5 = 4
#         j_6= 5             
#         for j_1 in range(len(actors_dictlist_plus10[i])-5):
#             actor_id = [actor_id_plus10[i]]
#             movie_1 = actors_dictlist_plus10[i][j_1][1:]
#             id_1 = [actors_dictlist_plus10[i][j_1][0]]
#             movie_2 = actors_dictlist_plus10[i][j_2][1:]
#             id_2 = [actors_dictlist_plus10[i][j_2][0]]
#             movie_3 = actors_dictlist_plus10[i][j_3][1:]
#             id_3 = [actors_dictlist_plus10[i][j_3][0]]
#             movie_4 = actors_dictlist_plus10[i][j_4][1:]
#             id_4 = [actors_dictlist_plus10[i][j_4][0]]
#             movie_5 = actors_dictlist_plus10[i][j_5][1:]
#             id_5 = [actors_dictlist_plus10[i][j_5][0]]
#             movie_6 = [actors_dictlist_plus10[i][j_6][16]]
#             id_6 = [actors_dictlist_plus10[i][j_6][0]]
# #            temp_list = movie_1 + movie_2 + movie_3 + movie_4
#             temp_list3 = actor_id + id_1 + id_2 + id_3 + id_4 + id_5 + id_6 + movie_1 + movie_2 + movie_3 + movie_4 + movie_5 + movie_6
#             #saving tem data into list to make a dataframe after.
#             actors_data_5_1_list.append(temp_list3)
#             #updating indices to go one more
#             j_2 = j_2 + 1
#             j_3 =  j_3 + 1
#             j_4 = j_4 + 1
#             j_5 = j_5 + 1
#             j_6 = j_6 +1  
# =============================================================================
            


            
    column_names =  ['movie_id', 'imdb', 'meta', 'actors_score', 'cast_score_total', 
                 'director_score', 'writer_score', 'producer_score', 'cinematography_score', 'star_1_list', 
                 'star_2_list', 'star_3_list', 'score_productions_co', 'no_reviews_imdb', 'no_reviews_critics',
                 'no_reviews_users',  'budget', 'box_office', 'binary_star_list_temp[i_2cast]']
#[movie_id, year, b_o, imdb, meta, actor_score, cast_score, director_score, writer_score, producer_score, cinematography_score, star_1, star_2, star_3, binary_star]


    
    actors_data_xxx_x_pd = pd.DataFrame(actors_data_xxx_x_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_000_0_pd = pd.DataFrame(actors_data_000_0_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4'])
    actors_data_111_0_pd = pd.DataFrame(actors_data_111_0_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_001_0_pd = pd.DataFrame(actors_data_001_0_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_011_0_pd = pd.DataFrame(actors_data_011_0_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_110_0_pd = pd.DataFrame(actors_data_110_0_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_010_0_pd = pd.DataFrame(actors_data_010_0_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_100_0_pd = pd.DataFrame(actors_data_100_0_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4'])   
    actors_data_101_0_pd = pd.DataFrame(actors_data_101_0_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 









    actors_data_000_1_pd = pd.DataFrame(actors_data_000_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4'])
    
    actors_data_111_1_pd = pd.DataFrame(actors_data_111_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 

    actors_data_001_1_pd = pd.DataFrame(actors_data_001_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_011_1_pd = pd.DataFrame(actors_data_011_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_110_1_pd = pd.DataFrame(actors_data_110_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_010_1_pd = pd.DataFrame(actors_data_010_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 
    actors_data_100_1_pd = pd.DataFrame(actors_data_100_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4'])   
    actors_data_101_1_pd = pd.DataFrame(actors_data_101_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4',
                                                                   'IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'score_productions_co_1', 'no_reviews_imdb_1', 'no_reviews_critics_1', 'no_reviews_users_1', 'budget_1', 'box_office_1', 'feature_binary_1', 
                                                                   'IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'score_productions_co_2', 'no_reviews_imdb_2', 'no_reviews_critics_2', 'no_reviews_users_2', 'budget_2', 'box_office_2', 'feature_binary_2',
                                                                   'IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'score_productions_co_3', 'no_reviews_imdb_3', 'no_reviews_critics_3', 'no_reviews_users_3', 'budget_3', 'box_office_3', 'feature_binary_3',                                                                    
                                                                   'feature_binary_4']) 

         
    


           
# =============================================================================
#     actors_data_4_1_pd =pd.DataFrame(actors_data_4_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4', 'movie_id_5',
#                                                                    'year_1', 'b.o_1','IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'feature_binary_1', 
#                                                                    'year_2', 'b.o_2','IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'feature_binary_2',
#                                                                    'year_3', 'b.o_3','IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'feature_binary_3',
#                                                                    'year_4', 'b.o_4','IMDb_4','meta_4','actor_score_4','cast_score_4','director_score_4', 'writer_score_4', 'producer_score_4','cinematography_score_4', 'star_4_1', 'star_4_2', 'star_4_3', 'feature_binary_4',                                                    
#                                                                    'feature_binary_5'])
# 
#     actors_data_5_1_pd =pd.DataFrame(actors_data_5_1_list,columns=['actor_id', 'movie_id_1', 'movie_id_2', 'movie_id_3', 'movie_id_4', 'movie_id_5', 'movie_id_6',
#                                                                    'year_1', 'b.o_1','IMDb_1','meta_1','actor_score_1','cast_score_1','director_score_1', 'writer_score_1', 'producer_score_1','cinematography_score_1', 'star_1_1', 'star_1_2', 'star_1_3', 'feature_binary_1', 
#                                                                    'year_2', 'b.o_2','IMDb_2','meta_2','actor_score_2','cast_score_2','director_score_2', 'writer_score_2', 'producer_score_2','cinematography_score_2', 'star_2_1', 'star_2_2', 'star_2_3', 'feature_binary_2',
#                                                                    'year_3', 'b.o_3','IMDb_3','meta_3','actor_score_3','cast_score_3','director_score_3', 'writer_score_3', 'producer_score_3','cinematography_score_3', 'star_3_1', 'star_3_2', 'star_3_3', 'feature_binary_3',
#                                                                    'year_4', 'b.o_4','IMDb_4','meta_4','actor_score_4','cast_score_4','director_score_4', 'writer_score_4', 'producer_score_4','cinematography_score_4', 'star_4_1', 'star_4_2', 'star_4_3', 'feature_binary_4',
#                                                                    'year_5', 'b.o_5','IMDb_5','meta_5','actor_score_5','cast_score_5','director_score_5', 'writer_score_5', 'producer_score_5','cinematography_score_5', 'star_5_1', 'star_5_2', 'star_5_3', 'feature_binary_5',
#                                                                    'feature_binary_6'])
# =============================================================================
            
    return  actors_data_000_1_pd,  actors_data_xxx_x_pd, actors_data_000_0_pd, actors_data_111_0_pd, actors_data_001_0_pd, actors_data_011_0_pd, actors_data_110_0_pd, actors_data_010_0_pd, actors_data_100_0_pd, actors_data_101_0_pd, actors_data_111_1_pd, actors_data_001_1_pd, actors_data_011_1_pd, actors_data_110_1_pd, actors_data_010_1_pd, actors_data_100_1_pd, actors_data_101_1_pd

actors_data_000_1_pd,  actors_data_xxx_x_pd, actors_data_000_0_pd, actors_data_111_0_pd, actors_data_001_0_pd, actors_data_011_0_pd, actors_data_110_0_pd, actors_data_010_0_pd, actors_data_100_0_pd, actors_data_101_0_pd, actors_data_111_1_pd, actors_data_001_1_pd, actors_data_011_1_pd, actors_data_110_1_pd, actors_data_010_1_pd, actors_data_100_1_pd, actors_data_101_1_pd = data_reformating_for_machinelearning_6k(actor_dictionary2_6k)

#actors_data_000_1_pd.to_csv(r'D:\Thesis\code\20-02-04\actors_data_000_1_pd.csv')
#actors_data_000_0_pd.to_csv(r'D:\Thesis\code\20-02-04\actors_data_000_0_pd.csv')
#actors_data_xxx_x_pd.to_csv(r'D:\Thesis\code\20-02-04\actors_data_xxx_x_pd.csv')


actors_data_000_0_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_000_0_pd.csv')
actors_data_111_0_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_111_0_pd.csv')
actors_data_001_0_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_001_0_pd.csv')
actors_data_011_0_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_011_0_pd.csv')
actors_data_110_0_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_110_0_pd.csv')
actors_data_010_0_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_010_0_pd.csv')
actors_data_100_0_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_100_0_pd.csv')
actors_data_101_0_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_101_0_pd.csv')

actors_data_000_1_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_000_1_pd.csv')
actors_data_111_1_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_111_1_pd.csv')
actors_data_001_1_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_001_1_pd.csv')
actors_data_011_1_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_011_1_pd.csv')
actors_data_110_1_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_110_1_pd.csv')
actors_data_010_1_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_010_1_pd.csv')
actors_data_100_1_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_100_1_pd.csv')
actors_data_101_1_pd.to_csv(r'D:\Thesis\code\20-02-10\actors_data_101_1_pd.csv')


# =============================================================================
#importances.to_csv(r'D:\Thesis\code\20-02-10\6kMovies_budget_and_bo_83120_dataPoints_xxx_x\importances.csv')
#
# with open(r'D:\Thesis\code\20-02-10\6kMovies_budget_and_bo_83120_dataPoints_xxx_x\importances.txt', 'w') as f:
#     for item in importances:
#         f.write("%s\n" % item)
# =============================================================================

#8.468051 millones en total
#365421 solo los que van de 000 a 1
#5759791 los que van de 000
