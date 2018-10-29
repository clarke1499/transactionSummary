# transactionSummary
A script to take transactions downloaded from a bank, (specifically Santander,
other banks may vary), in a .txt file and output the amount spent, the number of
weeks covered by the transactions and the amount spent per week.

Creates a file called outfile in ~/transactionSummary by default, this contains
the results of the last run, if this file is newer than the input file its
contents will be displayed as the results of the script.

Obviously this doesn't work if different files are used as input but this suits
by usecase.

Requires bc, everything else should be installed by default on linux.
