""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):

    min_value = arr[0]
    max_value = arr[0]
    
    for value in arr:
        if value < min_value:
            min_value = value
            
        if value > max_value:
            max_value = value
    
    denominator = max_value - min_value + 0.0
    retorno = []
    
    for value in arr:
        retorno.append((value-min_value)/denominator)

    return retorno

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
