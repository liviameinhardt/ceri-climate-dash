PD-00068-0071/2025

RESILIÊNCIA  DA  TRANSMISSÃO  DE  ENERGIA
ELÉTRICA A EVENTOS CLIMÁTICOS EXTREMOS

PRODUTO 1:

RELATÓRIO DE REVISÃO DE MODELAGEM CLIMÁTICA ISA
ENERGIA BRASIL

[02/2026]

Sumário Executivo

O  projeto  de  Pesquisa,  Desenvolvimento  e  Inovação  (PDI)  "Resiliência  da  Transmissão  de

Energia  Elétrica  a  Eventos  Climáticos  Extremos,  registrado  sob  o  número  PD-00068-

0071/2025, tem o objetivo de aprimorar os esforços de aprimoramento da resiliência climática

das linhas de  transmissão da ISA ENERGIA BRASIL. Mais especificamente, o projeto visa

antecipar  riscos  e  contribuir  para  a  avaliação  da  vulnerabilidade  das  linhas  e  subestações,

considerando os impactos em seus serviços. Entre as principais contribuições a serem geradas

por este projeto, podem ser destacadas:

•  Análise  Custo-Benefício  (CBA)  e  do  Custo  Total  Global  de  investimentos  em

resiliência a eventos climáticos extremos;

•  Dashbord de gestão de ameaças a climáticas extremas;

•  Proposição de melhorias regulatórias para incentivar investimentos eficientes.

Este relatório constitui o Produto 1 do projeto apresentado acima. O objetivo central é realizar

uma avaliação da modelagem climática e da metodologia de análise de riscos utilizada pela ISA

ENERGIA BRASIL, propondo aprimoramentos técnicos e científicos.

Escopo e Cenários Adotados

A  análise  baseia-se  em  documentos  e  metodologias  desenvolvidas  anteriormente  pela

consultoria WayCarbon:

•  Ameaças  Analisadas:  O  estudo  contempla  sete  fenômenos:  tempestades  (descargas

atmosféricas), incêndios florestais, inundações fluviais, ventos (alterações nos padrões

de ventos), deslizamentos, temperatura máxima (ondas de calor) e aumento do nível do

mar.

•  Horizontes  Temporais:  São  considerados  períodos  de  curto  (2030),  médio  (2040)  e

longo prazo (2050), comparados a um cenário histórico (1995-2014).

•  Modelagem  Climática:  Utiliza  os  cenários  de  emissões  do  IPCC  (CMIP6):  SSP1-

2.6, SSP2-4.5 e SSP3-7.0.

Página 2

Principais Achados

Embora  o  projeto  inicial  apresente  clareza  conceitual,  o  relatório  identifica  pontos  de

aprimoramento:

•  Rigor  Estatístico:  O  cálculo  de  probabilidades  utiliza  termos  não  consagrados  (ex:

"valor  bruto")  e  não  explicita  as  funções  de  densidade  de  probabilidade  (PDFs),

dificultando a reprodutibilidade.

•  Falta  de  Normalização:  Indicadores  somam  variáveis  com  unidades  incompatíveis

(mm, m/s e dias), gerando possíveis distorções.

•  Abordagem  Metodológica:  A  metodologia  atual  é  predominantemente  descritiva  e

pode  ser  enriquecida  por  uma  modelagem  estocástica  que  permita  simular  falhas

específicas em ativos.

•  Omissão  de  fenômenos  de  larga  escala:  Não  são  considerados  modos  de

variabilidade de larga escala, como El Niño e La Niña, que modulam diretamente os

extremos no Brasil.

Oportunidades de Melhoria e Bases de Dados

Sugere-se o enriquecimento das análises através da integração de novas fontes:

•  Dados  Nacionais  e  Internacionais:  Uso  de  bases  do  INMET  (BDMEP),  INPE

(CPTEC), ANA (SNIRH), ERA5, NASA e NOAA.

•  Evolução Metodológica: Transição para um  modelo "prescritivo", validando índices

com ocorrências reais de danos e desligamentos.

•  Deve-se  reconhecer  que  há  uma  limitação  severa  na  disponibilidade  de  dados

climáticos e meteorológicos no Brasil e que ela deve ser enfrentada de forma inovadora

com o objetivo de suprir esta lacuna.

Conclusão

A metodologia revisada é considerada uma base inicial, mas para ampliar o seu valor do ponto

de  vista  operacional,  é  recomendável  refinar  o  tratamento  estatístico,  aplicar  técnicas  de

downscaling,  correção  de  viés  (bias  correction),  entre  outras,  nos  modelos  climáticos,  por

exemplo.

Página 3

ÍNDICE

1  Introdução ao PDI ......................................................................................... 5

2  Introdução ao Produto 1 ............................................................................. 10

2.1  Documentos analisados ............................................................................................... 10

3  Abordagem para a estruturação do plano de ação climático da ISA
ENERGIA BRASIL .......................................................................................... 15

3.1  Visão geral ................................................................................................................... 15

3.2  Ameaças climáticas ..................................................................................................... 15

3.3  Cenários e horizontes temporais .................................................................................. 16

3.4  Cálculo das probabilidades .......................................................................................... 17

3.5  Análise por ameaça ...................................................................................................... 19
4  Bases de dados meteorológicos e climáticos .............................................. 33
4.1  Bases de dados nacionais ............................................................................................. 33

4.2  Principais conjuntos internacionais ............................................................................. 41
5  Conclusões .................................................................................................... 47

6  Referências ................................................................................................... 50

7  Glossário ....................................................................................................... 52

8  Anexos .......................................................................................................... 55

Página 4

1  Introdução ao PDI

O  projeto  de  Pesquisa,  Desenvolvimento  e  Inovação  (PDI)  "Resiliência  da  Transmissão  de

Energia  Elétrica  a  Eventos  Climáticos  Extremos,  registrado  sob  o  número  PD-00068-

0071/2025, tem o objetivo de aprimorar os esforços de aprimoramento da resiliência climática

das linhas de  transmissão da ISA ENERGIA BRASIL. Mais especificamente, o projeto visa

antecipar  riscos  e  contribuir  para  a  avaliação  da  vulnerabilidade  das  linhas  e  subestações,

considerando os impactos em seus serviços. Entre as principais contribuições a serem geradas

por este projeto, podem ser destacadas:

•  Análise  Custo-Benefício  (CBA)  e  do  Custo  Total  Global  de  investimentos  em

resiliência a eventos climáticos extremos;

•  Dashbord de gestão de ameaças a climáticas extremas;

•  Melhorias regulatórias para incentivar investimentos eficientes.

A Fundação Getulio Vargas (FGV) é a executora do projeto contratado pela  ISA ENERGIA

BRASIL, que conta com a parceria da Empresa de Pesquisa Energética (EPE). A participação

da  EPE  tem  o  objetivo  de  garantir  que  a  experiência  de  seus  técnicos  sobre  o  tema  seja

devidamente apropriada pelo projeto, bem como de que os seus achados gerem externalidades

positivas para todos o Setor Elétrico Brasileiro (SEB).

A lista de produtos que serão gerados por este PDI, bem como uma breve descrição de seus

conteúdos é apresentada abaixo:

PRODUTO 1: Relatório de revisão da modelagem climática da ISA ENERGIA BRASIL

O Produto 1, constituído por este documento, tem como objetivo avaliar a modelagem

climática e a metodologia de análise de riscos utilizada pela ISA ENERGIA BRASIL

em seus esforços anteriores para tratar a resiliência de seus ativos a eventos climáticos

extremos.

Página 5

PRODUTO  2:  Relatório  de  revisão  da  modelagem  de  engenharia  da  ISA  ENERGIA

BRASIL

O relatório de revisão da modelagem de engenharia da ISA irá organizar e analisar os

documentos enviados pela empresa sobre ativos, desligamentos, planos de contingência

e  planos  de  ação.  Ele  prevê  a  sistematização  dos  dados  de  linhas  de  transmissão  e

subestações em planilhas, classificadas por nível de tensão e comprimento, e considera

normas e regulamentos que definem por quanto tempo esses ativos podem permanecer

fora de operação sem penalidades. As ameaças climáticas  serão mapeadas a partir de

ocorrências  e  desligamentos,  destacando  ventos  extremos,  descargas  atmosféricas,

queimadas,  inundações  e  temperaturas  extremas;  o  relatório  aponta  maior  criticidade

para ventos, queimadas e inundações, com efeitos específicos como danos em linhas de

440 kV, rompimento de cabos para-raios, custos elevados de prevenção e redução das

distâncias mínimas entre cabos e nível da água, além de registrar que as variações de

temperatura afetam principalmente equipamentos de subestações.

A análise final será alinhada às discussões com a equipe da ISA ENERGIA BRASIL e

à proposta do projeto, aprofundando-se após a depuração dos planos de contingência e

planos  de  ação.  Entre  os  planos  de  contingência,  serão  avaliados  relatórios  sobre

logística e recursos para atendimento emergencial em linhas de transmissão, instruções

para  variantes  de  emergência  e  recuperação  de  linhas  avariadas,  bem  como  planos

específicos para incêndios florestais, inundações fluviais e ventos; entre os planos de

ação, serão examinados estudos de impactos das mudanças climáticas e estratégias de

mitigação  em  ativos  de  alto  risco,  planos  por  ameaça  (incêndios,  inundações,

temperaturas  máximas)  e  estudos  de  operação  e  proteção  para  a  temporada  de  verão

2025–2026.

PRODUTO  3:  Relatório  de  revisão  de  modelagem  do  Custo  Total  Global  da  ISA

ENERGIA BRASIL

O  custo  total  global  de  um  projeto  de  engenharia  é  o  somatório  de  todos  os  gastos

necessários  para  conceber,  implantar,  operar  e,  eventualmente,  desativar  o  projeto,

considerando todo o seu ciclo de vida. O relatório apresentará a revisão da metodologia

em uso e desenvolvida pela ISA ENERGIA BRASIL, buscando a conexão com inputs

Página 6

recebidos  de  fases  anteriores  O  objetivo,  para  além  da  revisão,  é  subsidiar  o

desenvolvimento do produto 5.

PRODUTO 4: Relatório de atualização de modelagem de impacto de eventos climáticos

extremos

Identificadas as possibilidades de aprimoramento apontadas no Produto 1, este produto

deverá  propor  melhorias  nas  projeções  de  cada  uma  das  variáveis  analisadas,  com

especial  atenção  a  inundações,  ventos  e  descargas  elétricas  que  estejam  alinhadas  às

projeções do Painel Intergovernamental sobre Mudanças Climáticas (IPCC, das iniciais

em inglês).

As  projeções  deverão  ser  realizadas  levando-se  em  consideração  as  linhas  de

transmissão de interesse da ISA ENERGIA BRASIL, com o maior grau de resolução

espacial possível.

PRODUTO 5: Relatório de atualização de modelagem do custo total global e de análise

de custo-benefício

A Análise Custo-Benefício (CBA) compreende um conjunto de técnicas econômicas com

vistas  a  comparação  entre  alternativas  possíveis,  incluindo,  quando  cabível,  a  visão  de

outros  stakeholders  e  elementos  intangíveis.  Deste  modo,  este  relatório  apresentará  as

potenciais melhorias dentro do apresentado no Produto 3, com destaque para:

•  Desenvolvimento de métricas para a tomada de decisão;

•

Inclusão da ideia de “métrica em risco” para ambas as visões;

•  Parametrização de impactos indiretos e intangíveis, sobre a companhia, sua região

geográfica de atuação e outros stakeholders.

Considerando-se  os  cenários  oriundos  da  modelagem  de  riscos  climáticos,  as  possíveis

soluções de engenharia e seus custos; o produto apresentará, para além do relatório, o design

de  parte  do  dashboard  do  projeto:  inputs,  outputs  e  configurações  para  a  ferramenta  de

cálculo de CBA sob diferentes cenários.

PRODUTO 6: Dashboard de gestão da resiliência de adaptação de ativos

Página 7

Primeira versão do dashboard de gestão da resiliência a eventos climáticos extremos das

linhas  de  transmissão  de  eletricidade  selecionadas  pela  ISA  ENERGIA  BRASIL.  O

dashboard deverá contar com:

•  Painel de histórico de eventos climáticos,

•  Painel de equipamentos de engenharia,

•  Painel de cenários futuros de eventos climáticos,

•  Painel de opções de investimentos em resiliência,

•  Painel de cenários climáticos e de investimentos em resiliência e seus efeitos sobre

os ativos.

PRODUTO 7: Implementação do dashboard em ambiente piloto

Implementação efetiva, implementação de possíveis sugestões de profissionais da ISA

ENERGIA BRASIL e teste do dashboard em ambiente de produção.

O dashboard poderá ser implementado em PowerBI, ou em outra plataforma sugerida

pela ISA ENERGIA BRASIL. O back-end deverá ser implementado na linguagem de

programação  aberta  Python,  que  é  a  linguagem  mais  utilizada  para  a  realização  de

estudos de Data Science no mundo.

PRODUTO  8:  Relatório  de  discussões  técnicas  com  profissionais  da  ISA  ENERGIA

BRASIL sobre as medidas de aprimoramento regulatório

Relatório  de  proposição  de  aprimoramentos  regulatórios  a  serem  realizados  na

regulação  do  segmento  de  transmissão  de  eletricidade  no  Setor  Elétrico  Brasileiro

(SEB).

Os  apontamentos  deverão  levar  em  consideração  os  achados  obtidos  ao  longo  da

realização  deste  projeto,  bem  como,  os  ensinamentos  a  serem  obtidos  com  as

experiências  internacionais.  As  lições  serão  obtidas  por  meio  de  dois  caminhos

principais:

•  Revisão  de

literatura

internacional  sobre

regulação  de

transmissão de energia elétrica,

Página 8

•  Missões internacionais a reguladores, operadores, transmissores

e outras instituições relevantes para a segmento de transmissão.

PRODUTO 9: Relatório Final

Relatório final compilando todos os achados do projeto, que incluirá:

•  Relatórios,

•  Arquivos de dados (CSV),

•  Arquivos de Excel,

•  Códigos em Python,

•  Apresentações de uso e de manutenção dos dashboards;

•  Sugestões  aprimoramentos  nos  estudos  realizados  pela  ISA  ENERGIA  BRASIL

relacionados aos temas tratados neste PDI,

•  Arquivos de PowerBI com os dashboards desenvolvidos.

A previsão de entrega dos produtos está disposta na Figura 1, com fevereiro de 2026 o mês da

entrega deste primeiro produto.

Figura 1 Cronograma de entregas de produtos

Página 9

2  Introdução ao Produto 1

O  presente  documento  se  constituiu  no  “PRODUTO  1:  Relatório  de  revisão  da  modelagem

climática da ISA ENERGIA BRASIL” que faz parte do PD-00068-0071/2025, Resiliência da

Transmissão  de  Energia  Elétrica  a  Eventos  Climáticos  Extremos. Ele tem o objetivo de fazer a

revisão dos produtos de análise climática da ISA ENERGIA BRASIL apresentados à equipe do FGV

CERI. Ele trata da modelagem de cada umas das sete ameaças e propor aprimoramentos, com destaque
para:

•  Modelagem  de  ventos  sinóticos,  comparando  o  previsto  no  projeto,  o  que

acontece hoje e a projeção para o futuro.

•  Observação  de  possibilidade  de  melhorias  da  modelagem  de  ventos  não

sinóticos.

Além de  avaliar os conteúdos dos documentos anteriores, este documento deve considerar  a

possibilidade de melhoria de modelagem das variáveis abaixo:

•  Descargas atmosféricas: Projeções de quantidades e intensidades, comparando

como elas eram no passado com como elas são projetadas para o futuro?

•  Cotas de inundação.

2.1  Documentos analisados

Para  a  elaboração  deste  relatório,  foram  considerados  os  documentos  enviados  pela  ISA

ENERGIA BRASIL que se encontram enumerados abaixo, segundo o diretório em que elas são

disponibilizadas:

1.  01. Metodologia Ameaças

a.  ABORDAGEM  PARA  A  ESTRUTURAÇÃO  DO  PLANO  DE  AÇÃO

CLIMÁTICO  DA  ISA  CTEEP,  Metodologia  Ameaças  Climáticas,  ISA  CTEEP,

Março

–

2024

(documento

de

Word

-

METODOLOGIA_AMEACAS_CLIMATICAS_ISA_v2.1.docx).

Página 10

b.  ACOMPANHAMENTO  DO  PROJETO,  PLANO  DE  AÇÃO  CLIMÁTICA,

Metodologia de cálculo dos índices de probabilidade  - Riscos Climáticos Físicos,

Julho  2024  (apresentação  de  Powerpoint  -  241025_Conceitos  e  limitações  -

ameaças_revWay.pptx).

c.  PLANO  DE  ADAPTAÇÃO  E  RESILIÊNCIA  CLIMÁTICA,  ISA  ENERGIA

BRASIL  (documento  de  Word  -  PLANO  DE  ADAPTAÇÃO  E  RESILIÊNCIA

CLIMÁTICA_ISAE_v1 ventos.docx).

2.  02.1 Apresentação EPE

a.   Atualização,  Adaptação  Climática,  Versão  preliminar,  23  de  Janeiro  de  2025.

(apresentação  em  PDF  -  Atualização  Adaptação  Climática  versão  completa  EPE

21.01.25 rev01.pdf)

3.  Mapas html

