% DEPENDS ON DATASET: data_time_flow_short.mat

subplot(4,1,1)
plot(time, flow)

subplot(4,1,2)
volume = cumsum(flow).*(1/100);
plot(time, volume)

subplot(4,1,3)
dt_volume = detrend(volume);
plot(time, dt_volume)


% plot(time, flow)

subplot(4,1,4)
[p,s,mu] = polyfit(time,volume,9);
f_y = polyval(p,time,[],mu);
nl_dt_volume = volume - f_y;
plot(time, nl_dt_volume)