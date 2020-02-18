# -*- coding: utf-8 -*-

import pandas as pd

films=pd.read_csv("imdb-1000.csv")
films=films.drop("content_rating",axis=1)
films=films.drop("duration",axis=1)

films=films.drop(1,axis=0)

rowsToDrop = [3,42,13,976]
films=films.drop(rowsToDrop,axis=0)
print(films)