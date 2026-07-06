# MATLAB 数学建模常用语法汇总

---

## 一、向量与矩阵的构建

### 1.1 向量生成
```matlab
% 等差数列向量
x = linspace(a, b, n)       % a到b之间等间隔取n个点
x = a:step:b                 % 步长为step的等差数列

% 等比数列向量
x = logspace(a, b, n)        % 10^a 到 10^b 之间等比取n个点（常用于对数坐标）

% 随机向量
x = rand(1, n)               % 1×n的(0,1)均匀分布
x = randn(1, n)              % 1×n的标准正态分布
```

### 1.2 矩阵创建
```matlab
% 直接创建
A = [1,2,3; 4,5,6; 7,8,9]   % 分号换行，逗号/空格换列

% 特殊矩阵
A = zeros(m, n)              % 全0矩阵
A = ones(m, n)               % 全1矩阵
A = eye(m, n)                % 单位矩阵（主对角线为1）

% 随机矩阵
A = rand(m, n)               % (0,1)均匀分布
A = randi([imin, imax], m, n)% [imin, imax]内均匀随机整数
A = randn(m, n)              % 标准正态分布 N(0,1)
A = randperm(n)              % 1~n的随机排列（行向量）

% 对角矩阵
D = diag(v)                  % 以向量v为主对角线创建方阵
D = diag(v, k)               % v放在第k条对角线上（k>0右上，k<0左下）
v = diag(A)                  % 提取矩阵A的主对角线元素

% 分块对角矩阵
B = blkdiag(A1, A2, A3)      % 将多个矩阵拼成块对角矩阵

% 其他
H = hilb(n)                  % Hilbert矩阵（病态矩阵，常用于数值实验）
T = toeplitz(c, r)           % Toeplitz矩阵
P = pascal(n)                % Pascal矩阵
M = magic(n)                 % 幻方矩阵
```

### 1.3 矩阵拼接与扩展
```matlab
% 横向拼接
C = [A, B]                   % 等价于 cat(2, A, B) 或 horzcat(A, B)

% 纵向拼接
C = [A; B]                   % 等价于 cat(1, A, B) 或 vertcat(A, B)

% 重复矩阵
B = repmat(A, m, n)          % 将A在行方向重复m次，列方向重复n次
B = repelem(A, m, n)         % 每个元素重复m×n次（R2015a+）

% 维度拼接
C = cat(dim, A, B)           % dim=1纵向, dim=2横向, dim=3增加页
```

---

## 二、矩阵运算

### 2.1 基本运算
```matlab
% 加减乘除
C = A + B                    % 矩阵加法
C = A - B                    % 矩阵减法
C = A * B                    % 矩阵乘法（线性代数乘法）
C = A .* B                   % 逐元素乘法（点乘）
C = A / B                    % 矩阵右除：A * inv(B)
C = A ./ B                   % 逐元素右除
C = A \ B                    % 矩阵左除：inv(A) * B（解方程组常用）
C = A .\ B                   % 逐元素左除

% 幂运算
C = A ^ n                    % 矩阵幂（A自乘n次，A必须为方阵）
C = A .^ n                   % 逐元素幂
```

### 2.2 矩阵变换
```matlab
% 转置与共轭转置
B = A.'                      % 普通转置
B = A'                       % 共轭转置（实矩阵与.'相同）

% 旋转与翻转
B = rot90(A)                 % 逆时针旋转90°
B = rot90(A, k)              % 旋转k×90°
B = flipud(A)                % 上下翻转
B = fliplr(A)                % 左右翻转

% 重塑
B = reshape(A, m, n)         % 保持元素总个数不变，改变形状
B = A(:)                     % 将矩阵A展开为列向量

% 矩阵求逆
B = inv(A)                   % 方阵的逆矩阵（数值不稳定时用A\b代替）
B = pinv(A)                  % 伪逆（Moore-Penrose逆，适用于非方阵/奇异阵）
```

