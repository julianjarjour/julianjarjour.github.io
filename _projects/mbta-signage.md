---
title: MBTA Signage in CSS
date: 2024/08/06
---
<head>
    <link rel="stylesheet" href='mbta.css'>
</head>
<span class="dc">M</span>y train-obsessed friend [Billy](https://www.btsully.net/){:target="_blank"} wanted an MBTA sign template for his website. This was my attempt, a success in my book and a load of fun to make. He recreated the icons in Inkscape, but we're hoping to receive better icon files straight from the agency soon.

<div class="MBTA-sign">
  <div class="T-top" id="green">Copley</div>
  <div class="T-bottom">
    <div class="bubble" id="green">Green Line - Gov Ctr & North</div>
  </div>
</div>

<div class="MBTA-sign">
  <div class="T-top" id="white">Downtown Crossing</div>
  <div class="T-bottom">
    <div class="bubble" id="orange">Orange Line - All Trains</div>
    <div class="bubble" id="red">Red Line - All Trains</div>
  </div>
</div>

<div class="MBTA-sign">
  <div class="T-top" id="red">Harvard</div>
  <div class="T-bottom">
    <div class="Tb-left"><img class="T-icon" src="assets/CircleUPLEFT.svg">OUTBOUND TRAINS</div>
    <div class="Tb-right">INBOUND TRAINS<img class="T-icon" src="assets/CircleUP.svg"></div>
  </div>
</div>
The multi-layered South Station sign is my magnum opus. The only deviation from accuracy is in the dividers between each icon; the MBTA includes a divider after the last icon, I thought that looked clunky so I did without it.
<div class="MBTA-sign">
  <div class="T-top" id="white">South Station</div>
  <div class="T-bottom">
    <img class="T-icon" src="assets/wheelchair.svg"><img class="T-icon" src="assets/elevator.svg"><img class="T-icon" src="assets/airplane.svg"><div class="bubble" id="silver">Silver Line - SL1/SL2</div>
    <div class="bubble" id="red">Red Line - All Trains</div>
  </div>
  <div class="T-bottom">
    <img class="T-icon" src="assets/wheelchair.svg"><img class="T-icon" src="assets/elevator.svg"><div class="bubble" id="commuter">Commuter Rail</div>
    <div class="bubble" id="amtrak">Amtrak</div>
  </div>
</div>

<div class="MBTA-sign">
  <div class="T-top" id="blue">Aquarium</div>
  <div class="T-bottom">
    <img class="T-icon" src="assets/airplane.svg" height=20 width=20><div class="bubble" id="blue">Blue Line - All Trains</div>
  </div>
</div>

The code is admittedly a bit convoluted. You're free to poke around in Inspect, maybe one day I'll make it more accessible.
