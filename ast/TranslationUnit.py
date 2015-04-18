__author__ = 'nidys'

class Translation_unit(object):
    def __init__(self, external_decl=''):
        self.external_decl = external_decl

    def __str__(self):
        return str(self.external_decl)

class External_decl(object):
    def __init__(self, decl=''):
        self.decl = decl

    def __str__(self):
        return str(self.decl)

class Decl(object):
    def __init__(self, decl_specs=''):
        self.decl_specs = decl_specs
        self.sem_colon = ';'

    def __str__(self):
        return str(self.decl_specs) + str(self.sem_colon)

class Decl_specs(object):
    def __init__(self, type_spec='', second_type_spec=''):
        self.type_spec = type_spec
        self.second_type_spec = second_type_spec

    def __str__(self):
        return str(self.type_spec) + str(self.second_type_spec)

class Type_spec(object):
    def __init__(self, type='', typedef_name=''):
         #TODO separate white spaces
        self.type = type
        self.typedef_name = typedef_name

    def __str__(self):
        return self.type + str(self.typedef_name)

class Typedef_name(object):
    def __init__(self, id):
        #TODO separate white spaces
        self.id = id

    def __str__(self):
        return self.id


