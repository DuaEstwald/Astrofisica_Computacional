# Astrofisica_Computacional
Repositorio de los códigos desarrollados para la asignatura de Astrofísica Computacional.


Podemos encontrar aquí todos los códigos desarrolados para la asignatura de Astrofisica Computacional. 

Tenemos cinco scripts principales: 


· parameters.py: código desarrollado para implementar los parámetros que cogen como input los códigos onlyLENS.py y onlyfits.py.

· onlyLENS.py: utilizado para el desarrollo de lentes gravitacionales con una guente gaussiana. El código está desarrollado con la idea de que se le puedan implementar fácilmente otro tipo de lentes. 

· onlyfits.py: su utilidad es la misma que en el código anterior, lo único que cambia es el hecho de que la fuente es una imagen tipo jpg. Debido a la diferencia al tratar estos archivos como fuentes, su tratamiento ha implementado en un script a parte.

· magmap_alcock.py: donde se presentan las causticas y los mapas de magnificación de las microlentes. En este caso se hace uso de la microlente LMC-9 que aparece en el artículo de Alcock 2000. El código está desarrollado para implementar cualquier microlente en el script auxiliar llamado: microlensing.py. Donde por ahora sólo encontramos LMC-9.

· qmic.py: código desarrollado para la simulación de quasar microlensing. 
