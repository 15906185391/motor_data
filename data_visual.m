T = readtable('0.csv','Range','A6:A87045');
T2=timetable(T.Var1,'SampleRate',1024);
T2
T3 = readtable('1.csv','Range','A6:A70661');
T4=timetable(T3.Var1,'SampleRate',1024);
T4