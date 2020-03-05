% DEPENDS ON DATASET: ecg.mat
%% b
time = transpose(0:1/Fs:size(ECG)/Fs - 1/Fs);

figure
subplot(4,1,1)
plot(time, ECG_raw)

subplot(4,1,2)
plot(time, ECG)

%% c
% Filtering; Probably not
% We have both high frequency noise, low frequency noise, and salt n' pepper noise (red circles)

%% d
% Moving average
subplot(4,1,3)
B = 1/10*ones(10,1); % Filter window
movavg = filter(B,1,ECG_raw);
plot(time, movavg)

% Median filtering
subplot(4,1,4)
n = 15;
median_filt = medfilt1(ECG_raw,n);
plot(time, median_filt)


%% e
figure
subplot(3,1,1)
plot(time, ECG_raw)

% Butterworth bandstop filtering
% I only bothered to plot one of them - this one is pretty good
subplot(3,1,2)
[b, a] = butter(2, [30/(Fs/2), 100/(Fs/2)], 'stop'); 
bw_bsf_filtered = filter(b, a, ECG_raw);
plot(time, bw_bsf_filtered)

% Filter designed with Filter Designer app
% DEPENDS ON FILTER: bw_bs_filter.fda
% Export filter from filter designer as the coefficients "SOS" and "G"
subplot(3,1,3)
bw_cheat_code_filter = filtfilt(SOS, G, ECG_raw);
plot(time, bw_cheat_code_filter)

% Can also be exported as object; then use the following line:
% object_filter = filter(Hd, ECG_raw);

%% f
% DEPENDS ON FILTER: bw_hp_filter.fda
% Export filter from filter designer as the coefficients "sos" and "g"
figure
subplot(2,1,1)
plot(time, ECG_raw)

subplot(2,1,2)
high_pass = filtfilt(sos, g, ECG_raw);
plot(time, high_pass)


%% g
% Not sure that it really matters? 
% Median -> high pass -> bandstop looks a little nicer to me but that's
% subjective
median_filter = medfilt1(ECG_raw, n);
highpass_filter = filtfilt(sos, g, median_filter);
bandstop_filter = filtfilt(b, a, highpass_filter);

figure
plot(time, bandstop_filter)

%% h
% filtfilt(), unlike filter(), has no phase shift