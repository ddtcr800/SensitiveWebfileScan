# SensitiveWebfileScan

针对于CTF-Web中敏感文件泄漏的扫描器

## Usage

```python
python scan.py [url]
```

eg:

```python
python scan.py http://ctf.test.com
```



可以指定关键字扫描，使用了generatedict来生成关于关键字字典

```python
python scan.py [url] -k 'flagSDK'
```



关于关键字、请求方式、线程、TIME_OUT时间、日志都可以在config.py里面设置

