# -*- coding: UTF-8 -*-

import os.path
import argparse
import subprocess

from db import Cursus

def get_human_size(path):
    stdout = subprocess.run(["du", "-h", path], stdout=subprocess.PIPE).stdout
    return stdout.decode("utf-8").strip().split("\t")[0]

def file_link(path, parent="all-archives"):
    size = get_human_size(os.path.join(parent, path))

    return """
        <a class="filename" href="/archives/%s">%s</a> (%s)
        """.strip() % (path, path, size)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cursus")
    args = p.parse_args()

    cursus = Cursus.get(Cursus.short_name == args.cursus.lower())

    filename = "%s.zip" % cursus.short_name.upper()

    print("Téléchargez tous les fichiers de %s&nbsp;: %s." % (
        cursus.name,
        file_link(filename)))

    print("""
        Vous pouvez aussi télécharger les fichiers d’une matière
        spécifique&nbsp;:
    """.strip())

    for course in cursus.courses:
        filename = "%s-%s.zip" % (cursus.short_name.upper(), course.short_name)

        if not os.path.isfile(os.path.join("all-archives", filename)):
            continue

        print("* %s&nbsp;: %s" % (course.name, file_link(filename)))


if __name__ == "__main__":
    main()
