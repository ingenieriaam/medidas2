# Agilent 9320A

## Mnemonicos
Muchos comandos tienen una forma larga y otra corta: use cualquiera (una combinación de los dos no está permitida). El Comando FREQuency por ejemplo:

    * forma corta: FREQ
    * forma larga :FREQUENCY 
 
SCPI no distingue entre mayúsculas y minúsculas, por lo que la fREquEncy es tan válida como FREQUENCY, pero FREQ  y FREQUENCY son las únicas formas válidas del comando FRECUENCIA.

Las letras mayúsculas indican la forma corta de la palabra clave. Las letras minúsculas indican la forma larga de la palabra clave.
___
## Puntuación
 * Una barra vertical "|" dicta la elección de un elemento de una lista. Por ejemplo: <A> | <B> indica que A o B pueden ser seleccionado, pero no ambos.
 * Los corchetes "[]" indican que los elementos son Opcionales.
 * Los corchetes angulares "<>" indican una variable de usuario.
 *  Un signo de interrogación "?" después de un comando del subsistema indica que el comando es una consulta. La información devuelta en <valor> varía su formato según el tipo de campo.
 ___

## Separador
* Los dos puntos ":" separan palabras claves en niveles, en general, se omite antes de la primer palabra.
* Un espacio separa una palabra clave y un parámetro, así como un parámetro y una unidad.

___

## Parameter Type
The command parameters introduced in this manual include 6 types: Bool, Keyword, Integer, Consecutive
Real Number, Discrete and ASCII String.

## Bool
The parameter could be "OFF", "ON", "0" or "1". For example,

```sh
:DISPlay:ANNotation:CLOCk[:STATe] OFF|ON|0|1
```

## Keyword
The parameter could be any of the values listed. For example,
```sh
:DISPlay:AFUnction:POSition BOTTom|CENTer|TOP
```
The parameter could be "BOTTom", "CENTer" or "TOP".

## Integer
Unless otherwise noted, the parameter can be any integer within the effective value range. Note that do not
set the parameter to a decimal; otherwise errors will occur. For example,

```sh
:DISPlay:BRIGhtness <integer>
```
<integer> can be set to any integer between 0 and 10.

## Consecutive Real Number
The parameter could be any value within the effective value range according to the accuracy requirement
(by default, there are 6 digits after the decimal points). For example,
```sh
:CALCulate:BANDwidth:NDB <rel_ampl>
```
<rel_ampl> can be set to any real number between -100 and 100.

## Discrete
The parameter could only be one of the specified values and these values are discontinuous. For example,
```sh
:CALCulate:MARKer<n>:MAXimum:MAX
```
<n> could only be set to 1, 2, 3 or 4.

## ASCII String
The parameter should be the combinations of ASCII characters. For example,
```sh
:SYSTem:DATE <year>,<month>,<day>
```
The parameter is a string in the specified date format.