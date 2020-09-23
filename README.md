# Criador-de-tabelas-verdade
Projeto criado como parte do portfólio da matéria "Fundamentos Matemáticos da Computação"

# Explicação do código

O código inicia-se declarando variáveis globais e pedindo pelo input da sentença a ser interpretada. A função das variáveis será explicada no decorrer do código. A declaração de algumas variáveis nessa sessão é redundante, mas por quesito de organização eu as declarei de qualquer forma.

A próxima sessão utiliza uma variável temporária para filtrar a string “sComp” (sentença completa) e padronizar seu espaçamento. Uma string “A&B” será feita em “ A & B” por exemplo. Note que os espaços extra serão removidos na próxima sessão.

A próxima sessão usa o método “split()” para gerar uma lista com os caracteres individuais da sentença completa e adiciona em uma nova lista “sBase” (sentenças base) as sentenças atômicas. Durante o processo é usada a variável “nC” para contar o número de colunas a serem geradas (uma para cada sentença atômica).

A próxima sessão usa a biblioteca “math” para calcular o número de linhas a serem criadas, sendo este dois elevado ao número de colunas (sem contar o cabeçalho com os nomes das colunas).

A próxima sessão é responsável por popular a tabela-verdade e por armazenar os valores lógicos de cada célula em uma lista. O processo começa com a criação de um valor de alternância máximo “va” inicialmente sendo igual ao número de linhas, mas que para cada iteração cai pela metade. Esse valor em conjunto com o valor-verdade “vv” é responsável por rastrear o próximo valor a ser salvo. Quando o valor de alternância atual “cva” se iguala ao valor de alternância máximo da iteração o valor-verdade se inverte e o valor de alternância atual retorna para zero. No fim os valores-verdade são salvos em duas listas: “ls”, uma lista temporária usada para popular a tabela-verdade, e “lsd”, uma lista temporária usada para salvar o valor lógico como um dicionário (contendo o nome da coluna e seu valor) em uma lista “llCol” (lista de linhas e colunas).

Para cada iteração, a próxima sessão usa a lista “llCol” para traduzir as sentenças atômicas em seus valores-verdade da linha em questão e traduz os conectivos “&”, “v” e “~” para a linguagem python. Depois disso ela usa da função “exec()” para calcular o valor-verdade da linha e o salva em “lF”.

A sessão final popula a última coluna da tabela com os valores armazenados e a imprime como saída para o usuário.

# Comentários e limitações

Devido a necessidade de dinamicamente criar funções eu usei o método “exec()”, um método bastante inseguro e que é raramente usado pela necessidade da filtração de input do usuário, que pode ser danoso sem ela.

Devido a necessidade de dinamicamente alocar variáveis eu usei dicionários contendo nomes como chaves e booleanos como valores, abordagem que também é bastante inusual.

Devido a maneira que é feita a filtração, todas as sentenças atômicas devem ser constituídas de apenas um caractere alfanumérico, excluindo a letra “v” minúscula, que é reservada como operador lógico.

O programa não tem suporte aos operadores “v”, “→”, “↔, “↑” e “↓”, mas esses podem ser usados se traduzidos para a forma de suas respectivas definições. Exemplos:

•	A v B como (A & ~B)v(~A & B)

•	A → B como ~A v B

•	A ↔ B como (~A v B)&(~B v A)

•	A ↑ B como ~(A & B)

•	A ↓ B como ~(A v B)
