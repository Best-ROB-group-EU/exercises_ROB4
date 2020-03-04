% DEPENDS ON DATASET: ecgdurran.mat
frequency = 100; %Hz
step_size = 1/frequency;
t = 0:step_size:size(ecg_dorran100Hz)/frequency - step_size;

[my_peaks, index] = threshold(ecg_dorran100Hz);
[peaks, locations] = findpeaks(ecg_dorran100Hz, 'MinPeakDistance', 50);

% Lazy, I know
bpm = size(peaks, 1)

figure
plot(t, ecg_dorran100Hz, index/frequency, my_peaks, 'rx', locations/frequency, peaks, 'ko')



function [result, indices] = threshold(dataset)
    result = [];
    indices = [];
    j = 1;
    for i = 1:size(dataset, 1)
        if dataset(i) > 1 && dataset(i+1) < dataset(i) && dataset(i-1) < dataset(i)
            result(j) = dataset(i);
            indices(j) = i;
            j = j+1;
        end    
    end
    result = transpose(result);
    indices = transpose(indices);
end
