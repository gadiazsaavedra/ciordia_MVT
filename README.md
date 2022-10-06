# ciordia_MVT
1.- falto crear views.py a nivel proyecto. Slide 25, clase 17. En el mismo archivo import HttpResponse, slide 26, clase 17. Iniciar la 1ra vista, slide 27 clase 17.
2.- En urls.py (nivel Proyecto) importar saludo con  template desde views.py (nivel App) slide 28, clase 17
3.- En models.py definir solo la clase Familiar 
4.- En views.py importar solo lo necesario . En la funcion saludo con template, agregar variable template con loader.get_template indicando la plantilla a usar. Luego definir los datos de cada familiar.
5.- Crear folder templates con el correspondiente archivo html.
6.- En models.py al definir la clase Familiar, el atributo edad NO es DateField() deberia ser IntegerField()


