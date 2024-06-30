###from net prices to gross prices###
vat = 23
calculated_vat = 1 + vat / 100

Java_course_price_net = 10
Ajax_course_price_net = 20

Java_course_price_gross = Java_course_price_net * calculated_vat
Ajax_course_price_gross = Ajax_course_price_net * calculated_vat
print("Java: ",Java_course_price_gross, "\nAjax: ", Ajax_course_price_gross)

