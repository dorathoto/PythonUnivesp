# Python Univesp

> Último update dos códigos: 28/05/2019 08:51
Necessário Python 3.6 ou superior

Faça o download [instalando o Git](https://git-scm.com/downloads "instalando o Git") e depois executando o comando:
`    git clone https://github.com/dorathoto/PythonUnivesp.git`


# 8º Bimestre
Folder: *(8_Bimestre)*
## Estatística: [Link](https://github.com/dorathoto/PythonUnivesp/tree/master/8_Bimestre)
**Semana 6**
Semana6_v1.py - Utilizando Scipy e Matplotlib para fazer distribuição normal.

**Semana 5**

**Semana 4**
> Estatística descritiva

[Semana4-v2.py](https://github.com/dorathoto/PythonUnivesp/blob/master/8_Bimestre/Semana4-v2.py) - Utilizando Pandas para s², s, moda, variancia, etc.
Foi executado com Spyder por ser uma IDE específica para analise de Dados
[Ajuda com spyder](http://mundoia.com.br/tutorial/analise-exploratoria-de-dados-extraindo-insights-do-fifa-18/)

**Semana 3**


**Semana 2**
[probabilidade-v3.py](https://github.com/dorathoto/PythonUnivesp/blob/master/8_Bimestre/probabilidade-v3.py) - Semana 2 - Mesmo exemplo  probabilidade-v1.py com Variância, Esperança


[probabilidade-v1.py](https://github.com/dorathoto/PythonUnivesp/blob/master/8_Bimestre/probabilidade-v1.py "probabilidade-v1.py") - Probabilidade básica, interessante notar como funciona o número aleatório em programação que não é exatamente aleatório, só com uma amostragem grande ele fornece dados interessante.
    execute: python probabilidade-v1.py 

[dist_probabilidades.ipynb](https://github.com/dorathoto/PythonUnivesp/blob/master/8_Bimestre/dist_probabilidades.ipynb "dist_probabilidades.ipynb") - Exercício de apoio 2 da semana 2 de Estatística, apresentado na forma de um notebook e visualização via biblioteca `matplotlib.pyplot`.


## Instalações Elétricas:
Os notebook misturam caraterísticas de um IDE e do console interativo, permitindo rodar pequenos scripts e observar na hora o resultado. O GitHub tem a capacidade de visualizar o notebook de forma nativa, por tanto, o que você vê na página do GitHub é o que você veria no Jupyter Lab, por exemplo. A diferencia é que ele aparece de forma estática. Se você quiser mexer com o código, pode experimentar com um notebook no navegador acessando [https://jupyter.org/](https://jupyter.org/), copiando e colando o conteudo das celdas, executando com "Run". O próprio notebook apresentará um breve instrutivo sobre o funcionamento do notebook online e instruções de instalação se quiser usar offline.

###  Semana 3
[transformadores.ipynb](https://github.com/dorathoto/PythonUnivesp/blob/master/8_Bimestre/transformadores.ipynb "Modelo de Transfomador Ideal") - Instalações Elétricas - Transformador Ideal. Abrir e executar no [Jupyter Notebook](https://jupyter.org/).

[instalacoes_eletricas1.ipynb](https://github.com/dorathoto/PythonUnivesp/blob/master/8_Bimestre/instalacoes_eletricas1.ipynb "Circuito Monofásico") - Instalações Elétricas - Circuito monofásico. Abrir e executar no [Jupyter Notebook](https://jupyter.org/).
 


------------


# 6º Bimestre
> PlayList no Youtube da diciplina: [Link](https://www.youtube.com/watch?v=OXPKrTqAXuw&list=PLxI8Can9yAHebCIYfnSq7xoITrKOQpI0p)
Folder: 6_Bimestre

Material de Python para ajuda em Cálculo numérico.
Cada arquivo vem precedido da semana, ex:

    S1_ -> significa Semana 1
    S2_ -> significa Semana 2
OBS: Esse material não tenta ser uma aula de Python para isso faça um curso:
[Link com diversos cursos](https://gist.github.com/aledruetta/9ea5996de69045087114d42ba230a587)
*Recomendo o Python para Zumbis*

## Semana 2

Equações algébricas e transcendentes. Métodos para encontrar raízes.

- [S2_Bissecao.py](https://github.com/dorathoto/PythonUnivesp/blob/master/S2_Bissecao.py) -> Método da bisseção ou Bolzano [Link fonte algoritimo](https://www.ufrgs.br/reamat/CalculoNumerico/livro-py/sdeduv-metodo_da_bissecao.html) 
- Método das cordas
- Método de Newton
- Método da interação Linear
- [S2_Secante.py](https://github.com/dorathoto/PythonUnivesp/blob/master/S2_Secante.py) -> Método da Secante - [fonte](https://www.ufrgs.br/reamat/CalculoNumerico/livro-py/sdeduv-metodo_das_secantes.html) - 
*Fonte para os algoritmos:* http://www.ufjf.br/flavia_bastos/files/2009/06/aula_raizes.pdf
 
| comando       | Link documentação                                                                     |
| ------------- | ------------------------------------------------------------------------------------- |
| float         | [Link inglês](https://docs.python.org/3/library/functions.html?highlight=float#float) |
| abs           | [Link inglês](https://docs.python.org/3/library/functions.html?highlight=abs#abs)     |
| try/Exception | [Link](https://pythonhelp.wordpress.com/2012/09/14/tratamento-de-excecoes/)           |

## Semana 1
**Conversão de bases, binário em decimal e vice-versa.**
*Usando funções internas do Python para conversão:* [S1_DecimalToBinario.py](https://github.com/dorathoto/PythonUnivesp/blob/master/S1_DecimalToBinario.py)
Utilizando algoritmo para conversão: [S1_funcDecimalBinario.py](https://github.com/dorathoto/PythonUnivesp/blob/master/S1_funcDecimalBinario.py)

----------------
**Exercícios propostos:**
- Converter decimal em binário, binário em decimal. *usando funções internas e a classe S1_funcDecimalBinario.py*
- Converter base 2, base 10 em base 8 (octogonal) *- usando funções interna do python*
- Modificar a funcDecimalBinario removendo código típicos de Python e deixando em uma lógica mais igual a Univesp

***Comandos a serem aprendidos em python para essa semana:***



| Comando    | Link documentação                                                                           |
| ---------- | ------------------------------------------------------------------------------------------- |
| bin()      | [Link](https://docs.python.org/3/library/functions.html?highlight=abs#bin)                  |
| formatspec | [Link](https://docs.python.org/3/library/string.html#formatspec)                            |
| def:       | [Link](https://wiki.python.org.br/PrincipiosFuncionais#Definindo_Fun.2BAOcA9Q-es_em_Python) |
| while:     | [Link](http://excript.com/python/while-else-python.html)                                    |
