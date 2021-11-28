# licorice
A python utility library for creating and printing more elegant strings.

## Example use-cases

#### Font-formatting using `licorice.font_format()`
```python
import licorice

message = licorice.font_format("This is licorice", ['BOLD', 'CYAN'])
print(message)
```
<img width="181" alt="Screen Shot 2021-11-28 at 12 26 41 AM" src="https://user-images.githubusercontent.com/47393421/143730814-7218d14c-8531-4df5-a63a-c61f92edcc9c.png">

#### Font-underlining using `licorice.underline()`
```python
licorice.underline("This is licorice:", ['BOLD', 'PURPLE'])
```
<img width="192" alt="Screen Shot 2021-11-28 at 12 31 35 AM" src="https://user-images.githubusercontent.com/47393421/143730941-d53e389d-54e2-404e-a247-1676be30f9d1.png">


## Installation
```python
pip install licorice
```
