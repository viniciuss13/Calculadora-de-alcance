# a cada 100 pessoas que visualizam o anúncio 12 clicam nele.
# a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
# cada compartilhamento nas redes sociais gera 40 novas visualizações.
# 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
# o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
# (1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa)

import unittest


def clicks_views(views: float) -> float:
    """
    A cada 100 pessoas que visualizam o anúncio 12 clicam nele.

    :param views: Quantidade de visualizações
    :return: Quantidade de cliques por visualizações
    """

    return views / 100 * 12


def shares_clicks(clicks: float) -> float:
    """
    A cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.

    :param clicks: Quantidade de cliques
    :return: Quantiade de compartilhamentos
    """

    return clicks / 20 * 3


def views_shares(shares: float) -> float:
    """
    Cada compartilhamento nas redes sociais gera 40 novas visualizações.

    :param shares: Quantidade de Compartilhamentos
    :return: Quantidade de visualizações
    """

    return shares * 40


def views_budget(budget: float) -> float:
    """
    30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.

    :param budget: Valor orçado
    :return: Visualizações recebidas
    """

    return budget * 30


def views_multiplier(views: float) -> float:
    """
    o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
    (1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa)

    :param views: Visualizações
    :return: Visualizações considerando compartilhamentos em sequência
    """

    return views * 4


def total_views(budget: float) -> int:
    """
    Calcula o total de visualizações considerando compartilhamentos e o valor orçado

    :param budget: Valor orçado
    :return: Quantidade aproximada de visualizações
    """

    views = views_budget(budget)
    clicks = clicks_views(views)
    shares = shares_clicks(clicks)
    views += views_shares(shares)
    views = views_multiplier(views)

    return int(views)


def main():
    budget = float(input('Digite o valor orçado: '))
    views = total_views(budget)
    print(f'Sua campanha terá no máximo {views} visualizações.')


class TestCases(unittest.TestCase):
    def test_views_budget(self):
        self.assertEqual(views_budget(1.), 30)
        self.assertEqual(views_budget(2.30), 69)
        self.assertEqual(views_budget(100), 3000)

    def test_clicks_views(self):
        self.assertEqual(clicks_views(100), 12)
        self.assertEqual(clicks_views(167), 20.04)
        self.assertEqual(clicks_views(170), 20.4)

    def test_shares_clicks(self):
        self.assertEqual(shares_clicks(100), 15)
        self.assertEqual(shares_clicks(130), 19.5)
        self.assertEqual(shares_clicks(170), 25.5)

    def test_views_shares(self):
        self.assertEqual(views_shares(100), 4000)
        self.assertEqual(views_shares(130), 5200)
        self.assertEqual(views_shares(170), 6800)

    def test_views_multiplier(self):
        self.assertEqual(views_multiplier(100), 400)
        self.assertEqual(views_multiplier(130), 520)
        self.assertEqual(views_multiplier(170), 680)

    def test_total_views(self):
        self.assertEqual(total_views(100), 20640)
        self.assertEqual(total_views(130), 26832)
        self.assertEqual(total_views(170), 35088)


if __name__ == "__main__":
    main()
