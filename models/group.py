class Group:
    def __init__(self, name='', header='', footer='', id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __str__(self):
        return "Group: {}, {}, {} (id={})".format(self.name, self.header, self.footer, self.id)

    def __repr__(self):
        return "Group: {}, {}, {} (id={})".format(self.name, self.header, self.footer, self.id)

    def __eq__(self, other):
        """ Для того, чтобы мы могли сравнивать наши объекты на равенство == """
        if self.id is not None:
            return self.id == other.id and self.name == other.name
        return self.name == other.name and self.header == other.header and self.footer == other.footer


if __name__ == "__main__":
    print(Group(name="Main"))
