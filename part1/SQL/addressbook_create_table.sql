CREATE TABLE addressbook (
  Idx int NOT NULL AUTO_INCREMENT COMMENT 'PK 자동증가',
  FullName varchar(50) NOT NULL COMMENT '이름',
  PhoneNum varchar(20) NOT NULL COMMENT '휴대폰 번호',
  Email varchar(120) DEFAULT NULL COMMENT '이메일 NULL 허용',
  Address varchar(250) CHARACTER SET DEFAULT NULL COMMENT '주소',
  PRIMARY KEY (Idx)
) COMMENT = '주소록테이블';