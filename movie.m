clear
clc
close all

t = linspace(0, 21, 210);
x = sin(t).^2 + cos(t);

fig = figure;

h = animatedline('LineWidth', 1.2);
for k = 1:length(t)             
    addpoints(h, t(k), x(k))
    
    xlabel('$t$','interpreter', 'latex')
    ylabel('$sin^2(t) + cos(t)$', 'interpreter', 'latex')
    ylim([-1.5 1.5])
    title(['t = ', num2str(t(k)), ' seconds'])
       
    movieVector(k) = getframe(fig); 
end


myVideo = VideoWriter('movie', 'MPEG-4');
myVideo.FrameRate = 50;

open(myVideo);
writeVideo(myVideo, movieVector);
close(myVideo);