### 2.3 矩阵分解（数值计算核心）
```matlab
% LU分解
[L, U] = lu(A)               % A = L*U，解Ax=b时常与\联用
[L, U, P] = lu(A)            % P*A = L*U

% QR分解
[Q, R] = qr(A)               % A = Q*R，Q正交，R上三角

% 特征值与特征向量
[V, D] = eig(A)              % A*V = V*D，D为特征值对角阵，V为特征向量
e = eig(A)                   % 只返回特征值

% 奇异值分解（SVD）
[U, S, V] = svd(A)           % A = U*S*V'，U、V正交，S为奇异值对角阵
s = svd(A)                   % 只返回奇异值向量

% Cholesky分解（对称正定矩阵）
R = chol(A)                  % A = R'*R，R为上三角

% Schur分解
[U, T] = schur(A)            % A = U*T*U'，U正交，T三角（特征值在T的对角线上）
```

### 2.4 矩阵属性与统计
```matlab
% 基本属性
[m, n] = size(A)             % 矩阵的行数和列数
d = length(A)                % 最大维度长度
n = numel(A)                 % 元素总个数
r = rank(A)                  % 矩阵的秩
d = det(A)                   % 行列式
t = trace(A)                 % 迹（对角线元素之和）
n = norm(A)                  % 默认2-范数
n = norm(A, 1)               % 1-范数（最大列和）
n = norm(A, inf)             % 无穷范数（最大行和）
n = norm(A, 'fro')           % Frobenius范数
c = cond(A)                  % 条件数（2-范数下）

% 极值统计
[val, idx] = max(A)          % 每列最大值及索引（矩阵默认按列）
[val, idx] = max(A, [], 2)   % 每行最大值
[val, idx] = min(A)          % 每列最小值
M = max(A, B)                % 逐元素取两矩阵较大者
m = min(A, B)                % 逐元素取两矩阵较小者

% 求和与累积
s = sum(A)                   % 每列求和（默认dim=1）
s = sum(A, 2)                % 每行求和
s = sum(A(:))                % 所有元素求和
s = sum(A, 'all')            % 所有元素求和（R2018b+）
c = cumsum(A)                % 逐列累加和
p = prod(A)                  % 逐列连乘积

% 均值与方差
mu = mean(A)                 % 每列均值
mu = mean(A, 2)              % 每行均值
v = var(A)                   % 每列方差（除以n-1）
v = var(A, 0, 2)             % 每行方差
s = std(A)                   % 每列标准差

% 极值范围
r = range(A)                 % 每列极差（max-min）

% 排序
B = sort(A)                  % 每列升序排列
B = sort(A, 'descend')       % 每列降序排列
[B, idx] = sort(A)           % 返回排序后矩阵与原索引
```

### 2.5 稀疏矩阵（大数据建模必备）
```matlab
S = sparse(A)                % 将满矩阵转为稀疏矩阵
S = sparse(i, j, v, m, n)    % 用行索引i、列索引j、值v构建稀疏矩阵
F = full(S)                  % 稀疏矩阵转回满矩阵
spy(S)                       % 可视化稀疏矩阵的非零元素分布
nnz(S)                       % 非零元素个数
```

---

## 三、线性方程组求解

```matlab
% 适定方程组（方阵无奇异）
x = A \ b                    % 推荐：比 inv(A)*b 更稳定

% 超定方程组（方程数 > 未知数，最小二乘解）
x = A \ b                    % 自动使用QR分解求最小二乘解

% 欠定方程组（方程数 < 未知数，最小范数解）
x = A \ b                    % 自动求最小范数解

% 最小二乘拟合（超定方程组）
x = lsqminnorm(A, b)         % 最小范数最小二乘解
x = pinv(A) * b              % 用伪逆求解

% 病态方程组（Tikhonov正则化）
lambda = 0.01;               % 正则化参数
x = (A'*A + lambda*eye(n)) \ (A'*b);

% 符号求解
x = linsolve(A, b)           % 符号线性方程组

% 非线性方程组
x = fsolve(@fun, x0)         % 数值求解非线性方程组
```

---

## 四、绘图与可视化

