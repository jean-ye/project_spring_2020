# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)


For my final project, I would like to write a python script to compute the mean framewise displacement for the fMRI data our lab collected. When our participants come in to participate in a study, we usually ask them to complete several different tasks multiple times. After their fMRI data go through the preprocessing pipeline, we would end up with a text file with all of their displacement information (including information on how much they move in three different directions and how much they rotate in three different ways) for each time point for all runs.The python script will be able to compute the average of these displacement values and give us some information on what the displacement looks like across runs. We will hopefully be able to use this information in our data analysis later on. Since we collect different number of runs for different tasks, and the run durations vary, the python script should be flexible enough to adjust accordingly depending on what task it is working on. 

Breaking the script into more manageable blocks:

1: Check to see if there is a text file in the folder; if not, return a message to let the user know the file is missing. 

2a: Open the text file to check the length. Since each time point gets a row, the script should make sure the number of rows is correct. If it contains too few rows, return a message to say one of the scans might have gotten aborted. 

2b (maybe): Make the script more flexible! Since different tasks have different time durations, the text file might have different rows depending on what task we want to look at. Maybe set up a task decoder to help us with this. 

3: Compute the mean for each of the six columns 

4: Compute a mean for all six of these displacement measurements. 
