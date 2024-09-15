def calculate(yname,cname):

    total_name=yname.lower()+"loves"+cname.lower()
    chars = {char:total_name.count(char) for char in total_name}
    val = list(chars.values())
    def cross(val):
        "Cross function"
        num = (len(val)//2)
        result = [val[i]+val[-(i+1)] for i in range(num)]
        if len(val)%2==1:
            result.append(val[num])
        new_res = "".join(map(str,result))
        return new_res

    while int(cross(val))>100:
        val = list(map(int,cross(val)))
    return cross(val)
# cnames = []
def main():
    
    print("--- FLAMES 3.0 ----\n")
    yname = input("Enter your name : ").replace(" ","")
    cname = input("Enter your crush name : ").replace(" ","")
    print(f"You love {cname} by", calculate(yname,cname),'%')
    print(f"{cname} loves you by", calculate(cname,yname),'%')
   

chc = ""
while not chc:
  main()
  chc = input("---Press Enter to continue---")
print("\nThank you for using Flames V3.0")