import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, binary_sensor, esp32_ble_tracker
from esphome.const import CONF_MAC_ADDRESS, CONF_ID, CONF_BINDKEY, CONF_ALERT, CONF_DEVICE_CLASS, CONF_LIGHT, CONF_BATTERY_LEVEL, UNIT_PERCENT, ICON_BATTERY

DEPENDENCIES = ['esp32_ble_tracker']
AUTO_LOAD = ['xiaomi_ble']

miot1_mccgq02hl_ns = cg.esphome_ns.namespace('miot1_mccgq02hl')
XiaomiMCCGQ02HL = miot1_mccgq02hl_ns.class_('XiaomiMCCGQ02HL',cg.Component, binary_sensor.BinarySensor,
                                             esp32_ble_tracker.ESPBTDeviceListener)

CONFIG_SCHEMA = cv.All(binary_sensor.BINARY_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(XiaomiMCCGQ02HL),
    cv.Required(CONF_MAC_ADDRESS): cv.mac_address,
    cv.Required(CONF_BINDKEY): cv.bind_key,
    cv.Optional(CONF_LIGHT): binary_sensor.BINARY_SENSOR_SCHEMA.extend({
        cv.Optional(CONF_DEVICE_CLASS, default='light'): binary_sensor.device_class,
    }),
    cv.Optional(CONF_ALERT): binary_sensor.BINARY_SENSOR_SCHEMA.extend({
        cv.Optional(CONF_DEVICE_CLASS, default='alert'): binary_sensor.device_class,
    }),
    cv.Optional(CONF_BATTERY_LEVEL): sensor.sensor_schema(UNIT_PERCENT, ICON_BATTERY, 0),
}).extend(esp32_ble_tracker.ESP_BLE_DEVICE_SCHEMA).extend(cv.COMPONENT_SCHEMA))


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield esp32_ble_tracker.register_ble_device(var, config)

    cg.add(var.set_address(config[CONF_MAC_ADDRESS].as_hex))
    cg.add(var.set_bindkey(config[CONF_BINDKEY]))

    if CONF_LIGHT in config:
        sens = yield binary_sensor.new_binary_sensor(config[CONF_LIGHT])
        cg.add(var.set_light(sens))
    if CONF_OPEN in config:
        sens = yield binary_sensor.new_binary_sensor(config[CONF_OPEN])
        cg.add(var.set_open(sens))
    if CONF_BATTERY_LEVEL in config:
        sens = yield sensor.new_sensor(config[CONF_BATTERY_LEVEL])
        cg.add(var.set_battery_level(sens))
