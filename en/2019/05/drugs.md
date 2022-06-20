# Drugs

### Routes

Data comes from UNODC, collected from individual arrests between
2011-2016. If they caught the smuggling en route from and to country
are usually recorded, or the intented destination had the transport
went ahead. Sometimes source, target is missing, but if they recorded
the production country I take that as source. If destination is
missing, I take country of arrest as final destination.

Report treats the weights of all drugs as equivalent, they are summed
per from-to route, to give a general idea of the importance of each
route. I multiply tablet quantities with 100 mg per tablet to turn
them into weights as well. I filter out all cannabis related transport
as this drug is becoming accepted at the same level of alcohol these
days, report's focus is harder drugs, opium, heroine, meth, and
others.

The strategy followed is to sum weight of all drugs

[Data Source](https://dataunodc.un.org/ids)

[Data (ZIP)](drug-trafficking-unodc.zip)

[Code](drugs.py)

[Output](drugs-out.html)