### 4.1 二维曲线图
```matlab
% 基本绘图
plot(x, y)                   % 默认实线
plot(x, y, 'r--')            % 红色虚线
plot(x, y, 'LineWidth', 2)   % 设置线宽
plot(x1, y1, 'b-', x2, y2, 'r--')  % 多条曲线
hold on                      % 保持当前图形，叠加绘图
hold off                     % 取消保持

% 线型、颜色、标记
% 颜色: r红 g绿 b蓝 c青 m品红 y黄 k黑 w白
% 线型: -实线 --虚线 :点线 -.点划线
% 标记: o圆 +加号 *星号 .点 x叉 s方形 d菱形 ^三角
plot(x, y, 'ro-', 'MarkerSize', 8, 'MarkerFaceColor', 'r')

% 子图
subplot(m, n, p)             % m行n列的第p个子图
subplot(2, 2, 1); plot(x, y);

% 自定义图形
figure('Name', '标题', 'NumberTitle', 'off')  % 新建窗口
clf                          % 清除当前图形
close all                    % 关闭所有图形窗口

% 坐标轴
xlabel('x轴标签', 'FontSize', 12)
ylabel('y轴标签')
title('图形标题')
legend('曲线1', '曲线2', 'Location', 'best')
xlim([xmin, xmax])           % x轴范围
ylim([ymin, ymax])           % y轴范围
axis equal                   % 等比例坐标轴
axis tight                   % 紧凑坐标轴
grid on                      % 显示网格
grid minor                   % 细网格
box on                       % 显示边框
```

### 4.2 常用统计图
```matlab
% 直方图
histogram(data)              % 自动分箱（推荐，R2014b+）
histogram(data, 20)          % 指定箱数
histogram(data, edges)       % 指定箱边

% 散点图
scatter(x, y)                % 基本散点图
scatter(x, y, sz, c, 'filled')  % sz:点大小, c:颜色, 'filled':填充
gscatter(x, y, group)        % 分组散点图（需Statistics Toolbox）

% 条形图
bar(x, y)                    % 垂直条形图
barh(x, y)                   % 水平条形图
bar(x, y, 'stacked')         % 堆叠条形图

% 箱线图
boxplot(data)                % 单个数据集
boxplot(data, group)         % 按分组画箱线图

% 饼图
pie(data)                    % 饼图
pie(data, explode)           % explode为1的位置会突出显示

% 误差棒图
errorbar(x, y, err)          % 对称误差
errorbar(x, y, neg, pos)     % 非对称误差

% 面积图
area(x, y)                   % 填充到x轴的面积图

% 茎叶图
stem(x, y)                   % 离散序列图（信号处理常用）

% 等高线图
contour(X, Y, Z)             % 二维等高线
contourf(X, Y, Z)            % 填充等高线
contour3(X, Y, Z)            % 三维等高线
```

### 4.3 三维绘图
```matlab
% 网格生成
[X, Y] = meshgrid(x, y)      % 从向量生成二维网格（配合三维曲面）

% 三维曲线
plot3(x, y, z)               % 三维空间曲线

% 三维曲面
surf(X, Y, Z)                % 曲面图（带颜色填充）
mesh(X, Y, Z)                % 网格曲面（线框）
meshz(X, Y, Z)               % 带幕帘的网格图
waterfall(X, Y, Z)           % 瀑布图
surfc(X, Y, Z)               % 曲面+底部等高线

% 颜色与光照
colormap(jet)                 % 设置颜色映射（jet/parula/hot/cool/gray/turbo等）
colorbar                      % 显示颜色条
shading interp                % 平滑着色
shading flat                  % 平面着色
camlight                      % 添加光源
lighting gouraud              % 光照模式
view(az, el)                  % 设置视角（az方位角, el仰角）

% 三维散点
scatter3(x, y, z, sz, c, 'filled')
```

