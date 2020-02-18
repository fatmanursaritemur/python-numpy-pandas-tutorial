# -*- coding: utf-8 -*-

import pandas as pd

films=pd.read_csv("imdb-1000.csv")
print(films)
print(films.columns)
print(films.head())
print(films.tail())
print(films["title"])
print("*************************")
print(films.actors_list)
print(films.actors_list.head())
print("*************************")
#print(films[(films["star_rating"]>8.5)&(films["star_rating"]<8.9)])
print(films.query("star_rating >= 8.3 & star_rating <=9.0 "))
