from django.core.management.utils import get_random_secret_key

if __name__ == "__main__":
    print(f"Django secret key:\n{get_random_secret_key()}")
