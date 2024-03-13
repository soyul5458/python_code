# 1. 압축하기
## 1.1 tar 압축
-----------------
$ tar -cvf [파일명.tar] [폴더명]
 
# abc라는 폴더를 aaa.tar로 압축 예시
$ tar -cvf aaa.tar abc
-----------------

## 1.2 tar.gz 압축
-----------------
$ tar -zcvf [파일명.tar.gz] [폴더명]
 
# abc라는 폴더를 aaa.tar.gz로 압축 예시
$ tar -zcvf aaa.tar.gz abc
-----------------

## 1.3 zip 압축
-----------------
$ zip [파일명.zip] [폴더명]
 
# 현재폴더 전체를 aaa.zip으로 압축 예시
$ zip aaa.zip ./*
 
# aaa.zip으로 압축하고 현재 폴더의 모든 것과 현재 폴더의 하위 폴더들도 모두 압축 예시
$ zip aaa.zip -r ./*
-----------------


# 2. 압축해제
## 2.1 tar 압축 해제
-----------------
$ tar -xvf [파일명.tar]
 
# aaa.tar라는 tar파일 압축해제 예시
$ tar -xvf aaa.tar
-----------------
     
## 2.2 tar.gz 압축 해제
-----------------
$ tar -zxvf [파일명.tar.gz]
 
#  aaa.tar.gz라는 tar.gz파일 압축 해제
$ tar -zxvf aaa.tar.gz
-----------------

## 2.3 zip 압축해제
-----------------
$ unzip [파일명.zip]
 
# aaa.zip 압축 해제 예시
$ unzip aaa.zip 
 
# 특정 폴더에 압축해제 예시
$ unzip aaa.zip -d ./target
-----------------
