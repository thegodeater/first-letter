        # Loads the data_set specified by 'filename' into a 2d array
def load_data_set("Namen_vrouw_per_10_jaar.csv":
    with open("Namen_vrouw_per_10_jaar.csv", "rU") as f:
        f.readline()
        return [[float(x) for x in row] for row in csv.reader(f+ delimiter=';')])
 data =load_data_set("Namen_vrouw_per_10_jaar.csv")

#gi
 # dit sorteert alle lijsten op het nummer voor 1900
one = data.sort(key=lambda x: x[2])
# dit sorteert alle lijsten op het nummer voor 1910
two = data.sort(key=lambda x: x[3])
# dit sorteert alle lijsten op het nummer voor 1920
 third = data.sort(key=lambda x: x[4])
# dit sorteert alle lijsten op het nummer voor 1930
fourth = data.sort(key=lambda x: x[5])
# dit sorteert alle lijsten op het nummer voor 1940
fifth = data.sort(key=lambda x: x[6])
# dit sorteert alle lijsten op het nummer voor 1950
six = data.sort(key=lambda x: x[7])
# dit sorteert alle lijsten op het nummer voor 1960
seven = data.sort(key=lambda x: x[8])
# dit sorteert alle lijsten op het nummer voor 1970
eight = data.sort(key=lambda x: x[9])
# dit sorteert alle lijsten op het nummer voor 1980
nine = data.sort(key=lambda x: x[10])
# dit sorteert alle lijsten op het nummer voor 1990
ten = data.sort(key=lambda x: x[11])
# dit sorteert alle lijsten op het nummer voor 2000
eleven = data.sort(key=lambda x: x[12])


 print("Names starting with the letter " + letter + " were most popular in the 1900's")
 print("Names starting with the letter " + letter2 + " were most popular in the 1910's")
 print("Names starting with the letter " + letter3 + " were most popular in the 1920's")
 print("Names starting with the letter " + letter4 + " were most popular in the 1930's")
 print("Names starting with the letter " + letter5 + " were most popular in the 1940's")
print("Names starting with the letter " + letter6 + " were most popular in the 1950's")
print("Names starting with the letter " + letter7 + " were most popular in the 1960's")
print("Names starting with the letter " + letter8 + " were most popular in the 1970's")
print("Names starting with the letter " + letter9 + " were most popular in the 1980's")
print("Names starting with the letter " + letter10 + " were most popular in the 1990's")
print("Names starting with the letter " + letter11 + " were most popular in the 2000's")
