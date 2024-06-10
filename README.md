# Automação de Construção de Imagens Base Seguras

Este repositório contém uma solução automatizada para a construção de imagens Docker base seguras, com o objetivo de evitar o uso de imagens públicas que podem conter vulnerabilidades. Minha abordagem garante que a equipe de desenvolvimento tenha acesso a imagens base atualizadas com frequência, melhorando a segurança e a confiabilidade dos ambientes de desenvolvimento e produção.

## Propósito

### Segurança e Confiabilidade

Imagens Docker públicas frequentemente contêm vulnerabilidades que podem comprometer a segurança de seus ambientes de desenvolvimento e produção. Utilizar essas imagens pode expor a sua infraestrutura a riscos desnecessários, dificultando a manutenção de um ambiente seguro e controlado.

### Imagens Base Atualizadas

Nossa solução visa proporcionar uma fonte confiável de imagens base que são frequentemente atualizadas, garantindo que as últimas correções de segurança e melhorias estejam sempre presentes. Isso reduz a superfície de ataque e aumenta a resiliência contra possíveis ameaças.

## Componentes Principais

### Script de Construção de Imagens Docker

O script Python fornecido automatiza a construção de imagens Docker a partir de Dockerfiles existentes, adiciona tags com base na versão do Git e realiza o push dessas imagens para qualquer registro privado compatível com Docker.

## Benefícios da Solução

1. **Melhoria na Segurança**: Reduz a dependência de imagens públicas vulneráveis ao utilizar imagens base construídas internamente e mantidas atualizadas.
2. **Consistência e Controle**: Garante que a equipe de desenvolvimento trabalhe com imagens base consistentes, controladas e frequentemente atualizadas.

## Integração com CI/CD

### Implementação em Plataformas de CI/CD

Este script pode ser facilmente integrado em plataformas de CI/CD para automação contínua da construção e distribuição de imagens Docker. Abaixo estão exemplos de como incorporar o script em pipelines de integração e entrega contínua em diferentes plataformas:

## Conteúdo Extra
### Implantação de Registro Privado no Kubernetes

1. **Instale o Helm**: Certifique-se de que o Helm está instalado em seu ambiente.
2. **Adicione o Repositório Bitnami**: Adicione o repositório Helm da Bitnami.
   ```bash
   helm repo add bitnami https://charts.bitnami.com/bitnami
   ```
3. **Implante o Registro Privado**: Utilize o Helm para implantar o registro de contêineres no Kubernetes.
   ```bash
   helm install my-registry bitnami/harbor
   ```

### Exemplos de Integração:

1. **GitHub Actions**: Utilize o GitHub Actions para criar workflows que executem o script de construção e push das imagens Docker sempre que houver uma alteração no repositório.
   - [Exemplo de workflow](https://docs.github.com/en/actions/guides/building-and-testing-docker#building-and-pushing-to-a-container-registry)

```yaml
name: Docker Build and Push

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1

    - name: Build and Push Docker Images
      run: python build_and_push_images.py --dockerfile-dir dockerfiles --registry-url ${{ secrets.REGISTRY_URL }} --project myproject --username ${{ secrets.REGISTRY_USERNAME }} --password ${{ secrets.REGISTRY_PASSWORD }}
```

2. **GitLab CI/CD**: No GitLab CI/CD, você pode definir stages para construir e push das imagens Docker em resposta a eventos de pipeline, como push ou merge requests.
   - [Exemplo de pipeline](https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#pushing-containers-to-a-container-registry)

```yaml
stages:
  - build

docker_build:
  stage: build
  image: docker:latest
  variables:
    DOCKER_DRIVER: overlay2
  script:
    - python build_and_push_images.py --dockerfile-dir dockerfiles --registry-url $REGISTRY_URL --project myproject --username $REGISTRY_USERNAME --password $REGISTRY_PASSWORD
  only:
    - main
```

3. **Jenkins**: Configure um pipeline Jenkins que execute o script como parte de um estágio de construção. Você pode agendar builds periódicos ou acionar builds manualmente.
   - [Exemplo de Jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#declarative-pipeline)

```groovy
pipeline {
    agent any

    stages {
        stage('Build and Push Docker Images') {
            steps {
                sh 'python build_and_push_images.py --dockerfile-dir dockerfiles --registry-url $REGISTRY_URL --project myproject --username $REGISTRY_USERNAME --password $REGISTRY_PASSWORD'
            }
        }
    }
    post {
        always {
            // Clean up steps if necessary
        }
    }
}
```

4. **AWS CodePipeline**: No AWS CodePipeline, você pode criar um pipeline que use o AWS CodeBuild para executar o script de construção das imagens Docker.
   - [Exemplo de pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-four-stage-pipeline.html)

```yaml
version: 0.2

phases:
  build:
    commands:
      - python build_and_push_images.py --dockerfile-dir dockerfiles --registry-url $REGISTRY_URL --project myproject --username $REGISTRY_USERNAME --password $REGISTRY_PASSWORD
```

5. **Azure Pipelines**: Utilize o Azure Pipelines para criar um pipeline YAML que execute o script em uma etapa de build. Você pode configurar gatilhos para acionar a execução do pipeline em resposta a eventos de repositório.
   - [Exemplo de pipeline YAML](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/docker?view=azure-devops#build-and-push-images)

```yaml
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- checkout: self

- script: python build_and_push_images.py --dockerfile-dir dockerfiles --registry-url $(REGISTRY_URL) --project myproject --username $(REGISTRY_USERNAME) --password $(REGISTRY_PASSWORD)
```

Substitua `$REGISTRY_URL`, `myproject`, `$REGISTRY_USERNAME` e `$REGISTRY_PASSWORD` pelos valores reais do seu ambiente.

## Próximos Passos

Explore os exemplos fornecidos para integrar o script em sua plataforma de CI/CD preferida. Adapte os fluxos de trabalho conforme necessário para atender aos requisitos específicos do seu projeto e ambiente.

## Conclusão

Esta solução oferece uma abordagem robusta para garantir que a equipe de desenvolvimento utilize imagens base seguras e frequentemente atualizadas, reduzindo a exposição a vulnerabilidades e melhorando a consistência dos ambientes de desenvolvimento e produção. A integração com registros privados e Kubernetes através de Helm charts da Bitnami simplifica a gestão e o armazenamento das imagens Docker, proporcionando uma infraestrutura segura e eficiente.
