# Dados

O arquivo `bank-additional-full.csv` usado neste projeto é o conjunto completo Bank Marketing (versão `bank-additional`), obtido do pacote oficial `bank-additional.zip` da UCI Machine Learning Repository.

- Página e origem: [UCI Machine Learning Repository — Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing)
- Arquivo: `bank-additional-full.csv`
- Separador: ponto e vírgula (`;`)
- Licença indicada pela UCI: Creative Commons Attribution 4.0 International (CC BY 4.0)
- SHA-256 do CSV utilizado: `74ADFC578BF77A7FF4BB1BA4A9F8709D9E3C6907342959C2C8416847E0AFB4D8`

O arquivo contém dados históricos de campanhas de uma instituição bancária portuguesa. A UCI descreve a versão completa como 41.188 exemplos e 20 variáveis de entrada, além do alvo `y`. Mantenha a atribuição à UCI e aos autores: Moro, S., Rita, P. e Cortez, P. (2014), DOI [10.24432/C5K306](https://doi.org/10.24432/C5K306).

As células `unknown` são valores categóricos presentes nos dados; nesta análise, são contabilizadas explicitamente e preservadas como categoria. O valor `999` em `pdays` representa ausência de contato anterior na convenção desta versão e não 999 dias literais. A decisão de codificação para o modelo será implementada e documentada na etapa de pré-processamento.