### 4.4 图形美化和导出
```matlab
% 字体与外观
set(gca, 'FontSize', 12, 'FontName', 'Times New Roman')
set(gcf, 'Color', 'w')       % 背景设为白色
set(gcf, 'Position', [100, 100, 800, 600])  % 窗口位置与大小

% 文字标注
text(x, y, '标注文字', 'FontSize', 10)
gtext('用鼠标点击放置文字')
annotation('textarrow', [x1,x2], [y1,y2], 'String', '注释')

% 多图合一
tiledlayout(m, n)            % 创建分块布局（R2019b+，推荐）
nexttile; plot(x, y);        % 切换到下一块

% 双y轴
yyaxis left                   % 左侧y轴
plot(x, y1)
yyaxis right                  % 右侧y轴
plot(x, y2)

% 对数坐标
semilogx(x, y)               % x轴对数
semilogy(x, y)               % y轴对数
loglog(x, y)                 % 双对数

% 极坐标
polarplot(theta, rho)

% 导出图形
saveas(gcf, 'figure.png')    % 保存为图片
print('figure', '-dpng', '-r300')  % 300dpi高清导出
exportgraphics(gcf, 'figure.pdf', 'ContentType', 'vector')  % 矢量图导出
```

---

## 五、数据预处理

### 5.1 数据导入导出
```matlab
% 读写表格数据
data = readtable('data.csv')              % 读取CSV/Excel为table类型
data = readtable('data.xlsx', 'Sheet', 1)
writetable(data, 'output.csv')            % 写入CSV
writetable(data, 'output.xlsx')           % 写入Excel

% 读写矩阵数据
M = readmatrix('data.csv')                % 读取为数值矩阵（R2019a+）
writematrix(M, 'output.csv')

% 读写Excel
[num, txt, raw] = xlsread('data.xlsx')    % 较老版本使用
[num, txt, raw] = xlsread('data.xlsx', 'Sheet1', 'A1:D100')

% 读写文本文件
data = load('data.txt')                   % 纯数值文本
fid = fopen('data.txt', 'r');
C = textscan(fid, '%f %s %f', 'Delimiter', ',');
fclose(fid);

% 读写MAT文件
save('data.mat', 'A', 'B', 'C')           % 保存变量到.mat文件
load('data.mat')                          % 加载所有变量
S = load('data.mat', 'A')                 % 只加载A

% 复制到剪贴板
clipboard('copy', data)                   % 复制数据到剪贴板，方便粘贴到Excel
```

### 5.2 缺失值处理
```matlab
% 检测缺失值
TF = isnan(A)                              % NaN检测
TF = ismissing(data)                       % 全面缺失检测（table类型）
TF = isinf(A)                              % Inf检测
TF = isoutlier(A)                          % 异常值检测

% 移除缺失值
A = rmmissing(A)                           % 删除含NaN的行（table/矩阵）
A(any(isnan(A), 2), :) = []                % 删除含NaN的矩阵行

% 填充缺失值
A = fillmissing(A, 'constant', 0)          % 用0填充
A = fillmissing(A, 'linear')              % 线性插值填充
A = fillmissing(A, 'previous')            % 用前一个值填充
A = fillmissing(A, 'movmean', 5)          % 用5点滑动均值填充

% 手动替换
A(isnan(A)) = 0                            % 将NaN替换为0
A(isinf(A)) = 0                            % 将Inf替换为0
```

### 5.3 异常值处理
```matlab
% 检测异常值
TF = isoutlier(data)                       % 默认方法（中位数+1.5倍IQR）
TF = isoutlier(data, 'mean')               % 均值+3倍标准差
TF = isoutlier(data, 'quartiles')          % 四分位数法
TF = isoutlier(data, 'grubbs')             % Grubbs检验
TF = isoutlier(data, 'gesd')               % 广义ESD检验

% 替换异常值
data_clean = filloutliers(data, 'linear')  % 线性插值替换
data_clean = filloutliers(data, 'center')  % 用中位数替换
data_clean = filloutliers(data, 'clip')    % 用阈值裁剪

% 手动N倍标准差法
mu = mean(data);
sigma = std(data);
TF = abs(data - mu) > 3 * sigma;           % 3σ原则
```

