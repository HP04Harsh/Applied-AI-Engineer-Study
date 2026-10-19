users = [
    {"name": "Alice", "total":120,"coupon_code":"P10"},
    {"name": "Bob", "total":80,"coupon_code":"P5"},
    {"name": "Charlie", "total":150,"coupon_code":"P15"}
]

discounts = {
    "P10": (0.1,0.1),
    "P5": (0.05,0),
    "P15": (0.15,0.15)
}

for user in users:
    name = user["name"]
    total = user["total"]
    coupon_code = user["coupon_code"]

    if coupon_code in discounts:
        discount_percentage, additional_discount = discounts[coupon_code]
        discount_amount = total * discount_percentage
        final_total = total - discount_amount - additional_discount
        print(f"{name} has a total of {total} dollars. After applying the coupon code '{coupon_code}', the final total is {final_total:.2f} dollars.")
    else:
        print(f"{name} has a total of {total} dollars. No valid coupon code applied.")
