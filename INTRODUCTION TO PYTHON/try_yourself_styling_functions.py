# Put the functions for the example printing_models.py in a separate file called printing 
# models_module.py Write an import statement at the top of printing_models_module.py, and modify
# the file to use the imported functions.


from printing_models_module import printing_designs, summarize_prints

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
printed_designs = []

printing_designs(unprinted_designs[:], printed_designs)
summarize_prints(printed_designs)

import printing_models_module 
from printing_models_module import printing_designs
from printing_models_module import printing_designs as dp 
import printing_models_module as pmm 
from printing_models_module import * 
