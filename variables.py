#Assignment of variables and creating a list
# In eu-west-2 they want to provision this ami  - ami- 0d729d2846a86a9e7, 
# In eu-west-1 this ami-  ami-0c1bc246476a5572b
# In, us-east-1 this ami ami-0022f774911c1d690

ami_list = ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"] #list
print(ami_list)

#for loop
ami_list = ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"]
for ami in ami_list:
     print["ami list"]
     print(ami)

#   Assigning a variable and creating a Tuple
regions_tuple = ("eu-west-2","eu-west-1","us-east-1") #tuple

for region in regions_tuple:
    print(region)
    if region == "eu-west-1":
       print("the region is equal to us-east-1")

#   Assigning a variable and creating a dictionary
region_ami_dict = {"eu-west-2" :"ami- 0d729d2846a86a9e7", "eu-west-1" : "ami-0c1bc246476a5572b", "us-east-1" : "ami-0022f774911c1d690"}

for v in region_ami_dict.items():
     print(v)