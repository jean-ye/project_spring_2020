# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)


For my final project, I would like to write a python script to compute the mean framewise displacement for the fMRI data our lab collected. When our participants come in to participate in a study, we usually ask them to complete several different tasks multiple times. After their fMRI data go through the preprocessing pipeline, we would end up with a text file with all of their displacement information (including information on how much they move in three different directions and how much they rotate in three different ways) for each time point for all runs.The python script will be able to compute the average of these displacement values and give us some information on what the displacement looks like across runs. We will hopefully be able to use this information in our data analysis later on. Since we collect different number of runs for different tasks, and the run durations vary, the python script should be flexible enough to adjust accordingly depending on what task it is working on. 
