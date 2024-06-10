class ConfigManager:
    _instance = None
    cfg = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def set_cfg(cls, cfg):
        cls.cfg = cfg

    @classmethod
    def get_cfg(cls):
        return cls.cfg
