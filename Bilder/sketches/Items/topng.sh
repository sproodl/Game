#!/bin/sh -x
for i in *.svg ; do
  j=$(basename $i .svg)
  inkscape $i --export-png=$j.png
done
