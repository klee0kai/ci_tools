import base64

from cryptography.fernet import Fernet


class EncryptingToolsPack:
    def __init__(self):
        pass

    def encrypt_file(self, key, in_file, out_file):
        """
        Encrypt file by fernet
        :param key: symmetric key for encrypting and decrypting
        :param in_file: input file
        :param out_file: input file for encrypt
        :return:
        """
        fernet_key = base64.urlsafe_b64encode((key + '&' * 32)[:32].encode("utf-8"))
        fernet = Fernet(fernet_key)

        encrypted = None
        with open(in_file, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)

        with(open(out_file, "wb")) as f:
            f.write(encrypted)

        return f"ecrypted {in_file} to {out_file}"

    def decrypt_file(self, key, in_file, out_file):
        """
        Decrypt file by fernet
        :param key: symmetric key for encrypting and decrypting
        :param in_file: input encrypted file
        :param out_file: output encrypted file
        :return:
        """
        fernet_key = base64.urlsafe_b64encode((key + '&' * 32)[:32].encode("utf-8"))
        fernet = Fernet(fernet_key)

        decrypted = None
        with open(in_file, 'rb') as file:
            original = file.read()
        decrypted = fernet.decrypt(original)

        with(open(out_file, "wb")) as f:
            f.write(decrypted)

        return f"decrypted {in_file} to {out_file}"
