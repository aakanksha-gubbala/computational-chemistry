
function [] = consecutiveReactions(t, x)
% Series or consecutive reactions (first order and irreversible) 
    function [f] = dXdT(t, x)
        A = x(1);
        B = x(2);
        C = x(3);
        D = x(4);

        k1 = 1;
        k2 = 0.8;
        k3 = 0.7;
        k4 = 0.9;
        
        km1 = 0.25;
        km2 = 0.25;
        km3 = 0.25;
        km4 = 0.25;

        dAdt = -k1*A + km1*B;
        dBdt = k1*A - k2*B - km1*B + km2*C;
        dCdt = k2*B - k3*D - km2*C + km3*D;
        dDdt = k3*C - km3*D;
        f = [dAdt; dBdt; dCdt; dDdt]; 
    end
[t,y] = ode15s(@dXdT,t, x);
figure
plot(t, y,'linewidth', 2)
legend({'[A]', '[B]', '[C]', '[D]'},'Location','bestoutside')
legend('boxoff')
title("Consecutive Reactions")
xlabel("t")
ylabel("Concentration")
end