# Simple multilateration for WGS84 (latitude, longitude)
## Usage:
```python
from multilateration import multilateration

# ((latitude,longitude), distance(in km))
# Support more then three points
datas = [
((25.0664615,121.5549009), 2.23),
((25.0336862,121.5648103), 3.14),
((25.0462432,121.5174745), 2.38)
]

print(multilateration(datas))
```
