#Importing relevant packages
import pandas as pd
import numpy as np 
from os import mkdir, chdir, getcwd, path, remove

#Below are the code used to compute displacement mean for each participant 
def move_into_directory(participant):
    """Move into the directory where each participant's motion file is saved"""
    path = "Motion_files/" + participant
    chdir(path)
    
def set_motion_file():
    """Check to make sure motion file exist and set the motion file to be the one the script wants to operate on"""
    if path.isfile('rp_s_full.txt'):
        column_names = ['roll', 'pitch', 'yaw', 'z', 'x', 'y']
        file = pd.read_csv('rp_s_full.txt', names = column_names, delim_whitespace = True)
        df = pd.DataFrame(file, columns = column_names)
    else:
        print("no motion file found!")
    return df 

def compute_mean_for_each_column(motion_dataframe):
    """Compute means for each of the six motion parameters"""
    means_separated = []
    for i in range(6):
        mean = motion_dataframe.iloc[:,i].mean()
        means_separated.append(mean)
    return means_separated

def compute_mean_of_all_columns(means_separated):
    """Compute the mean of the six motion parameter averages"""
    column_means = sum(means_separated)/6
    return column_means

def saving_out_text_files_with_averages(means,column_means):
    """Save the averages computed by the previous two functions in text files in the participant's directory"""
    np.savetxt('Mean_of_Each_Motion_Parameters', X = means)
    np.savetxt('Mean_of_All_Motion_Parameters', X = [column_means])

def main(participant):
    """This function puts all the previous functions in the script together"""
    basedir = '/Users/yesji/test_project_folder/project_spring_2020'
    chdir(basedir)
    move_into_directory(participant)
    motion_dataframe = set_motion_file()
    means_separated = compute_mean_for_each_column(motion_dataframe)
    column_means = compute_mean_of_all_columns(means_separated)
    saving_out_text_files_with_averages(means_separated,column_means)
    chdir(basedir)