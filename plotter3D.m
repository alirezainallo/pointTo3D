% ==============================
% Full Point Cloud Plotter
% ==============================

% CSV file path
filename = 'scan_points.csv';

% Read all data, skip header
data = readmatrix(filename, 'NumHeaderLines', 1);

% Extract X, Y, Z
X = data(:,1);
Y = data(:,2);
Z = data(:,3);

% Plot all points
figure;
scatter3(X, Y, Z, 5, Z, 'filled');  % 5=size of points, color by Z
axis equal;
xlabel('X');
ylabel('Y');
zlabel('Z');
title('3D Scan Points');
colorbar;
grid on;
view(3);

% Optional: rotate and zoom interactively
rotate3d on;
