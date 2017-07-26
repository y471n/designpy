#!/usr/bin/env python3

from order import Order
from shipper import Shipper
from shipping_cost import ShippingCost

order = Order(Shipper.fedex)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
print(cost)

