for i in range(10, 201, 10): 
    if i % 20 == 0:
        print("ctx.lineTo({}, {})".format(i, 70))
    else:
        print("ctx.lineTo({}, {})".format(i, 60))