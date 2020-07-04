#!/usr/bin/bash

# Notes
# 1. Remember that when copying files, retain the timestamps!
#     cp -p src_file dest_file
#     cp -pr src_dir dest_dir
# 2. For directories or files that have the same contents but different timestamps
#     touch file1 file2
#     touch dir1 dir2

ALLOWED_COMPARISONS_COUNT=2

TEMP_FILE_1="mimr_compare_dirfiles.sh.temp_file_1"
TEMP_FILE_2="mimr_compare_dirfiles.sh.temp_file_2"

should_display_help="false"
should_compare_contents="false"
dirfiles_to_compare=()

object_lhs=
object_rhs=
object_comparison_flags=

help()
{
    echo "See the differences between $ALLOWED_COMPARISONS_COUNT files or directories"
    echo
    echo "Usage"
    echo
    echo "    ./mimr_compare_dirfiles.sh [OPTION]... [FILE].."
    echo
    echo "    ./mimr_compare_dirfiles.sh file1 file2"
    echo "    ./mimr_compare_dirfiles.sh dir1 dir2"
    echo
    echo "Flags"
    echo
    echo "    --help"
    echo "        Display information about the script"
    echo
    echo "    -c"
    echo "        Compare the contents of files. This might take time if comparing big directories."
    echo "        If this isn't set, the file sizes and last modification date would be compared."
}

init_args()
{
    for input in "$@"
    do
        if [[ "$input" == "--help" ]]; then
            should_display_help="true"
        elif [[ "$input" == "-c" ]]; then
            should_compare_contents="true"
        else
            dirfiles_to_compare+=("$input")
        fi
    done
}

validate()
{
    if [[ "${#dirfiles_to_compare[@]}" != "$ALLOWED_COMPARISONS_COUNT" ]]; then
        echo "Error: Incorrect count of arguments. Invoke with --help for more details."
        exit 1
    fi
}

set_comparison_objects()
{
    if [[ "$should_compare_contents" == "true" ]]; then
        object_lhs="${dirfiles_to_compare[0]}"
        object_rhs="${dirfiles_to_compare[1]}"
        object_comparison_flags="-qr"
    else
        # tree -asD --du "${dirfiles_to_compare[0]}" > $TEMP_FILE_1
        # tree -asD --du "${dirfiles_to_compare[1]}" > $TEMP_FILE_2
        tree -aD "${dirfiles_to_compare[0]}" > $TEMP_FILE_1
        tree -aD "${dirfiles_to_compare[1]}" > $TEMP_FILE_2

        object_lhs="$TEMP_FILE_1"
        object_rhs="$TEMP_FILE_2"
    fi
}

compare()
{
    validate
    set_comparison_objects

    # No quotations on flags so that if they are empty, it would really seem that they don't exist
    diff $object_comparison_flags "$object_lhs" "$object_rhs"

    cleanup
}

cleanup()
{
    rm -f $TEMP_FILE_1 $TEMP_FILE_2 # or append # 2> /dev/null
}

init_args "${@:1}" # or simply # $@
if [[ "$should_display_help" == "true" ]]; then
    help
else
    compare
fi
