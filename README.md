# Parcial 1 - PG2 (Ejercicio 1)

:card_index: Carrera: *Sistemas Informaticos*

:notebook: Materia: *Programación 2* 

:bust_in_silhouette: Nombre Completo: *Jorge Daniel Choque Ferrufino*

:calendar: Fecha: *8 de Mayo del 2025*

## INFORMACION DEL EJERCICIO 1

Este repositorio contiene la implementación de un componente en Python basado en los principios de Programación Orientada a Objetos que realiza conversiones de unidades de distancia.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

- `conversor_basico.py`: Contiene la clase base `ConversorBasico` con métodos protegidos para realizar conversiones genéricas.
- `conversor_distancia.py`: Contiene la clase `ConversorDistancia` que hereda de `ConversorBasico` e implementa métodos específicos de conversión.
- `main.py`: Archivo principal que demuestra el funcionamiento de las clases.
- `README.md`: Documentación del proyecto.

## Funcionalidades

El proyecto implementa las siguientes funcionalidades:

1. **Clase ConversorBasico**:
   - Método protegido `_conversion_generica` para realizar conversiones entre unidades
   - Variables protegidas para almacenar información sobre la conversión
   - Método protegido `_mostrar_resultados` para mostrar los resultados de la conversión

2. **Clase ConversorDistancia**:
   - Hereda de `ConversorBasico`
   - Implementa métodos específicos: 
     - `metros_a_centimetros`: Convierte metros a centímetros
     - `centimetros_a_kilometros`: Convierte centímetros a kilómetros

## Cómo ejecutar

Para ejecutar el programa, simplemente ejecute el archivo `main.py`:

```
python main.py
```
