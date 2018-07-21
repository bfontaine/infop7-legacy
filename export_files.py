# -*- coding: UTF-8 -*-

import re
import shutil
import os.path
import argparse
from db import Cursus

def mkdir_p(path):
    return os.makedirs(path, exist_ok=True)

# /<cursus>/<course>/<year>/<type>/<content>/file title>

def export_content_files(content, source_dir, target_dir):
    mkdir_p(target_dir)
    if content.text:
        with open(os.path.join(target_dir, "description.txt"), "w") as f:
            f.write(content.text)

    for cf in content.files:
        f = cf.file
        new_path = os.path.join(target_dir, f.title)
        old_path = os.path.join(source_dir, f.path)

        print("Exporting %s" % repr(new_path))
        shutil.copyfile(old_path, new_path)

def export_course_files(course, source_dir, target_dir):
    for content in course.contents:
        if not content.year:
            continue

        if not content.content_type:
            continue

        title_slug = re.sub(r"\s+", "_", content.title)

        path = os.path.join(
                target_dir,
                str(content.year),
                content.content_type.short_name,
                title_slug)

        export_content_files(content, source_dir, path)



def export_all_files(source_dir, target_dir):
    for cursus in Cursus.select():
        # ./<cursus>
        cursus_path = os.path.join(target_dir, cursus.short_name)

        for course in cursus.courses:
            # ./<cursus>/<course>
            course_path = os.path.join(cursus_path, course.short_name)
            export_course_files(course, source_dir, course_path)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source-dir", default="./archive_data/usersfiles")
    p.add_argument("--target-dir", default="./all-files")
    args = p.parse_args()

    if not os.path.isdir(args.source_dir):
        raise Exception("Source must be a directory")

    if os.path.isdir(args.target_dir):
        raise Exception("Target '%s' already exists" % args.target_dir)

    export_all_files(args.source_dir, args.target_dir)

if __name__ == "__main__":
    main()
