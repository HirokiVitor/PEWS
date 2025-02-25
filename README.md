# 🏥 PEWS - Sistema de Triagem Infantil

## 📌 Descrição do Projeto
O **PEWS (Pediatric Early Warning Score)** é um sistema para **triagem pediátrica hospitalar**, permitindo que profissionais da saúde registrem avaliações de pacientes e monitorem sua evolução clínica. O sistema auxilia na previsão de intervenções médicas necessárias.

### 🔹 Funcionalidades
✅ Cadastro de Pacientes  
✅ Registro de Avaliações com cálculo automático do **PEWS Score**  
✅ Histórico de Avaliações com **gráficos interativos**  
✅ Autenticação de Usuários e Controle de Acesso  
✅ Perfis de Funcionários e Administração  
✅ **Gestão de Pacientes** (internação e alta médica)  
✅ Testes de unidade e E2E para validação do sistema  

---

## 🚀 Tecnologias Utilizadas
### 🔹 Backend
- **Django** - Framework principal  
- **Django REST Framework** - Criação das APIs  
- **SQLite** - Banco de dados (pode ser substituído por PostgreSQL)  

### 🔹 Frontend
- **HTML + CSS + JavaScript**  
- **Bootstrap** - Estilização da interface  
- **Chart.js** - Exibição de gráficos  

### 🔹 Outros
- **Git e GitHub** - Controle de versão e colaboração  
- **Docker (Opcional)** - Containerização do ambiente  
- **Pytest / Selenium** - Testes de unidade e testes E2E  

---

## 🔧 Instalação e Execução do Projeto
### 1️⃣ Clonar o Repositório
git clone https://github.com/HirokiVitor/PEWS.git cd PEWS

### 2️⃣ Criar um Ambiente Virtual e Instalar Dependências
python -m venv venv source venv/bin/activate # (Linux/macOS) venv\Scripts\activate # (Windows) pip install -r requirements.txt

### 3️⃣ Aplicar Migrações e Criar Superusuário
python manage.py migrate python manage.py createsuperuser

Após criar o superusuário, ele poderá **cadastrar funcionários e gerenciar avaliações**.

### 4️⃣ Rodar o Servidor Django
python manage.py runserver

Agora, acesse **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** e o sistema estará funcionando!

---

## 📌 Padrão de Projeto Utilizado: Facade
Para simplificar a **lógica de negócios do sistema**, utilizamos o **padrão de projeto Facade**, que centraliza operações complexas em uma única classe.

### 🔹 Implementação do Facade (`services.py`)
```python
from datetime import datetime
from .models import Paciente, Avaliacao

class TriagemService:
    """
    Classe Facade para operações de Paciente e Avaliação.
    """
    @staticmethod
    def cadastrar_paciente(nome, idade, leito, dih, diagnostico, data_internacao=None):
        if data_internacao is None:
            data_internacao = datetime.now()
        return Paciente.objects.create(
            nome=nome, idade=idade, leito=leito, dih=dih, 
            diagnostico=diagnostico, data_internacao=data_internacao
        )
    @staticmethod
    def registrar_avaliacao(paciente_id, score, freq_cardiaca, freq_respiratoria, 
                            av_neuro, av_cardio, av_resp, extras, analise=None):
        paciente = Paciente.objects.get(id=paciente_id)
        return Avaliacao.objects.create(
            paciente=paciente,
            score=score,
            freq_cardiaca=freq_cardiaca,
            freq_respiratoria=freq_respiratoria,
            av_neuro=av_neuro,
            av_cardio=av_cardio,
            av_resp=av_resp,
            extras=extras,
            analise=analise
        )
    @staticmethod
    def dar_alta_paciente(paciente_id):
        paciente = Paciente.objects.get(id=paciente_id)
        paciente.delete()
        return f"{paciente.nome} recebeu alta com sucesso!"
```

✅ Isso melhora a organização do código e facilita a manutenção do sistema!

📌 Testes Implementados
O sistema contém testes de unidade e testes E2E (end-to-end) para garantir o funcionamento correto.

🧪 Testes de Unidade
from django.test import TestCase
from .models import Paciente

```python
class PacienteTestCase(TestCase):
    def test_criacao_paciente(self):
        paciente = Paciente.objects.create(
            nome="João Silva", idade=5, leito="A12", dih="123456",
            diagnostico="Bronquite", data_internacao="2024-06-01"
        )
        self.assertEqual(paciente.nome, "João Silva")
```

📌 Executar os testes

```python
python manage.py test
pytest tests/
```
✅ Os testes garantem que o sistema está funcionando como esperado!
