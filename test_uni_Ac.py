import jeux_prik


def test_tresor_chateau(monkeypatch, capsys):
    reponses = iter([
        "Alex", "1", "1", "1", "1", "1", "1", "1"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(reponses))

    jeux_prik.debut()

    resultat = capsys.readouterr()

    assert "Tu trouves un trésor caché !" in resultat.out
    assert "FÉLICITATIONS" in resultat.out


def test_foret_hantee(monkeypatch, capsys):
    reponses = iter([
        "Alex", "2", "2", "2", "2", "2", "2", "2"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(reponses))

    jeux_prik.debut()

    resultat = capsys.readouterr()

    assert "Un gros monstre garde un trésor dans la grotte !" in resultat.out
    assert "FIN DE L'AVENTURE" in resultat.out
