CREATE TABLE brand
(
  bid INT NOT NULL,
  bname VARCHAR(20) NOT NULL,
  PRIMARY KEY (bid)
);

CREATE TABLE categories
(
  cid INT NOT NULL,
  category_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (cid)
);

CREATE TABLE supplier
(
  sid INT NOT NULL,
  sname VARCHAR(20) NOT NULL,
  address VARCHAR(20) NOT NULL,
  mobno INT NOT NULL,
  PRIMARY KEY (sid)
);

CREATE TABLE customer
(
  mobno INT NOT NULL,
  cust_id INT NOT NULL,
  cname VARCHAR(20) NOT NULL,
  PRIMARY KEY (cust_id)
);

CREATE TABLE transaction
(
  tid INT NOT NULL,
  total_amt_paid INT NOT NULL,
  due INT NOT NULL,
  gst INT NOT NULL,
  discount INT NOT NULL,
  payment_method VARCHAR(20) NOT NULL,
  cust_id INT NOT NULL,
  PRIMARY KEY (tid),
  FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
);

CREATE TABLE provides
(
  discount INT NOT NULL,
  bid INT NOT NULL,
  sid INT NOT NULL,
  PRIMARY KEY (bid, sid),
  FOREIGN KEY (bid) REFERENCES Brand(bid),
  FOREIGN KEY (sid) REFERENCES supplier(sid)
);

CREATE TABLE product
(
  pid INT NOT NULL,
  pname VARCHAR(20) NOT NULL,
  p_stock INT NOT NULL,
  price INT NOT NULL,
  bid INT NOT NULL,
  cid INT NOT NULL,
  sid INT NOT NULL,
  PRIMARY KEY (pid),
  FOREIGN KEY (bid) REFERENCES brand(bid),
  FOREIGN KEY (cid) REFERENCES categories(cid),
  FOREIGN KEY (sid) REFERENCES supplier(sid)
);

CREATE TABLE selects
(
  quantity INT NOT NULL,
  cust_id INT NOT NULL,
  pid INT NOT NULL,
  PRIMARY KEY (cust_id, pid),
  FOREIGN KEY (cust_id) REFERENCES customer(cust_id),
  FOREIGN KEY (pid) REFERENCES product(pid)
);