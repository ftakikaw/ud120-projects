#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ordered_data = []

    ### your code goes here
    #ordered_data.insert(0, (ages[0][0], net_worths[0][0], abs(predictions[0][0] - net_worths[0][0])))
    ordered_data.insert(0, (ages[0][0], net_worths[0][0], predictions[0][0] - net_worths[0][0]))
    
    i = 1
    
    while i < len(predictions):
        
        #error = abs(predictions[i][0] - net_worths[i][0])
        error = predictions[i][0] - net_worths[i][0]
        
        j = 0
        
        while j < len(ordered_data):
            
            if(ordered_data[j][2] > error):
                break
        
            j += 1
    
        ordered_data.insert(j, (ages[i][0], net_worths[i][0], error))
    
        i += 1
        
    tam = len(predictions) * 0.9
    
    i = 0
    
    while i < tam:
        
        cleaned_data.append(ordered_data[i])
        
        i += 1
    
    
    return cleaned_data

