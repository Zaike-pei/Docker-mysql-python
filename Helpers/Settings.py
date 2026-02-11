from dotenv import load_dotenv
from pathlib import Path
import os

class Settings:
    #.envファイルのパスを取得
    ENV_PATH = (Path(__file__).parent / "../.env").resolve()

    #ロード済みフラグ
    _loaded = False

    @classmethod
    def _load_env(cls):
        # envファイルを読み込んでいるかの判定
        if cls._loaded:
            return
        # pathが存在するか
        if not cls.ENV_PATH.exists():
            raise FileExistsError(f".envファイルが見つかりません：{cls.ENV_PATH}")
        
        result = load_dotenv(cls.ENV_PATH)

        if not result:
            raise RuntimeError(".envファイルの読み込みに失敗しました")
        
        cls._loaded = True

    @classmethod
    def get(cls, key:str, default = None):
        #文字列の取得
        cls._load_env()

        value = os.getenv(key, default)

        if value is None:
            raise KeyError(f"{key}は.envファイルに定義されていません")
        
        return value
    
    @classmethod
    def get_int(cls, key:str, default= None):
        value = cls.get(key, default)

        try:
            return int(value)
        except ValueError:
            raise ValueError("f{key}は整数ではありません: {value}")
     
    @classmethod
    def get_bool(cls, key:str, default=None):
        value = cls.get(key, default)

        if isinstance(value, bool):
            return value
        
        value.lower()

        if value in ('true', '1', 'yes', 'on'):
            return True
        elif value in ('false', '0', 'no', 'off'):
            return False
        else:
            raise ValueError('f{key}はbool型に変換できません: {value}')



