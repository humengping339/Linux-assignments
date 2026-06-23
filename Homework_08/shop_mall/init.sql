SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS user_info(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS goods(
    id INT PRIMARY KEY AUTO_INCREMENT,
    goods_name VARCHAR(100),
    price FLOAT,
    stock INT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS orders(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    goods_id INT,
    buy_num INT,
    create_time DATETIME DEFAULT NOW()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 插入测试商品
INSERT INTO goods(goods_name,price,stock) VALUES
('无线鼠标',79.9,200),
('机械键盘',199.0,100),
('27寸显示器',899.0,50);