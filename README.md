# ❓What is it ?

*Crpyto_tool* is a tool made in *python* for crpyotlogy, it allows you to encode and decode in different types !

For now, *crypto_tool* can encode up to **7 different** types, and decode them as well

 # 👨🏻‍💻Installation

This will clone the code and download all the depedencies necessary for the code to work.
```
git clone https://github.com/ArtyETH06/crypto_tool.git
cd crypto_tool
pip install -r requirements.txt
```
Finally you can start the code !

## ✅ Usage

To run the script you have to do:
```
python crypto.py [-m] X [-c] "XXX" [-r] X (ONLY FOR ROT ENCODING)
```
**-m** stands for the mode and **-c** stands for the content

## 💻Table of usage

| Mode      | Input     | Description                       |
| :-------- | :-------  | :-------------------------------- |
| `1`       | `string`  | **String --> Binary**             |
| `2`       | `string`  | **String --> ROT (all ROT possible)**              |
| `3`       | `string`  | **String --> Base64**             |
| `4`       | `string`  | **String --> Hexadecimal**        |
| `5`       | `string`  | **String --> URL**                |
| `6`       | `string`  | **String --> ASCII**              |
| `7`       | `string`  | **String --> Morse**              |
| `8`       | `int`     | **Binary --> String**             |
| `9`       | `string`  | **ROT (All possible) --> String**              |
| `10`      | `string`  | **Base64 --> String**             |
| `11`      | `int`     | **Hexadecimal --> String**        |
| `12`      | `string + special characters` | **url --> String** |
| `13`      | `int`     | **ASCII --> String**              |
| `14`      | `. and -` | **Morse --> String**              |
