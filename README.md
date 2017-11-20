# Clústering de documentos a partir de métricas de  similitud basado en Big Data utilizando la tecnologia spark

Este proyecto consiste en el diseño e implementación de una aplicación con tecnología y modelo de programación distribuida en Big Data, específicamente con tecnología Hadoop y Spark que permita agrupar (clustering) un conjunto de documentos utilizando el algoritmo de k–means y una métrica de similaridad entre documentos.

Para cumplir con dicho objetivo se desarrollo un programa en python el cual inicialemente crea un vectorTF-IDF (que me indica cuantas veces se repite una palabra por documento) para todos los documentos y se lo pasa al algoritmo k-means cuyo objetivo es categorizar los documentos procesados en subgrupos segun su similitud. El resultado es almacenado en un archivo en el file System.

El codigo se corre en spark, el cual se encarga de repartir automaticamente los documentos en cada uno de los nodos que posee.


## Ejecución
Para la ejecución del algoritmo se requiere:

* Tener el ambiente de spark configurado


Una vez cumplidos los requisitos unicamente se debe ejecutar el siguiente comando:

spark-submit --master yarn --depoy-mode client <nombre archivo>
