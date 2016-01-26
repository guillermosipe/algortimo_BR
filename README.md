# Implementación del algoritmo BR

Objetivo: Obtener los testores típicos de una matriz de incidencia.
Publicación: [BR: A New Method for Computing All Typical Testors](http://link.springer.com/chapter/10.1007%2F978-3-642-10268-4_50#page-1).
## Ejecución

```shell
python main.py
```
### Imprimir pasos
Se puede imprimir los pasos que sigue el algoritmo para obtener los testores típicos mediante la siguiente opción:

```shell
python main.py -i Y
python main.py -imprimir_pasos Y
```

### Seleccionar matriz de prueba
Se cuenta con las siguientes matrices de prueba:

Matriz "articulo_br" [BR: A New Method for Computing All Typical Testors](http://link.springer.com/chapter/10.1007%2F978-3-642-10268-4_50#page-1).
```
      [1,0,0,0,0,0,0,1,0]
      [0,1,0,0,0,1,0,0,0]
      [0,0,0,1,1,1,1,0,1]
      [0,0,1,0,1,0,0,1,1]
      [1,0,0,0,1,0,0,0,1]
```
Matriz "n2"
```
      [1,1,1,0,0]
      [1,1,0,0,1]
      [1,0,1,1,0]
      [1,0,1,0,1]
```
Matriz "s"
```
      [1,0,0,0,1,0]
      [1,1,0,0,0,1]
      [0,0,1,0,0,1]
      [1,0,0,1,0,1]
```
Matriz "identidad_basica"
```
      [0,0,0,1]
      [1,0,0,0]
      [0,0,1,0]
      [0,1,0,0]
```
Para hacer uso de alguna matriz en especifico:
```shell
python main.py -m ['articulo_br','identidad_basica','n2', 's']
python main.py -matriz ['articulo_br','identidad_basica','n2', 's']
```

### Cargar matriz externa
Se puede cargar una matriz externa a través de un archivo JSON con la siguiente estructura:

```json
{
  "matrix":[[1,1,0,0,0,0],
            [0,0,1,0,1,1],
            [0,1,0,1,1,1]]
}
```

La ejecución sería la siguiente:
```shell
python main.py -f matriz.json
python main.py --file matriz.json
```
