%K-neigh classifier
uklas1 = table2array(uklas(:,1));
uklas2 = table2array(uklas(:,2));
uklas3 = table2array(uklas(:,3));
uklas4 = table2array(uklas(:,4));

Idx = knnsearch(uklas1,uklas2);
Idx2 = knnsearch(uklas3,uklas4);
figure
plot(uklas1(Idx,:),'g')
hold on
plot(uklas2(Idx,:),'b')
legend({'k-neigh uklas1','k-neigh uklas2'})

figure
plot(uklas3(Idx2,:),'r')
hold on
plot(uklas4(Idx2,:),'c')
legend({'k-neigh uklas3','k-neigh uklas4'})
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Bayes classifier
tc = fitctree(uklas1,uklas2);
tc2 = fitctree(uklas3,uklas4);
Bayes1 = predict(tc,uklas1);
Bayes2 = predict(tc,uklas2);
Bayes3 = predict(tc2,uklas3);
Bayes4 = predict(tc2,uklas4);
figure
plot(Bayes1,'g')
hold on
plot(Bayes2,'b')
legend({'Bayes1','Bayes2'})

figure
plot(Bayes3,'r')
hold on
plot(Bayes4,'c')
legend({'Bayes3','Bayes4'})

