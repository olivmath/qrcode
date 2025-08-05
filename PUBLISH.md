# Guia de Publicação no PyPI

Este documento contém as instruções para publicar o pacote `myqr-gui` no PyPI.

## Pré-requisitos

1. Conta no PyPI (https://pypi.org/account/register/)
2. Conta no TestPyPI (https://test.pypi.org/account/register/) - para testes
3. Instalar o twine: `pip install twine`

## Passos para Publicação

### 1. Testar no TestPyPI (Recomendado)

Primeiro, teste a publicação no TestPyPI:

```bash
# Upload para TestPyPI
twine upload --repository testpypi dist/*

# Testar instalação do TestPyPI
pip install --index-url https://test.pypi.org/simple/ myqr-gui
```

### 2. Publicar no PyPI

Após confirmar que tudo funciona no TestPyPI:

```bash
# Upload para PyPI
twine upload dist/*
```

### 3. Verificar a Publicação

Após a publicação, você pode:

```bash
# Instalar o pacote
pip install myqr-gui

# Executar a aplicação
myqr
```

## Configuração de Credenciais

### Usando arquivo .pypirc

Crie um arquivo `~/.pypirc` com suas credenciais:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = <seu-token-do-pypi>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = <seu-token-do-testpypi>
```

### Usando tokens de API

1. Vá para https://pypi.org/manage/account/token/
2. Crie um novo token de API
3. Use o token como senha (username = `__token__`)

## Atualizações Futuras

Para publicar uma nova versão:

1. Atualize a versão em `pyproject.toml`
2. Atualize a versão em `myqr/__init__.py`
3. Reconstrua o pacote: `python -m build`
4. Publique: `twine upload dist/*`

## Verificações Antes da Publicação

- [ ] Versão atualizada em `pyproject.toml`
- [ ] Versão atualizada em `myqr/__init__.py`
- [ ] README.md atualizado
- [ ] Licença incluída
- [ ] Dependências corretas
- [ ] Pacote construído com sucesso
- [ ] Testado localmente

## Comandos Úteis

```bash
# Verificar o pacote antes do upload
twine check dist/*

# Limpar builds anteriores
rm -rf dist/ build/ *.egg-info/

# Reconstruir o pacote
python -m build
```