a.  01.  Mapas  HTMLs  –  Mapas  em  html  com  a  síntese  de  cada  uma  das  ameaças

climáticas por linha de transmissão e por subestatções

4.  Mapas Isótocas

a.  Mapas – Mapas das isótocas de 3ms, 10min e 30s.

5.  Matriz de Riscos

a.  LT - 241108_ISACT23A_Matriz_Riscos Físicos_v8.2_LT_ (v. equivalência)

i.  Elevação_Nivel_Mar

ii.  Incêndios Florestais

iii.  Inundações Fluviais

iv.  Temperatura Máxima

v.  Tempestades

vi.  Anomalias Ventos

vii.  Deslizamentos

b.  SE –

i.  Finais jun 25

1.  Versão atualizada (equivalência ISA ENERGIA)

a.  241108_ISACT23A_Matriz_Riscos

Físicos_v.8.4_SE_Elevação_Nível_Mar (v. equiv.XLSM

b.  241108_ISACT23A_Matriz_Riscos

Físicos_v8.5_SE_Inundacoes_Fluviais (v. equiv.XLSM

Página 11

c.  241129_ISACT23A_Matriz_Riscos

Físicos_v8.2_SE_Temperatura (v. equiv.XLSM

d.  241129_ISACT23A_Matriz_Riscos

Físicos_v8.2_SE_Tempestades (v. equiv.XLSM

e.  250102_ISACT23A_Matriz_Riscos

Físicos_v8.3_SE_Deslizamentos (v. equiv.XLSM

f.  250102_ISACT23A_Matriz_Riscos

Físicos_v8.3_SE_Incendios (v. equiv.XLSM

6.  06 Manual de gestão de riscos e criticidade de ativos

a.  avaliaçãoCriticidade_Rev2022_CálculoCriticidade.XLSM

b.  NOR.EI1. Manual de Gestao Integral de Riscos.pdf

c.  PRO.OP36 Qualificação de Criticidade dos Ativos.pdf

7.  07 Materiais adicionais

a.  15012024 Workshop Adaptação Climática.pptx

b.  241220_ISACT23A - Apresentação Benchmarking Planos de Adaptacao_v1.0.pdf

c.  241220_ISACT23A - Benchmarking de Recomendações IFRS S2_v1.0.pdf

d.  JC_ISA24_V4-E-1 (24).pdf

8.  Dados Desl Queimadas

a.  data (4).xlsx

b.  IE 2025_Queimadas.pptx

c.  Lista desligamentos por queimada - 2014 a 2024.xlsx

9.  Dados Quedas LTs

a.  Histórico de Quedas LT 440 kV JUP-BAU-CAV_Rev 0.xlsx

b.  LEVANTAMENTOS OCORRÊNCIAS QUEDAS_Atualizada 12-12-2025.xlsx

10. DadosClimáticos

11. Diario Unifilar LTs

a.  Croquis_ISAENERGIA_2025_R-20.pdf

12. Dados Relevantes

a.  Consulta Pública_ conselho-Alagoas.pdf

b.  Módulo 4 – Prestação dos Serviços - aren2020905_2_3.pdf

c.  SINOPSE LINHAS DE TRANSMISSAO CTEEP.pdf

d.  Submódulo 2.7-RQ_2020.12_Comentado.pdf

e.  Transmissão e Mudanças Climáticas 2.pdf

Página 12

13.  DocumentosEnviadosem13-01-2026

a.  Base_18_25_Queimadas_Descargas.xlsx

b.  Mapa Densidade Descargas Atmosfericas_1998-2013_pdf.pdf

c.  RES_ [Projeto Eventos Climáticos] - Reunião de Follow Up.eml

14.  KMZ LTs

a.  ISA ENERGIA BRASIL.kmz

15.  Planos Contingências

a.  IM-TM-165-2023-Rev.02  -  Logística  e  Recursos  Disponíveis  para  Atendimentos

Emergenciais em LTs

b.  PCE-LTA-074-2023-Rev.02  -  Plano  de  Contingência  de  Emergência  para  Linhas

Aéreas.pdf

c.  Plano de Contingência – Ameaça de Incêndios Florestais_Rev02.pdf

d.  Plano de Contingência – Ameaça de Inundações Fluviais_Rev03.pdf

e.  Plano de Contingência – Ameaça de Ventos_Rev03.pdf

16.  Planos de Ações

a.  0. Plano de adaptação_Tempestades_R3.pdf

b.  Mudanças Climáticas_Ameaçãos de Ventos-R02.pdf

c.  Plano de Ações – Ameaça de Incêndios Florestais-Rev 05.pdf

d.  Plano de Ações – Ameaça de Inundações Fluviais-Rev 04.pdf

e.  Plano de Ações – Ameaça de Temperatura Máxima_Revisão_01.pdf

f.  TOxE-E-0153-2025_Temporada_de_Verao_2025-2026_R0.pdf

17. Tempestade - Descarga Atmosféricas

a.  DADOS CABOS PARA RAIOS_LTS.docx

b.  Descarga Atmosférica - Premissas Cálculos.JGP

c.  Mapa Densidade Descargas Atmosfericas_1998-2013_pdf.pdf

Para  a  elaboração  deste  documento  também  foram  consideradas  informações  obtidas  pelos

pesquisadores do FGV CERI ao longo das reuniões realizadas ao longo do tempo de execução

deste projeto, com destaque para a reunião que contou com os colaboradores da WayCarbon,

em  reunião  realizada  em  29/01/2026.  Entre  os  participantes,  destacam-se  Jessica  da  Silva

Balbinot,  Vandinaldo  Alberto  Vieira,  por  parte  da  ISA  ENERGIA  BRASIL,  e  de  Daniel

Carvalho, Melina Amoni, Fraciele Barros, Mayara Cristiane de Abreu Moraes Vieira Ribeiro,

por parte da WayCarbon. Nessa reunião foi apontado que o principal documento a ser usado

como referência foi o ABORDAGEM PARA A ESTRUTURAÇÃO DO PLANO DE AÇÃO

Página 13

CLIMÁTICO DA ISA CTEEP, Metodologia Ameaças Climáticas, ISA CTEEP, Março – 2024.

Esse é o documento no qual se baseia a análise da modelagem climática proposta realizada pela

WayCarbon.

Página 14

3  Abordagem para a estruturação do plano de ação

climático da ISA ENERGIA BRASIL

3.1  Visão geral

Segundo o próprio o documento ABORDAGEM PARA A ESTRUTURAÇÃO DO PLANO

DE  AÇÃO  CLIMÁTICO  DA  ISA  CTEEP,  Metodologia  Ameaças  Climáticas,  ISA  CTEEP,

Março – 2024, ele “tem como objetivo apresentar a metodologia utilizada para a priorização

dos riscos climáticos físicos na matriz de riscos da ISA ENERGIA BRASIL, incluindo a análise

de tendência de ameaças climáticas no curto, médio e longo prazo para os anos de 2030, 2040

e 2050, respectivamente, baseado em cenários de aquecimento do IPCC, sendo eles SSP1-2.6,

SSP2-4.5 e SSP3-7.0, e o grau de impacto das ameaças climáticas sobre os diversos ativos da

empresa.”

Nesta  linha,  entende-se  que  a  principal  contribuição  realizada  pela  empresa  contratada

anteriormente  foi  o  produto  definido  como  a  “Metodologia  Way  Carbon  para  cálculo  de

probabilidade”, que foi apresentada e discutida no documento sob análise. Esta seção versará

sobre os achados neste documento.

3.2  Ameaças climáticas

O relatório em questão  aborda sete  ameaças  climáticas, apresentadas na  Figura 2 (obtida no

próprio  relatório  sob  análise),  a  saber:  Tempestades  (descargas  atmosféricas),  incêndios

florestais,  inundações  fluviais,  ventos  (alterações  nos  padrões  de  ventos),  deslizamentos,

temperatura máxima (ondas de calor) e aumento do nível do mar.

Figura 2 Ameaças climáticas analisadas

Fonte: WayCarbon.

Página 15

3.3  Cenários e horizontes temporais

Segundo o documento sob análise, o projeto conduzido anteriormente utilizou três cenários do

IPCC  que  consideram  a  combinação  de  diferentes  trajetórias  de  emissão  e  concentração  de

gases  de  efeito  estufa  (RCP,  Representative  Concentration  Pathways),  com  diferentes

trajetórias  de  desenvolvimento  socioeconômico  (SSP,  Shared  Socio-economic  Pathways):

SSP1-2.6, SSP2-4.5 e SSP3-7.0. Eles são descritos na Tabela 1, conforme segue:

Cenário

SSP1-2.6

SSP2-4.5

SSP3-7.0

Tabela 1 Descrição dos cenários climáticos adotados no projeto

Descrição

As emissões de GEE adotadas neste cenário consideram como pico o ano de 2020, iniciando a redução
das emissões a partir nos anos seguintes. A neutralidade nas emissões de CO2 é atingida entre 2070 e
2080, ao custo de um alto desenvolvimento nas políticas e ações de combate à mudança climática. A
narrativa de evolução socioeconômica se mantém neste cenário.
As emissões de Gases de Efeito Estufa (GEE) atingem o pico na segunda metade do século XXI,
iniciando uma redução abrupta a partir de então, chegando a metade dos valores atuais até 2100;
Associado à um aumento de aproximadamente 2,7°C na temperatura média global até 2100.
As emissões de GEE se elevam crescentemente ao longo do século 21. Neste cenário, o aumento da
temperatura média global possivelmente superará 2°C até 2050, sendo o que apresenta maiores desafios
tanto para a mitigação quanto para a adaptação. O contexto global é de nacionalização política, com a
presença de conflitos regionais e maior foco das nações para as questões internas do que as externas,
havendo menor cooperação internacional, incluindo para os problemas ambientais.

Fonte: WayCarbon.

Os dados das projeções para cada uma das variáveis dos modelos climáticos globais utilizados

são provenientes do repositório do Coupled Model Intercomparison Project Phase 6 (CMIP6)1.

O repositório de dados já apresenta os resultados do Sexto Relatório de Avaliação (AR6) do

Painel Intergovernamental sobre Mudanças Climáticas (IPCC) (IPCC et al., 2021).

O  relatório  indica  que  foram  estabelecidos  quatro  horizontes  temporais  para  a  análise  das

ameaças climáticas para cada um dos três cenários utilizados. O primeiro foi indicado  como

cenário histórico (HIS), compreendendo os anos entre 1995 e 2014 (os anos inicial e final fazem

parte  da  amostra).  Para  as  projeções  foram  considerados  três  horizontes  temporais:  (i)  O  de

curto prazo, abrangendo o período de 2021 até 2040 (indicado como 2030); o de médio prazo,

abrangendo intervalo de 2031 a 2050 (indicado como 2040); (iii) o de longo prazo, abrangendo

os períodos de 2041 a 2060 (indicado como 2050).

1 Os dados podem ser obtidos neste site: https://wcrp--cmip-org.translate.goog/cmip-
phases/cmip6/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc#cmip6_data_request.

Página 16

A avaliação da equipe responsável por este relatório é que os modelos e cenários escolhidos são

adequados e que os mesmos devem ser mantidos nos exercícios a serem realizados no projeto

de PDI em curso.

3.4  Cálculo das probabilidades

Um ponto importante e cuja modelagem chama atenção no relatório sob análise é o cálculo de

probabilidades. Embora ele não esteja apresentado em uma subseção específica no documento

original, dada a importância do tema, isso será feito neste relatório.

Segundo o documento, cada extremo climático é representado por “um valor bruto”. A ideia de

“valor  bruto”  não  é  um  conceito  formalmente  definido  em  Estatística,  nem  é  descrito

precisamente  ao longo do texto. O relatório segue  afirmando que posteriormente este “valor

bruto” é convertido em uma escala de 0 a 1 através de sua “respectiva função de densidade de

probabilidade, levando em consideração as características do clima natural durante o período

de  referência  de  1950  até  1994”.  O  documento  não  descreve  precisamente  qual  seria  a  sua

“respectiva função de densidade”. Dessa forma, o processo utilizado para a  identificação do

modelo probabilístico mais adequado aos dados não foi explicitado com clareza.

Ainda,  o  documento  segue  afirmando  que  “sendo  assim,  é  possível  correlacionar  extremos

relacionados a frequência, duração e severidade”. O conteúdo também não permite identificar

como foi possível “correlacionar os extremos” apontados. Por fim, o parágrafo com a descrição

do  “cálculo  das  probabilidades”  termina  afirmando  que  “esse  índice  não  expressa  a

probabilidade  absoluta  da  ocorrência  do  evento  climático  nem  seu  impacto  associado”  e

propondo uma interpretação, como se segue:

“No  entanto,  à  medida  que  os  modelos  projetam  extremos  climáticos

mais  intensos,  essas  projeções  tendem  a  se  situar  mais  à  direita  no

espectro de valores possíveis, resultando em um aumento do  índice de

ameaça para refletir essa intensificação. Um valor médio próximo a 50%

indica  que  os  eventos  extremos  projetados  terão  uma  severidade,

frequência,  intensidade  e  duração  semelhantes  àquelas  observadas  no

clima de referência. Portanto, mesmo esse valor médio demanda atenção,

Página 17

pois  implica  que  as  condições  extremas  persistirão  em  um  nível

significativo.”

A Figura 3 reproduz o gráfico utilizado para ilustrar as ideias apresentadas no parágrafo acima.

Figura 3 Exemplo de distribuição normal para a variável 𝑾𝑿𝟏𝒅𝒂𝒚 no cenário de referência

Fonte: WayCarbon.

A  avaliação  que  a  equipe  técnica  responsável  por  este  documento  faz  é  que  a  modelagem

proposta usa conceitos não consagrados na Teoria Estatística e que ela não apresenta todas as

características de reprodutibilidade que seriam desejáveis.

Com base no que foi relatado e no conhecimento técnico de Modelagem Estatística de Dados,

pode-se imaginar que foi obtida uma amostra de dados (diários, segundo o que pode-se apurar

a  partir  de  reunião  técnica)  obtidos  durante  os  anos  de  1950  a  1994,  totalizando  (supõe-se)

aproximadamente 16.425 observações de dados de cada uma das variáveis climática analisadas.

Desta  forma,  o  procedimento  consagrado  na  literatura  estatística  para  a  estimação  da

probabilidade de eventos associados a variáveis climáticas passa por elencar um conjunto de

modelos probabilísticos teóricos com base literatura e na experiência profissional. A partir daí

parte-se  para  estimação  de  seus  parâmetros,  usando  a  amostra  de  dados  coletada.

Posteriormente  são  realizados  testes  estatísticos  formais  para  identificação  dos  modelos

teóricos mais adequados para cada uma das variáveis de interesse. Este mesmo procedimento

deveria ser utilizado para a modelagem das distribuições conjuntas das variáveis (a modelagem

que considera o comportamento de duas ou mais variáveis) e estimação dos seus parâmetros

multivariados (correlações, por exemplo).

Página 18

Este  procedimento  garantiria  uma  estimação  formal,  o  que  os  autores  do  estudo  anterior

parecem  ter  tratado  como  “probabilidade  absoluta”  (termo  que  não  existe  na  literatura

estatística).  Da  forma  em  que  foi  tratada  aqui,  a  modelagem  proposta  suporia  que  as  séries

temporais  (amostras  obtidas  ao  longo  do  tempo)  sejam  estacionárias  ao  longo  do  tempo

(hipótese bastante razoável).

A  partir  daí,  a  forma  mais  adequada  de  investigar  a  existência  de  mudança  no  padrão  de

comportamento dos dados deveria ser através da realização de testes estatísticos formais para

detectar a existência de tendência nos mesmos. Outra maneira de obter evidência de mudança

de comportamento nas variáveis seria a realização de testes estatísticos para verificar o aumento

da proporção de eventos relacionados aos quantis superiores das distribuições de probabilidades

estimadas no período de referência. Mais precisamente, pode-se comparar os quantis (percentis

das distribuições teóricas estimadas) com os percentis das distribuições empíricas das variáveis

projetadas. Caso os quantis mais altos das distribuições empírica das variáveis projetadas sejam

significativamente  maiores  do  que  as  das  distribuições  teóricas  estimadas,  reforça-se  a

evidência  de  que  a  mudança  climática  gerará  fenômenos  climáticos  extremos  com  maior

frequência. A metodologia sugerida nestas linhas é a prevista formalmente pela literatura para

lidar com a suspeita de aumento das frequências de eventos relacionados à cauda direita das

distribuições de probabilidade e é muito diferente da que foi sugerida com observação se “um

valor médio” está “próximo a 50%”.

A  equipe  responsável  pela  elaboração  deste  relatório  entende  que  há  boas  possibilidades  de

aprimorar  os  pontos  apontados  nesta  subseção.  Os  exercícios  de  melhoria  são  objetos  dos

próximos relatórios que envolverem modelagem climática.

3.5  Análise por ameaça

3.5.1  Tempestades/Descargas atmosféricas

A  modelagem  proposta  pelo  relatório  sob  análise  une  a  modelagem  de  tempestades  com  a

modelagem das descargas atmosféricas. A discussão qualificada do tema é  importante, visto

que se estima que cerca de 70% dos desligamentos no sistema de transmissão e 40% no sistema

de  distribuição  sejam  provocados  por  descargas  atmosféricas,  conforme  apontado  por

Página 19

SCHROEDER (2001), INPE (2024) e RAKOV (2003). Além disso, de acordo com o “Relatório

de  Análise:  Desligamentos  Forçados  do  Sistema  de  Transmissão”  publicado  pela  Agência

Nacional  de  Energia  Elétrica  (ANEEL),  75%  das  interrupções  não  programadas  no

fornecimento de energia no Brasil ocorreram devido a falhas nas linhas de transmissão, sendo

aproximadamente 29% dessas falhas causadas por descargas atmosféricas (ANEEL, 2023).

Perante os significativos quantitativos percentuais citados acima, pode-se perceber a expressiva

relevância da quantificação de parâmetros que consigam expressar as taxas de incidências de

descargas  atmosféricas  em  sistemas  elétricos,  justificando,  portanto,  esforços  técnico-

científicos nesta temática.

No relatório avaliado, a ameaça de tempestades é calculada de acordo com a equação:

𝑇𝑒𝑚𝑝𝑒𝑠𝑡𝑎𝑑𝑒𝑠 =

𝑅𝑋1𝑑𝑎𝑦+𝑅99𝑝+𝑊𝑋1𝑑𝑎𝑦

3

,

na qual:

•  𝑅𝑋1𝑑𝑎𝑦 representa a máxima precipitação anual em 1 dia;

•  𝑅99𝑝 representa a precipitação total  anual dos dias em que a precipitação excedeu o

99° percentil do período de referência; e

•  𝑊𝑋1𝑑𝑎𝑦 representa a máxima velocidade (média) do vento atingida em determinado

dia do ano.

O indicador de "ameaça de tempestades" apresentado é uma forma de tentar capturar elementos

de eventos intensos relevantes para inundações e falhas em linhas de transmissão (chuva  que

provoca cheia; vento que provoca quebra de  torres). No entanto, há limitações conceituais e

técnicas que sugerem refinamentos para maior rigor em P&D.

Como pontos fortes podem ser destacados:

•  Relevância  setorial:  𝑅𝑥1𝑑𝑎𝑦  e  𝑅99𝑝  são  boas  proxies  para  cheias  convectivas;

𝑊𝑋1𝑑𝑎𝑦 aborda danos eólicos comuns em transmissão.

•  Simplicidade: Média aritmética facilita comunicação e monitoramento operacional.

•  Base padronizada: Usa índices climáticos validados globalmente.

Página 20

Limitações:

•  Falta de normalização: Unidades incompatíveis (𝑅𝑥1𝑑𝑎𝑦/𝑅99𝑝 em mm; 𝑊𝑋1𝑑𝑎𝑦

em 𝑚/𝑠) invalidam a soma direta e podem resultar em escala dominada por

precipitação, subestimando vento.

•  Ausência de não-linearidade: Eventos extremos são raros; média simples ignora

caudas pesadas.

•  Sem contexto probabilístico: Não considera thresholds de dano nem

frequência/retorno.

•  Estacionariedade implícita: Não ajusta por tendências climáticas até 2050.

•  Não consideração da intensidade de descargas atmosféricas em termos de distribuições

temporais  de  suas  correntes  elétricas  típicas,  com  ênfase  na  componente  de  corrente

contínua, tendo em vista sua capacidade de afetar nocivamente cabos para-raios.

Possíveis oportunidades de melhoria:

•  Normalização e Ponderação: Normalização tornaria todas as unidades unidimensionais

e evitaria a soma de parcelas medidas em unidades diferentes. A Ponderação permitiria

que os pesos fossem escolhidos de forma a contemplar diferenças nos impactos de cada

um dos componentes nas variáveis de interesse.

•  Versão  Probabilística/Composta:  estimação  de  excessos  (Calcule  excedência:

𝑃(Tempestade > threshold) e possibilidade de criação de outros índices.

•  Projeções: Explicitação das tendências de aumento de extremos.

•

Inclusão  da  modelagem  da  intensidade  de  descargas  atmosféricas  em  termos  de

distribuições temporais de suas correntes elétricas típicas.

•  Eventos compostos: modelagem das correlações e estruturas de dependência de maneira

formal, por meio de funções de probabilidade e de cópulas.

•  Avaliar  as  quantidades  de  descargas  atmosférica  temporalmente  e  comparar  com  os

horizontes futuros.

•  Avaliar na literatura as suportabilidades de nível de descarga em Coulombs por tipos de

cabo para-raios instalados nas linhas.

•  Avaliar  as  vulnerabilidades  dos  cabos  para-raios  existentes  frente  as  descargas

atmosféricas nos horizontes futuros.

Página 21

3.5.2

Incêndios florestais

A modelagem de ameaças relacionadas  incêndios florestais proposta no relatório sob análise

utiliza as variáveis Tipo de Vegetação (𝑣𝑒𝑔), Declividade (𝑑𝑒𝑐), Orientacao das Encostas (𝑜𝑒),

Altimetria (𝑎𝑙𝑡) e Fórmula de Monte Alegre (𝐹𝑀𝐴), que são utilizadas para a construção do

Indicador  “Incêndios  Florestais”,  dado  pela  Fórmula  de  Monte  Alegre  Modificada  (𝐹𝑀𝐴 +,

apresentado na Equação 1).

O cálculo é definido pela Equação abaixo.

𝐼𝑛𝑐ê𝑑𝑖𝑜𝑠𝐹𝑙𝑜𝑟𝑒𝑠𝑡𝑎𝑖𝑠 = √𝐹𝑀𝐴 ∗ √𝑣𝑒𝑔 ∗ [

𝑑𝑒𝑐+𝑜𝑒+𝑎𝑙𝑡

3

], (1)

na qual:

•  𝐹𝑀𝐴 representa o resultado da Fórmula de Monte Alegre Alterada.

•  𝑣𝑒𝑔: Tipo de Vegetação,

•  𝑑𝑒𝑐: Declividade,

•  𝑜𝑒: Orientação das Encostas, e

•  𝑎𝑙𝑡: Altimetria.

A  variável  𝑣𝑒𝑔  foi  obtida  através  do  mapa  anual  de  cobertura  e  uso  da  terra  do  Brasil  do

MapBiomas (Coleção 8) e  as variáveis  𝑑𝑒𝑐, 𝑜𝑒 e  𝑎𝑙𝑡 foram  extraídos do Modelo Digital de

Elevação (MDE).

Sobre esta seção há alguns pontos que podem ser destacados.

Há alguns pontos interessantes:

•  Processamento rápido.

•

Integração multivariable: 𝐹𝑀𝐴 + (umidade + vento + seca) + topografia (𝑑𝑒𝑐, 𝑜𝑒, 𝑎𝑙𝑡)

+ 𝑣𝑒𝑔 capturam drivers físicos; reescalonamento 0-1 permite soma/media ponderada.

•  Fontes atualizadas: MapBiomas Coleção 8 (até 2023) é padrão ouro para uso/vegetação

BR; MDE para topografia é adequado.

Página 22

•  Foco natural: Correto excluir ação humana para projeções climáticas.

•  Relevância

energia:

Incêndios

em

cerrados/caatingas

afetam

corredores

Nordeste/Centro-Oeste.

Também há algumas limitações:

•  Falta  de  drivers  meteorológicos  centrais:  Ausência  de  temperatura  (𝑇𝑚𝑎𝑥),  déficit

hídrico (SPI/PDSI) e duração seca — 𝐹𝑀𝐴 + é bom, mas incompleto sem eles.

•  Estacionariedade: Parâmetros fixos (topografia/veg) ignoram mudanças até 2050.

•  Método  de  composição:  Soma  simples  não  pondera  susceptibilidade;  sem  thresholds

probabilísticos.

•  Validação ausente: Não menciona teste com incêndios reais.

Entre as possíveis sugestões, destacam-se:

•  Buscar aprimoramento dos indicadores utilizados,  com estimação de pesos com base

em dados.

•  Validação  e  Probabilidade:  Testes  de  verificação  de  correlação  e  estimação  de

probabilidades de queimadas.

•  Avaliar as quantidades de incêndios florestais (queimadas) temporalmente e comparar

com os horizontes futuros.

•  Avaliar  quais  trechos  das  linhas  de  transmissão  têm  maior  exposição  ao  risco  de

desligamento por incêndios florestais.

3.5.3

Inundações fluviais

A seção ameaça de inundação fluvial trata exclusivamente do transbordamento de rios, canais,

açudes  e  similares  (cheias  fluviais),  não  tratando  de  alagamentos  causados  por  falhas  nos

sistemas  de  drenagem.  A  abordagem  faz  uso  de  índices  climáticos  padrão  (𝑅𝑥1𝑑𝑎𝑦,  𝑅95𝑝,

𝑅𝑋𝑋𝑚𝑚),  combinados  com  um  Índice  Morfométrico  (IM)  baseado  em  ordem  de  canais,

declividade,  distâncias  vertical/horizontal  aos  rios.  Os  pesos  hidrologicamente  coerentes

priorizam áreas planas de várzea próximas a rios de maior ordem.

Página 23

Entre as limitações, destacam:

•  Soma  variáveis  medidas  em  unidades  diferentes  não  normalizadas  (mm  +  dias  +

adimensional), causando dominância de 𝑅𝑥1𝑑𝑎𝑦;

•  Ausência de validação empírica com cheias reais (ANA/ONS);

•  Não há ligação probabilística com impactos em transmissão (𝑃(𝑓𝑎𝑙ℎ𝑎 𝑡𝑜𝑟𝑟𝑒)).

Entre as sugestões, podem ser anotadas:

•  Normalizar precipitação.

•  Validar correlações entre variáveis;

•  Estimar probabilidades de eventos de inundação.

•  Verificar as cotas dos ativos (torres e subestações).

•  Verificar as cotas de elevação das inundações fluviais.

Com a introdução da modelagem probabilística sugerida, o indicador passaria de descritivo para

prescritivo, quantificando as probabilidades de submersão de torres em cada trecho até trecho

até 2050.

3.5.4  Ventos (Alterações nos padrões de ventos)

O  documento  descreve  o  fenômeno  climático  dos  ventos  e  argumenta  que  a  modelagem  da

ameaça considera dados de velocidade de ventos médios por limitação da disponibilidade de

dados de velocidade máxima para os modelos existentes no Sexto Relatório de Avaliação (AR6)

do IPCC. Embora ressalte que “o intuito da modelagem é verificar tendências climáticas, ou

seja,  entender  as  variações  consideradas  normais  na  região  e  a  partir  desse  comportamento

climático descrever como o histórico recente e os cenários futuros se comportam, o estudo não

apresenta  as  distribuições  de  probabilidade  associadas  aos  ventos  nem  faz  uma  descrição

precisa do racional por trás do indicador proposto. Por fim, o documento descreve a ameaça de

alteração nos padrões de ventos pela equação:

𝐴𝑙𝑡𝑒𝑟𝑎çã𝑜𝑛𝑜𝑠𝑝𝑎𝑑𝑟õ𝑒𝑠𝑑𝑒𝑣𝑒𝑛𝑡𝑜𝑠 =

(𝑊𝑋1𝑑𝑎𝑦+𝑊90𝑝)
,

2

Página 24

na qual:

•  𝑊𝑋1𝑑𝑎𝑦 representa a máxima velocidade (média) do vento atingida em determinado

dia do ano; e

•  𝑊90𝑝 representa a velocidade do vento acima do percentil 90º ao longo de determinado

ano.

A  medida  é  uma  simples  média  aritmética  da  de  duas  medidas  relacionadas  à  ventos  e  não

apresenta  uma  modelagem  que  permita  fazer  simulação  de  cenários  baseados  em  modelos

probabilísticos.

Entre os pontos fortes, destacam-se:

•  Referenciação precisa a AR6 e estudos sobre correlação média-extremo.

•

•

foco em tendências climáticas é apropriado para P&D longo prazo.

Índices 𝑊90𝑝/𝑊𝑋1𝑑𝑎𝑦 (análogos ETCCDI) capturam frequência/intensidade eólica

relevante para linhas (frentes frias/LIPs BR).

•  Ligação explícita com danos infraestruturais.

Há também algumas limitações:

•  Fórmula  média  simples  não  normaliza  unidades/tendências  regionais  (ex.:  𝑊90𝑝

Nordeste vs. Sul).

•  Ausência de validação com rajadas reais (INMET/CPTEC) ou falhas  registradas pela

ONS.

•  Proxy média para extremo é controverso sem correlação quantificada local.

•  Sem  projeções  CMIP6  específicas  para  vento  até  2050  ou  composição  com

cisalhamento direcional.

Há algumas possibilidades de melhoramentos, entre elas:

•  Normalização  as  medidas  utilizadas  para  que  elas  sejam  adimensionais  e  avaliar  a

otimização dos pesos utilizados.

•  Validação  das  correlações  com  rajadas  INMET  e  desligamentos  ONS  por  vento  por

meio de análise de regressões.

•  Para vulnerabilidade, avaliar histórico de queda e definir a probabilidades associadas a

novas ocorrências nos horizontes temporais.

Essas  mudanças  permitiram  estimar  probabilidade  de  falhas  geradas  por  ventos  por  trechos,

ajudando a priorizar investimentos em resiliência.

Página 25

3.5.5  Deslizamentos

O tratamento sobre o tema é iniciado fazendo uma caracterização do fenômeno, bem como os

principais  condicionantes  para  a  sua  ocorrência.  O  documento  aponta  que,  segundo  ABGE

(1998), estas são as principais condicionantes para deslizamentos:

•  Características climáticas, com destaque para o regime pluviométrico;

•  Características  e  distribuição  dos  materiais  que  compõem  o  substrato  das  encostas,

abrangendo solos, rochas, depósitos e estruturas geológicas;

•  Características geomorfológicas, com destaque para a inclinação, amplitude e forma do

perfil das encostas;

•  Regime das águas de superfície e subsuperfície;

•  Características de uso e ocupação.

Assim, reproduz-se aqui a tabela que sintetiza as variáveis utilizadas na avaliação do índice de

suscetibilidade do solo, como pode ser visto na Tabela 2.

Tabela 2 Variáveis utilizadas para a avaliação do índice de Suscetibilidade do Solo

Variável

Uso do solo

(MapBiomas)

Descrição

Cobertura florestal contribui para a boa interceptação da água da chuva no solo, evitando o
escoamento e, consequentemente, os processos de deslizamento. Por outro lado, áreas não
vegetadas tendem a favorecer o escoamento superficial e reduzir a infiltração da água no
solo, além de deixar o solo desprotegido, o que torna mais suscetível a deslizamentos.

Declividade

(MDE)

Encostas mais íngremes são mais propensas a deslizamentos e é um dos fatores principais
na indução da instabilidade da encosta. A declividade é calculada em graus, de 0 a 90, é um
fator definidor de regiões de atenção, sendo que regiões com inclinação menor que 15 graus
são desconsiderados.

Curvatura Vertical

(Topodata/INPE)

A curvatura vertical refere-se ao caráter convexo/côncavo do terreno. As curvaturas verticais
convexas e retilínea eleva a classe de suscetibilidade, pois refletem ambientes que favorecem
o escoamento superficial para erosões laminares (Nascimento et al., 2016).

Curvatura Horizontal

(Topodata/INPE)

A  curvatura  horizontal  refere-se  ao  caráter  divergente/convergente  dos  fluxos  de  matéria
sobre  o  terreno  quando  analisado  em  projeção  horizontal.  As  curvaturas  horizontais
divergente,  planar  e  convergente  foram  consideradas  de  baixa  a  alta  suscetibilidade  ao
deslizamento,
respectivamente.  As  curvaturas  horizontais,  caracterizadas  como
convergentes  e  planares  foram  consideradas  como  agravantes  à  suscetibilidade,  por

Página 26

Variável

Descrição

favorecerem a concentração de fluxo de escoamento superficial para a ocorrência de erosões
lineares (Nascimento et al., 2016).

Susceptibilidade a
Deslizamentos

(NASA, 2017)

O mapa de suscetibilidade a deslizamentos produzido pela NASA foi desenvolvido para
mostrar onde o terreno é mais suscetível a deslizamentos. O modelo de susceptibilidade
considera se foram construídas estradas, se as árvores foram cortadas ou queimadas, se
existe uma falha tectónica importante nas proximidades, se a rocha local é fraca e/ou se as
encostas são íngremes.

Fonte: WayCarbon.

O  documento  também  aponta  para  fatores  climáticos,  como  chuvas  extremas  e  acumuladas

relacionam-se  diretamente  com  a  dinâmica  das  águas  de  superfície.  Por  isso,  o  índice  de

deslizamentos  é  computando  levando-se  em  consideração  variáveis  pluviométricas.  Sendo

assim, a ameaça de deslizamento é calculada de acordo com a equação:

𝐷𝑒𝑠𝑙𝑖𝑧𝑎𝑚𝑒𝑛𝑡𝑜𝑠 = √(𝑅𝑋5𝑑𝑎𝑦+𝐶𝑊𝐷+𝑅𝑋𝑋𝑚𝑚)

3

∗ 𝐼𝑆𝑆,

na qual:

•  𝑅𝑋5𝑑𝑎𝑦  representa  a  máxima  precipitação  anual  em  mm  acumulada  em  5  dias

consecutivos. Elevados índices de 𝑅𝑥5𝑑𝑎𝑦, pode indicar que fenômenos extremos de

precipitação  se  dão  em  uma  escala  curta  de  tempo,  facilitando  a  deflagração  de

deslizamentos de terra

•  𝐶𝑊𝐷  representa  o  número  máximo  de  dias  consecutivos  com  chuva  no  ano

(precipitação acima de 1mm),

•  𝑅𝑋𝑋𝑚𝑚 representa o número de dias no ano com precipitação total diária outlier, ou

seja, definido regionalmente em relação ao período de referência; ou seja, é quantidade

de chuva acumulada nos dias considerados muito úmidos. Esse índice normalmente está

associado a eventos extremos de chuva que podem produzir deslizamentos, e

•

𝐼𝑆𝑆 o índice de susceptibilidade do solo.

Novamente,  a  modelagem  desta  variável  não  apresenta  uma  abordagem  estocástica

(probabilística) que permita simular cenários de deslizamentos.

Diante deste quadro, podem ser apontados alguns pontos interessantes:

Página 27

•  Houve uma escolha de variáveis espaciais (declividade, curvaturas, uso do solo) e da

base MapBiomas.

•  O uso do mapa global de suscetibilidade da NASA agrega informação integrada sobre

fragilidades estruturais que seria custosa de reproduzir.

•  A inclusão de índices de chuva extrema e acumulada (𝑅𝑋5𝑑𝑎𝑦, 𝐶𝑊𝐷, 𝑅𝑋𝑋𝑚𝑚) segue

boas  práticas  em  geotecnia  climática.  A  explicação  sobre  o  papel  diferenciado  de

escorregamentos em rocha e em solo, e o destaque  para chuvas acumuladas de três a

quatro  dias  como  particularmente  críticas,  mostra  bom  alinhamento  com  relatórios

técnicos.

Algumas limitações podem ser identificadas:  Apesar da boa fundamentação, a construção do

índice  ainda  parece  essencialmente  heurística:  as  camadas  de  𝐼𝑆𝑆  são  combinadas  e

reescalonadas sem explicitação clara dos pesos relativos nem de um procedimento quantitativo

para escolhas dos mesmos. Ainda  mais  importante,  a fórmula que combina  𝑅𝑋5𝑑𝑎𝑦, 𝐶𝑊𝐷,

𝑅𝑋𝑋𝑚𝑚  e  𝐼𝑆𝑆  é  uma  combinação  de  variáveis  medidas  em  unidades  diferentes  (mm,  dias,

índice adimensional), o que pode comprometer a interpretação física e a comparabilidade entre

regiões.  A  dependência  do  mapa  global  de  suscetibilidade  da  NASA  é  uma  vantagem

operacional, mas traz incertezas espaciais que não são discutidas; esses mapas têm resolução

relativamente  grosseira  e  podem  não  captar  bem  particularidades  locais  de  geologia  e

intervenções humanas. Outro ponto é que o texto destaca a importância da chuva antecedente e

de  diferentes  tipos  de  instabilização,  mas  a  fórmula  de  ameaça  usa  apenas  três  índices

pluviométricos,  sem  considerar  explicitamente,  por  exemplo,  a  combinação  de  um  evento

extremo de 𝑅𝑋5𝑑𝑎𝑦 após um período longo de 𝐶𝑊𝐷 ou a variação sazonal. Por fim, a ligação

com a  infraestrutura de  transmissão não  está ainda  traduzida em  termos de probabilidade de

impacto  em  torres,  taludes  de  acessos  ou  fundações,  permanecendo  num  nível  mais

geomorfológico que setorial.

Finalmente, pode-se apontar algumas oportunidades de aprimoramento. Para fortalecer o 𝐼𝑆𝑆 e

a ameaça de deslizamento, sugere-se explicitar a forma de agregação das camadas e, se possível,

adotar  um  procedimento  de  ponderação  fundamentado  em  dados,  técnicas  estatísticas  ou

calibração  estatística  com  inventários  de  deslizamentos  (por  exemplo,  ajuste  de  pesos  para

maximizar a correlação espacial entre o índice e mapas históricos de movimentos de massa). A

combinação climática pode ser refinada normalizando 𝑅𝑋5𝑑𝑎𝑦, 𝐶𝑊𝐷 e 𝑅𝑋𝑋𝑚𝑚 em relação

aos  seus  percentis  históricos  (por  exemplo,  percentil  95)  e  combinando-os  em  um  índice

Página 28

adimensional. Em termos probabilísticos, recomenda-se validar o índice resultante com séries

históricas de deslizamentos: relacionar a ocorrência/não ocorrência de eventos em cada célula

com o valor do índice e, a partir daí, derivar curvas de probabilidade 𝑃(deslizamento ∣ ıˊndice).

Isso  permitiria,  por  exemplo,  dizer  que  em  um  trecho  de  linha  com  𝐼𝑆𝑆  elevado  e  𝑅𝑋5𝑑𝑎𝑦

acima de um limiar, a probabilidade anual de um deslizamento que afete uma torre é de  𝑋%,

comparação que é extremamente útil para análise de risco e priorização de obras de contenção.

Finalmente,  para  fins  de  mudança  climática  até  2050,  seria  importante  explicitar  como

𝑅𝑋5𝑑𝑎𝑦, 𝐶𝑊𝐷 e 𝑅𝑋𝑋𝑚𝑚 são projetados com modelos climáticos (CMIP6), de modo a estimar

o aumento na frequência ou intensidade dos cenários desencadeadores de deslizamentos, em

particular nas regiões de encosta onde se localizam linhas de transmissão e acessos.

3.5.6  Temperatura Máxima (Ondas de calor)

A seção sobre ondas de calor faz uma breve descrição do fenômeno, com referências a padrões

estabelecidos  pela  Organização  Meteorológica  Mundial  (OMM):  “Ondas  de  calor  são

caracterizadas por dias muito quentes com temperaturas máximas acima da média climatológica

com persistência de pelo menos três dias consecutivos (OMM, 2018), para a mesma região e

época  do  ano”.  Após  esta  introdução,  o  documento  apresenta  o  indicador  utilizado  para  a

modelagem das ondas de calor, conforme a equação abaixo:

𝑂𝑛𝑑𝑎𝑠𝑑𝑒𝐶𝑎𝑙𝑜𝑟 =

𝑊𝑆𝐷𝐼+𝐻𝑊.𝐷+𝐻𝑊.𝑁

3

,

na qual:

•  𝑊𝑆𝐷𝐼 (Warm Spell Duration Index) representa contagem anual de dias com pelo menos

três dias consecutivos em que a temperatura diária excede o 90º percentil em relação

ao período de referência;

•  𝐻𝑊. 𝐷 (Heat Wave Duration) representa a duração da maior onda de calor registrada

no ano em dias, sendo calculado considerando pelo menos  três dias consecutivos em

que a temperatura diária excede o  90º percentil em relação ao período de referência,

sendo uma métrica da intensidade desses eventos extremos no período analisado; e

Página 29

•  𝐻𝑊. 𝑁 (Heat Wave Number) representa o número de ondas de calor registradas no ano,

sendo essa onda definida como pelo menos  três dias consecutivos com a temperatura

acima  do  90º  percentil  do  período  de  referência,  proporcionando  uma  métrica  de

recorrência de eventos extremos no período.

O documento ainda informa que “para avaliar o impacto da temperatura que podem exceder os

parâmetros  operacionais  das  linhas  de  transmissão  foi  realizado  também  a  modelagem  de

temperatura máxima para esses ativos”.

Assim  como  para  as  demais  ameaças,  não  fica  clara  abordagem  estatística  utilizada  para

modelar a probabilidade de ocorrência destes eventos, nem quais foram as referências utilizadas

para a construção do indicador proposto.

Há algumas possibilidades de melhoramentos, entre elas:

•  Avaliar a condição previstas nos ativos em projetos versus a condição nos horizontes

futuros.

3.5.7  Aumento do Nível do Mar

O relatório apresenta uma breve descrição das causas do fenômeno, bem as características locais

que causam variação nas suas consequências.  O documento ainda aponta, segundo os modelos

climáticos do IPCC (2021), uma projeção de aumento significativo ao longo deste século.

O estudo utiliza os dados de elevação do nível do  mar provenientes da NASA e da altura da

superfície, proveniente de modelos digitais de elevação. Para essa ameaça climática, a análise

avalia os tempos de retorno (𝑇𝑅)2 considerando os eventos de ressaca e a elevação do nível do

mar, por meio dos seguintes indicadores3:

•  𝐻𝑡𝑖𝑑𝑒: nível da água durante eventos de maré alta;

•  𝑇𝑅100: nível da água durante evento de ressaca que ocorre ou é superado a cada

100 anos;

•  𝑇𝑅1000: nível da água máximo esperado de acordo com série histórica durante

evento de ressaca (similar aos 1000 anos).

2 Os valores de maré alta para cada TR foram calculados a partir da base de dados de ressaca, baseados na metodologia de
tempo de retorno de MUIS et al. (2016).
3 Os indicadores são componentes que captam a frequência e a severidade do evento de aumento do nível do mar.

Página 30

Segundo  o  relatório,  a  metodologia  proprietária  da  WayCarbon,  o  MOVE,  incrementou  as

projeções de aumento do nível do mar feita pela NASA aos valores de ressaca do Global Storm

Surge Reanalysis (GSSR), e esse resultado foi comparado aos valores de MDE.

Como  limitações,  pode-se  apontar  que  apesar  da  boa  base  conceitual,  a  seção  ainda  trata  a

combinação entre Htide, TR100 e TR1000 de forma descritiva, sem explicitar claramente se há

uma fórmula de índice composto, quais pesos são atribuídos a cada componente ou se eles são

usados apenas como cenários discretos; isso dificulta a interpretação quantitativa do risco e a

comparação entre diferentes localidades. A abordagem assume implicitamente que a simples

soma entre o aumento projetado do nível médio do mar e os níveis de ressaca 𝑇𝑅100/𝑇𝑅1000

é  suficiente,  mas  não  discute  incertezas  associadas  aos  modelos  de  projeção  da  NASA,  às

reanálises  de  ressaca  ou  à  qualidade  dos  MDE  utilizados,  o  que  pode  ser  relevante  para

diferenças de poucos decímetros que definem se uma área costeira será ou não inundada. Por

fim, não há uma discussão explícita de probabilidade de ocorrência ao longo do horizonte até

2050  ou  2100,  ou  de  como  esses  níveis  extremos  e  seus  tempos  de  retorno  se  alteram  sob

diferentes  cenários  climáticos,  o  que  é  central  para  decisões  de  projeto  de  longo  prazo  em

infraestrutura elétrica costeira.

Como  sugestões  de  aprimoramentos,  poderia  ser  interessante  explicitar  o  esquema  de

combinação  dos  indicadores,  por  exemplo  definindo  um  índice  adimensional  que  normalize

𝐻𝑡𝑖𝑑𝑒, 𝑇𝑅100 e 𝑇𝑅1000 em relação a uma cota de referência e, se for o caso, atribua pesos

diferenciados (por exemplo, maior peso a 𝑇𝑅100 para horizontes de projeto típicos de 50–100

anos,  e  a  𝑇𝑅1000  para  avaliação  de  segurança  máxima).  Recomenda-se  também  incorporar

uma análise de incerteza, apresentando faixas de variação para o aumento projetado do nível do

mar (por exemplo, cenários de menor e maior aquecimento do IPCC) e para os níveis extremos

de ressaca. Em termos probabilísticos, pode-se traduzir os tempos de retorno em probabilidades

anuais de excedência (por exemplo, TR100 ≈ 1% ao ano, TR1000 ≈ 0,1% ao ano) e, a partir

disso, calcular a probabilidade acumulada de pelo menos um evento de ressaca crítico ocorrer

ao  longo  da  vida  útil  da  infraestrutura  (por  exemplo,  50  anos),  o  que  fornece  informação

diretamente  utilizável  para  dimensionamento  e  análise  custo-benefício  de  medidas  de

adaptação. Finalmente, é recomendável explicitar como as projeções de aumento do nível do

mar  da  NASA  e  os  campos  de  ressaca  se  alteram  sob  diferentes  cenários  de  emissões  (por

exemplo, SSP2-4.5 versus SSP5-8.5), permitindo avaliar em que medida as zonas de inundação

Página 31

costeira e o risco para ativos do sistema de transmissão se expandem em cenários mais severos

de mudança climática.

Há algumas possibilidades de melhoramentos, entre elas:

•  Verificar as cotas dos ativos (torres e subestações).

•  Verificar as cotas de elevação do nível do mar.

Página 32

4  Bases de dados meteorológicos e climáticos

Uma das principais oportunidades identificadas para o aprimoramento da modelagem climática

adotada  no  documento  sob  análise  é  o  enriquecimento  da  diversidade  das  fontes  e  bases  de

dados utilizadas. Para isto, podem ser consideradas bases de dados provenientes de outras fontes

diversas, tanto do Brasil quando do exterior. Esta seção trata sobre este aspecto, a começar pelas

bases de dados oferecidas por instituições nacionais.

4.1  Bases de dados nacionais

Atualmente há um ecossistema relativamente rico de dados meteorológicos públicos no Brasil,

cobrindo séries históricas em superfície, monitoramento por satélite e rede hidrometeorológica.

Abaixo  listamos  as  principais  instituições,  com  foco  no  que  cada  uma  oferece  e  os  links  de

acesso.

4.1.1  Instituto Nacional de Meteorologia

O Instituto Nacional de Meteorologia (INMET) é responsável por monitorar, analisar e prever

o  tempo  e  o  clima  no  Brasil,  operando  uma  rede  de  cerca  de  750  estações  meteorológicas

automáticas e convencionais espalhadas pelo território nacional, além de representar o país na

Organização Meteorológica Mundial (OMM) desde 1950. É a principal fonte de observações

meteorológicas de superfície (estações convencionais e automáticas) em nível nacional4.

Suas principais atribuições incluem a geração diária de previsões do tempo, boletins especiais,

avisos meteorológicos  e estudos  climatológicos aplicados à agricultura, defesa civil e outros

setores  econômicos,  com  destaque  para  o  Banco  de  Dados  Meteorológicos  para  Ensino  e

Pesquisa (BDMEP), que preserva séries históricas desde 1961 (e projetos para digitalizar dados

ainda  mais  antigos).  O  INMET  evoluiu  de  métodos  manuais  de  plotagem  em  mapas  para

tecnologias  modernas,  como  supercomputadores  e  transmissão  via  satélite,  modernizando-se

continuamente com expansão de estações e parcerias para maior precisão em previsões e alertas

sobre eventos extremos como secas e inundações.

4 https://portal.inmet.gov.br/noticias/saiba-como-acessar-os-dados-meteorológicos-

disponíveis-no-site-do-inmet.

Página 33

Abaixo  são  apresentadas,  rapidamente,  algumas  características  das  bases  de  dados

disponibilizadas pelo INMET:

•  Banco de Dados Meteorológicos para Ensino e Pesquisa (BDMEP)

o  Variáveis:  temperatura  máxima/mínima/média,  precipitação  diária,  umidade

relativa, pressão atmosférica, vento, entre outras.

o  Cobertura:  séries  históricas  de  estações  convencionais  da  rede  INMET,  com

milhões de registros, atualizadas em janelas de aproximadamente 90 dias.

o  Formato: arquivos texto/CSV, por estação e período.

o  URL (portal INMET): https://bdmep.inmet.gov.br/

o  Periodicidade: Dados históricos diários.

•  Tabela de Dados de Estações (dados horários/instantâneos, mais recentes)

o  Acesso a dados recentes de estações automáticas, permitindo escolha da estação

e do período (tipicamente dados horários ou subdiários)

o  URL

(portal

INMET

–

Tabela

de  Dados

de

Estações):

https://tempo.inmet.gov.br/TabDadosEstacao

(via  menu  Portal

/  Dados

Meteorológicos).

•  Previsão do tempo e avisos meteorológicos

o  Previsão por município (curto prazo) com temperatura, umidade, chuva, etc.

o  Avisos meteorológicos especiais com área de abrangência, severidade e duração

(chuvas intensas, ondas de calor, etc.).

o  URLs:

▪  Portal principal (previsão): https://portal.inmet.gov.br.

▪  Avisos/alertas: https://alertas2.inmet.gov.br/.

•  APIs e serviços não oficiais/auxiliares

o  Existem  iniciativas  comunitárias  que  encapsulam  os  serviços  do  INMET  em

APIs REST (por exemplo, INMET API em Vercel, wrappers em GitHub).

o  Útil  para

automação,  mas

é

recomendável

sempre

conferir

a

documentação/limites de uso.

o  Exemplo: https://inmet-api-front.vercel.app

4.1.2  Instituto Nacional de Pesquisas Espaciais

O Instituto Nacional de Pesquisas Espaciais (INPE) é uma autarquia federal brasileira vinculada

ao Ministério da Ciência, Tecnologia e Inovações (MCTI). INPE tem como missão principal

Página 34

desenvolver  pesquisas  e  tecnologias  espaciais  civis,  abrangendo  áreas  como  sensoriamento

remoto, meteorologia por satélite, previsão do tempo e clima via Centro de Previsão de Tempo

e  Estudos  Climáticos  (CPTEC),  monitoramento  ambiental  (desmatamento  na  Amazônia  via

PRODES  e  DETER),  geofísica  e  programas  espaciais  como  o  CBERS  (satélites  sino-

brasileiros) e Amazônia-1. Por meio do CPTEC, disponibiliza dados e produtos baseados em

sensoriamento  remoto  (satélites,  radares,  reanálises)  e  ferramentas  de  monitoramento

climático5.

Atualmente,  o  INPE  opera  estações  terrenas  de  recepção  de  dados  de  satélites  (como  em

Cuiabá-MT), supercomputadores para modelagem climática (Tupã), laboratórios de integração

de  satélites  e  programas  de  pós-graduação  pioneiros  desde  1968,  além  de  parcerias

internacionais com China, NASA e Agência Espacial Europeia. Seus dados abertos são cruciais

para  monitoramento  de  queimadas,  projeções  climáticas,  agricultura  e  defesa  civil,  com

plataformas como TerraBrasilis  e plataformas de dados climáticos disponíveis gratuitamente

em https://www.gov.br/inpe/pt-br.

Os principais canais de dados são apresentados abaixo:

•  Portais CPTEC/INPE para monitoramento do clima e tempo

o  Produtos:  mapas  de  precipitação  estimada  por  satélite,  temperatura,  vento,

radiação solar, focos de queimadas, entre outros parâmetros atmosféricos.

o  Ferramentas: visualização interativa e download de dados quantitativos (formato

binário ou texto) para diversos produtos.

o  Exemplo de portal de monitoramento:

▪  Clima

–

Monitoramento

Brasil:

https://clima.cptec.inpe.br/monitoramentobrasil/pt

•  Aplicação DSAT (visualização de satélite)

o

Imagens de satélite em intervalos aproximados de 10 minutos, com histórico de

30 dias, em múltiplos canais espectrais.

o  Permite  regular  opacidade,  escolher  datas,  gerar  animações  e  acessar

informações qualitativas e quantitativas.

5 https://leopardus.com.br/2022/03/31/inpe-permite-acesso-livre-a-dados-e-produtos-

meteorologicos/.

Página 35

o  Acessível via portais de sensoriamento remoto do INPE/CPTEC (referidos como

“DSAT” nas páginas institucionais).

•  Dados abertos INPE

o  Catálogo geral de conjuntos de dados sob política de dados abertos (inclui temas

de meteorologia, clima, queimadas, etc.).[gov]

o  URL: https://www.gov.br/inpe/pt-br/acesso-a-informacao/dados-abertos[gov]

4.1.3  Agência Nacional de Águas e Saneamento Básico

A Agência Nacional de Águas e Saneamento Básico (ANA) é uma autarquia federal brasileira

vinculada  ao  Ministério  da  Integração  e  do  Desenvolvimento  Regional,  com  a  missão  de

implementar a Política Nacional de Recursos Hídricos e regular o uso sustentável da água em

rios de domínio da União. Suas ações incluem outorga e fiscalização do uso da água, cobrança

pelo  recurso  hídrico,  regulação  de  serviços  de  saneamento  básico,  segurança  de  barragens  e

monitoramento de secas/inundações, promovendo gestão participativa via comitês de bacias e

o Sistema Nacional de Gerenciamento de Recursos Hídricos (Singreh).

No  contexto  hidrometeorológico,  a  ANA  coordena  a  Rede  Hidrometeorológica  Nacional

(RHN),  com  quase  23  mil  estações  pluviométricas,  fluviométricas  e  evaporimétricas,

gerenciando diretamente ~4,8 mil postos para medir chuvas, níveis/vazões de rios, evaporação,

sedimentos  e  qualidade  da  água.  Os  dados  estão  disponíveis  no  Sistema  Nacional  de

Informações  sobre  Recursos  Hídricos  (SNIRH)  via  Hidroweb6  com  séries  históricas  e

monitoramento em tempo quase real, essenciais para estudos de balanço hídrico, agricultura e

energia hidrelétrica.

Algumas informações sobre os dados da ANA são apresentadas abaixo:

•  Redes pluviométrica e fluviométrica

o  Parâmetros: chuva (pluviométrica), nível de rios, vazão, evaporação,

sedimentos em suspensão e qualidade de água.

o  Em 2020, a RHN contava com quase 23 mil estações sob diversas entidades; a

ANA gerencia diretamente 4.841 estações, sendo 2.717 pluviométricas e 2.024

fluviométricas.

•  Portais de monitoramento e metadados

6 http://www.snirh.gov.br/hidroweb.

Página 36

o  Portal de monitoramento (SNIRH/ANA): oferece séries históricas e dados em

tempo quase real da rede hidrometeorológica (chuvas, níveis, vazões),

integrados para todo o país.

o  Catálogo de metadados da Rede Hidrometeorológica Nacional: descrição de

estações, parâmetros medidos, localização etc.

o  URLs principais:

▪  Portal de monitoramento ANA (SNIRH – seção

“Monitoreo/Monitoramento”): https://www.gov.br/ana/es/monitoreo-2

(há versões em português no domínio gov.br/ana).

▪  Catálogo de metadados RHN:

https://metadados.snirh.gov.br/geonetwork/srv/api/records/f85dbf06-

a869-414c-afc5-bb01869e9156

4.1.4  Repositórios secundários e iniciativas de dados abertos

Além dos portais institucionais, há repositórios que republicam dados meteorológicos oficiais

em formatos consolidados, úteis para ciência de dados.

•  Base dos Dados – BDMEP (INMET)

o  Repositório  estruturado  do  Banco  de  Dados  Meteorológicos  (BDMEP)  em

formato tabular padronizado (tipicamente para integração com SQL/BigQuery,

etc.).

o

Inclui  metadados  de  estações  e  cobertura  temporal  (por  exemplo,  2000–2025

para a tabela principal).

o  URLs:

▪  Versão

em

português

(Brasil):

https://basedosdados.org/dataset/782c5607-9f69-4e12-b0d5-

aa0f1a7a94e2

▪  Espelho

em

espanhol

(Base

de

los

Datos):

https://basedelosdatos.org/dataset/782c5607-9f69-4e12-b0d5-

aa0f1a7a94e2

•  Repositórios GitHub relacionados ao INMET/BDMEP

o  Scripts e wrappers para automatizar acesso ao BDMEP, incluindo listagem de

variáveis  (precipitação,

temperatura  máxima/mínima,  pressão,  umidade,

visibilidade etc.).

Página 37

o  Exemplo: https://github.com/fabinhojorge/INMET-API-temperature

4.1.5  Limitações e desafios das bases nacionais

Apesar do ecossistema de dados meteorológicos e hidrometeorológicos, a rede de observações

no Brasil ainda apresenta lacunas importantes de cobertura espacial, especialmente em áreas de

baixa  densidade  populacional,  regiões  de  floresta  e  partes  do  semiárido,  o  que  reduz  a

capacidade de caracterizar gradientes climáticos finos e extremos localizados. Além disso, uma

parcela relevante das estações de superfície opera há décadas com infraestrutura envelhecida,

registrando índices elevados de panes e perda de dados, situação que vem sendo reportada tanto

em  estudos  setoriais  quanto  em  análises  de  imprensa  especializada.  Essas  descontinuidades

impactam diretamente a qualidade das normais climatológicas, dos estudos de variabilidade e

dos modelos de previsão numérica dependentes de observações de boa qualidade.

Do  ponto  de  vista  estatístico,  a  literatura  nacional  mostra  que  grande  número  de  séries

climatológicas apresenta problemas de homogeneidade decorrentes de mudanças de localização

de  estações,  substituição  de  instrumentos,  alterações  de  horário  de  observação  e  falhas

prolongadas, gerando quebras artificiais que podem ser confundidas com sinais de tendência

climática.  Por  isso,  diversos  trabalhos  recomendam  a  aplicação  sistemática  de  testes  de

homogeneidade  e  o  uso  de  técnicas  de  reconstrução  de  séries,  como  modelos  SARIMA,

métodos geoestatísticos espaço-tempo e uso de estações vizinhas, sempre com quantificação do

erro  associado  ao  preenchimento.  Na  prática,  contudo,  esses  procedimentos  ainda  não  são

aplicados  de  forma  padronizada  em  escala  nacional,  o  que  leva  pesquisadores  e  analistas  a

realizarem rotinas próprias de controle de qualidade, com resultados nem sempre comparáveis

entre estudos.

Essas  limitações  repercutem  diretamente  na  modelagem  de  riscos  climáticos  e  hidrológicos,

pois  a  subamostragem  de  extremos,  as  falhas  em  períodos  críticos  e  a  heterogeneidade  não

tratada  das  séries  tendem  a  subestimar  ou  distorcer  frequências  de  eventos  raros,  afetando

estimativas de vazões de projeto, dimensionamento de infraestrutura e avaliação de impactos

em setores como energia, agricultura e gestão de desastres. Em estudos de mudanças climáticas,

a  incerteza  adicional  associada  à  qualidade  das  séries  observadas  dificulta  a  calibração  de

modelos regionais, a validação de produtos de reanálise e a construção de indicadores robustos

de tendência, especialmente quando se comparam diferentes regiões do país. Por consequência,

Página 38

análises  de  custo-benefício  de  medidas  de  adaptação  e  resiliência  precisam  explicitar  essas

incertezas de dados, sob risco de superestimar a precisão de projeções e métricas de risco.

Nos  últimos  anos,  instituições  brasileiras  têm  chamado  atenção  para  o  risco  de  deterioração

adicional  das  redes  meteorológica  e  hidrológica,  em  função  de  restrições  orçamentárias,

contingenciamentos  e  redução  de  equipes  técnicas  dedicadas  à  operação  e  manutenção  das

estações. A “Carta Aberta pelo Fortalecimento do Monitoramento Meteorológico e Hidrológico

no  Brasil”,  assinada  por  dezenas  de  entidades  em  2024  (CARTA,  2024),  alerta  que  a

continuidade  de  milhares  de  estações  está  ameaçada,  com  potenciais  perdas  irreversíveis  de

séries centenárias e impactos diretos sobre a segurança hídrica, alimentar, energética e a gestão

de desastres. Esse contexto reforça a necessidade de políticas de Estado ou setoriais voltadas à

recomposição e modernização das redes observacionais, integração entre bases (INMET, INPE,

ANA,  Cemaden,  SGB-CPRM)  e  estabelecimento  de  protocolos  nacionais  de  controle  de

qualidade  e  homogeneização  de  dados,  alinhados  às  recomendações  da  Organização

Meteorológica Mundial.

4.1.6  Síntese executiva por tipo de dado

•  Estações  de  superfície  (temperatura,  precipitação,  vento,  etc.):  INMET  –  BDMEP

(histórico)  e  Tabela  de  Dados  de  Estações  (operacional),  com  acesso  principal  via

https://portal.inmet.gov.br e https://bdmep.inmet.gov.br/.portal.inmet.gov+2

•  Satélites,  radares  e  produtos  de  sensoriamento  remoto  (chuva  estimada,  radiação,

queimadas, etc.): CPTEC/INPE, via portais de monitoramento e DSAT (por exemplo,

https://clima.cptec.inpe.br/monitoramentobrasil/pt

e

https://www.gov.br/inpe/pt-

br/acesso-a-informacao/dados-abertos).[10] )

•  Rede  hidrometeorológica  (chuva,  nível  e  vazão  de  rios,  evaporação,  sedimentos,

qualidade  da  água):  ANA/SNIRH,  com  dados  e  metadados  acessíveis  via

https://www.gov.br/ana

e

o

catálogo

https://metadados.snirh.gov.br/geonetwork/.gov+1.

•  Versões consolidadas para análise de dados da Base dos Dados (BDMEP INMET) em

https://basedosdados.org/dataset/782c5607-9f69-4e12-b0d5-aa0f1a7a94e2.

A  Tabela  3  apresenta  um  resumo  das  fontes  e  dados  disponíveis,  com  foco  em  cobertura
espacial/temporal,  granularidade  e  variáveis,  pensando  em  uso  para  modelos  (por  exemplo,
energia, extremos, hidrologia).

Página 39

Tabela 3 Fontes públicas de dados meteorológicos e hidrometeorológicos – Brasil

Cobertura espacial

Cobertura
temporal típica

Granularidade
temporal

Principais
variáveis
disponíveis

URLs principais

Fonte /
Portal

Tipo de
dado
principal

INMET –
BDMEP
(histórico)

Observações
de superfície
(estações
convenciona
is)

Rede nacional de
estações do INMET

Séries históricas
com milhões de
registros (por
ex. 2000–2025
em versões
consolidadas)in
met+1

Diária (valores
agregados por
dia)[portal.inmet
.gov]

Precipitação
diária, temperatura
máxima/mínima/
média, umidade
relativa, pressão
atmosférica,
vento, entre
outras.inmet+2
Temperatura
instantânea,
umidade,
precipitação
acumulada,
pressão, vento
(direção/velocidad
e), radiação, etc.
(conjunto
completo varia por
estação).[portal.in
met.gov]
Precipitação
observada/total,
temperatura
máxima,
temperatura
mínima,
anomalias de
precipitação e de
temperatura.[clim
a.cptec.inpe]
Campos
atmosféricos
(pressão, vento,
temperatura em
níveis, chuva
prevista, radiação,
etc.), imagens de
satélite
multiespectrais,
descargas
atomosférica,
poluição
atmosférica.educa
cao.cemaden+2
Volume de chuvas
(pluviometria),
nível de rios,
vazão,
evaporação,
sedimentos em
suspensão,
parâmetros de
qualidade da
água.metadados.sn
irh+1

BDMEP INMET:
https://bdmep.inmet.gov.br[bdmep.in
met.gov]; Descrição institucional:
https://portal.inmet.gov.br/servicos/bd
mep-dados-
hist%C3%B3ricos[portal.inmet.gov]

Acesso via portal:
https://portal.inmet.gov.br → menu
“Dados Meteorológicos” → “Tabela
de Dados de Estações” (endereço
usado:
https://tempo.inmet.gov.br/TabDados
Estacao)[5]

Portal de monitoramento:
https://clima.cptec.inpe.br/monitoram
entobrasil/pt[clima.cptec.inpe]

Página de dados abertos INPE:
https://www.gov.br/inpe/pt-br/acesso-
a-informacao/dados-abertos[gov];
Serviço gov.br para modelos
numéricos: https://www.gov.br/pt-
br/servicos/obter-dados-provenientes-
de-modelos-numericos-de-previsao-
de-tempo-inpe-pnt[gov]

Catalogação RHN:
https://metadados.snirh.gov.br/geonet
work/srv/api/records/f85dbf06-a869-
414c-afc5-
bb01869e9156[metadados.snirh.gov];
Acesso a dados (Hidroweb/SNIRH):
http://www.snirh.gov.br/hidroweb/[m
etadados.snirh.gov]; Portal ANA:
https://www.gov.br/ana[gov]

Mesmas variáveis
do BDMEP
(precipitação,
temperatura,
pressão, umidade,
vento etc.), com
esquemas de
dados
padronizados e
documentação
adicional.[basedos
dados]

Dataset na Base dos Dados:
https://basedosdados.org/dataset/782c
5607-9f69-4e12-b0d5-
aa0f1a7a94e2[basedosdados]

INMET –
dados
operaciona
is (Tabela
de Dados
de
Estações)

Observações
em tempo
quase real
de estações
automáticas

Rede nacional de
estações automáticas
do INMET

Principalmente
período recente
(dias/meses
mais
próximos)[porta
l.inmet.gov]

Horária ou
subdiária, a
depender da
estação[portal.in
met.gov]

CPTEC/IN
PE –
Monitoram
ento do
Clima
Brasil

Produtos de
análise/moni
toramento
(gradeados,
mapas)

Grade cobrindo todo
o território brasileiro

Séries mensais
e/ou diárias
conforme o
produto[clima.c
ptec.inpe]

Diária ou mensal
(dependendo do
campo
selecionado)[cli
ma.cptec.inpe]

CPTEC/IN
PE – Dados
e produtos
de modelos
numéricos
e satélite

Saídas de
modelos
numéricos
de previsão
de tempo e
clima,
imagens de
satélite,
outros
produtos
meteorológi
cos

América do Sul /
Brasil (dependendo
do
modelo/produto)edu
cacao.cemaden+1

Depende do
modelo
(previsão
sazonal, diária,
etc.) e do
produto;
atualizações
diárias e
mensaisscielo+1

Horária, diária,
mensal ou
sazonal,
conforme o
produto/modelos
cielo+1

ANA /
SNIRH –
Rede
Hidromete
orológica
Nacional
(Hidroweb)

Hidrometeor
ologia:
chuva, nível
e vazão de
rios,
evaporação,
qualidade da
água,
sedimentos

Rede nacional de
estações
pluviométricas,
fluviométricas,
evaporimétricas, etc.
(quase 23 mil
estações; ANA
diretamente: ~4,8
mil)metadados.snirh
+1

Séries históricas
de
monitoramento
hidrológico
(décadas em
muitos
postos)[metadad
os.snirh.gov]

Diária ou
subdiária,
dependendo do
tipo de estação
(convencional ou
telemétrica)meta
dados.snirh+2

Base dos
Dados –
BDMEP
(consolidad
o para
análise)

Versão
tabular
consolidada
do BDMEP
(INMET)
para ciência
de dados

Rede nacional de
estações
convencionais do
INMET (mesma
base do
BDMEP)[basedosda
dos]

Cobertura
documentada,
por exemplo
2000–2025-12-
31 na tabela
principal[basedo
sdados]

Diária (mantém
granularidade do
BDMEP)[basedo
sdados]

Fonte: FGV CERI.

Página 40

4.2  Principais conjuntos internacionais

4.2.1  ERA5 – Reanálise global (ECMWF/Copernicus)

O ERA5 é a quinta geração de reanálise atmosférica global produzida pelo European Centre for

Medium-Range  Weather  Forecasts  (ECMWF)  no  âmbito  do  Copernicus  Climate  Change

Service (C3S). Ele combina um modelo numérico de previsão do tempo com um vasto conjunto

de observações (satélites, sondagens, estações de superfície e outros sistemas) para gerar um

campo global completo e fisicamente consistente do estado da atmosfera, da superfície terrestre

e de componentes oceânicos, desde 1940 até o presente, em grade de aproximadamente 31 km,

com estimativas horárias para muitas variáveis. A reanálise resolve a atmosfera em 137 níveis

verticais, desde a superfície até cerca de 80 km de altura, o que permite estudar desde processos

de superfície até a alta troposfera e estratosfera.

Além de substituir a geração anterior ERA-Interim, o ERA5 introduz melhorias importantes na

representação  da  circulação  atmosférica,  do  ciclo  hidrológico,  de  ciclones  tropicais  e  dos

balanços de energia, e inclui ainda um componente  de  ensemble em resolução reduzida para

fornecer  estimativas  de  incerteza  espacial  e  temporal.  O  conjunto  de  dados  é  amplamente

utilizado em climatologia, hidrologia, estudos de energia (eólica, solar, demanda), pesquisa em

eventos extremos e aplicações em aprendizado de máquina, justamente por oferecer uma série

longa, global, densa no tempo (horária) e com múltiplas variáveis atmosféricas, de superfície e

oceânicas em formato padronizado.

•  Tipo de dado: reanálise atmosférica global (modelo + assimilação de observações).

•  Cobertura espacial: global, grade ~31 km (0,25° × 0,25°).

•  Cobertura temporal: de 1940 até o presente, com atualização quase em tempo real.

•  Granularidade temporal: horária.

•  Variáveis principais:

o  Superfície / níveis únicos: temperatura a 2 m, precipitação total, vento a 10 m,

radiação de onda curta/longa (fluxos à superfície e no topo), pressão ao nível do

mar, umidade específica/relativa, neve, evapotranspiração, etc.

o  Níveis de pressão: campos 3D de temperatura, vento, umidade, geopotencial em

137 níveis da superfície a ~80 km.

•  URLs:

Página 41

o  Descrição

ERA5

(ECMWF):

https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5

o  Download

(Climate

Data

Store):

https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels

4.2.2  NOAA NCEI – Integrated Surface Database (ISD) e GSOD

O  National  Oceanic  and  Atmospheric  Administration  (NOAA)  é  uma  agência  científica  e

regulatória do governo dos Estados Unidos, vinculada ao Departamento de Comércio, criada

em  1970  para  monitorar  e  prever  condições  oceânicas  e  atmosféricas,  emitir  previsões

meteorológicas,  gerenciar  recursos  pesqueiros,  proteger  ecossistemas  marinhos  e  estudar

mudanças climáticas.

O  National  Centers  for  Environmental  Information  (NCEI)  é  uma  agência  do  NOAA

responsável pelo arquivamento, preservação, monitoramento e disponibilização pública de um

dos  maiores  acervos  globais  de  dados  ambientais,  abrangendo  atmosfera,  oceanos,  costas,

geofísica  e  clima,  com  mais  de  60  petabytes  de  informações  coletadas  de  satélites,  estações

terrestres, boias e outros sistemas.

O  NOAA  NCEI  Integrated  Surface  Database  (ISD)  é  um  banco  de  dados  global  que  reúne

observações meteorológicas de superfície horárias e sinóticas de mais de 35.000 estações ao

redor  do  mundo,  compiladas  a  partir  de  diversas  fontes  em  um  formato  ASCII  comum  e

padronizado. Desenvolvido desde 1998 pelo National Centers for Environmental Information

(NCEI,  ex-National  Climatic  Data  Center),  o  ISD  inclui  dados  desde  1901,  com  aumento

significativo na década de 1940 e nos anos 1970, abrangendo parâmetros como velocidade e

direção do vento, rajadas, temperatura, ponto de orvalho, nuvens, pressão ao nível do mar e na

estação,  visibilidade,  precipitação  acumulada  em  vários  períodos,  profundidade  de  neve  e

condições presentes. Atualmente, mais de 14.000 estações ativas são atualizadas diariamente,

totalizando cerca de 600 GB não comprimidos, com controle de qualidade automatizado para

formatação, valores extremos, consistência entre parâmetros e continuidade temporal.

O Global Summary of the Day (GSOD), por sua vez, é um produto derivado do ISD que oferece

resumos  diários  agregados  de  cerca  de  9.000-10.000  estações,  calculando  médias  diárias  de

temperatura, ponto de orvalho, pressão ao nível do mar e na estação, visibilidade e velocidade

do vento, além de máximas/mínimas de temperatura, rajada máxima sustentada, precipitação

Página 42

total, profundidade de neve e indicadores de tempo (neblina, tempestades etc.). Disponível em

formato fixo de largura e hospedado em repositórios como AWS Open Data, o GSOD é ideal

para análises climatológicas rápidas e estudos de longo prazo, mantendo a cobertura temporal

do ISD (1929-presente, com boa completude pós-1973), mas com menor granularidade espacial

e temporal em comparação ao ISD horário.

Abaixo  são  apresentadas,  rapidamente,  algumas  características  das  bases  de  dados

disponibilizadas pelo ISD e GSOD:

•  Tipo de dado: observações de superfície (estações meteorológicas) globais.

•  Cobertura espacial: mais de 20.000 estações com dados horários/sinóticos (ISD);

aproximadamente 9.000 estações com resumos diários (GSOD).

•  Cobertura temporal: histórico desde 1929, com melhor completude a partir de 1973.

•  Granularidade temporal:

o

ISD: horária e sinótica, em formato ASCII padronizado.

o  GSOD: diária, derivada do ISD.

•  Variáveis principais:

o  Horárias: temperatura, ponto de orvalho, pressão ao nível do mar e na estação,

visibilidade,  vento,  precipitação,  tempo  presente  (códigos  de  tempo),  entre

outras.

o  Diárias:  temperatura  média/máxima/mínima,  velocidade  média  do  vento,

precipitação,  profundidade  de  neve,  rajadas  máximas,  indicadores  de  tempo

(neblina, tempestades, etc.).

•  URLs:

o

ISD / Global Hourly: https://www.ncei.noaa.gov/products/land-based-

station/integrated-surface-database

o  Busca de dados (Global Hourly):

https://www.ncei.noaa.gov/access/search/data-search/global-hourly

o  GSOD em AWS Open Data: https://registry.opendata.aws/noaa-gsod/

4.2.3  NASA POWER

NASA  Langley  Research  Center  (LaRC)  é  o  mais  antigo  centro  de  pesquisa  de  campo  da

NASA,  fundado  em  1917  como  Langley  Memorial  Aeronautical  Laboratory  pela  NACA

(precursora  da  NASA),  localizado  em  Hampton,  Virgínia,  EUA.  Inicialmente  focado  em

Página 43

pesquisa aeronáutica com túneis de vento pioneiros (incluindo o maior do mundo na época, de

30x60 pés), o LaRC expandiu-se para ciências espaciais durante a era Apollo, contribuindo com

design de módulos lunares, simuladores de rendezvous e redes de rastreamento global, além de

missões como Viking em Marte e instrumentos para rovers modernos.

O  Prediction  Of  Worldwide  Energy  Resources  (NASA  POWER)  é  um  projeto  da  NASA

Langley  Research  Center  que  fornece  dados  meteorológicos  e  de  energia  solar  derivados  de

observações por satélite e modelos de assimilação, como Modern-Era Retrospective analysis

for Research and Applications, Version 2, (MERRA-2) e Clouds and the Earth's Radiant Energy

System  (CERES),  com  cobertura  global  em  grades  de  aproximadamente  0,5°  desde  1981

(diários/horários) até quase tempo real. Voltado para aplicações práticas em energia renovável

(solar,  eólica),  eficiência  de  edifícios  e  agroclimatologia,  o  POWER  oferece  mais  de  380

parâmetros, incluindo irradiância solar global/difusa/UV (sob céu real e limpo), temperatura a

2 m, vento a 10/50 m, umidade relativa, pressão de superfície, precipitação, evapotranspiração

e índices derivados como graus-dia de aquecimento/resfriamento.

Acessível  via  portal  web  interativo  (https://power.larc.nasa.gov),  APIs  REST,  serviços  de

imagem  geoespaciais  e  visualizador  Data  Access  Viewer,  o  POWER  facilita  análises  de

viabilidade para projetos fotovoltaicos, dimensionamento eólico, balanços térmicos de edifícios

e zoneamento agrícola, com dados  analysis ready em formatos CSV/NetCDF para múltiplas

escalas  temporais  (horária,  diária,  mensal,  climatológica).  É  amplamente  usado  por

engenheiros, agrônomos e tomadores de decisão em todo o mundo, com pacotes clientes como

nasapower em R e bibliotecas Python (disponíveis no GitHub) para automação.

Abaixo  são  apresentadas,  rapidamente,  algumas  características  das  bases  de  dados

disponibilizadas pelo NASA POWER:

•  Tipo de dado: meteorologia de superfície, energia solar e climatologia para aplicações

em energia, agricultura e construção.

•  Cobertura espacial: global, em grades de resolução variável (típico ~0,5°), derivadas

de reanálises como MERRA-2 e produtos de radiação CERES.

•  Cobertura temporal: séries históricas diárias e horárias (para alguns parâmetros) por

várias décadas; detalhes por variável na documentação.

•  Granularidade temporal: diária, mensal, climatológica e, para muitos parâmetros,

horária.

Página 44

•  Variáveis principais (exemplos):

o  Meteorologia: temperatura a 2 m (T2M), umidade, pressão à superfície, vento

a 10 m e 50 m (velocidade e direção).

o  Radiação: irradiância global, difusa, UV, PAR, sob céu limpo e céu real

(parâmetros ALLSKY_SFC_PAR_TOT, ALLSKY_SFC_UVB, etc.).

o  Derivados climáticos (graus-dia etc.) para aplicações agrícolas e de energia.

•  URLs:

o  Portal principal: https://power.larc.nasa.gov.

o  Documentação / API (via pacote R nasapower): https://CRAN.R-

project.org/package=nasapower

4.2.4  Panorama resumido (internacional)

A Tabela 4 apresenta um resumo das fontes e dados internacionais disponíveis.

Página 45

Tabela 4 Fontes públicas de dados meteorológicos e hidrometeorológicos – Internacionais
Fonte /
Portal

Granularidad
e temporal

Tipo de dado
principal

Cobertura
espacial

Cobertura
temporal

URLs principais

ERA5
(ECMWF/C
opernicus)

Reanálise
atmosférica
global
(modelo +
observações)

Global,
grade ~31
km

1940–presente,
atualização contínua

Horária

Principais
variáveis
Temperatura 2 m,
precipitação,
vento 10 m,
radiação, pressão
ao nível do mar,
umidade, neve,
ET, campos 3D
em 137 níveis.

Descrição:
https://www.ecmwf.int/en/for
ecasts/dataset/ecmwf-
reanalysis-v5[ecmwf];
Dados:
https://cds.climate.copernicus
.eu/datasets/reanalysis-era5-
single-levels

NOAA
NCEI – ISD
/ Global
Hourly

NOAA –
GSOD

NASA
POWER

Observ
ações
de
superfí
cie
horária
s e
sinótica
s

Resum
o diário
derivad
o do
ISD

Meteor
ologia
de
superfí
cie,
radiaçã
o solar,
climato
logia

>20.000 estações
globais

Desde 1929 (melhor
desde 1973)

Horária
sinótica

~9.000 estações
globais

1929–presente, com
boa completude
pós-1973

Diária

Temperatura,
ponto de orvalho,
pressão, vento,
visibilidade,
precipitação,
tempo presente,
etc.

Produto:
https://www.ncei.noaa.gov/pr
oducts/land-based-
station/integrated-surface-
database; Busca:
https://www.ncei.noaa.gov/ac
cess/search/data-
search/global-hourly

Temperatura
média/máx/mín,
vento médio,
precipitação,
neve, rajada
máxima,
indicadores de
tempo.

AWS Open Data:
https://registry.opendata.aws/
noaa-gsod/

Global (grade
~0,5°)

Várias décadas
(detalhe por variável)

Diária, mensal,
climatológica e
horária (para
vários
parâmetros)

T2M, vento
10/50 m, pressão,
umidade,
irradiância
global/difusa/UV,
PAR, índices
climáticos para
energia/agro

Portal:
https://power.larc.nasa.gov;
Doc/API: https://CRAN.R-
project.org/package=nasapo
wer

Fonte: FGV CERI.

Página 46

5  Conclusões

O  projeto  inicial  apresenta  uma  abordagem  metodológica  para  a  aplicação  e  alinhada  às

principais referências internacionais para avaliação de riscos climáticos físicos, em especial às

recomendações  da  TCFD/ISSB  e  ao  arcabouço  científico  do  IPCC  (AR6/CMIP6).  A

estruturação das análises a partir de cenários de emissões (SSPs) e de janelas climatológicas de

20 anos estabelecidas por  entidades internacionais  confere robustez científica às inferências,

reduzindo  a  influência  da  variabilidade  interanual  e  evitando  interpretações  baseadas  em

eventos isolados. O projeto tem ainda algumas limitações que são identificadas pelos autores.

Entre os principais pontos positivos, destaca-se:

•  A clareza conceitual na distinção entre ameaça climática, impacto e risco, reconhecendo

explicitamente que o escopo atual do trabalho se concentra na avaliação de tendências

e exposição climática, deixando a análise detalhada de vulnerabilidade dos ativos para

etapas posteriores;

•  O  uso  sistemático  de  indicadores  consolidados  de  extremos  climáticos,  amplamente

reconhecidos  na  literatura  científica,  o  que  assegura  transparência  metodológica,

rastreabilidade e comparabilidade dos resultados;

•  A  incorporação  de  fatores  físicos  e  ambientais  (topografia,  uso  e  cobertura  do  solo,

morfometria,  suscetibilidade  do  terreno)  na  caracterização  de  ameaças  como

inundações, incêndios florestais e deslizamentos, indo além de uma análise puramente

climatológica;

•  O  reconhecimento  explícito  das  limitações  inerentes  aos  modelos  climáticos  globais,

especialmente  para  fenômenos  locais  e  convectivos  (rajadas  de  vento,  descargas

atmosféricas,  microdrenagem),  com  encaminhamento  adequado  dessas  questões  para

análises complementares;

•  A orientação clara à priorização de ativos críticos, compatível com a lógica de gestão

de  risco  corporativo  e  com  a  necessidade  de  apoiar  decisões  estratégicas  e  de

planejamento de adaptação.

Apesar dessas virtudes, o projeto também apresenta limitações, que têm consequências sobre o

grau  de  detalhamento  e  a  aplicabilidade  operacional  direta  dos  resultados  e  que  podem  ser

tratadas como oportunidades de aprimoramento metodológico. Em particular, observa-se que:

Página 47

•  As análises não incorporam explicitamente modos de variabilidade climática de grande

escala como El Niño/La Niña, que são reconhecidamente relevantes para a modulação

interanual de extremos de precipitação e ondas de calor em diversas regiões do Brasil.

A ausência dessa condicionante pode ocultar diferenças relevantes no comportamento

das ameaças sob estados climáticos específicos;

•  O  projeto  não  dá  indícios  de  contemplar  a  geração  de  cenários  climáticos  em  grade

regular,  com  resolução  espacial  e  temporal  refinada,  nem  um  pipeline  explícito  de

regridding,  bias  correction  ou  downscaling.  Como  consequência,  os  resultados  são

majoritariamente  expressos  por  índices  agregados  de  ameaça,  e  não  por  campos

climáticos contínuos que permitiriam análises espaço-temporais mais detalhadas;

•  A  vulnerabilidade  física  e  operacional  dos  ativos  ainda  não  é  modelada  de  forma

quantitativa, permanecendo dependente de avaliações posteriores baseadas em dados de

engenharia,  características  construtivas,

limiares  operacionais  e  histórico  de

manutenção;

•  A  incerteza  associada  aos  cenários  climáticos,  aos  modelos  utilizados  e  aos  próprios

indicadores não é plenamente explorada ou comunicada, o que poderia limitar o uso dos

resultados  em  processos  decisórios  que  demandam  avaliação  explícita  de  risco  e

robustez.

•  Conforme apontado ao longo do texto, há a necessidade de aprimorar as bases de dados

climáticos e meteorológicos nacionais. Essa melhoria deve se dar tanto do ponto de vista

da  manutenção  e  atualização  das  estações  meteorológicas  já  existentes,  quanto  da

expansão do parque de medições com o objetivo tornar cobrir todo o território nacional

adequada.

Considerando todos os apontamentos, uma evolução natural do projeto seria a complementação

da análise de ameaças com abordagens condicionadas a estados climáticos ativos, bem como a

incorporação  de  uma  etapa  de  harmonização  e  refinamento  espacial  e  temporal  dos  dados

climáticos,  permitindo  maior  integração  com  dados  de  observação  da  Terra,  reanálises  e

informações específicas dos ativos. Tais avanços não substituem  a metodologia atual, mas a

fortalecem, ampliando sua capacidade de apoiar análises de vulnerabilidade, risco sistêmico e

definição de planos de adaptação mais direcionados.

Em  síntese,  o  projeto  mapeia  e  prioriza  ameaças  climáticas  físicas  em  escala  estratégica,

oferecendo uma base para a gestão de riscos climáticos. Ao mesmo tempo, apresenta espaço

Página 48

claro  para  aprofundamentos  metodológicos  que  podem  aumentar  significativamente  sua

relevância operacional e seu valor para o planejamento de médio e longo prazo da companhia.

Página 49

6  Referências

ANEEL.  Relatório  de  análise:  Desligamentos  forçados  dos  sistemas  de  transmissão.
Brasília, DF: Agência Nacional de Energia Elétrica, 2023.
ASSOCIAÇÃO  BRASILEIRA  DE  GEOLOGIA  DE  ENGENHARIA  E  AMBIENTAL
(ABGE).  Geologia  de  engenharia.  Editores:  A.  M.  S.  Oliveira;  S.  N.  A.  Brito.  São  Paulo:
ABGE, 1998.

CARTA  apoio  redes:  versão  27  nov.  2024. Microsoft  Word  -  CARTA  APOIO
REDES_versão_27nov2024.
Disponível
em: https://www.gov.br/ana/pt-br/assuntos/noticias-e-eventos/noticias/carta-aberta-pelo-
fortalecimento-do-monitoramento-meteorologico-e-hidrologico-no-brasil/carta-apoio-
redes_versao_10dez2024.pdf  Acesso em: 9 mar. 2026.

Brasília,

2024.

ANA,

DF:

INSTITUTO  NACIONAL  DE  PESQUISAS  ESPACIAIS  (INPE).  2024.  Sistema  elétrico:
relâmpagos
em:
http://www.inpe.br/webelat/homepage/menu/infor/relampagos.e.efeitos/sistema.eletrico.php.
Acesso em: 11 jan. 2026.

Disponível

efeitos.

seus

e

IPCC. Climate Change 2021: The Physical Science Basis. Contribution of Working Group I
to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. MASSON-
(eds.).  Cambridge:  Cambridge  University  Press,  2021.
DELMOTTE,  V.  et  al.
doi:10.1017/9781009157896. Acesso em: 11/fev./2026.

MUIS,  S.  et  al.  A  global  reanalysis  of  storm  surges  and  extreme  sea  levels.  Nature
Communications, v. 7, n. 1, p. 11969, 2016.

NASA EARTH OBSERVATORY. A Global View of Landslide Susceptibility.  Greenbelt,
MD, 2017. Disponível em: https://earthobservatory.nasa.gov/images/89937/a-global-view-of-
landslide-susceptibility. Acesso em: 11/fev./2026.

NASCIMENTO, D. T. F. et al. Mapeamento da Suscetibilidade e Potencialidade a Processos
Erosivos Laminares e Lineares ao longo do duto OSBRA da Petrobras. UNESP, Geociências,
2016.
https://www.revistageociencias.com.br/geociencias-
arquivos/35/volume35_4_files/35-4-artigo-07.pdf. Acesso em: 11 fev. 2026.

Disponível

em:

NUNES, J. R. S. et al. Fma+ - um novo índice de perigo de incêndios florestais para o estado
do Paraná, Brasil. Floresta, v. 36, n. 1, 2006.

RAKOV,  V.  A.;  UMAN,  M.  A.  Lightning:  Physics  and  Effects.  Cambridge:  Cambridge
University Press, 2003.

SCHROEDER,  M.  A.  O.  Modelo  Eletromagnético  para  Descontaminação  de  Ondas  de
Corrente  de  Descargas  Atmosféricas:  Aplicação  às  Medições  da  Estação  do  Morro  do
Cachimbo. 2001. Tese (Doutorado) – Universidade Federal de Minas Gerais, Belo Horizonte,
2001. Disponível em: https://www.ppgee.ufmg.br/defesas/683M.PDF.

Página 50

SOARES, R. V. Determinação de um índice de perigo de incêndio para a região centro
paranaense, Brasil. 1972. Dissertação (Mestrado) – Instituto Interamericano de Ciências
Agrícolas da OEA, Turrialba, 1972.

SOARES, R. V. Desempenho da “Fórmula de Monte Alegre”  índice brasileiro de perigo de
incêndios florestais. Cerne, v. 4, n. 1, p. 87-99, 1998.

VAN WAGNER, C. E. Calculations on forest fire spread by flame radiation. Ottawa: Queen's
Printer and Controller of Stationery, 1967.

WEBER, R. O. Analytical Models for Fire Spread Due to Radiation. Combustion and Flame,
v. 78, p. 398-408, 1989.

WORLD  METEOROLOGICAL  ORGANIZATION  (WMO).  Guidelines  on  the  definition
and  monitoring  of  extreme  weather  and  climate  events.  2018.  Disponível  em:
https://library.wmo.int/viewer/58396/download?file=1310_Guidelines_on_DEWCE_en.pdf&
type=pdf&navigator=1. Acesso em: 11/fev./2026.

Página 51

7

Glossário

ABGE (Associação Brasileira de Geologia de Engenharia e Ambiental): Entidade que
classifica e codifica fatores condicionantes de deslizamentos e outros processos geológicos,
sendo a referência para os condicionantes físicos de movimentos de massa.

Altimetria (𝒂𝒍𝒕): Elevação topográfica extraída de Modelos Digitais de Elevação (MDE),
utilizada como fator de suscetibilidade a incêndios e deslizamentos.

Ameaça climática: Fenômeno meteorológico ou geofísico extremo associado a mudanças
climáticas com potencial de impacto em ativos de transmissão (ex.: tempestades, incêndios,
inundações, deslizamentos).

BDMEP  (Banco  de  Dados  Meteorológicos  para  Ensino  e  Pesquisa):  Repositório  do
INMET que preserva séries históricas de observações de superfície desde 1961.

Bias  Correction  (Correção  de  Viés):  Ajuste  estatístico  aplicado  às  saídas  de  modelos
climáticos para alinhar as projeções com as observações históricas reais, visando reduzir
discrepâncias sistemáticas.

CPTEC  (Centro  de  Previsão  de  Tempo  e  Estudos  Climáticos):  Unidade  do  INPE
responsável pelo desenvolvimento de pesquisas, tecnologias espaciais e modelos numéricos
de previsão de tempo e clima no Brasil.

CWD (Consecutive Wet Days): Número máximo de dias consecutivos com precipitação
>1 mm no ano, servindo como indicador de saturação do solo para análise de deslizamentos.

Declividade (𝒅𝒆𝒄): Inclinação do terreno em graus (0-90°), calculada a partir de MDE; é o
principal fator de suscetibilidade a deslizamentos em encostas.

Downscaling: Técnica utilizada para aumentar a resolução espacial de modelos climáticos
globais  (GCMs),  permitindo  a  obtenção  de  informações  climáticas  em  escala  local  ou
regional.

ERA5:  Quinta  geração  de  reanálise  atmosférica  global  do  ECMWF,  fornecendo  dados
horários de clima e superfície desde 1940 em grade de aproximadamente 31 km.

ETCCDI (Expert Team on Climate Change Detection and Indices): Conjunto padrão
de 27 índices de extremos climáticos validados globalmente, utilizado no relatório para o
cálculo de tempestades, inundações e deslizamentos.

𝑭𝑴𝑨 + (Fórmula de Monte Alegre Alterada): Índice brasileiro de perigo de incêndios
baseado  em  umidade  relativa,  vento  e  seca,  fundamentado  nos  estudos  de  Soares  (1972,
1998) e Nunes et al. (2006).

GSSR (Global Storm Surge Reanalysis): Reanálise global utilizada para a estimativa de
ressacas e níveis extremos do mar (𝑇𝑅100 e 𝑇𝑅1000) (Muis et al. 2016).

Página 52

𝑯𝒕𝒊𝒅𝒆: Nível da água durante eventos de maré alta, utilizado na modelagem de ameaças
costeiras em combinação com ressacas e aumento do nível do mar.

𝑰𝑴  (Índice  Morfométrico):  Indicador  composto  pela  Ordem  de  Strahler,  declividade  e
distâncias  vertical/horizontal  aos  rios;  atua  como  proxy  para  a  propensão  a  inundações
fluviais.

𝑰𝑵 (Índice de Inundação): Cálculo que combina a precipitação extrema (𝑅𝑥1𝑑𝑎𝑦, 𝑅95𝑝,
𝑅𝑋𝑋𝑚𝑚) com as características do terreno (𝐼𝑀).

Incêndios  florestais:  Propagação  de  fogo  em  vegetação  influenciada  por  drivers
meteorológicos; a modelagem de sua intensidade considera fundamentos da física do fogo
e radiação propostos por Van Wagner (1967) e Weber (1989).

Inundações  fluviais:  Transbordamento  de  corpos  hídricos  causado  por  precipitação
excessiva em combinação com a morfologia da bacia; o fenômeno é distinto de alagamentos
pluviais urbanos que dependem de microdrenagem.

IPCC AR6 (Sexto Relatório de Avaliação do IPCC): Base científica para os cenários SSP
e projeções de extremos climáticos adotados neste estudo.

ISS  (Índice  de  Suscetibilidade  do  Solo):  Indicador  que  combina  pedologia,  geologia  e
geomorfologia  (NASA  2017)  com  curvaturas  do  terreno  (Topodata/INPE)  para  mapear
riscos de deslizamento.

MapBiomas:  Plataforma  de  mapeamento  anual  de  cobertura  e  uso  da  terra  no  Brasil
(Coleção 8), essencial para definir a variável vegetação em modelos de incêndio.

MDE  (Modelo  Digital  de  Elevação):  Representação  matemática  da  altitude  do  terreno
utilizada para derivar declividade, curvaturas e índices morfométricos.

MOVE: Metodologia proprietária da WayCarbon para análise de riscos climáticos.

NASA  (2017):  Mapa  global  de  suscetibilidade  a  deslizamentos  que  integra  dados  de
infraestrutura, desmatamento, geologia e topografia.

Ordem de Strahler: Hierarquia numérica usada para classificar a magnitude e ramificação
dos canais dentro de uma rede de drenagem hidrológica.

𝑹𝟗𝟓𝒑: Precipitação anual total acima do 95º percentil histórico, representando dias com
chuvas muito úmidas.

𝑹𝒙𝟏𝒅𝒂𝒚: Máxima precipitação diária anual (em mm), utilizada como indicador para cheias
convectivas e tempestades intensas.

𝑹𝒙𝟓𝒅𝒂𝒚: Máxima precipitação acumulada em 5 dias consecutivos, principal gatilho para
deslizamentos devido à saturação prolongada do solo.

Página 53

𝑹𝑿𝑿𝒎𝒎:  Número  de  dias  anuais  com  precipitação  considerada  outlier  (acima  do  95º
percentil regional).

SNIRH / Hidroweb: Sistemas da Agência Nacional de Águas (ANA) que disponibilizam
dados da Rede Hidrometeorológica Nacional, incluindo séries históricas de vazões e níveis
de rios.

SSP  (Shared  Socio-economic  Pathways):  Cenários  socioeconômicos  do  IPCC  que
descrevem  diferentes  trajetórias  de  emissões  e  desenvolvimento  global  (ex:  SSP1-2.6,
SSP2-4.5).

Indicador de Tempestades: Índice composto que combina a máxima precipitação diária
(𝑅𝑥1𝑑𝑎𝑦), a precipitação extrema (𝑅99𝑝) e a velocidade máxima do vento (𝑊𝑋1𝑑𝑎𝑦).

Tempo de Retorno (𝑻𝑹): Intervalo médio de recorrência estimado para um evento extremo
de determinada magnitude (ex: 𝑇𝑅100 possui 1% de chance de ocorrer anualmente).

𝑾𝟗𝟎𝒑: Frequência anual de ventos com velocidade acima do 90º percentil histórico.

𝑾𝑿𝟏𝒅𝒂𝒚: Máxima velocidade média diária de vento registrada em um ano, expressa em
𝑚/𝑠.

Página 54

8

Anexos

ANEXO 1 – Reunião de Kick Off do Projeto

•  Data: 12/12/2025

•  Objetivo: Alinhamento inicial de expectativas, definição do cronograma e

apresentação da equipa técnica do FGV CERI e da ISA ENERGIA BRASIL.

•  Arquivo: KickOff-FGVCERI-ISAEnergiaBrasil-12-12-2025.PPTX

ANEXO 2 – Reunião de Acompanhamento Técnico

•  Data: 07/01/2026

•  Objetivo: Discussão sobre o progresso da recolha de dados e revisão preliminar das

ameaças climáticas.

•  Arquivo: Reunião-FGVCERI-ISAEnergiaBrasil-07-01-2026.pptx

ANEXO 3 – Reunião de Acompanhamento Técnico

•  Data: 21/01/2026

•  Objetivo: Validação da metodologia de cálculo das probabilidades e alinhamento

sobre as bases de dados nacionais (INMET/INPE).

•  Arquivo: Reunião-FGVCERI-ISAEnergiaBrasil-21-01-2026.pptx

ANEXO 4 – Reunião Técnica com Consultoria Externa (WayCarbon)

•  Data: 29/01/2026

•  Objetivo: Revisão crítica da modelagem anterior, discussão sobre o "valor bruto" das

ameaças e identificação de oportunidades de melhoria metodológica.

•  Arquivo: Reunião-FGVCERI-ISAEnergiaBrasil-29-01-2026.pptx

ANEXO 5 – Reunião de Fechamento do Produto 1

•  Data: 04/02/2026

•  Objetivo: Apresentação final dos achados do relatório de revisão da modelagem

climática e validação do sumário executivo.

•  Arquivo: Reunião-FGVCERI-ISAEnergiaBrasil-04-02-2026.pptx

Página 55

Resiliência da Transmissão
de Energia Elétrica
a Eventos Climáticos
Extremos

Reunião de Kick Off

Agenda

• Objetivos
• Escopo
• Premissas
• Roadmap
• Time
• Riscos Mapeados

Agenda

• Objetivos
• Escopo
• Premissas
• Roadmap
• Time
• Riscos Mapeados

Objetivos

Construir  um  dashboard/plataforma  de  gestão  de  riscos  climáticos

associados  às

linhas  de  transmissão  da  Isa  Energia  Brasil.  O

dashboard  deverá  antecipar  riscos  e  contribuir  para  a  avaliação  da

vulnerabilidade das linhas e impactos no serviço.

A partir dele será possível:

• Analisar custos e benefícios de investimentos

• Propor aprimoramentos regulatórios

Agenda

• Objetivos
• Escopo
• Premissas
• Roadmap
• Time
• Riscos Mapeados

A Abordagem a ser utilizada

O projeto de PDI será iniciado contemplando os avanços já obtidos

pela  Isa  Energia  Brasil  na  modelagem  climática  para  antecipar

riscos e na avaliação da vulnerabilidade das linhas.

Missões Internacionais

O  projeto  prevê  a  realização  de  missões  internacionais  para  entender  como  outros  países  estão  lidando
com temas relacionados aos que são abordados neste projeto de PDI. Alguns possíveis destinos:

EUA:  Nova  Jersey  e  Pensilvânia,  Nova  York,  Flórida,  Lousiana,  Arkansas.  Reuniões  com  reguladores,
operadores e empresas que possuem experiência em lidar com furações, inundações por conta de eventos
como Katrina, Sandy, entre outros.

China: Grande sistema de inovação global, com uso de tecnologia em infraestrutura e experiência em lidar
com clima árido e enchentes.

Japão: Benchmark em resiliência pela ocorrência constante de terremotos. Cidade projetada pela Toyota é
referência em inovações em infraestrutura.

Noruega  e  Suécia:  Polos  de  inovação  energética  e  otimização  para  extremos  climáticos.  Laboratório  da
Cruz Vermelha atuou na enchente do RS.

Mestrado Profissional

O  projeto  prevê  a  realização  de  um  curso  de  mestrado

profissional  em  Economia  na  Escola  de  Pós-Graduação  em

Economia  da  Fundação  Getulio  Vargas  (FGV  EPGE),  com  ênfase

em  economia  da  infraestrutura  e  regulação.  O  mestrado  tem  a

duração prevista de dois anos.

Modelagem dos Impactos
do Clima na Transmissão

A modelagem dos impactos na transmissão envolve:

• Uso da modelagem já realizada pela Isa Energia Brasil

na avaliação da vulnerabilidade das linhas e impactos

em serviço

•

•

Identificação de oportunidades e implementação

daquelas que forem aprovadas pela Isa Energia Brasil

Discussão de premissas com profissionais da Isa

Energia Brasil para simulação dos impactos dos

eventos futuros

Modelagem de Engenharia e
Finanças

• Construção de alternativas que contemplem aumento de resiliência e

adaptação das instalações

•

Simulação de impactos com uso de novos equipamentos

• Definição de preços de referência para custear alternativas

• Avaliação de ajustes na metodologia do Mínimo Custo Global

• Metodologia robusta de Análise de Custo-Benefício (CBA)

O Elo Social da
Resiliência em
Infraestrutura:
Avaliando a
Vulnerabilidade
Social a interrupções
de Longa Duração

14

Vulnerabilidade Social a Interrupções de Longa Duração Decorrentes de
Eventos Climáticos Extremos - O IVS CERI

Criação de uma medida para avaliar a
vulnerabilidade social por meio do grau de preparação para
emergências, saúde e capacidade de evacuação

15

Agenda

• Objetivos
• Escopo
• Premissas
• Roadmap
• Time
• Riscos Mapeados

Premissas

• Os  dados,  documentos  e  informações  de  propriedade  da  Isa  Energia

Brasil  necessários  para  o  desenvolvimento  do  projeto

serão

disponibilizados tempestivamente e em formato acessível

• Haverá  uma  equipe  da

Isa  Energia  Brasil  que

responderá

tempestivamente as dúvidas das equipes da FGV e Facto Energy

Agenda

• Objetivos
• Escopo
• Premissas
• Roadmap
• Time
• Riscos Mapeados

Principais Produtos:
Relatórios de Modelagem de Engenharia

• Caracterização das linhas e equipamentos

• Custos de alternativas de investimentos em resiliência

• Custos de uso das medidas corretivas

Principais Produtos:
Relatórios de Modelagem Financeira

• Criação de Matriz de Riscos adaptada a eventos extremos/resiliência de

redes

•

Simulação dos impactos dos eventos extremos em diferentes cenários de

investimentos, de mudanças climáticas e de compartilhamento de riscos

• Análise Custo-Benefício (CBA) de diferentes escolhas de investimento em

resiliência

• Apresentação dos resultados associados ao Mínimo Custo Global

• Reporte Público de Riscos Físicos em linha com a IFRS S2

Principais Produtos: Dashboard de
Adaptação de Ativos

Principais Produtos: Relatório de
Aprimoramento Regulatório

• Discussão sobre investimentos prudentes em resiliência e fontes de

financiamento

• Avaliação da necessidade de repartição dos riscos associados a eventos

climáticos extremos entre a transmissora e poder concedente

• Avaliação de modelos e mecanismos de compartilhamento de riscos entre

os diferentes stakeholders, bem como possibilidades de seguros

• Discussão de mecanismos de incentivo para reações a ocorrências

climáticas

Agenda

• Objetivos
• Escopo
• Premissas
• Roadmap
• Time
• Riscos Mapeados

Cronograma de entregas
(a partir da entrega de documentos e dados)

Agenda

• Objetivos
• Escopo
• Premissas
• Roadmap
• Time
• Riscos Mapeados

Time

Z

Diretora - Joisa Dutra
Dra. em Economia

Edson Gonçalves
Dr. em Economia

Rafael Martins de Souza
Dr. em Economia

Salman  Mohaghueghui
PhD. em Engenharia
Elétrica

Diogo Lisbona
Dr. em Economia

Vivian Figer
Dra. em Economia

Dario Oliveira
PhD. em Matemática

Luciana Costa
Dra. em Economia

Gustavo Kaercher
Dr. em Direito

Agenda

•Objetivos
•Escopo
•Premissas
•Roadmap
•Time
•Riscos Mapeados

Riscos Mapeados

• Atraso ou falha na entrega de dados de estudos já realizados ou

necessários para o desenvolvimento do projeto

• Atraso ou falha na entrega de documentos de estudos já realizados ou

necessários para o desenvolvimento do projeto

• Demora na resolução de dúvidas a respeito dos dados e documentos

enviados pela equipe da Isa Energia Brasil

Muito obrigado!

Resiliência da Transmissão
de Energia Elétrica
a Eventos Climáticos
Extremos

Reunião de 07-01-2026

Agenda

Primeira análise da modelagem climática conforme documentos
fornecidos pela ISA ENERGIA BRASIL (ISA CTEEP).

Objetivo e Escopo
A modelagem visa identificar, quantificar e priorizar riscos climáticos
para aumentar a resiliência da infraestrutura de transmissão (linhas e
subestações).

O estudo abrange 284 linhas de transmissão (cerca de 22 mil km) e
129 subestações no estado de São Paulo.

O objetivo final é subsidiar um Plano de Adaptação e Resiliência
Climática que oriente investimentos e ações operacionais.

Base Metodológica e Cenários
A modelagem foi desenvolvida com o suporte da consultoria WayCarbon e
utiliza dados do CMIP6 (Coupled Model Intercomparison Project Phase 6),
alinhados ao Sexto Relatório de Avaliação do IPCC (AR6).

Cenários de Emissões (SSPs): Foram considerados três cenários: SSP1-2.6
(otimista), SSP2-4.5 (intermédio) e SSP3-7.0 (pessimista/políticas atuais). O
cenário SSP3-7.0 foi priorizado para a análise de risco e priorização de ativos,
pois reflete uma trajetória de aquecimento mais severa (aprox. 3,6°C até 2100),
garantindo uma avaliação conservadora da segurança.

Horizontes Temporais: A análise compara um período histórico (1995-2014)
com projeções para 2030 (curto prazo), 2040 (médio) e 2050 (longo).

Matriz de Risco
O nível de risco de cada ativo é calculado pela fórmula:

Risco = (Probabilidade x Vulnerabilidade) x Criticidade.

Probabilidade (Ameaça): Baseada na tendência de intensificação de
indicadores climáticos extremos (frequência, duração e severidade) modelados
no software MOVE.

Vulnerabilidade: Avalia a suscetibilidade técnica do ativo (ex: histórico de
quedas, características do terreno, premissas de projeto originais).

Criticidade: Baseada no procedimento interno (PRO.OP36), ponderando
impactos Financeiros, Sistêmicos (importância para a rede), Reputacionais, de
Segurança e Ambientais.

Ameaças Climáticas Modeladas (I)
Tempestades (Descargas Atmosféricas): Como os modelos climáticos não
projetam raios diretamente, a modelagem utiliza uma combinação de
precipitação extrema (RX1day, R99p) e ventos fortes (WX1day) como proxy
para tempestades severas e incidência de raios.

Ventos Extremos: Inicialmente, a modelagem usou ventos médios (WX1day e
W90p) devido a limitações dos modelos globais. Para o estudo detalhado de
engenharia, foi aplicada a Distribuição de Gumbel para converter dados
históricos e projeções em rajadas de 3 segundos, considerando tempos de
recorrência de 150 e 250 anos, conforme normas técnicas (NBR 5422).

Ameaças Climáticas Modeladas (II)
Incêndios Florestais: Utiliza a Fórmula de Monte Alegre Alterada (FMA+), que
cruza dados de umidade e vento com o tipo de vegetação (MapBiomas) e
topografia (declividade e orientação das encostas) para estimar o risco de
propagação do fogo.

Inundações Fluviais: Combina projeções de chuvas extremas (RX1day, R95p)
com um Índice Morfométrico (derivado do modelo digital de elevação) para
identificar áreas próximas a cursos d'água propensas a transbordamento. Não
cobre alagamentos urbanos por drenagem insuficiente.

Deslizamentos: Analisa a precipitação acumulada (RX5day - 5 dias
consecutivos) combinada com o Índice de Suscetibilidade do Solo (ISS), que
considera geologia, declividade e uso do solo.

Ameaças Climáticas Modeladas (III)
Temperaturas Máximas e Ondas de Calor: Avalia a frequência de ondas de
calor (HW.N) e o aumento da temperatura máxima média (TMAX). Para linhas
de transmissão, o impacto é verificado simulando a ampacidade e o aumento
da flecha (dilatação dos cabos) conforme a norma IEEE 738-2006, para garantir
distâncias de segurança.

Aumento do Nível do Mar: Combina dados da NASA sobre elevação do nível
do mar com projeções de eventos de ressaca (maré meteorológica) para
identificar ativos costeiros em risco de inundação.

Planos de Ação e Soluções Propostas

Com base na modelagem, a Isa desenvolveu planos de ação específicos para
os ativos priorizados:

Para Ventos: Reforço estrutural (torres estaiadas ou de ancoragem), uso de
grampos deslizantes para evitar efeito cascata e instalação de estações
anemométricas.

Para Incêndios: Uso de câmeras off-grid, sensores IoT e plataforma de
monitoramento SMAC (Climatempo).

Para Inundações: Monitoramento via satélite/IoT e elevação de equipamentos
em subestações críticas.

Para Temperatura: Monitoramento com espaçadores inteligentes para aferir a
temperatura real dos cabos e validar o modelo teórico.

Dúvidas e Solicitações (I)

Levantamento de dados e métodos de previsão
É possível fornecer os dados e a especificação dos métodos utilizados nas previsões de eventos climáticos futuros, com
destaque para ventos e descargas atmosféricas?

Distribuições estatísticas adotadas
Quais foram as distribuições estatísticas foram assumidas para cada evento climático na transformação dos valores brutos
de probabilidade para seus equivalentes normalizados entre 0 e 1.

Validação dos cálculos
Considerando que os dados utilizados abrangem o período de 1994 a 2014, é possível utilizar os registros de 2014 a 2025
para validar os cálculos realizados?

Linhas de transmissão e normas aplicáveis
Realizar o levantamento dos dados relevantes dos ativos, incluindo, por exemplo, o ano de construção das linhas de
transmissão e as normas vigentes à época, com o objetivo de verificar sua capacidade de suportar novos eventos climáticos
e, a partir dessa análise, calcular as probabilidades de falha.

Georreferenciamento
Como é feito o georreferenciamento dos resultados para as linhas de transmissão? Os resultados apresentados para as
linhas de transmissão são apresentados por trechos? Como são definidos estes trechos?

Dúvidas e Solicitações (II)

Ativos com problemas atuais
É possível identificar os ativos que já apresentam problemas, indicando as melhorias necessárias para adequação às
normas? É possível fornecer também os dados referentes à quantidade de desligamentos ocorridos em decorrência desses
problemas?

Incidência de descargas atmosféricas
Considerando o aumento substancial das taxas de incidência de descargas atmosféricas nas últimas duas ou três décadas,
avaliar se:
• valores médios anuais devem ser evitados;
• valores únicos para uma linha de transmissão devem ser evitados, dado que seus trajetos abrangem regiões com

características orográficas distintas. Verificar se situação semelhante ocorre nas avaliações de ventos, onde valores
médios foram assumidos.

Capacidade de absorção de energia dos cabos para-raios
Esclarecer se existem valores de energia máxima que podem ser absorvidos pelos tentos que compõem os cabos para-raios
(convencionais ou OPGW). Caso contrário, indicar qual parâmetro é utilizado pela Isa para avaliar a suportabilidade desses
cabos em relação às correntes de descargas atmosféricas, especialmente a componente de corrente contínua.

Eventos críticos
Avaliar se todos os eventos devem ser considerados e definir quais são os mais críticos para análise.

Muito obrigado!

Resiliência da Transmissão
de Energia Elétrica
a Eventos Climáticos
Extremos

Reunião de 14-01-2026

Objeto

Segunda discussão sobre a análise da modelagem climática
conforme documentos fornecidos pela ISA ENERGIA BRASIL
(ISA CTEEP).

Agenda

• Preparativas para a reunião missão internacional
• Pontos adicionais sobre as dúvidas
• Modelagem de valores extremos
• Primeiros achados sobre a modelagem de tempestade

Comentários sobre as
perguntas apresentadas na
última reunião

Primeira Pergunta

Quais distribuições estatísticas foram assumidas para cada evento climático na transformação dos valores
brutos de probabilidade para seus equivalentes normalizados entre 0 e 1?

Resposta: Não indica a probabilidade exata do evento, mas mostra se os extremos projetados são mais
severos ou frequentes que no passado.

Réplica: Todo conjunto composto de variáveis aleatórias contínuas possui suas funções densidade e
distribuição acumulada de probabilidade. A primeira é a derivada da segunda e, portanto, a segunda é a
integral da primeira. Nesta perspectiva, a pergunta não foi adequadamente respondida. O que se pretendia
com a pergunta é conhecer a função matemática.

Oportunidade de aprimoramento: Formalização das distribuições de probabilidade usadas para modelar os
fenômenos climáticos.

Demais perguntas

As demais perguntas foram esclarecidas.

Modelagem de Valores Extremos

A teoria dos valores extremos é a área da Estatística que estuda a

distribuição dos valores máximos e mínimos de uma variável

aleatória de interesse, sendo que no âmbito deste estudo o

interesse é a utilização da teoria dos valores máximos. O modelo de

distribuição de valores extremos generalizado (GEV) é a família de

distribuições de probabilidade para valores máximos, que inclui as

distribuições de Gumbel, Fréchet e Weibull.

Distribuição Generalizada de Valores
Extremos

Considerando X uma variável aleatória com distribuição GEV, sua função de distribuição poder ser:

Com                              na qual os parâmetros a, b, c são a localização, escala e forma, respectivamente.

Oespaço de parâmetros é dado por

Possíveis Aplicações da Modelagem de
Valores Extremos

Tempestades (Descargas Atmosféricas): Como os modelos climáticos não projetam raios diretamente, a
modelagem utiliza uma combinação de precipitação extrema (RX1day, R99p) e ventos fortes (WX1day) como
proxy para tempestades severas e incidência de raios.

Ventos Extremos: Inicialmente, a modelagem usou ventos médios (WX1day e W90p) devido a limitações dos
modelos globais. Para o estudo detalhado de engenharia, foi aplicada a Distribuição de Gumbel para
converter dados históricos e projeções em rajadas de 3 segundos, considerando tempos de recorrência de
150 e 250 anos, conforme normas técnicas (NBR 5422).

Temperaturas Máximas e Ondas de Calor: Avalia a frequência de ondas de calor (HW.N) e o aumento da
temperatura máxima média (TMAX). Para linhas de transmissão, o impacto é verificado simulando a
ampacidade e o aumento da flecha (dilatação dos cabos) conforme a norma IEEE 738-2006, para garantir
distâncias de segurança.

Muito obrigado!

Resiliência da Transmissão
de Energia Elétrica
a Eventos Climáticos
Extremos

Reunião de 29-01-2026

Resiliência da Transmissão
de Energia Elétrica
a Eventos Climáticos
Extremos

Dúvidas sobre a Modelagem Climática

Modelagem

Como  foi  feita  a  modelagem  de  probabilidades  de
ocorrência  de  valores  extremos  para  cada  uma  das
ameaças?

Dados

É possível no repassar o conjunto de dados utilizados e
produzidos durante o projeto?

Projeções

Como  as  probabilidades  foram  projetadas,  de  acordo
com cada um dos cenários climáticos?

Muito obrigado!

Resiliência da Transmissão
de Energia Elétrica
a Eventos Climáticos
Extremos

Reunião de 04-02-2026

Objeto

Terceira discussão sobre a análise da modelagem climática
conforme documentos fornecidos pela ISA ENERGIA BRASIL
(ISA CTEEP).

Agenda

Repercussão da reunião com profissionais da WayCarbon e
discussão sobre a primeira versão do Produto I

Estimação das Probabilidades
Introdução & Problema

•

•

•

•

Conceito de "Valor Bruto" indefinido: Documento não define formalmente o que
é "valor bruto" para extremos climáticos

Falta de precisão metodológica: Conversão para escala 0-1 via função de
densidade não está descrita com clareza

Período de referência: Características climáticas naturais de 1950-1994 usadas
como baseline

Lacuna crítica: Processo de identificação do modelo probabilístico não foi
explicitado

Estimação das Probabilidades
Problemas Identificados

•

•

•

•

•

Correlação entre extremos (frequência, duração, severidade) não é transparente

Índice proposto não expressa probabilidade absoluta da ocorrência do evento

Impacto associado também não é capturado explicitamente

Uso de conceitos não consagrados na Teoria Estatística

Falta de reprodutibilidade desejável em modelagem científica

Estimação das Probabilidades
Interpretação do Documento

• Valor médio próximo a 50% → extremos semelhantes ao clima de referência

• Valores acima de 50% → maior intensidade de extremos projetados

• Atenção: Mesmo valor médio de 50% implica persistência de condições extremas

significativas

•

Intensidade, frequência, duração aumentam com deslocamento para direita

Estimação das Probabilidades
Amostra & Base de Dados

• Dados diários de 1950 a 1994 → ~16.425 observações por variável climática

• Múltiplas variáveis climáticas analisadas

• Série temporal suficientemente longa para estimação estatística robusta

• Hipótese de estacionariedade das séries é razoável

Estimação das Probabilidades
Metodologia Estatística Recomendada

• Especificar modelos probabilísticos teóricos com base em literatura

• Estimar parâmetros a partir dos dados coletados

• Realizar testes estatísticos formais para validação dos modelos

• Aplicar o mesmo rigor para distribuições conjuntas (correlações, dependências)

• Garantir estimação formal vs. procedimentos ad-hoc

Estimação das Probabilidades
Detecção de Mudanças Climáticas

• Teste 1: Detecção formal de tendências nos dados

• Teste 2: Análise de proporção de eventos nos quantis superiores

• Comparar quantis teóricos (referência) vs. empíricos (projeção)

• Se quantis projetados >> quantis teóricos → evidência robusta de extremos mais

frequentes

• Metodologia baseada em cauda direita das distribuições

Estimação das Probabilidades
Por Que a Abordagem Atual é Inadequada

• Conceito de "probabilidade absoluta" não existe em teoria estatística

• Análise simplista de "valor médio próximo a 50%" é insuficiente

• Falta de testes estatísticos formais compromete conclusões

• Não há validação rigorosa do ajuste dos modelos aos dados

•

Impossibilidade de reprodução por terceiros

Estimação das Probabilidades
Caminhos para Melhoria

• Documentar explicitamente toda modelagem probabilística

•

Implementar testes estatísticos formais para validação

• Adotar metodologia consagrada para análise de eventos extremos

• Próximos relatórios devem incorporar melhorias sugeridas

• Objetivo: Aumentar robustez, transparência e reprodutibilidade

Estimação das Probabilidades

Muito obrigado!

