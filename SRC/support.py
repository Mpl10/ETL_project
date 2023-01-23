import pandas as pd
import numpy as np
import re
import string
from deep_translator import GoogleTranslator



class Dataframe_info:
    def  __init__(self,dataframe):
        self.df = dataframe
        
    def info_resumen(self):
        return self.df.info()
    
    def descripcion_df_obj(self):
        return self.df.describe(include = "object").T

    def descripcion_df_num(self):
        return self.df.describe().T                
     
    def muestra_filas(self,num_rows):
        return self.df.head(num_rows)
    
    def campos_nulos_num(self):
        nulos=self.df.isnull().sum()
        return nulos[nulos != 0]
    
    def campos_nulos_porc(self):
        nulos=(self.df.isnull().sum() * 100) / df_inicial.shape[0]
        return nulos[nulos != 0]
    
    def duplicados(self):
        return self.df.duplicated().sum()
    
    def columnas(self):
        return self.df.columns
    
    def valores_columna(self, columna):
        return self.df[columna].value_counts()
    

class Limpieza_columnas_general:
    def  __init__(self,df,col):
        self.df = df
        self.col= col 
        
        '''
        Clase que agrupa aquellas funciones que pueden ser aplicadas las columnas del Dataframe. Argumentos:
            df= nombre del dataframe
            col= nombre de la columna (entre comillas) 
        '''     
        
    def reemplazo_valores_nulos(self, string):
        '''
        Reemplaza los valores nulos de una columna por el valor elegido. Argumentos:
            De la clase (Limpieza_columnas_general)= df y col
            De la función=  string (valor de reemplazo)
        '''
        self.df[self.col].fillna(string, inplace = True)
    
    def reemplazo_string(self,string_1,string_2):
        '''
        Sustituye el string seleccionado como primer argumento por el segundo. Argumentos:
            De la clase (Limpieza_columnas_general)= df y col
            De la función=  string_1 (string a reemplazar)
                            string_2 (string de reemplazo)
        '''
        self.df[self.col] = self.df[self.col].apply(lambda x: x.replace(string_1, string_2))
        
    def series_a_string(self):
        '''
        Transforma el formato de una columna con contenido object(panda.Series) a string. Argumentos:
            De la clase (Limpieza_columnas_general)= df y col  
        '''
        self.df[self.col] = pd.Series(self.df[self.col], dtype="string")
        
    def conversion_formato_columna(self, formato):
        '''
        Convierte el formato de la columna al tipo que se indique. Argumentos:
            De la clase (Limpieza_columnas_general)= df y col
            De la función=  formato (entre comillas)
        '''
        self.df[self.col]=self.df[self.col].astype(formato)
              
    def borrado_columna(self):
        '''
        Elimina una columna del dataframe. Argumentos:
            De la clase (Limpieza_columnas_general)= df y col
        '''
        self.df.drop([self.col], axis=1, inplace=True)
        
    def busqueda_patrones_regex(self,col1,patron):
        '''
        Localiza el patron elegido en la columna de origen y lo devuelve en una nueva columna.Argumentos:
        De la clase (Limpieza_columnas_general)= df y col (columna origen)
        De la función=  col1 (nueva columna)
                            patron (patron regex)
        '''
        self.df[col1] = self.df[self.col].apply(lambda x: re.findall(patron, x))
        
    def reemplazo_patrones_regex(self,col1,patron, reemplazo):
        '''
        Localiza el patron elegido en la columna de origen y lo sutituye por el reemplazo indicado en una nueva columna.Argumentos:
        De la clase (Limpieza_columnas_general)= df y col (columna origen)
        De la función=  col1 (nueva columna)
                        patron (patron regex)
                        reemplazo (string por el que se quiere sustituir)
        '''
        self.df[col1] = self.df[self.col].apply(lambda x: re.sub(patron,reemplazo, x))
        
    def funcion_traduccion_en_es(self, col1):
        '''
        Esta función traduce del inglés al español el contenido de una columna. Argumentos:
        De la clase (Limpieza_columnas_general)= df y col (columna origen)
        De la función=  col1 (nueva columna)                    
        '''
        traductor = GoogleTranslator(source='en', target='es')
    
        self.df[col1] = self.df[self.col].apply(lambda x: traductor.translate(x))



class Limpieza_dataframe_general:
    def  __init__(self,df):
        self.df = df
        '''
        Clase que agrupa aquellas funciones que pueden ser aplicadas a todo el Dataframe. Argumentos:
            df= nombre del dataframe
        '''
        
    def limpieza_espacios_cabeceras(self, caracter):
        '''
        Reemplaza los espacios de las cabeceras por un caracter. Argumentos:
            De la clase (Limpieza_dataframe)= df
            De la función= caracter (string por el que queremos reemplazar los espacios en las columnas)   
        '''
        self.df.columns = [column.replace(" ", caracter) for column in self.df.columns]
        
    def limpieza_espacios_columnas_str(self):
        '''
        Selecciona las columnas tipo objeto y elimina los espacios al inicio y al final de los string. Argumentos:
            De la clase (Limpieza_dataframe)= df
        '''
        df_obj =self.df.select_dtypes(['object'])
        self.df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())

    def eliminar_filas_nan_arg_columnas(self, subset_list):
        '''
        Elimina todas aquellas filas del Dtaframe que contienen nulos las columnas especificadas. Argumentos:
            De la clase (Limpieza_dataframe)= df
            De la función=  subset_list (columnas que se utilizan como criterio de eliminación. Formato; ["col1","col2"...])   
        '''
        self.df.dropna(subset=subset_list, how='all',inplace = True)
        
    def resetear_indice(self):
        '''
        Resetea el índice y elimina el anterior. Argumentos:
            De la clase (Limpieza_dataframe)= df
        '''
        self.df.reset_index(drop=True, inplace=True)
  


