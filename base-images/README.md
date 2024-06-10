
## Funcionalidades

- **Automação Completa**: Construção, tagueamento e push das imagens Docker são realizados automaticamente.
- **Versionamento com Git**: As imagens são tagueadas com a versão atual do repositório Git, garantindo rastreabilidade e consistência.
- **Integração com Registro Privado**: As imagens são enviadas para um registro privado, proporcionando um repositório seguro.
- **Saídas Informativas e Coloridas**: Utiliza as bibliotecas `click` e `rich` para uma interface de linha de comando amigável e com saídas coloridas.

## Pré-requisitos

Antes de executar o script, certifique-se de que você tem o seguinte instalado:

1. Python 3.x
2. Docker
3. Git
4. Bibliotecas Python necessárias:
   - `click`
   - `rich`

Você pode instalar as bibliotecas Python necessárias com o seguinte comando:

```bash
pip install click rich
```

Além disso, você deve estar autenticado no registro privado e estar em um repositório Git com tags válidas.

## Como Usar

1. **Clone o repositório ou copie o script para o seu ambiente local.**

2. **Navegue até o diretório onde o script está localizado.**

3. **Coloque os Dockerfiles que você deseja construir no diretório especificado (padrão: `dockerfiles`).**

4. **Execute o script com os seguintes parâmetros:**

```bash
python build_and_push_images.py --dockerfile-dir DOCKERFILE_DIR --registry-url REGISTRY_URL --project PROJECT --username USERNAME --password PASSWORD
```

### Parâmetros

- `--dockerfile-dir`: Diretório contendo os Dockerfiles existentes. (Padrão: `dockerfiles`)
- `--registry-url`: URL do registro privado.
- `--project`: Nome do projeto no registro.
- `--username`: Nome de usuário do registro.
- `--password`: Senha do registro.

### Exemplo de Uso

```bash
python build_and_push_images.py --dockerfile-dir dockerfiles --registry-url registry.example.com --project myproject --username myusername --password mypassword
```

### Exemplo de Saída

```plaintext
Using Git version: v1.0.0
Found 3 Dockerfiles in 'dockerfiles' directory
Processing Dockerfiles...: 100%|██████████| 3/3 [00:00<00:00, 4.35it/s]
Building Docker image myapp_image_1:v1.0.0...
Pushing Docker image myapp_image_1:v1.0.0 to registry.example.com/myproject...
Docker image myapp_image_1:v1.0.0 pushed successfully!
Building Docker image myapp_image_2:v1.0.0...
Pushing Docker image myapp_image_2:v1.0.0 to registry.example.com/myproject...
Docker image myapp_image_2:v1.0.0 pushed successfully!
Building Docker image myapp_image_3:v1.0.0...
Pushing Docker image myapp_image_3:v1.0.0 to registry.example.com/myproject...
Docker image myapp_image_3:v1.0.0 pushed successfully!
All images built and pushed successfully!
```

## Benefícios

- **Segurança Melhorada**: Utilizando imagens base construídas internamente, minimizamos a exposição a vulnerabilidades encontradas em imagens públicas.
- **Consistência e Controle**: A equipe de desenvolvimento trabalha com imagens base consistentes e controladas, reduzindo surpresas e inconsistências entre ambientes.
- **Atualizações Frequentes**: As imagens base podem ser atualizadas frequentemente, garantindo que as últimas correções de segurança e atualizações sejam incorporadas.

## Notas

- Certifique-se de que o Docker está em execução e que você está autenticado no registro privado antes de executar o script.
- O script pressupõe que os Dockerfiles estão nomeados no formato `Dockerfile_*` e ajusta os nomes das imagens baseados nesses arquivos.
- Certifique-se de que o repositório Git tem tags válidas para que o script possa obter a versão correta.
