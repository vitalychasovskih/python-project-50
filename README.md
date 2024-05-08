<div align="center">

<h1>GenDiff: Key-Value Difference Generator</h1>

<p></p>

[![Actions Status](https://github.com/vitalychasovskih/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vitalychasovskih/python-project-50/actions)
[![Python application](https://github.com/vitalychasovskih/python-project-50/actions/workflows/python-app.yml/badge.svg)](https://github.com/vitalychasovskih/python-project-50/actions/workflows/python-app.yml)
</div>

<div align="center">

[![Maintainability](https://api.codeclimate.com/v1/badges/201e4f996bf08ecdd3e2/maintainability)](https://codeclimate.com/github/vitalychasovskih/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/201e4f996bf08ecdd3e2/test_coverage)](https://codeclimate.com/github/vitalychasovskih/python-project-50/test_coverage)

</div>

## Usage

### _getting help_
```bash
>> gendiff -h

usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

<a href="https://asciinema.org/a/658400" target="_blank"><img src="https://asciinema.org/a/658400.svg" width="300"/></a>

### _comparing flat JSON files_
```bash
>> gendiff file1.json file2.json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

<a href="https://asciinema.org/a/658399" target="_blank"><img src="https://asciinema.org/a/658399.svg" width="300"/></a>

### _comparing flat YAML files_
```bash
>> gendiff file1.yaml file2.yml
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```
<a href="https://asciinema.org/a/658401" target="_blank"><img src="https://asciinema.org/a/658401.svg" width="300"/></a>

---

This is the second training project of the ["Python Developer"](https://ru.hexlet.io/programs/python) course on [Hexlet.io](https://hexlet.io)

> GitHub [@Vitaly Сhasovskih](https://github.com/vitalychasovskih)