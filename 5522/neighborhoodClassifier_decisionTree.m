load 2008data.mat
x_data_2008 = data(:,2:12);
label_2008 = data(:,1);

tree = fitctree(x_data_2008,label_2008);

view(tree,'Mode','graph')