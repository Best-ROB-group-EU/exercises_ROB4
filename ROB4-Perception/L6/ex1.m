%Ex 1
sample1 = table2array(mnklasse1(:, 1));
sample2 = table2array(mnklasse1(:, 2));
sample3 = table2array(mnklasse2(:, 3));
sample4 = table2array(mnklasse2(:, 4));
sample5 = table2array(mnklasse3(:, 1));
sample6 = table2array(mnklasse3(:, 3));
sample7 = table2array(mnklasse4(:, 1));
sample8 = table2array(mnklasse4(:, 4));

g1= {sample1,sample2};
g2= {sample3,sample4};
g3= {sample5,sample6};
g4= {sample7,sample8};
figure
gscatter(sample1,sample2,g1,'br','xo')
figure
gscatter(sample3,sample4,g2,'br','xo')
figure
gscatter(sample5,sample6,g3,'br','xo')
figure
gscatter(sample7,sample8,g4,'br','xo')