import pytest
from routes.main_routes import validate_email

# Expression régulière pour valider une adresse e-mail
emailRegex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

@pytest.mark.parametrize("email, expected_result", [
    # Jeux de données de test avec des adresses e-mail valides et invalides
    ("user@example.com", True),
    ("user.name@example.com", True),
    ("user123@example.com", True),
    ("invalid_email", False),
    ("   ", False),  # Chaîne vide considérée comme invalide
])
def test_validate_email(email, expected_result):
    """
    Test unitaire pour la fonction validate_email.

    Args:
        email (str): Adresse e-mail à tester.
        expected_result (bool): Résultat attendu de la validation.
    """
    # Act
    result = validate_email(email)

    # Assert
    assert result == expected_result