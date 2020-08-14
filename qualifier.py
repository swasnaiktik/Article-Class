"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import re


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type
        self.attribute = None

    def __get__(self, instance, owner):
        return self.attribute

    def __set__(self, instance, value):
        if self.field_type == type(value):
            self.attribute = value
        else:
            raise TypeError("expected an instance of type '{0}' for "
                            "attribute '{1}', got '{2}' instead".format(self.field_type, instance, type(value)))


class Article:
    """The `Article` class you need to write for the qualifier."""
    id = -1
    attribute = ArticleField(field_type=int)

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):

        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
        self.word_dict = None
        self.last_edited = None
        Article.id += 1
        self.id = Article.id

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    def __eq__(self, other):
        return self.publication_date == other.publication_date

    def __setattr__(self, key, value):
        if key == "content":
            self.__dict__["last_edited"] = datetime.datetime.now()
        self.__dict__[key] = value

    def __repr__(self):
        return """<Article title="{}" author='{}' publication_date='{}'>""".format(self.title, self.author,
                                                                                   self.publication_date.isoformat())

    def __len__(self):
        return len(self.content)

    def short_introduction(self, n_characters: int):
        if self.content[n_characters] == " " or self.content[n_characters] == "\n":
            return self.content[:n_characters]
        else:
            return self.short_introduction(n_characters=n_characters - 1)

    def splitContent(self):
        a = self.content
        return re.findall(r"\w+", a)

    def most_common_words(self, n_words):
        split = self.splitContent()
        self.word_dict = {}
        for word in split:
            self.word_dict[word.lower()] = self.word_dict.get(word.lower(), 0) + 1
        Value = self.word_dict
        Value = list(Value.items())
        Value.sort(key=lambda x: (x[1]), reverse=True)
        returnV = {}
        for key, value in Value[:n_words]:
            returnV[key] = value
        return returnV
