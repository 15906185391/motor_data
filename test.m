frequency=1024;
axis_x=[500 1000 1500 2000 2500 3000];
T1 = readtable('1.csv','range',[5 1]);
T1_data=T1.x____ch1(1:(20*frequency));
length(T1_data);
effective_value_1=sqrt(mean(T1_data.^2));


T2 = readtable('2.csv','range',[5 1]);
T2_data=T2.x____ch1(1:(20*frequency));
length(T2_data);
effective_value_2=sqrt(mean(T2_data.^2));


T3 = readtable('3.csv','range',[5 1]);
T3_data=T3.x____ch1(1:(20*frequency));
length(T3_data);
effective_value_3=sqrt(mean(T3_data.^2));


T4 = readtable('4.csv','range',[5 1]);
T4_data=T4.x____ch1(1:(20*frequency));
length(T4_data);
effective_value_4=sqrt(mean(T4_data.^2));


T5 = readtable('5.csv','range',[5 1]);
T5_data=T5.x____ch1(1:(20*frequency));
length(T5_data);
effective_value_5=sqrt(mean(T5_data.^2));

T6 = readtable('6.csv','range',[5 1]);
T6_data=T6.x____ch1(1:(20*frequency));
length(T6_data);
effective_value_6=sqrt(mean(T6_data.^2));
effective_value=[effective_value_1 effective_value_2 effective_value_3 effective_value_4 effective_value_5 effective_value_6];
plot(axis_x,effective_value)
title('加速度a随转速n变化图')
xlabel('输入转速 n/(r/min)')
ylabel('加速度 a/g')
legend('加速度 a/g')