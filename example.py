"""Module to run chemical kintetics library."""

from flamespeed import chemkin

# =====================
# Elementary reactions
# =====================

# Specie concentrations
x = [0.5, 0, 0, 2, 0, 1]

# Import reaction data
a = chemkin.ReactionRate()
a.read_XML('./flamespeed/data/rxns_units.xml', verify_integrity=False, convert_units=True)
print(a)

# Set temperature
a.set_temp(900)

# Progress rate
r = a.get_reaction_rate(x)
print("\nReaction rate:")
print(r)

# Set temperature
a.set_temp(2500)

# Progress rate
r = a.get_reaction_rate(x)
print("\n\nReaction rate:")
print(r)

# ==============================
# Parse non-elementary reactions
# ==============================

# Import reaction data
a = chemkin.ReactionRate()
print ("\n\n[Tree Body Parsed]")
a.read_XML('./flamespeed/data/rxn_ThreeBody.xml', verify_integrity=True, convert_units=True)
for idx, item in enumerate(a.k_params_nonelementary):
	print ("Reaction {}".format(str(idx)))
	for rxn in item:
		print (rxn)


print ("\n[Troe Tree Body Parsed]")
a = chemkin.ReactionRate()
a.read_XML('./flamespeed/data/rxn_TroeFalloffThreeBody.xml', verify_integrity=True, convert_units=True)
for idx, item in enumerate(a.k_params_nonelementary):
	print ("Reaction {}".format(str(idx)))
	for rxn in item:
		print (rxn)

print ("\n[Duplicate Parsed]")
a = chemkin.ReactionRate()
a.read_XML('./flamespeed/data/rxn_Duplicate.xml', verify_integrity=True, convert_units=True)
for idx, item in enumerate(a.k_params_nonelementary):
	print ("Reaction {}".format(str(idx)))
	for rxn in item:
		print (rxn)