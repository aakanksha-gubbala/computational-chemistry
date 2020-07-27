syms x;
fn = input('Enter function in x: ','s'); 
f = str2sym(fn);
df = diff(f); 
error = 0.0000001;
x0 = input('Enter the guess value:');
for i=1:100000
    f0=vpa(subs(f,x,x0)); 
     d0=vpa(subs(df,x,x0)); 
     y=x0-f0/d0; 
     err=abs(y-x0);
     if err<error 
        break
     end
     x0=y;
end 
fprintf('The Root is : %f \n',y);
fprintf('No. of Iterations : %d\n',i);