# Project objectives.
The project's main objective is to make a tool that can do autotrading on FOREX market with more than average **profit**.<br /> 
This goal can be split in parts. In this approach, the **first** part is a Chart Analaser and Signal Maker (**CASM**) which is a model that looks at the historical data (and whatever extra data input is important) and tries to its best to predict near future market move. The CASM model should generate signals "buy", "sell" or "do nothing".<br /><br />
The **second** part, Strategy Optimizer and Trading Manager (**SOTM**), takes the CASM signal and makes a decision whether to follow the recommendation or not. It also decides on take profit, stop loss and trailing stop loss levels when placing orders<br /><br />
The **third** part, Steepest Gradient Minimization Manager (**SGMM**). Given the multidemensional problems addressed by CASM and SOTM they should have their variables to be optimized. The SGMM would search iteratively for the best possible set of variables in the CASM/SOTM space which would give the best profit (*) 

# Implementation plan
1. Implement CASM model (search space is large, ARIMA, Bollinger bands, LSTM, random, etc.) that generates a singnal at every time step
    1. line 1.1
2. Implement SOTM model (trading rules with variables that can be varied for searching the best profit)
3. Implement SGMM model which can refine CASM and SOTM models self consistently in their variables space to get the best profit


_*_ The _best profit_ can be defined in different ways, so one has to adopt a specific definition here. For the time being the most consistent profit as a function of time is a preferrence, but it can be varied. 
