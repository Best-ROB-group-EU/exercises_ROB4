% Exercises ECG

srate = 1/100;

% Data is a 6000x1 so tf = 6000.
tf = (6000/100)-srate;
% Tf time to finish

t = 0:srate:tf;

figure("Name","Raw data")
plot(t,ecg_dorran100Hz)

% Rectify signal
rectified_data = abs(ecg_dorran100Hz);
figure("Name","Rectified")
plot(t,rectified_data)

% Extract R-waves
thr = 1;
ECG_thr= ecg_dorran100Hz;
ECG_thr(find(ecg_dorran100Hz<thr)) = 0;

figure("Name","R_waves")
plot(t,ecg_dorran100Hz),hold on
plot(t,ECG_thr,'r')


