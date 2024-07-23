#!/bin/bash
# 
# Renders .dot and .png files from an annotated script file, using YesWorkflow.
# Make sure you build the yesworkflow docker image before running this script.
# 
# Usage: ./render.sh <path-to-script>
# 

input_filepath=$1
input_abs_filepath=$(realpath $input_filepath)
input_dirname=$(dirname $input_abs_filepath)
input_filename=$(basename $input_abs_filepath)
input_name="${input_filename%.*}"

echo "$input_dirname"

# Render script annotations into a graphviz .dot file
docker run -v ${input_dirname}:/data yesworkflow graph /data/${input_filename} > ${input_dirname}/${input_name}.dot

# Render the .dot file into a png using graphviz
docker run -v ${input_dirname}:/data --entrypoint "dot" yesworkflow  -Tpng -o /data/${input_name}.png /data/${input_name}.dot

# Open the png file
open ${input_dirname}/${input_name}.png
