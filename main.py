f = open("busy_day.in")

import numpy as np

# ciao is the list of all lines in the file
ciao = f.readlines()

counter = 0

# PARAMETERS
(nrows, ncols, ndrones, Tmax, maxload) =  map(int,ciao[counter].split())
counter += 1

# NUMBER OF PRODUCTS
nprods =  map(int,ciao[counter].split())[0]
counter +=1

# VECTOR OF THE PRODUCTS with their weight
prod_weight = np.array(map(int,ciao[counter].split()))
counter +=1

# NUMBER OF WEREHOUSES
nwere =  map(int,ciao[counter].split())[0]
counter += 1

# VECTOR OF WEREHOUSES locations (row,col)
were_loc = np.array([None]*nwere)

# VECTOR OF WEREHOUSES content. Every element is a list long #PRODUCTS with the
# number of elements of each products
were_content = np.array([None]*nwere)

for i in  range(nwere):
    were_loc[i] = map(int,ciao[counter].split()) #line 4,6,8...
    were_content[i] = map(int,ciao[counter + 1].split()) #line 5,7,9...
    counter += 2

# NUMBER OF ORDERS
norders =  map(int,ciao[counter].split())[0]
counter += 1

# VECTOR OF ORDERS locations (row,col)
ord_loc = np.array([None]*norders)

# VECTORS OF ORDERS
# First one has the total number of producs
# Second a list of the products with number referring to array "prod_weight"
ord_n_prods = np.array([None]*norders)
ord_type_prods = np.array([None]*10000)

for i in  range(norders):
    ord_loc[i] = map(int,ciao[counter].split())
    ord_n_prods[i] = map(int,ciao[counter + 1].split())[0]
    ord_type_prods[i] = map(int,ciao[counter + 2].split())
    counter += 3
