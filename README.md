<h1>Repositório dedicado ao curso de CC turma 01 2026</h1>
<p>Este repositório contém os seguintes conhecimentos:</p>
<ul>
    <li>Resumos Conteúdos</li>
    <li>Exercícios</li>
</ul>

## 📚 Estrutura do repositório

```
/
├── <nome-da-materia>/
│   ├── resumos/
│   │   ├── aula-01.pdf
│   │   ├── recursividade.pdf
│   │   └── ...
│   └── exercicios/
│       ├── 0.1-fatorial.py
│       ├── 0.2-fibonacci.c
│       └── ...
```

## 🏷️ Nomenclatura dos arquivos

### Resumos

- Formato: **PDF** (`.pdf`)
- Nome: **`aula-x`** (ex: `aula-01.pdf`, `aula-02.pdf`) **ou** o nome do conteúdo abordado (ex: `recursividade.pdf`, `arvores-binarias.pdf`)
- Use `kebab-case` (palavras separadas por hífen, sem acentos ou espaços)

### Exercícios

- Formato: sequencial, no padrão **`X.Y - nome_do_exercicio.linguagem`**
- Extensão: de acordo com a linguagem usada (`.py`, `.c`, `.java`, etc.)
- Exemplos:
  - `0.1 - fatorial.py`
  - `0.2 - soma_vetores.c`
  - `0.3 - lista_encadeada.java`

## 🤝 Como contribuir

1. **Faça um fork** deste repositório para a sua conta.
2. **Clone o fork** para sua máquina:
   ```bash
   git clone https://github.com/<seu-usuario>/<nome-do-repo>.git
   ```
3. **Crie uma branch** para sua contribuição:
   ```bash
   git checkout -b materia/nome-do-conteudo
   ```
   Exemplo: `git checkout -b algoritmos/recursividade`
4. **Adicione seus arquivos** na pasta correta (`<materia>/resumos/` ou `<materia>/exercicios/`), seguindo a nomenclatura definida acima. Se a matéria ainda não existir no repositório, crie a pasta seguindo o mesmo padrão.
5. **Faça o commit** com uma mensagem clara e objetiva:
   ```bash
   git add .
   git commit -m "Adiciona resumo de recursividade"
   ```
6. **Envie para o seu fork**:
   ```bash
   git push origin materia/nome-do-conteudo
   ```
7. **Abra um Pull Request** para a branch principal deste repositório, descrevendo brevemente o que foi adicionado.
8. Aguarde a revisão. Ajustes podem ser solicitados antes do merge.

### ✅ Boas práticas

- Um Pull Request por conteúdo/assunto (evite misturar matérias diferentes em um mesmo PR).
- Confira se o arquivo já não existe antes de subir, para evitar duplicidade.
- Resumos devem estar em PDF legível (não enviar fotos borradas de caderno).
- Códigos de exercícios devem compilar/rodar sem erros antes do envio.
- Sempre respeite a nomenclatura combinada — isso mantém o repositório organizado para todos.