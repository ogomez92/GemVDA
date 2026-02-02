# GemVDA NVDA Add-on - API Key Manager
# -*- coding: utf-8 -*-

import os
import ctypes
import ctypes.wintypes
from logHandler import log


class DPAPIError(Exception):
    """Exception raised when DPAPI operations fail."""
    pass


class DPAPI:
    """Windows Data Protection API wrapper for encrypting/decrypting data."""

    # DPAPI structures
    class DATA_BLOB(ctypes.Structure):
        _fields_ = [
            ("cbData", ctypes.wintypes.DWORD),
            ("pbData", ctypes.POINTER(ctypes.c_char)),
        ]

    def __init__(self):
        self._crypt32 = ctypes.windll.crypt32
        self._kernel32 = ctypes.windll.kernel32

    def encrypt(self, data: str) -> bytes:
        """
        Encrypt a string using Windows DPAPI.
        The encrypted data can only be decrypted by the same Windows user.
        """
        data_bytes = data.encode("utf-8")

        # Input blob
        input_blob = self.DATA_BLOB()
        input_blob.cbData = len(data_bytes)
        input_blob.pbData = ctypes.cast(
            ctypes.create_string_buffer(data_bytes, len(data_bytes)),
            ctypes.POINTER(ctypes.c_char)
        )

        # Output blob
        output_blob = self.DATA_BLOB()

        # Call CryptProtectData
        # Flags: CRYPTPROTECT_UI_FORBIDDEN (0x1) - don't show UI
        result = self._crypt32.CryptProtectData(
            ctypes.byref(input_blob),  # pDataIn
            None,  # szDataDescr (optional description)
            None,  # pOptionalEntropy (additional entropy)
            None,  # pvReserved
            None,  # pPromptStruct
            0x1,   # dwFlags - CRYPTPROTECT_UI_FORBIDDEN
            ctypes.byref(output_blob)  # pDataOut
        )

        if not result:
            error_code = ctypes.get_last_error()
            raise DPAPIError(f"CryptProtectData failed with error code: {error_code}")

        # Copy encrypted data
        encrypted_data = ctypes.string_at(output_blob.pbData, output_blob.cbData)

        # Free the memory allocated by DPAPI
        self._kernel32.LocalFree(output_blob.pbData)

        return encrypted_data

    def decrypt(self, encrypted_data: bytes) -> str:
        """
        Decrypt data that was encrypted with Windows DPAPI.
        Must be decrypted by the same Windows user who encrypted it.
        """
        # Input blob
        input_blob = self.DATA_BLOB()
        input_blob.cbData = len(encrypted_data)
        input_blob.pbData = ctypes.cast(
            ctypes.create_string_buffer(encrypted_data, len(encrypted_data)),
            ctypes.POINTER(ctypes.c_char)
        )

        # Output blob
        output_blob = self.DATA_BLOB()

        # Call CryptUnprotectData
        result = self._crypt32.CryptUnprotectData(
            ctypes.byref(input_blob),  # pDataIn
            None,  # ppszDataDescr
            None,  # pOptionalEntropy
            None,  # pvReserved
            None,  # pPromptStruct
            0x1,   # dwFlags - CRYPTPROTECT_UI_FORBIDDEN
            ctypes.byref(output_blob)  # pDataOut
        )

        if not result:
            error_code = ctypes.get_last_error()
            raise DPAPIError(f"CryptUnprotectData failed with error code: {error_code}")

        # Copy decrypted data
        decrypted_data = ctypes.string_at(output_blob.pbData, output_blob.cbData)

        # Free the memory allocated by DPAPI
        self._kernel32.LocalFree(output_blob.pbData)

        return decrypted_data.decode("utf-8")


class APIKeyManager:
    """Manages Gemini API key storage and retrieval with encryption."""

    ENV_VAR_NAMES = ["GEMINI_API_KEY", "GOOGLE_API_KEY"]

    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.key_file = os.path.join(data_dir, "api.key.enc")
        self._legacy_key_file = os.path.join(data_dir, "gemini.key")
        self._dpapi = DPAPI()

        # Migrate legacy plaintext key if exists
        self._migrate_legacy_key()

    def _migrate_legacy_key(self):
        """Migrate old plaintext key to encrypted format."""
        if os.path.exists(self._legacy_key_file):
            try:
                with open(self._legacy_key_file, "r", encoding="utf-8") as f:
                    plaintext_key = f.read().strip()

                if plaintext_key:
                    # Save with encryption
                    if self.save_api_key(plaintext_key):
                        # Remove old plaintext file
                        os.remove(self._legacy_key_file)
                        log.info("Migrated API key from plaintext to encrypted storage")
                    else:
                        log.warning("Failed to migrate API key to encrypted storage")
            except Exception as e:
                log.error(f"Error migrating legacy API key: {e}")

    def get_api_key(self) -> str | None:
        """
        Get the API key from encrypted file or environment variable.
        Priority: encrypted file > GEMINI_API_KEY > GOOGLE_API_KEY
        """
        # Try encrypted file first
        if os.path.exists(self.key_file):
            try:
                with open(self.key_file, "rb") as f:
                    encrypted_data = f.read()
                    if encrypted_data:
                        key = self._dpapi.decrypt(encrypted_data)
                        if key:
                            return key
            except DPAPIError as e:
                log.error(f"Error decrypting API key: {e}")
            except Exception as e:
                log.error(f"Error reading API key file: {e}")

        # Try environment variables
        for env_var in self.ENV_VAR_NAMES:
            key = os.environ.get(env_var, "").strip()
            if key:
                return key

        return None

    def save_api_key(self, key: str) -> bool:
        """Save the API key to encrypted file using Windows DPAPI."""
        try:
            # Ensure directory exists
            os.makedirs(self.data_dir, exist_ok=True)

            # Encrypt the key
            encrypted_data = self._dpapi.encrypt(key.strip())

            # Write encrypted data
            with open(self.key_file, "wb") as f:
                f.write(encrypted_data)

            return True
        except DPAPIError as e:
            log.error(f"Error encrypting API key: {e}")
            return False
        except Exception as e:
            log.error(f"Error saving API key: {e}")
            return False

    def delete_api_key(self) -> bool:
        """Delete the stored API key."""
        try:
            if os.path.exists(self.key_file):
                os.remove(self.key_file)
            # Also remove legacy file if exists
            if os.path.exists(self._legacy_key_file):
                os.remove(self._legacy_key_file)
            return True
        except Exception as e:
            log.error(f"Error deleting API key: {e}")
            return False

    def is_ready(self) -> bool:
        """Check if an API key is available."""
        return self.get_api_key() is not None

    def get_key_source(self) -> str:
        """Get where the API key is coming from."""
        if os.path.exists(self.key_file):
            try:
                with open(self.key_file, "rb") as f:
                    if f.read():
                        return "encrypted file"
            except Exception:
                pass

        for env_var in self.ENV_VAR_NAMES:
            if os.environ.get(env_var, "").strip():
                return f"environment ({env_var})"

        return "none"


# Global instance
_manager: APIKeyManager | None = None

def get_manager(data_dir: str) -> APIKeyManager:
    """Get or create the API key manager instance."""
    global _manager
    if _manager is None:
        _manager = APIKeyManager(data_dir)
    return _manager
