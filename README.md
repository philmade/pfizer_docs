# Verifying the Pfizer data

This is my attempt at verifying JikkyLeaks count of patients in the Pfizer trial who were N-antibody NEGATIVE at Week_1, then POSITIVE at Week_3. 

He claimed that the court ordered data showed that Pfizer's claims of 98% efficacy were
likely bogus. There was a much reduced difference between Placebo/Vaccinated when looking at
N-antibody data contained in the court ordered Pfizer documents. 

## MAKING THIS WORK

You'll need poetry and pandas.
With poetry, just type 'poetry shell' then 'poetry install'
You'll need to be able to have Jupyter or Vscode use the new poetry python environment

Alternatively, if you don't have poetry you can make it work with pip because pandas is the only dependency. Just create an environment, install pandas, and run Jupyter with that environment.

# There are two ways to verify:

## VERIFY JIKKY'S DATA
Download the CSV data as it was originally posted by Jikky. This is because Github won't let me upload the CSV here as its too large. Download it directly from JikkyLeaks source then add it to your environment root. Rename it to remove the messy .zip extension so you just have a neat .csv
https://files.catbox.moe/i544mb.zip

Use the file "negative_to_positive_jikky.ipynb" to see for yourself.


## VERIFY DIRECT FROM PFIZER DATA
The jupyter notebook called "negative_to_positive_pfizer.ipynb" takes
the original .xpt file from icandecide and verifies JikkyLeaks original claim.

The advantage of this is it shows that direct from the court ordered data, we can get the same result.


###### The original documents are all posted here:
https://www.icandecide.org/pfizer-documents/
https://phmpt.org/pfizers-documents/

The file we're using for this is linked directly here:
https://www.icandecide.org/wp-content/uploads/2022/05/FDA-CBER-2021-5683-0123168%20to%20-0126026_125742_S1_M5_c4591001-A-D-adva.zip

Alternatively, direct link via phmpt.org
https://pdata0916.s3.us-east-2.amazonaws.com/pdocs/050222/FDA-CBER-2021-5683-0123168+to+-0126026_125742_S1_M5_c4591001-A-D-adva.zip


###### Twitter Thread that will make you underestand this:
The thread (obviously) has now been censored
https://twitter.com/Jikkyleaks/status/1529076970486923264

