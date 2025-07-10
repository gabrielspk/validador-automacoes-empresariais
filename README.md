# 🤖 Sistema de Automações Empresariais

Este projeto realiza a automação de rotinas empresariais envolvendo **extração de arquivos**, **validação de dados** e **envio automatizado de relatórios**, com foco na integração com o sistema GA e os portais de clientes como **Banco Safra**, **Itaú**, **Mercado Pago**, **Redecard**, entre outros.

---

## ⚙️ Funcionalidades

### 1. Validação Automatizada de Dados
- Extração de planilhas do sistema **GA**.
- Validação dos dados para verificar se os arquivos foram corretamente importados.
- Geração de relatórios automatizados por cliente.
- Envio dos relatórios por e-mail utilizando a **API do Mailgrid**.

### 2. Integração com o Portal do Banco Safra
- Acesso automático ao portal do **Banco Safra**.
- Login e extração de arquivos via RPA com **Selenium**.
- Envio dos arquivos diretamente para o sistema **GA**.
- Disparo de e-mail de feedback sobre o processamento.

---

## 🧱 Estrutura do Projeto

```
├── app/             # Scripts de controle por cliente (ex: safra.py, mercado_pago.py)
├── rpa/             # Scripts de RPA (navegador, extração, login, envio)
│   └── autenticadores/   # Logins específicos por cliente
├── scheduler/       # Agendamento de tarefas automáticas
├── src/             # Módulos principais: carregamento, validação, envio
│   ├── itau/             # Validador e gerador do Itaú
│   ├── mercado_pago/     # Validador e gerador do Mercado Pago
│   ├── redecard/         # Validador e gerador do Redecard
│   ├── skypostal/        # Validador e gerador do Skypostal
│   ├── email/            # Disparo de e-mails
│   └── carregamento/     # Leitura de planilhas
├── utils/           # Funções auxiliares (formatação, manipulação de arquivos)
├── config.py        # Configurações do sistema
├── main.py          # Execução principal do projeto
└── documentacao/    # Documentação formal do projeto (.docx)
```

---

## 🚀 Como Executar

### 1. Instalar dependências

```bash
pip install .
```

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz com os dados sensíveis:

```
GA_LOGIN=seu_usuario
GA_SENHA=sua_senha
MAILGRID_API_KEY=sua_chave
```

### 3. Executar o sistema

```bash
python main.py
```

### 4. Rodar o agendador (opcional)

```bash
python scheduler/agendador.py
```

---

## 🧾 Documentação Completa

A documentação técnica detalhada está disponível em:  
`/documentacao/documentacao_automacoes_v1.docx`

---

## 👨‍💻 Desenvolvedor

**Gabriel Ferreira**  
📧 gabrielsilvaferreira007@gmail.com  
📅 Última atualização: Julho/2025

---

## 🏷️ Tecnologias Utilizadas

- Python 3.11  
- Selenium  
- pandas / openpyxl  
- dotenv  
- Mailgrid API   
- Scheduler
