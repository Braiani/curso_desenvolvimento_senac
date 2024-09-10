import os, sys
import hashlib

class Utils:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_base_path():
        return os.path.dirname(os.path.abspath(sys.argv[0]))
    
    @staticmethod
    def generate_md5(text: str):
        return hashlib.md5(text.encode('utf-8')).hexdigest()

if __name__ == "__main__":
    import Main
    
    Main