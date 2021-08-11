# ZMAi-90 Energy Meter

The `zmai90v1` sensor platform allows you to use `ZMAi-90` energy meters sensors with `ESPHome`.

> This page refers to version V1 of the `ZMAi-90`, which has been out of stock for a while. For using the newer V2 see [zmai90.yaml](../zmai90.yaml) or V3 please fill the request.

```yaml
# Example configuration entry
...
external_components:
  - source: github://dentra/esphome-components
...
uart:
  rx_pin: GPIO3
  tx_pin: GPIO1
  baud_rate: 9600

sensor:
  - platform: zmai90v1
    energy:
      name: Energy
    voltage:
      name: Voltage
    current:
      name: Current
    active_power:
      name: Active Power
    reactive_power:
      name: Reactive Power
    apparent_power:
      name: Apparent Power
    power_factor:
      name: Power Factor
    frequency:
      name: Frequency
    update_interval: 30s
```