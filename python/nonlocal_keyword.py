def main_chai():
    chai_flavour = "Ginger"
    def change_tea():
      nonlocal chai_flavour
      chai_flavour = "Masala"
      print("Inside function, chai flavour is:", chai_flavour)
    change_tea()
    print("Outside function, chai flavour is:", chai_flavour)

main_chai()
