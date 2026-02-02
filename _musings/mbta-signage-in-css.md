---
title: MBTA Signage in CSS
description: A demo of Boston's MBTA signs replicated in CSS.
date: 2024/08/06
---
My train-obsessed friend Billy wanted to incorporate custom MBTA signs throughout his website. This is my attempt at creating a CSS template to that end: a success in my book and a load of fun to make. He whipped up some icons as we reached out to the agency in hopes of receiving the official ones (to no avail), and then I got to work on these bad boys.

<link rel="stylesheet" href='assets/mbta/mbta.css'>

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
The multi-layered South Station sign is my magnum opus. The only deviation from accuracy is in the dividers between each icon; the MBTA includes a divider after the last icon, but I thought that looked clunky so I did without it.
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

The code is probably a bit convoluted, but it works. If this interests you, feel free to poke around in Inspect.
