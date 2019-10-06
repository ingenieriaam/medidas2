# Medidas2

## [presentación](https://ingenieriaam.github.io/medidas2) 

usar: 
```sh
	git branch --set-upstream-to=origin gh-pages
```

para compilación se requiere:
```sh
	npm install
```

para compilar:
```sh
	npm start
```

para imprimir, agregar previo al cierre del head:
```html
	<script>
	var link = document.createElement( 'link' );
	link.rel = 'stylesheet';
	link.type = 'text/css';
	link.href = window.location.search.match( /print-pdf/gi ) ? 'css/print/pdf.css' : 'css/print/paper.css';
	document.getElementsByTagName( 'head' )[0].appendChild( link );
	</script>
```
luego, abrir el link: http://localhost:8000/?print-pdf

## Control de equipos por Python

### Equipos a controlar:
 * [analizador de espectro Agilent 9320A](https://www.keysight.com/en/pd-817002-pn-N9320A/rf-spectrum-analyzer-9-khz-3-ghz?cc=US&lc=eng) - no pudo controlarse
 * [analizador de espectro Rigol DSA815](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-06f0/1/-/-/-/-/dsa800programpdf.pdf) - actualmente en proceso 
 * [generador de señal Agilent 9310A](https://www.keysight.com/en/pdx-x202262-pn-N9310A/rf-signal-generator-9-khz-to-3-ghz?cc=AR&lc=eng)
 * [medidor de potencia](https://www.anritsu.com/en-US/test-measurement/products/ml2487b) y [sensor](https://www.bellnw.com/manufacturer/Anritsu/MA2472D.htm)
___

### instalar dependencias
- pip install -U pyvisa
- pip install -U pyvisa-py
- pip install pyserial
- pip install pyusb
- agilent requiere io [library](https://www.keysight.com/main/software.jspx?ckey=2175637&nid=-33330.977662&cc=eng&lc=eng) - ni asi anda

---

a chequear [pyvisa para keysight](http://na.support.keysight.com/fieldfox/help/Programming/webhelp/Examples/Python_Example.htm)

### pasos basicos

Ver si se reconoce al equipo

```py
>>> import visa
>>> rm = visa.ResourceManager()
>>> print(rm.list_resources())
>>> a = rm.list_resources()
>>> print(a[0])
	USB0::6833::2400::DSA8A194601374::0::INSTR
>>> inst = rm.open_resource(a[0])
>>> print(inst.query("*IDN?"))
	Rigol Technologies,DSA815,DSA8A194601374,00.01.18.00.02

```
