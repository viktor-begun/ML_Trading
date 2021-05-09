def pd_moving_average(in_pandas, in_window):
    # Input:
    ## in_pandas: input column of a pandas DataFrame
    ## in_window: the number of input values to take into account counting backwards from the last input value
    #
    # Output:
    ## mean: rolling mean
    ## std: rolling standard deviation
    ## trend: rolling derivative. The line assumingly starts at the first point and ends in the mean at half distance by "x-axis".
    ## strend: sign of the trend.
    mean   = in_pandas.rolling(window=in_window).mean().dropna()
    std    = in_pandas.rolling(window=in_window).std().dropna()
    trend  = 2*(in_pandas-mean).dropna()
    strend = np.sign(trend).dropna()
    
    # Convert to list
    mean   = list(mean.values.flatten())
    std    = list(std.values.flatten())
    trend  = list(trend.values.flatten())
    strend = list(strend.values.flatten())
    
    return mean, std, trend, strend

def moving_average(in_list, in_window):
    # The same as pd_moving_average(in_pandas, in_window) but for list inputs.
    nlist = len(in_list)
    mean, std, trend, strend = [], [], [], []
    m, s, t, st = None, None, None, None
    for i in range(nlist-in_window+1):
        m, s, t, st = [average(in_list[i:i+in_window])[j] for j in range(4)]
        mean.append(m)
        std.append(s)
        trend.append(t)
        strend.append(st)
    return mean, std, trend, strend

def average(in_list):
    # A part of moving_average(in_list, in_window)
    num  = len(in_list)
    if num!=0 and num!=1:
        mean  = sum(in_list)/num
        std   = math.sqrt(sum([(x-mean)**2 for x in in_list])/(num-1))
        trend = 2*(mean-in_list[0])/(num-1)
        strend = np.sign(trend)
        return mean, std, trend, strend
    return 'Error: Too short input!'
