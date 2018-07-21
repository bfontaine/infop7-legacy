#! /bin/bash -e

mkdir -p all-archives

echo "==> Cursus archives"
for cursus in $(\ls -1 all-files/); do
  echo "--> $cursus"
  pushd all-files
  zip --quiet -r ../all-archives/$cursus.zip $cursus
  popd 2>/dev/null

  for course in $(\ls -1 all-files/$cursus/); do
     base="$cursus-$course"
     echo "------> $course"
     pushd all-files/$cursus
     zip --quiet -r ../../all-archives/${cursus}-$course.zip $course
     popd 2>/dev/null
  done
done

# fix names
pushd all-archives
rename 's/^l/_L/g' *
rename 's/^m/_M/g' *
rename 's/^_//g' *
