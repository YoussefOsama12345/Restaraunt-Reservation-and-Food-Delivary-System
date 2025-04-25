from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

if __name__ == "__main__":
    password = input("Enter the password to hash: ")
    print("Hashed password:", pwd_context.hash(password))
