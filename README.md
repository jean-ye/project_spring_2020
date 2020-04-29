# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)


This python script computes the mean framewise displacement for the fMRI data our lab collected. We usually ask our participants complete several different tasks a few times each time they come in. After their fMRI data go through the preprocessing pipeline, we would end up with a text file with all of their displacement information (including information on how much they move in three different directions and how much they rotate in three different ways) for each time point for all runs. The python script will compute the average of these displacement values and help us access motion during the runs. We will hopefully be able to use this information in our data analysis later on.