
       
        # Loads the data_set specified by 'filename' into a 2d array
def load_data_set("Namen_vrouw_per_10_jaar.csv"):
    with open("Namen_vrouw_per_10_jaar.csv", "rU") as f:
        f.readline()
        return [[float(x) for x in row] for row in csv.reader(f, delimiter=';')])
 data =load_data_set("Namen_vrouw_per_10_jaar.csv")

# dit sorteert alle lijsten op het nummer voor 1900
one = data.sort(key=lambda x: x[2],reverse=True)
# dit sorteert alle lijsten op het nummer voor 1910
two = data.sort(key=lambda x: x[3,reverse=True])
# dit sorteert alle lijsten op het nummer voor 1920
 third = data.sort(key=lambda x: x[4],reverse=True)
# dit sorteert alle lijsten op het nummer voor 1930
fourth = data.sort(key=lambda x: x[5],reverse=True)
# dit sorteert alle lijsten op het nummer voor 1940
fifth = data.sort(key=lambda x: x[6],reverse=True)
# dit sorteert alle lijsten op het nummer voor 1950
six = data.sort(key=lambda x: x[7],reverse=True)
# dit sorteert alle lijsten op het nummer voor 1960
seven = data.sort(key=lambda x: x[8],reverse=True)
# dit sorteert alle lijsten op het nummer voor 1970
eight = data.sort(key=lambda x: x[9],reverse=True)
# dit sorteert alle lijsten op het nummer voor 1980
nine = data.sort(key=lambda x: x[10],reverse=True)
# dit sorteert alle lijsten op het nummer voor 1990
ten = data.sort(key=lambda x: x[11],reverse=True)
# dit sorteert alle lijsten op het nummer voor 2000
eleven = data.sort(key=lambda x: x[12],reverse=True)

print("The top 10 names for the 1900's were:",\nl,
print("The top 10 names for the 1910's were:",\nl,
print("The top 10 names for the 1920's were:",\nl,
print("The top 10 names for the 1930's were:",\nl,
print("The top 10 names for the 1940's were:",\nl,
print("The top 10 names for the 1950's were:",\nl,
print("The top 10 names for the 1960's were:",\nl,
print("The top 10 names for the 1970's were:",\nl,
print("The top 10 names for the 1980's were:",\nl,
print("The top 10 names for the 1990's were:",\nl,
print("The top 10 names for the 2000's were:",\nl,









