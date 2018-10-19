from types import ModuleType
from typing import Any, Union, Tuple

__all__ = ['SivMode']

class SivMode(object):
    block_size: int
    nonce: bytes
    def __init__(self, factory: ModuleType, key: Union[bytes, bytearray, memoryview], nonce: Union[bytes, bytearray, memoryview], kwargs: Any) -> None: ...
    def update(self, component: Union[bytes, bytearray, memoryview]) -> SivMode: ...  # TODO Is the return type correct?
    def encrypt(self, plaintext: Union[bytes, bytearray, memoryview]) -> bytes: ...
    def decrypt(self, ciphertext: Union[bytes, bytearray, memoryview]) -> bytes: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def verify(self, received_mac_tag: Union[bytes, bytearray, memoryview]) -> None: ...
    def hexverify(self, hex_mac_tag: str) -> bytes: ...
    def encrypt_and_digest(self, plaintext: Union[bytes, bytearray, memoryview]) -> Tuple[bytes, bytes]: ...
    def decrypt_and_verify(self, ciphertext: Union[bytes, bytearray, memoryview], mac_tag: Union[bytes, bytearray, memoryview]) -> bytes: ...
