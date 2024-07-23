# @BEGIN main
# @PARAM param_1
# @PARAM param_2
# @PARAM param_3
# @PARAM param_4
# @IN file_1 @URI file:./data/file1.csv


# @BEGIN task_1
# @PARAM param_1
# @PARAM param_2
# @IN file_1 @URI file:./data/file1.csv
# @OUT file_2 @URI file:./data/file2.csv

print('Processing demographic data...')

# @END task_1



# @BEGIN task_2
# @PARAM param_3
# @PARAM param_4
# @IN file_2 @URI file:./data/file2.csv
# @OUT file_3 @URI file:./data/file4.csv

print('Processing demographic data...')

# @END task_2

# @END main
