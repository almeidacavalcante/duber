import psycopg2
import uuid
import re
import smtplib
from email.message import EmailMessage


class AccountService:
    def __init__(self):
        pass

    def send_email(self, email, subject, message):
        # Implemente aqui o código para enviar o e-mail.
        print(email, subject, message)

    def validate_cpf(self, cpf_str):
        try:
            cpf_str = re.sub(r"[.-\s]", "", cpf_str)
            if len(cpf_str) == 11 and not all(c == cpf_str[0] for c in cpf_str):
                d1, d2 = 0, 0
                for i in range(9):
                    d1 += int(cpf_str[i]) * (10 - i)
                    d2 += int(cpf_str[i]) * (11 - i)
                d1 = 11 - d1 % 11 if d1 % 11 >= 2 else 0
                d2 = 11 - (d2 + d1 * 2) % 11 if (d2 + d1 * 2) % 11 >= 2 else 0
                return cpf_str[-2:] == f"{d1}{d2}"
            return False
        except Exception as e:
            print(f"Erro: {e}")
            return False

    def signup(self, input_data):
        connection = psycopg2.connect(
            "dbname=app user=postgres password=123456 host=localhost port=5432"
        )
        cursor = connection.cursor()

        try:
            account_id = str(uuid.uuid4())
            verification_code = str(uuid.uuid4())
            date = "CURRENT_TIMESTAMP"

            cursor.execute(
                "SELECT * FROM cccat13.account WHERE email = %s", (input_data["email"],)
            )
            existing_account = cursor.fetchone()

            if not existing_account:
                if re.match(r"[a-zA-Z]+\s[a-zA-Z]+", input_data["name"]):
                    if re.match(r"(.+)@(.+)", input_data["email"]):
                        if self.validate_cpf(input_data["cpf"]):
                            if input_data.get("isDriver"):
                                if re.match(
                                    r"[A-Z]{3}[0-9]{4}", input_data["carPlate"]
                                ):
                                    cursor.execute(
                                        "INSERT INTO cccat13.account (account_id, name, email, cpf, car_plate, is_passenger, is_driver, date, is_verified, verification_code) VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, %s, %s)",
                                        (
                                            account_id,
                                            input_data["name"],
                                            input_data["email"],
                                            input_data["cpf"],
                                            input_data["carPlate"],
                                            input_data.get("isPassenger", False),
                                            input_data.get("isDriver", False),
                                            False,
                                            verification_code,
                                        ),
                                    )
                                    self.send_email(
                                        input_data["email"],
                                        "Verification",
                                        f"Please verify your code at first login {verification_code}",
                                    )
                                    connection.commit()
                                    return {"accountId": account_id}
                                else:
                                    raise ValueError("Invalid plate")
                            else:
                                cursor.execute(
                                    "INSERT INTO cccat13.account (account_id, name, email, cpf, car_plate, is_passenger, is_driver, date, is_verified, verification_code) VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, %s, %s)",
                                    (
                                        account_id,
                                        input_data["name"],
                                        input_data["email"],
                                        input_data["cpf"],
                                        input_data.get("carPlate", None),
                                        input_data.get("isPassenger", False),
                                        input_data.get("isDriver", False),
                                        False,
                                        verification_code,
                                    ),
                                )
                                self.send_email(
                                    input_data["email"],
                                    "Verification",
                                    f"Please verify your code at first login {verification_code}",
                                )
                                connection.commit()
                                return {"accountId": account_id}
                        else:
                            raise ValueError("Invalid CPF")
                    else:
                        raise ValueError("Invalid email")
                else:
                    raise ValueError("Invalid name")
            else:
                raise ValueError("Account already exists")
        finally:
            cursor.close()
            connection.close()

    def get_account(self, account_id):
        connection = psycopg2.connect(
            "dbname=app user=postgres password=123456 host=localhost port=5432"
        )
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM cccat13.account WHERE account_id = %s", (account_id,)
        )
        account = cursor.fetchone()
        cursor.close()
        connection.close()
        return account


if __name__ == "__main__":
    # Teste o código aqui
    pass
