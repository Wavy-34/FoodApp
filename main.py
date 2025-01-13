from food_app.consts import *
from food_app.create_hashed_password import hash_password

def main() -> None:
    password = DATABASE_PASSWORD
    print(hash_password(password))

if __name__ == '__main__':
    main()