### 5.4 数据标准化与归一化
```matlab
% z-score标准化（均值为0，标准差为1）
X_std = zscore(X)                          % 按列标准化
X_std = (X - mean(X)) ./ std(X)            % 手动实现
X_std = normalize(X, 'zscore')             % R2018a+推荐写法

% min-max归一化（映射到[0,1]）
X_norm = (X - min(X)) ./ (max(X) - min(X))
X_norm = normalize(X, 'range')             % [0,1]
X_norm = normalize(X, 'range', [-1, 1])    % [-1,1]

% 其他标准化
X_norm = normalize(X, 'norm')              % 单位L2范数
X_norm = normalize(X, 'scale')             % 除以标准差
X_norm = normalize(X, 'center')            % 去均值（中心化）

% 手动Min-Max函数
function X_norm = minmax_normalize(X)
    minX = min(X, [], 1);
    maxX = max(X, [], 1);
    X_norm = (X - minX) ./ (maxX - minX);
end
```

### 5.5 数据变换
```matlab
% 平滑
y_smooth = smooth(y)                       % 默认移动平均法
y_smooth = smooth(y, span, 'moving')       % 移动平均
y_smooth = smooth(y, span, 'lowess')       % 局部加权回归
y_smooth = smooth(y, span, 'loess')        % 二次局部加权回归
y_smooth = smooth(y, span, 'sgolay')       % Savitzky-Golay滤波
y_smooth = movmean(y, k)                   % k点滑动平均

% 插值
yq = interp1(x, y, xq)                     % 一维插值（默认线性）
yq = interp1(x, y, xq, 'spline')          % 三次样条插值
yq = interp1(x, y, xq, 'pchip')           % 分段三次Hermite插值
yq = interp1(x, y, xq, 'nearest')         % 最近邻插值
Zq = interp2(X, Y, Z, Xq, Yq)             % 二维插值
Zq = griddata(x, y, z, xq, yq)            % 散点数据网格插值
Vq = scatteredInterpolant(x, y, z)         % 散点插值对象（高效批量插值）

% 多项式拟合
p = polyfit(x, y, n)                       % n次多项式拟合
y_fit = polyval(p, x)                      % 计算拟合值
[p, S, mu] = polyfit(x, y, n)             % mu为均值和标准差（数值更稳定）

% 其他拟合
f = fit(x, y, 'poly2')                     % 二次多项式拟合（Curve Fitting Toolbox）
f = fit(x, y, 'exp1')                      % 指数拟合 a*exp(b*x)
f = fit(x, y, 'fourier1')                  % 傅里叶拟合
```

### 5.6 数据分组与聚合
```matlab
% 条件筛选
idx = A > 0                                % 逻辑索引
B = A(A > 0)                               % 取出满足条件的元素
idx = A(:, 1) == 1                         % 第1列等于1的行
rows = A(idx, :)                           % 提取这些行

% 逻辑运算
idx = (A > 0) & (A < 10)                   % 与
idx = (A < 0) | (A > 100)                  % 或
idx = ~idx                                 % 非

% 分组统计
G = findgroups(data.Category)              % 生成分组索引
stats = splitapply(@mean, data.Value, G)   % 对每组计算均值
groupsummary(data, 'Category', 'mean')     % 一键分组汇总

% table筛选
T = data(data.Age > 20, :)                 % table按条件筛选行
T = data(:, {'Name', 'Score'})             % 按列名选取
T = data(ismember(data.City, {'北京','上海'}), :)

% 去重
[C, ia, ic] = unique(A)                    % 返回唯一值、首次出现索引、映射
[C, ia, ic] = unique(A, 'rows')            % 按行去重
```

---

## 六、优化与建模常用函数

### 6.1 优化函数
```matlab
% 线性规划
% min c'*x  s.t. A*x <= b, Aeq*x = beq, lb <= x <= ub
[x, fval] = linprog(c, A, b, Aeq, beq, lb, ub)

% 整数规划
[x, fval] = intlinprog(c, intcon, A, b, Aeq, beq, lb, ub)  % intcon为整数变量索引

% 非线性规划（无约束）
[x, fval] = fminunc(@fun, x0)             % 无约束非线性优化
[x, fval] = fminsearch(@fun, x0)          % 单纯形法（无需梯度）

% 非线性规划（有约束）
% min f(x)  s.t. c(x)<=0, ceq(x)=0, A*x<=b, Aeq*x=beq, lb<=x<=ub
[x, fval] = fmincon(@fun, x0, A, b, Aeq, beq, lb, ub, @nonlcon)

% 二次规划  min 0.5*x'*H*x + f'*x
[x, fval] = quadprog(H, f, A, b, Aeq, beq, lb, ub)

% 多目标优化
[x, fval] = fgoalattain(@fun, x0, goal, weight)  % 目标达到法
```

