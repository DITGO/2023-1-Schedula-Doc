# Plano de Custos

## 1. Introdução

<p align="justify" style="text-indent: 20px">O objetivo do Plano de Custos proposto é estabelecer uma previsão orçamentária precisa para o projeto Schedula, incluindo todos os custos associados aos recursos necessários para sua execução. Esse plano é fundamental para garantir que o projeto seja executado dentro do orçamento previsto e para evitar possíveis surpresas financeiras ao longo do caminho. Portanto, é essencial que todos os custos sejam devidamente estimados e documentados, para que se possa ter uma visão clara dos gastos e garantir a viabilidade financeira do projeto.</p>

<p align="justify" style="text-indent: 20px">Dentre os principais aspectos que serão analisados neste plano de custos estão: o custo médio de um aluno em uma universidade federal, os custos fixos, os custos relacionados ao tempo de desenvolvimento definido e custos adicionais, sendo que este último pode ser decorrente de imprevistos, ajustes de escopo, entre outros fatores.</p>


## 2. Custo médio de um aluno em uma universidade federal

<p align="justify" style="text-indent: 20px">De acordo com a matéria do jornal da unesp, em 2019 [<a href=./#10-referencia>1</a>], o custo anual de um aluno em universidades federais é de <b>R$ 40.900,00</b>. Com essa informação, é possível calcular o custo de um aluno por mês: <b>R$ 3.408,33</b>, por semana: <b>R$ 852,08</b>, por dia (considerando que o projeto será desenvolvido ao longo dos 7 dias da semana): <b>R$ 121,73</b> e por hora (levando em consideração que em média gasta-se 6h por dia com a faculdade): <b>R$ 20,29</b>.</p>

<p align="justify" style="text-indent: 20px">Levando em conta que serão gastas 10h por semana para as disciplinas de EPS/MDS, o custo por semana, por aluno, para essas disciplinas é de <b>R$ 202,88</b>. Como a equipe possui 17 integrantes, por semana a equipe custará <b>R$ 3.448,96</b>. Para o projeto de 15 semanas, o custo com pessoal será de <b>R$ 51.734,40</b>. Para o MVP, que será desenvolvido em 10 semanas, o custo será de <b>R$ 34.489,60</b>.</p>


## 3. Custos por equipamento

<p align="justify" style="text-indent: 20px">Levando em conta que o projeto é realizado em computador, é consenso que cada aluno necessita de uma unidade para si, pois é inviável que os desenvolvimento seja feito ao mesmo tempo em conjunto em uma só máquina ou poucas unidades, já que muitas necessidades do projeto podem ser feitas em paralelo, e se levar em conta o tempo em si, essa necessidade é até obrigatória.</p>
<p align="justify" style="text-indent: 20px">Assim, foi feita a escolha de um computador específico com base em uma pesquisa de mercado, levando em contas os requisitos necessários para desenvolver o projeto de maneira eficiente, mas que não sejam desnecessariamente custosos demais. Dessa maneira a equipe levantou os seguintes requisitos de hardware para o computador: <b>Processador Intel Core i3, 8 GB de memória RAM e SSD de 256 GB</b>. O equipamento escolhido tem custo na data de 05/05/2023 de <b>R$ 2.868,00</b> no site da fabricante, que pode ser visualizado <a href="https://www.hp.com/br-pt/shop/notebook-hp-256-g8-78l98la.html">aqui</a>.</p>
<p align="justify" style="text-indent: 20px">O valor total desse custo, multiplicado pela quantidade de alunos, 17, é de cerca de <b>R$ 48.756,00</b>.</p>

## 4. Custos com internet

<p align="justify" style="text-indent: 20px">Para poder contribuir com o projeto remotamente, é necessário ter uma conexão com internet, e para uma conexão de qualidade, evitando problemas de velocidade, é necessário pelo menos 50 Mbps. Fazendo pesquisas [<a href=./#10-referencia>2</a>], [<a href=./#10-referencia>3</a>], foi possível constatar que, no DF, a média de valores de planos para internet acima de 50 Mbps é de <b>R$ 90,00</b> por mês.</p>
<p align="justify" style="text-indent: 20px">Levando em consideração que o projeto será desenvolvido nos meses Abril, Maio, Junho e Julho, um único desenvolvedor irá gastar para o projeto <b>R$ 360,00</b> com internet.</p>
<p align="justify" style="text-indent: 20px">Este valor, multiplicado pela quantidade de alunos, 17, é <b>R$ 6120,00</b>.</p>

## 5. Custos com energia

<p align="justify" style="text-indent: 20px">Utilizando como base que um computador consome, em uma hora, 5kWh/mês [<a href=./#10-referencia>4</a>], e a tarifa de energia no DF é de R$0,81 kWh [<a href=./#10-referencia>5</a>], iremos considerar que cada membro dedicará para a disciplina 10 horas semanais. Multiplicando a tarifa pelo consumo mensal têm-se o valor de <b>R$ 4,05</b> por pessoa, por mês.</p>
<p align="justify" style="text-indent: 20px">Logo, ao longo dos 4 meses do projeto, um desenvolvedor terá o gasto de <b>R$ 16,20</b> com energia dedicada ao projeto.</p>
<p align="justify" style="text-indent: 20px">Este valor, multiplicado pela quantidade de alunos, 17, é <b>R$ 275,40</b>.</p>

## 6. Custos com hospedagem

<p align="justify" style="text-indent: 20px">A hospedagem do Schedula para o ambiente de produção foi realizada no <a href='heroku.com'>Heroku</a>, uma plataforma que oferece serviços pagos, mas também concede créditos estudantis ao associar a conta ao Github Student[<a href=./#10-referencia>7</a>]. No entanto, nos deparamos com a limitação de que esses créditos fornecem apenas um desconto máximo de 13 dólares por mês, e que essa quantia não foi suficiente para cobrir o valor total do consumo dos microsserviços do Schedula.</p>
<p align="justify" style="text-indent: 20px">Ao dividirmos o valor entre os 17 membros do grupo, o total individual ficou em <b>R$10,45</b>. Durante a reunião interna (planning) do Schedula em 07/06/23, foi questionado se esse montante seria inviável para alguém, mas todos concordaram que seria possível arcar com ele.</p>
<p align="justify" style="text-indent: 20px">Esse valor corresponde à hospedagem do mês de Maio e a cobrança se repetirá nos meses de Junho e Julho, que estão dentro do semestre, mas que ainda não foram debitados em dólares na conta dos estudantes. Além disso, a equipe decidiu informar o professor Hilmer sobre essas despesas durante a aula em 13/06/23.</p>

## 7. Planilha

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQaJZhNjvmjiZMV7ZtQAhq12H-o__7WrhTwNoBjrpmmSAENPBS3udDJegV8NBoUiwYFhUTNy8ApLTFo/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false"
        width='100%'
        height='500px'
        style='min-width: 640px; min-height: 500px; background-color: #f4f4f4; border: 1px solid #efefef'
        sandbox='allow-same-origin allow-scripts allow-modals allow-popups allow-popups-to-escape-sandbox'>
</iframe>

## 8. Agile EVM - Earned Value Management

<p align="justify" style="text-indent: 20px">O Agile EVM (Earned Value Management)[<a href=./#10-referencia>6</a>] é uma adaptação da técnica de gerenciamento do valor agregado para projetos ágeis. Ele é usado para monitorar e controlar o desempenho de projetos ágeis, fornecendo uma visão objetiva do valor do trabalho realizado em relação ao valor planejado.</p>

<p align="justify" style="text-indent: 20px">Agile EVM combina princípios ágeis, como a entrega incremental de valor, com a abordagem tradicional do valor agregado do EVM. Ele utiliza três métricas principais:</p>

- Valor Planejado (Planned Value - PV): Representa o valor planejado para as atividades concluídas em um determinado momento. Corresponde ao valor estimado do trabalho planejado para a sprint ou para o projeto como um todo.

- Valor Ganho (Earned Value - EV): Refere-se ao valor do trabalho concluído e aceito até o momento. É uma medida objetiva do progresso alcançado em relação ao valor planejado.

- Custo Real (Actual Cost - AC): Representa o custo real incorrido para executar as atividades até o momento.

<p align="justify" style="text-indent: 20px">Com base nessas métricas, o Agile EVM calcula duas principais medidas de desempenho:</p>

- Índice de Desempenho de Valor Ganho (Earned Value Performance Index - EVPI): É a relação entre o valor ganho (EV) e o valor gasto (AC). Ele indica se o trabalho está sendo concluído de acordo com o orçamento.

- Índice de Desempenho de Custo (Cost Performance Index - CPI): É a relação entre o valor ganho (EV) e o valor planejado (PV). Ele indica se o trabalho está sendo concluído dentro do orçamento planejado.

<p align="justify" style="text-indent: 20px">Essas métricas e índices ajudam os gerentes de projeto e as equipes ágeis a avaliar o desempenho do projeto, identificar possíveis desvios em relação ao planejado e tomar medidas corretivas, se necessário. Eles fornecem uma visão objetiva do progresso do projeto, permitindo que a equipe tome decisões informadas sobre ajustes no escopo, cronograma e custos, a fim de manter o projeto no caminho certo para alcançar seus objetivos.</p>

<p align="justify" style="text-indent: 20px">A equipe Schedula realizou o levantamento desses índices para cada sprint do projeto, e toda essa análise pode ser acessada <a href='https://docs.google.com/spreadsheets/d/e/2PACX-1vTf-XCyaUycOe-57oOX3AhqMNJQ3rjs2RxASj2tfT8iD6ZaG1WDOvViSU4eSI2uFnxT45LltfjWjp54/pubhtml?widget=true&amp;headers=false'>aqui</a>, ou visualizada abaixo:</p>

<iframe style="width: 100%; height: 500px" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTf-XCyaUycOe-57oOX3AhqMNJQ3rjs2RxASj2tfT8iD6ZaG1WDOvViSU4eSI2uFnxT45LltfjWjp54/pubhtml?widget=true&amp;headers=false"></iframe>

## 9. Versionamento

<center>

|    Data    | Versão |            Descrição                   |        Autor        |
| :--------: | :----: | :------------------------------------: | :-----------------: |
|  04/05/23  |  1.0   |   Documento inicial                    |     Ian Ferreira    |
|  05/05/23  |  1.1   |   Adicionando custo por aluno          |     Ítalo Serra     |
|  05/05/23  |  1.2   |   Adicionando custo por equipamento    | Guilherme de Morais |
|  19/05/23  |  1.3   |   Adicionando planilha, alterando referências    | Álvaro Leles |
|  26/05/23  |  1.4   |   Adicionando custos referentes a equipamento e internet    | Álvaro Leles |
|  03/06/23  |  1.5   |   Adicionando custos referentes a energia   | Álvaro Leles |
|  03/07/23  |  1.6   |   Documento revisado   | Ian Ferreira e Ítalo Vinícius |
|  08/07/23  |  1.7   |   Adicionando tabela de EVM  |  Álvaro, Gabriel B. e Guilherme |
|  09/07/23  |  1.8   |   Adicionando custos com hospedagem |  Guilherme de Morais |

</center>

## 10. Referência

> [1] Cobrança de mensalidade não é a solução para o financiamento da universidade pública. Disponível em: https://jornal.unesp.br/2022/06/08/cobranca-de-mensalidade-nao-e-a-solucao-para-o-financiamento-da-universidade-publica. Acessado em 05 mai. 2023.

> [2] Melhor escolha internet em brasília. Disponível em: https://melhorescolha.com/internet-banda-larga/brasilia-df. Acessado em 26 mai. 2023.

> [3] Melhor Internet em Brasília - DF. Disponível em: https://www.minhaconexao.com.br/ranking/df/brasilia. Acessado em 26 mai. 2023.

> [4] DICAS PARA ECONOMIA DE ENERGIA AO USAR O COMPUTADOR. Disponível em: http://www.mpgo.mp.br/portal/conteudo/dicas-para-economia-de-energia-ao-usar-o-computador. Acessado em 02 jun. 2023.

> [5] Conta de luz fica mais cara no DF. Disponível em: https://g1.globo.com/df/distrito-federal/noticia/2021/10/22/conta-de-luz-fica-mais-cara-no-df-a-partir-desta-sexta-feira-22.ghtml. Acessado em 02 jun. 2023.

> [6] AgileEVM – Earned Value Management in Scrum Projects. Tamara S.; Brent B.; Thomas B. Proceedings of AGILE 2006 Conference. 2006.

> [7] Heroku for GitHub Students. Disponível em: https://www.heroku.com/github-students. Acessado em 08 jul. 2023.