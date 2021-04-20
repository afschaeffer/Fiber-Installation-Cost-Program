print("WeLcOmE tO fIbEr OpTiC cAbLe InStAlLaTiOn CoMpAnY!")
company_name = input('Company Name: ')
feet_required = input('Feet of fiber optic cable needed to be installed: ')
calculated_cost = int(feet_required) * .87
message = f"{company_name}, your estimated cost is: $ {calculated_cost}"
print(message)
