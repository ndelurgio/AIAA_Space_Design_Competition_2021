clear
clc
close all;
%% Sun Access Graph
load("sunaccess.mat");
STARTTIME1 = STARTTIME1 + years(100);
STOPTIME1 = STOPTIME1 + years(100);

daterange = STARTTIME1(1):seconds(600):STOPTIME1(end);
%xtick = STARTTIME1(1):days(2):STOPTIME1(end);
xtick = datetime(2040,6,27):days(2):STOPTIME1(end);

figure
hold on;
for i = 1:length(daterange)-1
    for j = 1:length(STARTTIME1)
       if daterange(i) > STARTTIME1(j) && daterange(i) < STOPTIME1(j)
           plot([daterange(i), daterange(i+1)],[1,1],'y','LineWidth',30)
           break;
       elseif j == length(STARTTIME1)
           plot([daterange(i), daterange(i+1)],[1,1],'k','LineWidth',30)
       end
   end
end
title("Sun Access")
%ylabel('Sun Access')
set(gcf,'position',[100 100 1200 400])
set(gca,'YTick', [])
set(gca,'XTick',xtick)
grid on;
xtickangle(45)

%% Comm Access Graph
load("comaccess.mat");

STARTTIME = STARTTIME + years(100);
STOPTIME = STOPTIME + years(100);

figure
hold on;
for i = 1:length(daterange)-1
    for j = 1:length(STARTTIME)
       if daterange(i) > STARTTIME(j) && daterange(i) < STOPTIME(j)
           plot([daterange(i), daterange(i+1)],[1,1],'g','LineWidth',30)
           break;
       elseif j == length(STARTTIME)
           plot([daterange(i), daterange(i+1)],[1,1],'k','LineWidth',30)
       end
   end
end
title("Comm Access")
%ylabel('Sun Access')
set(gcf,'position',[100 100 1200 400])
set(gca,'YTick', [])
set(gca,'XTick',xtick)
grid on;
xtickangle(45)