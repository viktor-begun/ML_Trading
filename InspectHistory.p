path='H:\My documents\Trading\SelfConsistentStrategy\CST\MCWM\case0\2013b\'
#set terminal pngcairo dashed size 960,581 font 'Verdana,10'
set terminal wxt persist
#set output ""
#set key autotitle columnhead
#set autoscale
set datafile separator ","
#set timefmt '%Y.%m.%d,%h:%m'
#set xrange [0:100]
#plot path.'EURUSD_M1_2013b.thd' every ::0::1000 using 0:3:5:4:6 with candlesticks title 'raw'
plot path.'EURUSD_H1_2013b.thd' every ::1902::2002 using 0:3:5:4:6 with candlesticks title 'raw'