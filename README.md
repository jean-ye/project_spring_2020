# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)

This script computes the mean framewise displacement for the fMRI data our lab collected. After the fMRI data go through our existing preprocessing pipeline, we would end up with a text file containing motion displacement information for each time point for all the runs the participant completed. The text file has 6 different columns. Each columns represent a different motion parameters - the first three columns tell us how much participant rotated in three different ways, and the last three columns give us information on how much participant moved in three different directions. Each row give us motion information for each time point. 

The python script will compute the mean of each motion parameter and save out a text file containing the 6 averages. Additionally, the script will compute the mean of these six averages to give us a summary displacement measure. Hopefully these displacement values will give us some additional information on motion and help with QC and later analysis. 
