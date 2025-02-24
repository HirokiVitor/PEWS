from django.test import TestCase
from triagem.models import Paciente, Avaliacao
from triagem.services import TriagemService

class TriagemServiceTest(TestCase):
    def setUp(self):
        """
        Configuração inicial: cria um paciente para ser usado nos testes.
        """
        self.paciente = TriagemService.cadastrar_paciente(
            "João Pedro", 5, "102A", "D789", "Pneumonia"
        )

    def test_cadastro_paciente(self):
        """
        Verifica se o paciente foi cadastrado corretamente.
        """
        self.assertEqual(self.paciente.nome, "João Pedro")
        self.assertEqual(self.paciente.idade, 5)

    def test_cadastro_avaliacao(self):
        """
        Verifica se a avaliação está sendo registrada corretamente.
        """
        avaliacao = TriagemService.registrar_avaliacao(
            self.paciente.id, 4, 110, 28, "Alerta", "Pressão normal", "Respiração normal", "Nenhum", "Paciente estável"
        )
        self.assertEqual(avaliacao.paciente, self.paciente)
        self.assertEqual(avaliacao.score, 4)
