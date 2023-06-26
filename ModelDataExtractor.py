# This file is used to extract the data from the models in the Models/OriginalModels folder
# It will create a new file in the Models/ExtractedModels folder with the same name as the original file
# The new file will be a python file with a class for each model in the original file
# Each class will have a get_data() function that returns a dictionary with the same variables as the original model
# The dictionary will have empty strings as values for each variable unless otherwise specified
# Overall this code is used to provide a shoddy way to convert C# models to python models

# I will not include the original or extracted models in this repository as they contain potentially sensitive information about the database

import os
import errno
import re

extracted_models = '../Models/ExtractedModels'
original_models  = '../Models/OriginalModels'

class_match = "public class ([a-zA-Z]+ ?)(: [a-zA-Z]+)?"
var_match = "public .* ([a-zA-Z]+) { get; set; }"

def main():
    for subdir, dirs, files in os.walk(original_models):
        for file in files:

            oldFile = os.path.join(subdir, file)
            newFile = oldFile.replace('OriginalModels', 'ExtractedModels')

            if not os.path.exists(os.path.dirname(newFile)):
                try:
                    os.makedirs(os.path.dirname(newFile))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise

            with open(oldFile, 'r') as modelcs, open(newFile.replace(".cs", ".py"), 'w') as newModel:
                oldFileLine = modelcs.readline()
                class_dict = {}
                current_class = ''
                while oldFileLine:
                    class_matched = re.search(class_match, oldFileLine)
                    var_matched = re.search(var_match, oldFileLine)
                    if class_matched is not None and len(class_matched.groups()) > 0:
                        current_class = class_matched.group(1)
                        class_dict[current_class] = {}
                    if var_matched is not None and len(var_matched.groups()) > 0:
                        class_dict[current_class][var_matched.group(1)] = ''
                    
                    oldFileLine = modelcs.readline()

                for key in class_dict:
                    newModel.write(f"class {key}:\n")
                    newModel.write(f"\tdef get_data():\n")
                    newModel.write("\t\tdata = {\n")
                    for var in class_dict[key]:
                        newModel.write(f"\t\t\t'{var}' : '',\n")
                    newModel.write("\t\t}\n")
                    newModel.write("\t\treturn data\n\n")

if __name__ == "__main__":
    main()