from src.app import create_app

client = create_app()

# Allows us to test our routes


def create_test_client():
    # Allows us to test our routes
    return client.test_client()
