# Below function will print all possible sentances in subject, verb, object format
def createMeaningfulStatements(subjects,verbs,objects):
    for x in subjects:
        for y in verbs:
            for z in objects:
                print (x+" "+ y +" "+z)

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

# Passing the list arguments to the createMeaningfulStatements functions
createMeaningfulStatements(subjects,verbs,objects)

