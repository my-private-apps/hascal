class Variable(object):
    def __init__(self, t_type, t_name, t_value):
        self.type = t_type
        self.value = t_value
        self.name = t_name

    def __repr__(self):
        return "Variable(\"{}\",\"{}\",\"{}\")".format(self.type, self.name,
                                                       self.value)


class Validate():
    variables = []
    funcs = []

    def __init__(self):
        pass

    def AddVariable(self, var_type, var_name, var_value):
        for x in self.variables:
            if x == var_name:
                print(f"Error : variable existed {var_name}")
            else:
                self.variables.append(Variable(var_type, var_name, var_value))

    def ValidateAssign(self, var_name, assign_value, assign_type):
        for x in self.variables:
            if x.name == var_name:
                if x.type == assign_type:
                    x.value = assign_value
                    return True
                else:
                    print(f"Error : Incompatible types : {var_name}")
                    return False
            else:
                print(f"Error : {var_name} not defined\n")
                return False

    def Exist(self, name):
        if x in self.variables or xx in self.funcs:
            return True
        else:
            print(f"Error : {name} not defined.")
