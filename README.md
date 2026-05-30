# TechFlow - Sistema de Gerenciamento de Tarefas Ágil

O TechFlow é um sistema de gerenciamento de tarefas desenvolvido em Python utilizando Programação Orientada a Objetos (POO). O projeto foi criado para atender às necessidades de uma startup de logística que busca acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

O sistema permite o gerenciamento completo de tarefas por meio das operações de CRUD (Criar, Ler, Atualizar e Excluir), além de possuir autenticação de usuários e controle de permissões baseado em perfis de acesso.

# Objetivo

O objetivo do projeto é fornecer uma solução simples e eficiente para o gerenciamento de tarefas, aplicando conceitos de metodologias ágeis e boas práticas de desenvolvimento de software.

Entre os principais objetivos estão:

Organizar e acompanhar tarefas da equipe.
Controlar o fluxo de trabalho por meio de diferentes status.
Permitir a priorização de atividades críticas.
Implementar controle de acesso entre administradores e usuários locais.
Aplicar testes automatizados para garantir a qualidade do sistema.
Utilizar Integração Contínua (CI) com GitHub Actions para validação automática do código.

# Funcionalidades

## Usuários
    -Cadastro de usuários.
    -Login e logout.
    -Controle de acesso por perfil:
        -Administrador
        -Usuário Local

## Tarefas
-Criar tarefas.
-Listar tarefas.
-Editar tarefas.
-Excluir tarefas (apenas administradores).
-Definir prioridade:
    -Baixa
    -Média
    -Alta
    -Crítica

## Controle de Fluxo
Cada tarefa pode possuir os seguintes status:

-A Fazer
-Em Progresso
-Concluído

## Relatórios
- Relatório geral de desempenho.
- Quantidade de tarefas por status.
- Quantidade de tarefas críticas.
- Relatório de produtividade por usuário.

# Metodologia Utilizada

O desenvolvimento do projeto foi baseado em conceitos de metodologias ágeis, utilizando a organização de atividades por meio de um quadro Kanban.

O fluxo das tarefas segue as etapas:

A Fazer
   ↓
Em Progresso
   ↓
Concluído

Além disso, foram aplicadas práticas de qualidade de software, incluindo:

- Programação Orientada a Objetos (POO).
- Controle de versão com Git e GitHub.
- Testes automatizados com PyTest.
- Integração Contínua com GitHub Actions.

# Tecnologias Utilizadas
Python 3
PyTest
Git
GitHub
GitHub Actions

# Como Executar o Sistema

## 1. Clonar o Repositório
git clone https://github.com/SandeHuginn/TechFlow.git

## 2. Acessar a Pasta do Projeto
cd TechFlow

## 3. Instalar as Dependências
pip install -r requirements.txt

## 4. Executar o Sistema
python Techflow.py

# Executando os Testes

Para executar os testes automatizados:

pytest -v

# Integração Contínua

O projeto utiliza GitHub Actions para execução automática dos testes sempre que alterações são enviadas ao repositório ou quando um Pull Request é criado.

Essa abordagem garante maior confiabilidade do sistema e auxilia na identificação precoce de erros durante o desenvolvimento.

# Alteração de Escopo do Projeto

## Solicitação do Cliente

Durante o desenvolvimento do sistema, a startup de logística identificou a necessidade de acompanhar melhor o desempenho da equipe e o andamento das atividades.

Por esse motivo, foi solicitada uma alteração no escopo original do projeto para incluir funcionalidades de geração de relatórios gerenciais.

## Justificativa

A alteração foi motivada pela necessidade de fornecer aos administradores informações que auxiliem na tomada de decisões, permitindo:

Monitorar a quantidade de tarefas concluídas.
Identificar tarefas críticas pendentes.
Acompanhar o desempenho individual dos colaboradores.
Detectar possíveis gargalos no fluxo de trabalho.

Essa mudança está alinhada aos princípios das metodologias ágeis, que permitem adaptar o produto às necessidades do cliente durante o desenvolvimento.

## Funcionalidades Adicionadas
Foram adicionadas as seguintes funcionalidades:

Relatório geral de desempenho.
Relatório de produtividade por usuário.
Contagem de tarefas por status.
Identificação de tarefas com prioridade crítica

## Impacto no Projeto

A alteração exigiu:

Atualização do backlog do produto.
Criação de novas tarefas de desenvolvimento.
Atualização do quadro Kanban.
Implementação de novos testes automatizados.
Atualização da documentação do sistema.

# Autor

Projeto desenvolvido para a disciplina de Software Engineering AGR.EAD26/1, com foco na aplicação de metodologias ágeis, controle de qualidade e integração contínua. 
