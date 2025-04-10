---
title: MBTA Signage in CSS
description: A demo of Boston's MBTA signs replicated in CSS.
date: 2024/08/06
---
<head>
    <link rel="stylesheet" href='assets/mbta/mbta.css'>
</head>
<span class="dc">M</span>y train-obsessed friend [Billy](https://www.btsully.net/){:target="_blank"} wanted an MBTA sign template for his website. This is my attempt at creating one: a success in my book and a load of fun to make. He recreated the icons in Inkscape, but we're hoping to receive better icon files straight from the agency soon.

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
    <div class="Tb-left"><img class="T-icon" src="assets/mbta/CircleUPLEFT.svg">OUTBOUND TRAINS</div>
    <div class="Tb-right">INBOUND TRAINS<img class="T-icon" src="assets/mbta/CircleUP.svg"></div>
  </div>
</div>
The multi-layered South Station sign is my magnum opus. The only deviation from accuracy is in the dividers between each icon; the MBTA includes a divider after the last icon, I thought that looked clunky so I did without it.
<div class="MBTA-sign">
  <div class="T-top" id="white">South Station</div>
  <div class="T-bottom">
    <img class="T-icon" src="assets/mbta/wheelchair.svg"><img class="T-icon" src="assets/mbta/elevator.svg"><img class="T-icon" src="assets/mbta/airplane.svg"><div class="bubble" id="silver">Silver Line - SL1/SL2</div>
    <div class="bubble" id="red">Red Line - All Trains</div>
  </div>
  <div class="T-bottom">
    <img class="T-icon" src="assets/mbta/wheelchair.svg"><img class="T-icon" src="assets/mbta/elevator.svg"><div class="bubble" id="commuter">Commuter Rail</div>
    <div class="bubble" id="amtrak">Amtrak</div>
  </div>
</div>

<div class="MBTA-sign">
  <div class="T-top" id="blue">Aquarium</div>
  <div class="T-bottom">
    <img class="T-icon" src="assets/mbta/airplane.svg" height=20 width=20><div class="bubble" id="blue">Blue Line - All Trains</div>
  </div>
</div>

The code is admittedly a bit convoluted, but it works. If you want to use this, you're free to poke around in Inspect and/or email me for help.
