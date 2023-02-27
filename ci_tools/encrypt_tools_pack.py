import base64

from cryptography.fernet import Fernet


class EncryptingToolsPack:
    def __init__(self):
        pass

    def encrypt(self, key, file_name=None, txt=None):
        """
        Encrypt message or file
        :param key: symmetric key for encrypting and decrypting
        :param file_name: input file for encrypt
        :param txt: message for encrypt
        :return:
        """
        fernet_key = base64.urlsafe_b64encode((key + '&' * 32)[:32].encode("utf-8"))
        fernet = Fernet(fernet_key)

        encrypted = None
        if file_name is not None:
            with open(file_name, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)

        if txt is not None:
            encrypted = fernet.encrypt(txt.encode("utf-8"))

        return encrypted.decode("utf-8")

    def decrypt(self, key, file_name=None, txt=None):
        """
        Decrypt message or file
        :param key: symmetric key for encrypting and decrypting
        :param file_name: input file for encrypt
        :param txt: message for encrypt
        :return:
        """
        fernet_key = base64.urlsafe_b64encode((key + '&' * 32)[:32].encode("utf-8"))
        fernet = Fernet(fernet_key)

        decrypted = None
        if file_name is not None:
            with open(file_name, 'rb') as file:
                original = file.read()
            decrypted = fernet.decrypt(original)

        if txt is not None:
            decrypted = fernet.decrypt(txt)

        return decrypted.decode("utf-8")