### 6.2 方程求解
```matlab
% 符号求解
syms x
sol = solve(x^2 + 2*x + 1 == 0, x)        % 单方程
sols = vpasolve(eqn, x)                    % 数值近似解
[sol_x, sol_y] = solve(eqn1, eqn2, x, y)  % 方程组

% 数值求解
x = fzero(@fun, x0)                        % 单变量零点
x = fsolve(@fun, x0)                       % 多变量方程组
x = fminbnd(@fun, a, b)                    % 单变量区间最小值
```

### 6.3 微积分
```matlab
% 符号微分
syms x
df = diff(f, x)                            % 一阶导数
df2 = diff(f, x, 2)                        % 二阶导数

% 符号积分
F = int(f, x)                              % 不定积分
F = int(f, x, a, b)                        % 定积分

% 数值积分
I = integral(@fun, a, b)                   % 一维数值积分
I = integral2(@fun, xmin, xmax, ymin, ymax)% 二重积分
I = trapz(x, y)                            % 梯形法数值积分

% 数值微分
dy = diff(y) ./ diff(x)                    % 前向差分
dy = gradient(y, x)                        % 梯度（推荐，精度更高）
```

### 6.4 常微分方程（ODE）
```matlab
% 求解器
[t, y] = ode45(@odefun, tspan, y0)         % 非刚性首选（4/5阶Runge-Kutta）
[t, y] = ode23(@odefun, tspan, y0)         % 精度较低，适合轻度刚性问题
[t, y] = ode15s(@odefun, tspan, y0)        % 刚性方程求解器
[t, y] = ode113(@odefun, tspan, y0)        % 高精度非刚性问题

% 示例：Lotka-Volterra捕食者模型
% function dydt = odefun(t, y)
%     dydt = [2*y(1) - 0.04*y(1)*y(2);
%             -y(2) + 0.02*y(1)*y(2)];
% end
% [t, y] = ode45(@odefun, [0, 50], [100, 20]);
% plot(t, y); legend('猎物', '捕食者');
```

---

## 七、编程与控制流

### 7.1 条件判断
```matlab
if condition
    % 代码
elseif condition2
    % 代码
else
    % 代码
end

% 单行条件
x = (a > b) * 1 + (a <= b) * 2             % 使用逻辑值做选择
```

### 7.2 循环
```matlab
% for循环
for i = 1:n
    % 代码
end

% 向量化代替循环（强烈推荐）
A = 1:n                                    % 比for循环快数十倍

% 遍历矩阵元素
for i = 1:size(A, 1)
    for j = 1:size(A, 2)
        % A(i, j)
    end
end

% while循环
while condition
    % 代码
end

% 提前退出
break                                      % 跳出当前循环
continue                                   % 跳过本次迭代剩余代码
```

### 7.3 函数定义
```matlab
% 独立函数文件（文件名：myfun.m）
function [out1, out2] = myfun(in1, in2)
    % 帮助文档（用help myfun查看）
    out1 = in1 + in2;
    out2 = in1 - in2;
end

% 匿名函数（简洁，常用于传参）
f = @(x) x^2 + 2*x + 1                     % 单变量
f = @(x, y) x.^2 + y.^2                     % 多变量
f(3); f(3, 4)

% 嵌套函数
function outer(x)
    function inner(y)
        disp(x + y);
    end
end
```

