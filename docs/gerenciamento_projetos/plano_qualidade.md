# Plano de Qualidade

## 1. Introdução

A ISO/IEC 25010 define que um plano de qualidade é o pilar de uma evolução da qualidade de um produto. Um modelo desses consegue determinar quais características serão analisadas na hora de considerar os avanços feitos nas propriedades de um produto de software.

## 2. Objetivo

Este documento tem como objetivo tratar das métricas analisadas quando falamos em qualidade, além de técnicas que contemplem seus requisitos durante o andar do projeto. Dada essa observação, tal documento terá como foco:

- Observar as métricas de qualidade utilizadas pela equipe;
- Elicitar as ferramentas utilizadas para avaliação de qualidade;
- Descorrer sobre os testes e as metodologias utilizadas.

Neste documento, está registrado como estabelecemos os padrões de qualidades durante o período de desenvolvimento e planejamento da equipe.

## 3. Métricas de Qualidade

Durante o projeto, a equipe se baseou nas métricas retornadas do [SonarCloud](https://docs.sonarcloud.io/digging-deeper/metric-definitions/), sendo elas:

- Complexidade: o cálculo de complexidade que é calculado baseado no números de caminhos pelo código. 
- Duplicações: o número de blocos de linhas duplicados, baseado na densidade do código.
- Problemas: o número de problemas que apareceram no código.
- Manutenabilidade: quantidade de "code smells", assim como a nota na escala de manutenabilidade. Tal escala se dá nominalmente (A até E), mas reflete o resultado de uma nota numérica.
- "Portões de Qualidade": limites de métricas de qualidade a fim de evitar taxas muito inferiores às esperadas.
- Confiabilidade: métrica que reflete a confiabilidade do projeto, considerando quantidade de bugs apresentados e sua escala de nota de confiabilidade.
- Segurança: trata da segurança do código, a fim de evitar problemas de vulnerabilidade.
- Tamanho: número de classes, comentários no código, a fim de se entender a porcentagem do código total que está comentada.
- Testes: cobertura de testes, sua rapidez de execução e testes unitários.

Tais métricas são responsáveis para se entender melhor a qualidade do código — funcionam como guias, para que se busque melhorias e novas alterações para que a qualidade do código aumente.

- No decorrer do desenvolvimento, a equipe buscou entender algumas dessas métricas e evoluir de forma com que atingissem pelo menos o limite de valor estipulado por padrão do [SonarCloud](https://docs.sonarcloud.io/improving/quality-gates/):

### 3.1 Requisitos de aprovação de qualidade

<center>

**Métricas** | **Limite de valor** 
:---------------:                     | :-----------:
**Duplicação**                        |  Até 3%
**Testes passando**                   |  Acima de 0
**Vulnerabilidades de Segurança**     |  0  
**Cobertura de testes**               |  Acima de 80%
**Classificação de Confiabilidade**   |  A     
**Classificação de Manutenabilidade** |  A

</center>

## 4. Controle de versão

O controle de versão, também conhecido como controle de fonte, é a prática de rastrear e gerenciar alterações em um código de software. Ele é realizado por meio de sistemas de controle de versão, que são ferramentas de software que auxiliam as equipes de software a gerenciar as mudanças no código ao longo do tempo. Esses sistemas são especialmente úteis para equipes de DevOps, pois ajudam a reduzir o tempo de desenvolvimento e aumentar as implementações bem-sucedidas, mantendo o controle de qualidade do código-fonte.

O controle de versão protege o código-fonte contra erros humanos e evita a degradação do software. Ele também ajuda as equipes a lidarem com o trabalho simultâneo, evitando conflitos entre as alterações feitas por diferentes desenvolvedores. Além disso, o controle de versão facilita o teste e o desenvolvimento contínuos, permitindo que o software seja testado antes de ser considerado confiável.

### 4.1 Padrões adotados como metodologia de controle de versão para manutenção da qualidade

A equipe Schedula adota os seguintes padrões de controle de versão para que a qualidade do código seja mantida de maneira linear, buscando assim reduzir a quantidade de erros não rastreáveis e manter os índices das métricas de qualidade dentro do padrão exigido:

1. Para desenvolver a solução de uma issue, o desenvolvedor deve criar uma branch do código atual a partir da develop, com o seguinte padrão: "#*[número da issue]*_*[nome resumido da issue]*". 

    Exemplo: a issue #45 tem o título de "[US13] - Exportar relatórios". O desenvolvedor deve então criar uma branch com o nome *"#45_exportar_relatorios"*.

2. A cada *commit* nessa branch, o desenvolvedor deve utilizar o padrão de *commits* com mensagens semânticas, em que há uso dos prefixos *feat* (quando o *commit* implementa uma nova feature no produto), *fix* (quando o *commit* corrige algum erro identificado pela equipe), dentre outros.

3. Ao finalizar o desenvolvimento de código-fonte que solucione uma issue, o desenvolvedor deve abrir um *pull request* respeitando o template configurado no nosso repositório, incluindo plano de testes.

4. O desenvolvedor deve aguardar a esteira de CI retornar os índices extraídos para esse *pull request*. Em caso de o Quality Gate do Sonarcloud falhar, o desenvolvedor deve realizar *commits* nesse *pull request* corrigindo o código-fonte para que ele passe nos requisitos de aprovação de qualidade ditos anteriormente.


## 5. Ferramentas

No início do projeto, algumas configurações foram feitas a fim de exigir a utilização de certas ferramentas para que uma padronização fosse implementada e a qualidade esperada fosse atingida.

Na hora de realizar um "git commit" ou dar um "git push" no [front-end](https://github.com/fga-eps-mds/2023-1-schedula-front), por exemplo, certas ferramentas eram acionadas a fim de garantir uma mínima qualidade no código — sem erros. Algumas ferramentas como:

- [ESLint](https://eslint.org/) - framework que retorna possíveis erros.
- [Type-check](https://www.npmjs.com/package/type-check) - framework que também analisa e retorna possíveis erros.
- [Vitest](https://vitest.dev/) - framework de testes unitários que utilizamos para o front-end.

Além dessas, outras foram utilizadas com o mesmo propósito da melhoria de qualidade.

- [SonarCloud](https://docs.sonarcloud.io/) - como já elicitado.
- [Jest](https://jestjs.io/pt-BR/) - framework de testes que utilizamos para o back-end.

</center>

## 6. Versionamento

<center>

|    Data    | Versão |            Descrição             |      Autor      |
| :--------: | :----: | :------------------------------: | :-------------: |
|  10/07/23  |  1.0   |  Criação do documento de plano de qualidade | Gabriel Bonifácio e Guilherme Richter |
|  11/07/23  |  1.1   |  Revisão do documento | Ian Ferreira |

</center>

## 7. Referências

> [1] ISO/IEC 25010. Disponível em: <https://iso25000.com/index.php/en/iso-25000-standards/iso-25010>. Acesso em: 10 de julho de 2023.

> [2] Metric Definitions. Disponível em: <https://docs.sonarcloud.io/digging-deeper/metric-definitions/>. Acesso em: 10 de julho de 2023.

> [3] O que é controle de versão?. Disponível em: <https://www.atlassian.com/br/git/tutorials/what-is-version-control>. Acesso em: 10 de julho de 2023.

> [4] Conventional Commits. Disponível em: <https://www.conventionalcommits.org/en/v1.0.0/>. Acesso em: 10 de julho de 2023.

> [5] A importância de um plano de qualidade de software e a estratégia de testes. Disponível em: <https://www.linkedin.com/pulse/import%C3%A2ncia-de-um-plano-qualidade-software-e-testes-farias-ctfl/?originalSubdomain=pt>. Acesso em: 10 de julho de 2023.