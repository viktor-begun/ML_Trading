# ML_Traiding
# Project objectives.
The project's main objective is to make a tool that can do autotrading on FOREX market with more than average **profit**.<br /> 
This goal can be split in parts. In this approach, the **first** part is a Chart Analaser and Signal Maker (**CASM**) which is a model that looks at the historical data (and whatever extra data input is important) and tries to its best to predict near future market move. The CASM model should generate signals "buy", "sell" or "do nothing".<br /><br />
The **second** part, Strategy Optimizer and Trading Manager (**SOTM**), takes the CASM signal and makes a decision whether to follow the recommendation or not. It also decides on take profit, stop loss and trailing stop loss levels when placing orders<br /><br />
The **third** part, Steepest Gradient Minimization Manager (**SGMM**). Given the multidemensional problems addressed by CASM and SOTM they should have their variables to be optimized. The SGMM would search iteratively for the best possible set of variables in the CASM/SOTM variables space which would give the best profit (*) 

# Implementation plan
- Implement CASM model (search space is large, ARIMA, Bollinger bands, LSTM, random, etc.) that generates a singnal at every time step
- Implement SOTM model (trading rules with variables that can be varied for searching the best profit)
- Implement SGMM model which can refine CASM and SOTM models self consistently in their variables space to get the best profit


_*_ The _best profit_ can be defined in different ways, so one has to adopt a specific definition here. For the time being the most consistent profit as a function of time is a preferrence, but it can be varied. 


# CASM section
# Predictive model implementation (in progress)
# Plan:
- Implement MA using Python on the EURUSD_1H data (In progress)
- Make a standard ARIMA based model (In progress), see [ML_ARIMA.ipynb](https://github.com/viktor-begun/ML_Traiding/blob/main/ML_Arima.ipynb)
    - Explanation of SARIMAX
- Make the LSTM based model (TODO)
  - Combine LSTM and ARIMA (TODO)
  - Improve the LSTM by applying a wavelet transformation (TODO)
- Make a fully atomated Algorithmic Trading in python (In progress), see [Alg_Traiding.ipynb](https://github.com/viktor-begun/ML_Traiding/blob/main/Alg_Traiding.ipynb)
# Signal generation logic implementation (pending)
- Take ARIMA 1 hour/tick future prediction of open/close/high/low prices and generate one of the [buy, sell, do_nothing] signals. Try simple for now: 

  if (future_high > current_high + L1)and(future_low > current_low + L2) then buy else
  
  if (future_high < current_high - L2)and(future_low < current_low - L1) then sell else do_nothing

Here, L1 and L2  are optimizabe variables for the SGMM

# SOTM section (pending)

this code to be carried over from the old implementation in to python separate module.

# SGMM section (pending)

this code to be carried over from the old implementation in to python separate module.
 