### 7.4 常用向量化技巧
```matlab
% 避免使用循环，用向量化操作替代（MATLAB性能关键）

% 差的不是循环
% for i = 1:n
%     B(i) = A(i)^2;
% end
% 好的是向量化
B = A.^2;

% 条件向量化
B = A;
B(A > 0) = 1;                              % 大于0的设为1
B(A <= 0) = -1;                            % 小于等于0的设为-1

% 用逻辑索引替代find+循环
idx = A > 0;                               % 比find更好
B(idx) = sqrt(A(idx));

% 隐式扩展（R2016b+，自动bsxfun）
C = A + B'                                 % 不同维度自动扩展
C = bsxfun(@plus, A, B')                   % 旧版本需显式调用
```

---

## 八、符号计算（Symbolic Math Toolbox）

```matlab
% 定义符号变量
syms x y a b c                              % 声明符号变量
syms n integer                              % 声明为整数符号
syms f(x, y)                                % 声明符号函数

% 简化与变换
S = simplify(expr)                          % 代数简化
S = expand(expr)                            % 展开表达式
S = factor(expr)                            % 因式分解
S = collect(expr, x)                        % 按x合并同类项
S = subs(expr, x, value)                    % 符号替换（代入数值）
S = subs(expr, [x, y], [1, 2])              % 多个替换

% 极限
L = limit(f, x, 0)                          % x→0的极限
L = limit(f, x, inf)                        % x→∞的极限
L = limit(f, x, a, 'left')                  % 左极限

% 级数
T = taylor(f, x, 'Order', 5)               % 5阶泰勒展开

% 符号矩阵运算
syms a b c d
A = [a, b; c, d]
det(A), inv(A), eig(A)

% 拉普拉斯变换
F = laplace(f, t, s)
f = ilaplace(F, s, t)

% 傅里叶变换
F = fourier(f, t, w)
f = ifourier(F, w, t)
```

---

## 九、概率统计（Statistics Toolbox）

```matlab
% 分布函数
y = normpdf(x, mu, sigma)                   % 正态分布PDF
y = normcdf(x, mu, sigma)                   % 正态分布CDF
y = chi2pdf(x, k)                           % 卡方分布PDF
y = tpdf(x, v)                              % t分布PDF

% 随机数生成
r = normrnd(mu, sigma, m, n)                % 正态分布随机数
r = exprnd(mu, m, n)                        % 指数分布随机数
r = unifrnd(a, b, m, n)                     % 均匀分布随机数
r = mvnrnd(mu, Sigma, n)                    % 多元正态分布

% 参数估计
[mu, sigma, muCI, sigmaCI] = normfit(data)  % 正态分布参数估计
[phat, pci] = mle(data, 'distribution', 'norm')  % 极大似然估计

% 假设检验
[h, p] = ttest(x)                           % 单样本t检验（均值是否为0）
[h, p] = ttest2(x, y)                       % 双样本t检验
[h, p] = ranksum(x, y)                      % Wilcoxon秩和检验（非参数）
[h, p] = signrank(x, y)                     % Wilcoxon符号秩检验（配对）
[h, p] = kstest(x)                          % Kolmogorov-Smirnov正态性检验
[h, p] = chi2gof(x)                         % 卡方拟合优度检验

% 相关性分析
[R, P] = corrcoef(A)                        % Pearson相关系数及p值
[R, P] = corr(A, 'type', 'Spearman')        % Spearman秩相关
[R, P] = corr(A, 'type', 'Kendall')         % Kendall秩相关

% 回归分析
mdl = fitlm(X, y)                           % 线性回归模型
mdl = fitglm(X, y)                          % 广义线性模型
mdl = fitlm(X, y, 'quadratic')             % 含二次项的回归
[y_pred, ci] = predict(mdl, Xnew)           % 预测及置信区间
coef = mdl.Coefficients                     % 回归系数
anova(mdl)                                  % 方差分析表

% 主成分分析（PCA）
[coeff, score, latent, ~, explained] = pca(X)  % PCA分析
% coeff: 主成分系数（载荷矩阵）
% score: 主成分得分
% latent: 特征值
% explained: 各主成分解释的方差百分比（%）
% 降维：取前k个主成分
X_reduced = score(:, 1:k);

% 聚类分析
idx = kmeans(X, k)                          % K-means聚类
Z = linkage(X)                              % 层次聚类
dendrogram(Z)                               % 层次聚类树状图

% 判别分析
mdl = fitcdiscr(X, y)                       % 线性判别分析（LDA）
[label, score] = predict(mdl, Xnew)
```

