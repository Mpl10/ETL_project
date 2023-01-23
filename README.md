
# Proyecto ETL

# Contenidos 

1. Objetivo
2. Punto de partida y fuentes de información
3. Estructura de carpetas
4. Archivos y datos
5. Tecnología


# 1. Objetivo

El objetivo de este proyecto es obtener la información que nos permita hacer un análisis completo de lo que comemos. Se utilizarán como referente principal recetas de cocina, y tendremos toda la información de interés relativa a las mismas:

- Coste de realización de la receta en base a información de un supermercado

- Información nutricional

- Tiempos de cocinado

- Cómo prepararlas

... etc


Todo esto nos permitirá elegir en base a los criterios que más nos interesen en cada momento y optimizar nuestros menús de cocina a todos los efectos!




# 2. Punto de partida y fuentes de información

## Punto de partida

El set de datos original que será el punto de partida del proyectos es el siguiente dataset de Kaggle : https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews?select=recipes.csv). En este archivo encontraremos información de más de 500.000 recetas así como las reviews de las mismas. Para el objetivo del proyecto se descartarán los comentarios y sólo se utilizará la información de las recetas.


## fuentes de información

Las fuentes de información que constituyen el proyecto son las siguientes:
1. Kaggle; el fichero csv nombrado como punto de partida
2. Food.com; la web de la que procede el archivo de Kaggle (https://www.food.com/)
3. Página web de supermercado; como ejemplo se ha seleccionado el Ahorramás (https://www.ahorramas.com/)




# 3. Estructura de carpetas 

- Data

    - 0_Others_data: Others es la carpeta en la que se almacenará aquella información que no es objeto de análisis en sí misma, sino que constituye un apoyo a las fuentes de información principales. (PE; listados de Url, de limpieza..)

    - 1_Initial_data: Información de partida (csv de Kaggle)

    - 2_Extracted_data: Los ficheros resultado de las extracciones

    - 3_Clean_data: Los csv depurados tras todas las transformaciones

- Notebooks; Archivos de extracción, limpieza y creación de la BBDD

- SRC; Documento con el pipeline



# 4. Archivos y datos

## otebooks:

1_Recipes_Extractor
2_Supermarket_Extractor
3_Recipes_Cleaning
4_Supermarket_Cleaning
5_Ingredients_Cleaning
6_MONGO_Database

## Data final:

1_INGREDIENTS_CLEAN.csv
2_RECIPES_CLEAN.csv
3_SUPERMARKET_CLEAN.csv

Los archivos contienen la siguiente información:

- 1_INGREDIENTS_CLEAN.csv

    - RecipeId: identificador de la receta

    - raciones: cuantas raciones o unidades se obtienen

    - etiqueta_raciones: especifica si son raciones o unidades

    - ingredientes: descripción del ingrediente completa

    - id_ingrediente: descripción del ingrediente limpia (vincula con los productos del supermercado)

    - cantidad: cantidad de ingredientes


- 2_RECIPES_CLEAN.csv

    - RecipeId: identificador de la receta

    - Nombre: nombre de la receta

    - AggregatedRating: calificación de la receta en la web

    - ReviewCount: conteo de comentarios

    - Información nutricional: desglosada en 10 columnas (Calories, FatContent, SaturatedFatContent CholesterolContent, SodiumContent, CarbohydrateContent, FiberContent,SugarContent,ProteinContent)

    - Categoria_receta: clasificación del tipo de receta

    - Instrucciones

    - Prep_time: tiempo de preparación

    - Total_time: tiempo de cocinado total



- 3_SUPERMARKET_CLEAN.csv

    - producto_desc: descripción de producto (nombre completo de la web)

    - precio_ud: precio unitario

    - precio_por_medida: percio por unidad de medida

    - unidad_de_medida: unidad de medida del precio anterior

    - descuento

    - categoria_1: clasificación del supermercado

    - categoria_2: clasificación del supermercado

    - categoria_3: clasificación del supermercado

    - categoria_4: clasificación del supermercado

    - id_ingrediente: identificador de ingrediente (poductos de alimentación con base a las recetas)

    - Ratio_coincidencia: el ratio de coincidencia del id_ingrediente con producto_desc

    - gramos_unit: peso en gramos de los productos




# 4. 5. Tecnología

Las librerías utilizadas son las siguientes:

import pandas as pd
import numpy as np
import random
from random import randint
import string
import requests
from tqdm import tqdm
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import warnings
import re
import datetime
import matplotlib.pyplot as plt
from fuzzywuzzy import process, fuzz
import pickle
from deep_translator import GoogleTranslator
import sys 
import support as sp 
import pymongo

También encontramos funciones de información y limpieza en el archivo .py de la carpeta SRC

La obtención de información para el enriquecimiento de los datos iniciales se ha realizado utilizando Selenium y BeautifulSoup.
El almacenamiento posterior de los resultados se ha realizado en una BBDD Mongo.











