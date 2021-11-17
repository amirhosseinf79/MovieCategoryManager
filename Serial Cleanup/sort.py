import re
import os
import sys

def diffrences(movies, ignore):
    movies_len = len(movies)
    if movies_len>=3:
        mean = int(movies_len / 2) - 1
    elif movies_len == 2:
        mean = 0
    else:
        return 0, 0

    main_movie = movies[mean + 1]
    second_movie = movies[mean]

    format = re.split("\.", main_movie)[-1]
    regex, is_space, bracket = ('', 0, 0)

    to_end = len(main_movie) - len(format) - 1

    for i in range(0, to_end):
        if main_movie[i] == second_movie[i]:
            if re.findall("\[", main_movie[i]):
                bracket = 1

            if bracket == 0:
                if len(re.findall("[0-9]", main_movie[i])) == 0:
                    main_word = re.sub("[._]", " ", main_movie[i])
                    regex += main_word

            if re.findall("]", main_movie[i]):
                bracket = 0

    ignore = re.sub("[._]", " ", ignore)
    regex = re.sub(f"\s*{ignore}\s*", "", regex)
    regex = re.sub(" +", " ", regex)
    regex = regex.strip()
    return regex, format


def proccess(app_name):
    regex = input("Enter static Serial name: ")
    movies = os.listdir()

    movies_ = movies
    movies = []

    for movie in movies_:
        if movie!=app_name:
            movies.append(movie)

    if regex:
        main_movie = movies[mean + 1]
        format = re.split("\.", main_movie)[-1]
        regex = regex.strip()
    else:
        ignore = input("which text must be ignored: ")
        regex, format = diffrences(movies, ignore)

        if regex == 0:
            return print("You must have 2 or more Movie")


    n = 1
    confirm = 0
    for movie in movies:
        if movie==app_name:
            continue

        if len(movies)<100:
            if n<10: m = f"0{n}"
            else: m = n
        elif len(movies)<1000:
            if n<10: m = f"00{n}"
            elif n<100: m = f"0{n}"
            else: m = n
        elif len(movies)<10000:
            if n<10: m = f"000{n}"
            elif n<100: m = f"00{n}"
            elif n < 1000: m = f"0{n}"
            else: m = n

        print(movie, "->", f"{regex} {m}.{format}")
        if confirm==0:
            rename = input("Do you confirm?[y/n] ")
        else:
            rename = "y"

        if rename=="y":
            confirm = 1
            os.rename(movie, f"{regex} {m}.{format}")
        else:
            break

        n += 1

app_name = re.split("\\\\", sys.argv[0])[-1]
print(app_name)
proccess(app_name)