---

## 十、快速参考速查

| 需求 | 函数 | 说明 |
|------|------|------|
| 解方程 Ax=b | `x = A \ b` | 比inv快且稳定 |
| 多项式拟合 | `p = polyfit(x,y,n)` | n为阶数 |
| 一维插值 | `interp1(x,y,xq,'spline')` | spline最平滑 |
| 数据平滑 | `smooth(y, span, 'loess')` | 局部加权 |
| 快速傅里叶变换 | `Y = fft(y)` | 频域分析 |
| 数值积分 | `integral(@f,a,b)` | 替代quad |
| 求解ODE | `[t,y] = ode45(@f,tspan,y0)` | 首选求解器 |
| 非线性方程 | `x = fsolve(@f,x0)` | 多变量 |
| 求函数极值 | `[x,fval] = fmincon(@f,x0,...)` | 有约束 |
| 特征值分解 | `[V,D] = eig(A)` | D为特征值 |
| SVD分解 | `[U,S,V] = svd(A)` | 矩阵压缩/去噪 |
| 标准化 | `zscore(X)` 或 `normalize(X)` | z-score |
| 归一化 | `normalize(X,'range')` | [0,1] |
| 缺失值填充 | `fillmissing(A,'linear')` | 插值填充 |
| 异常值检测 | `isoutlier(data)` | 多种方法 |
| 统计汇总 | `summary(T)` | table概览 |
| 随机排列 | `randperm(n)` | 不重复抽样 |

---

## 十一、实用建模代码模板

### 模板1：数据预处理完整流程
```matlab
% 1. 导入数据
data = readtable('data.csv');

% 2. 查看数据概览
summary(data);

% 3. 处理缺失值
data = fillmissing(data, 'linear');

% 4. 检测和处理异常值
for i = 1:width(data)
    if isnumeric(data{:, i})
        TF = isoutlier(data{:, i});
        data{TF, i} = NaN;
        data{:, i} = fillmissing(data{:, i}, 'linear');
    end
end

% 5. 标准化（z-score）
X = table2array(data(:, 2:end));   % 假设第1列不是特征
X = normalize(X, 'zscore');

% 6. 保存处理后的数据
writematrix(X, 'processed_data.csv');
```

### 模板2：拟合与绘图
```matlab
% 数据拟合与可视化
x = data.x;
y = data.y;

% 多项式拟合
p = polyfit(x, y, 2);
x_fit = linspace(min(x), max(x), 100);
y_fit = polyval(p, x_fit);

% 绘图
figure('Color', 'w');
scatter(x, y, 'ko', 'DisplayName', '原始数据'); hold on;
plot(x_fit, y_fit, 'r-', 'LineWidth', 2, 'DisplayName', '拟合曲线');
xlabel('x'); ylabel('y'); title('多项式拟合');
legend('Location', 'best'); grid on;
```

### 模板3：回归分析
```matlab
% 多元线性回归
X = data{:, {'x1', 'x2', 'x3'}};
y = data.y;
mdl = fitlm(X, y);
disp(mdl);

% 残差诊断
figure;
subplot(2,2,1); plot(mdl.Residuals.Raw); title('残差序列');
subplot(2,2,2); qqplot(mdl.Residuals.Raw); title('Q-Q图');
subplot(2,2,3); histogram(mdl.Residuals.Raw); title('残差直方图');
subplot(2,2,4); plot(mdl.Fitted, mdl.Residuals.Raw, 'o'); title('残差vs拟合值');
```

### 模板4：优化模型
```matlab
% 定义目标函数（匿名函数）
obj_fun = @(x) (x(1)-1)^2 + (x(2)-2)^2;

% 约束条件（匿名函数）
nonlcon = @(x) deal([], x(1)^2 + x(2)^2 - 1);  % 非线性等式约束 x1^2+x2^2=1

% 求解
x0 = [0, 0];
[x_opt, fval] = fmincon(obj_fun, x0, [], [], [], [], [], [], nonlcon);
```