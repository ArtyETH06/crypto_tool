# ❓What is it ?

*Crpyto_tool* is a tool made in *python* for crpyotlogy,it allows you to encode and to encode in different type !

For the instant, *crypto_tool* can encode up to **7 different** type,and decode them as well

 # 👨🏻‍💻Installation
 
 First,you have to copy the code with:
 ```
 git clone github.com/ArtyETH06/crypto_tool
 ```
 Then,go in the directory with:
 ```
 cd crypto_tool
 ```
 And now,you'll have to install the necessary packages with
 ```
 pip install -r requirements.txt
 ```
 It will download all the depedencies necessary for the code to work.

Then you can start the code !

## ✅ Usage

To run the script you have to do:
```
python crypto.py -m X -c "XXX"
```
The **-m** stands for the mode and **-c** stands for the content

## 💻Table of usage

| Mode      | Input     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `1`       | `string` | **String --> Binary**             |
| `2`       | `string` | **String --> ROT13**             |
| `3`       | `string` | **String --> Base64**             |
| `4`       | `string` | **String --> Hexadecimal**         |
| `5`       | `string` | **String --> URL**             |
| `6`       | `string` | **String --> ASCII**             |
| `7`       | `string` | **String --> Morse**             |
| `8`       | `int` | **Binary --> String**             |
| `9`       | `string` | **ROT13 --> String**             |
| `10`       | `string` | **Base64 --> String**             |
| `11`       | `int` | **Hexadecimal --> String**             |
| `12`       | `string + special characters`  | **url --> String**             |
| `13`       | `int` | **ASCII --> String**             |
| `14`       | `. and -` | **Morse --> String**             |
