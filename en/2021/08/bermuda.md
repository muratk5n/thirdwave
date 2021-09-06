# The Bermuda Triangle

The claim is there are mysterious accidents in the so-called Bermuda
Triangle, an area roughly between Bermuda Island, Puerto Rico and
Southeast US. If this theory is true more accidents should be visible
in the said area.

Looked at a ship accidents data to confirm. The data comes from US
Coast Guard, its "Marine Casualty & Pollution Data for Researchers",
btw 1982-2001 [1,2]. Plotted accidents in the BT in one color, others
(a bigger region) in a different color. As concluded in [2] there
doesn't appear to be any glaring patterns. Accidents, as stated by [2]
decrease in frequency as one gets further from the shore, whether or
not one is inside the Bermuda Triangle.

[Script](bermuda.py)

[Output](bermuda-out.html)

A statistical idea could be taking the bigger area, look at the
distribution of incident counts based on smaller regions in that area,
then get counts in the same region without ones in the triangle. Are
both counts the same Poisson distribution?

References

[1] [Marine Casualty & Pollution Data for Researchers ](https://www.dco.uscg.mil/Our-Organization/Assistant-Commandant-for-Prevention-Policy-CG-5P/Inspections-Compliance-CG-5PC-/Office-of-Investigations-Casualty-Analysis/Marine-Casualty-and-Pollution-Data-for-Researchers/)

[2] [Research](https://www.rebellionresearch.com/the-mystery-of-the-bermuda-triangle-a-scientific-analysis)

