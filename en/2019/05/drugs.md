# Drugs

### Routes

Data comes from arrests, if they caught it en route, from and to
country were recorded, or the intented destination had the transport
went ahead. Sometimes source, target is missing. If they record the
production country of the drug I take that as source if missing. If
destination is missing, I take country of arrest as final destination.

Per route weights of all drugs are summed as if they are one drug, to
give a general idea. I multiply tablet quantity with 100 mg per tablet
to turn it into weight. I filtered out all cannabis related transport.

The strategy followed is to sum weight of all drugs

[Data Source](https://dataunodc.un.org/ids)

[Data (ZIP)](drug-trafficking-unodc.zip)

[Code](drugs.py)

[Output](drugs-out.html)

