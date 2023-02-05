
class Category:
    general = 0
    artist = 1
    copyright = 3
    character = 4
    meta = 5

    def __init__(self):
        self.__tags = {
            "artist": 1,
            "copyright": 3,
            "character": 4,
            "meta": 5
        }

        self.__sgat = {
            0: "general",
            1: "artist",
            3: "copyright",
            4: "character",
            5: "meta"
        }

    def get_category(self, _i):
        if isinstance(_i, str):
            return self.__tags.get(_i)
        else:
            return self.__sgat.get(_i)


get_category = Category().get_category


class Tag:
    def __init__(self,
                 _id: int = None,
                 name: str = None,
                 post_count: int = None,
                 category: int = None,
                 created_at: str = None,
                 updated_at: str = None,
                 is_locked: bool = None,
                 words: list[str] = None,
                 is_deprecated: bool = None
                 ):
        self.id = _id
        self.name = name
        self.words = words
        self.post_count = post_count
        self.category = category
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_locked = is_locked
        self.is_deprecated = is_deprecated

    def __str__(self):
        return str(self.__dict__())

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "post_count": self.post_count,
            "category": self.category,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "words": self.words,
            "is_locked": self.is_locked
        }


class Autocomplete:
    def __init__(self,
                 _type: str = None,
                 label: str = None,
                 value: str = None,
                 category: int = None,
                 post_count: int = None,
                 antecedent: str = None
                 ):
        self.type = _type
        self.label = label
        self.value = value
        self.category = category
        self.post_count = post_count
        self.antecedent = antecedent

    def __str__(self):
        return str(self.__dict__())

    def __dict__(self):
        return {
            "type": self.type,
            "label": self.label,
            "value": self.value,
            "category": self.category,
            "post_count": self.post_count,
            "antecedent": self.antecedent
        }
